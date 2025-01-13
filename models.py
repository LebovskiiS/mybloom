from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy import Column, Field, CheckConstraint

class Base(DeclarativeBase):
    pass



class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # Уникальный идентификатор пользователя
    name: Mapped[str] = mapped_column(String(255), nullable=False)  # Имя пользователя
    surname: Mapped[str] = mapped_column(String(255), nullable=False)  # Фамилия
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)  # Email
    phone: Mapped[str] = mapped_column(String(255), nullable=False)  # Телефон
    password: Mapped[str] = mapped_column(String(255), nullable=False)  # Пароль
    address: Mapped[str] = mapped_column(String(255), nullable=False)  # Адрес

    farms = relationship("FarmModel", back_populates="user")
    wallets = relationship("WalletModel", back_populates="user")
    deliveries = relationship("DeliveriesModel", back_populates="user")



class FarmModel(Base):
    __tablename__ = 'farms'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    farm_name: Mapped[str] = mapped_column(String(255), nullable= False)
    land_size: Mapped[int] = mapped_column(Integer, nullable= False)
    plants_id: Mapped[int] = mapped_column(ForeignKey('plants.id'), nullable= True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable= False)

    user = relationship("UserModel", back_populates="farms")
    plants = relationship("FarmModel", back_populates="farms")



class PlantModel(Base):
    __tablename__ = 'plants'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False)
    sort_id: int = Column(Integer, ForeignKey('sorts.id'), nullable=False)
    start_time: int = Column(Integer, nullable= True)
    end_time: int = Column(Integer, nullable= True)
    total_weight: int = Column(Integer, nullable= True)
    growing_on_percent: int = Column(Integer, CheckConstraint('growing_on_percent >= 0 AND growing_on_percent <= 100'),
                                     nullable=True)
    is_active: bool = Field(default=False)

    sort = relationship("SortModel", back_populates="plants")
    farms = relationship("FarmModel", back_populates="plants")








class SortModel(Base):
    __tablename__ = 'sorts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    family_id: Mapped[int] = mapped_column()
    color: Mapped[str] = mapped_column()
    grow_time: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    min_unit_number: Mapped[int] = mapped_column()

    plants = relationship("FarmModel", back_populates="sort")



class WalletModel(Base):
    __tablename__ = 'wallets'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False, unique=True)
    card_number: Mapped[str] = mapped_column(String(255), nullable=True)
    card_exp_date: Mapped[str] = mapped_column(String(5), nullable=True)
    card_cvv: Mapped[str] = mapped_column(String(3), nullable=True)
    state: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(255), nullable=True)
    apartment: Mapped[str] = mapped_column(String(255), nullable=True)
    zip_code: Mapped[str] = mapped_column(String(255), nullable=True)
    spending: Mapped[int] = mapped_column(Integer(), nullable=True)
    refill_history: Mapped[str] = mapped_column(String(), nullable=True)

    user = relationship("UserModel", back_populates="wallets")



class DeliveryModel(Base):
    __tablename__ = 'deliveries'

    id: Mapped[int] = mapped_column(primary_key=True)
    date_of_initializing: Mapped[int] = mapped_column()
    est_delivery: Mapped[str] = mapped_column()
    status: Mapped[bool] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="deliveries")




