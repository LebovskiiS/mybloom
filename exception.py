class Base(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

class NotUniqueData(Base):
    pass


class SecurityError(Base):
    pass

class DataBaseError(Base):
    pass

class UpdateFarmFailed(Base):
    pass


class AddFarmFailed(Base):
    pass


class FarmsNotFound(Base):
    pass