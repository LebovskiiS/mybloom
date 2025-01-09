from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy import Column

class Base(DeclarativeBase):
    pass



class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    surname: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)

    farms = relationship("FarmsModel", back_populates="user")
    wallets = relationship("WalletsModel", back_populates="user")
    deliveries = relationship("DeliveriesModel", back_populates="user")



class FarmsModel(Base):
    __tablename__ = 'farms'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    farm_name: Mapped[str] = mapped_column(String(255), nullable= False)
    land_size: Mapped[int] = mapped_column(Integer, nullable= False)
    plants_id: Mapped[int] = mapped_column(ForeignKey('plants.id'), nullable= True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable= False)

    user = relationship("UserModel", back_populates="farms")
    plants = relationship("PlantsModel", back_populates="farms")



class PlantsModel(Base):
    __tablename__ = 'plants'
    id: Mapped[int] = mapped_column(primary_key=True)
    sort_id: Mapped[int] = mapped_column(ForeignKey('sorts.id'))
    plants_name: Mapped[str] = mapped_column()
    start_time: Mapped[int] = mapped_column()
    end_time: Mapped[int] = mapped_column()
    total_weight: Mapped[int] = mapped_column()
    growing_on_persent: Mapped[int] = mapped_column()
    status: Mapped[bool] = mapped_column()

    farms = relationship("FarmsModel", back_populates="plants")
    sort = relationship("SortModel", back_populates="plants")


class SortModel(Base):
    __tablename__ = 'sorts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    family_id: Mapped[int] = mapped_column()
    color: Mapped[str] = mapped_column()
    grow_time: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    min_unit_number: Mapped[int] = mapped_column()

    plants = relationship("PlantsModel", back_populates="sort")


class WalletsModel(Base):
    __tablename__ = 'wallets'

    id: Mapped[int] = mapped_column(primary_key=True)
    card_info: Mapped[str] = mapped_column()
    spending: Mapped[int] = mapped_column()
    wast_purchase: Mapped[str] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="wallets")


class DeliveriesModel(Base):
    __tablename__ = 'deliveries'

    id: Mapped[int] = mapped_column(primary_key=True)
    date_of_initializing: Mapped[int] = mapped_column()
    est_delivery: Mapped[str] = mapped_column()
    status: Mapped[bool] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="deliveries")




