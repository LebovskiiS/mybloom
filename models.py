from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String, Column, CheckConstraint, Boolean


class Base(DeclarativeBase):
    pass



class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)  # Имя пользователя
    surname: Mapped[str] = mapped_column(String(255), nullable=False)  # Фамилия
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)  # Email
    phone: Mapped[str] = mapped_column(String(255), nullable=False)  # Телефон
    password: Mapped[str] = mapped_column(String(255), nullable=False)  # Пароль
    address: Mapped[str] = mapped_column(String(255), nullable=False)  # Адрес

    farms = relationship("FarmModel", back_populates="user")
    wallets = relationship("WalletModel", back_populates="user")
    deliveries = relationship("DeliveryModel", back_populates="user")



class FarmModel(Base):
    __tablename__ = 'farms'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    farm_name: Mapped[str] = mapped_column(String(255), nullable=False)
    land_size: Mapped[int] = mapped_column(Integer, nullable=False)
    plants_id: Mapped[int] = mapped_column(ForeignKey('plants.id'), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    user = relationship("UserModel", back_populates="farms")
    plants = relationship("PlantModel", back_populates="farms")




class PlantModel(Base):
    __tablename__ = 'plants'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    sort_id: Mapped[int] = mapped_column(ForeignKey('sorts.id'), nullable=False)
    start_time: Mapped[int] = mapped_column(Integer, nullable=True)
    end_time: Mapped[int] = mapped_column(Integer, nullable=True)
    total_weight: Mapped[int] = mapped_column(Integer, nullable=True)
    growing_on_percent: Mapped[int] = mapped_column(
        Integer, CheckConstraint('growing_on_percent >= 0 AND growing_on_percent <= 100'), nullable=True
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)

    sort = relationship("SortModel", back_populates="plants")
    farms = relationship("FarmModel", back_populates="plants")



class SortModel(Base):
    __tablename__ = 'sorts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    family_id: Mapped[int] = mapped_column(Integer, nullable=False)
    color: Mapped[str] = mapped_column(String(255), nullable=False)
    grow_time: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    min_unit_number: Mapped[int] = mapped_column(Integer, nullable=False)

    plants = relationship("PlantModel", back_populates="sort")
    user = relationship("UserModel", back_populates="wallets")



class WalletModel(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Добавлен id
    user_id = Column(Integer, nullable=False)  # Поле user_id
    card_holder = Column(String(255), nullable=False)
    card_number = Column(String(16), nullable=False)
    card_exp_date = Column(String(5), nullable=False)
    card_cvv = Column(String(3), nullable=False)
    state = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    apartment = Column(String(255), nullable=False)
    zip_code = Column(String(255), nullable=False)



class DeliveryModel(Base):
    __tablename__ = 'deliveries'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date_of_initializing: Mapped[int] = mapped_column(Integer, nullable=False)
    est_delivery: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="deliveries")
