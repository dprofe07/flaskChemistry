class BaseChemException(Exception):
    pass


class ElementNotFoundException(BaseChemException):
    pass


class IncorrectElementNumberException(BaseChemException):
    pass


class IncorrectOrbitalNameException(BaseChemException):
    pass