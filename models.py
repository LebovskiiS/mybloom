from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String, CheckConstraint, Boolean, UniqueConstraint, Float


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
    role: Mapped[str] = mapped_column(String(255), default= 'user')


    farm = relationship("FarmModel", back_populates="user", uselist=False)
    wallets = relationship("WalletModel", back_populates="user")
    deliveries = relationship("DeliveryModel", back_populates="user")


class FarmModel(Base):
    __tablename__ = 'farms'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    farm_name: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)


    __table_args__ = (UniqueConstraint('user_id', name='uq_user_farm'),)

    user = relationship("UserModel", back_populates="farm")
    plants = relationship("PlantModel", back_populates="farm")


class PlantModel(Base):
    __tablename__ = 'plants'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    farm_id: Mapped[int] = mapped_column(ForeignKey('farms.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    sort_id: Mapped[int] = mapped_column(ForeignKey('sorts.id'), nullable=True)
    start_time: Mapped[int] = mapped_column(Integer, nullable=True)
    end_time: Mapped[int] = mapped_column(Integer, nullable=True)
    growing_on_percent: Mapped[int] = mapped_column(
        Integer, CheckConstraint('growing_on_percent >= 0 AND growing_on_percent <= 100'), nullable=True
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)

    sort = relationship("SortModel", back_populates="plants")
    farm = relationship("FarmModel", back_populates="plants")


class SortModel(Base):
    __tablename__ = 'sorts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable= False)
    description: Mapped[str] = mapped_column(String(255), nullable= True)
    color: Mapped[str] = mapped_column(String(255), nullable= False)
    grow_time: Mapped[int] = mapped_column(Integer(), nullable= False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    unit_weight: Mapped[float] = mapped_column(
        Float, CheckConstraint('unit_weight > 0')) #waight of fully grown unit
    min_unit_number: Mapped[float] = mapped_column(
        Float, CheckConstraint('min_unit_number >= 5 AND min_unit_number <= 25'), nullable= False)

    plants = relationship("PlantModel", back_populates="sort")



class WalletModel(Base):
    __tablename__ = 'wallets'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    card_holder = mapped_column(String(), nullable=True)
    card_number = mapped_column(String(), nullable=True)
    card_exp_date = mapped_column(String(), nullable=True)
    card_cvv = mapped_column(String(), nullable=True)
    state = mapped_column(String(), nullable=True)
    city = mapped_column(String(), nullable=True)
    apartment = mapped_column(String(), nullable=True)
    zip_code = mapped_column(String(), nullable=True)

    user = relationship("UserModel", back_populates="wallets")


class DeliveryModel(Base):
    __tablename__ = 'deliveries'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date_of_initializing: Mapped[int] = mapped_column(Integer, nullable=False)
    est_delivery: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="deliveries")
