from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str]
    phone: Mapped[int]
    password: Mapped[str]
    address: Mapped[str]

    farms = relationship("FarmsModel", back_populates="user")
    wallets = relationship("WalletsModel", back_populates="user")
    deliveries = relationship("DeliveriesModel", back_populates="user")


class FarmsModel(Base):
    __tablename__ = 'farms'

    id: Mapped[int] = mapped_column(primary_key=True)
    farm_name: Mapped[str]
    land_size: Mapped[int]
    plants_id: Mapped[int] = mapped_column(ForeignKey('plants.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user = relationship("UserModel", back_populates="farms")
    plants = relationship("PlantsModel", back_populates="farms")


class PlantsModel(Base):
    __tablename__ = 'plants'
    id: Mapped[int] = mapped_column(primary_key=True)
    sort_id: Mapped[int] = mapped_column(ForeignKey('sorts.id'))
    plants_name: Mapped[str]
    start_time: Mapped[int]
    end_time: Mapped[int]
    total_weight: Mapped[int]
    growing_on_persent: Mapped[int]
    status: Mapped[bool]

    farms = relationship("FarmsModel", back_populates="plants")
    sort = relationship("SortModel", back_populates="plants")


class SortModel(Base):
    __tablename__ = 'sorts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    family_id: Mapped[int]
    color: Mapped[str]
    grow_time: Mapped[str]
    price: Mapped[int]
    min_unit_number: Mapped[int]

    plants = relationship("PlantsModel", back_populates="sort")


class WalletsModel(Base):
    __tablename__ = 'wallets'

    id: Mapped[int] = mapped_column(primary_key=True)
    card_info: Mapped[str]
    spending: Mapped[int]
    wast_purchase: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="wallets")


class DeliveriesModel(Base):
    __tablename__ = 'deliveries'

    id: Mapped[int] = mapped_column(primary_key=True)
    date_of_initializing: Mapped[int]
    est_delivery: Mapped[str]
    status: Mapped[bool]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="deliveries")

