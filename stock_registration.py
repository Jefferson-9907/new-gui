class StockRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del stock de un producto y
        establecer todos los datos en la tabla de la base de datos backend
    """

    def __init__(self, stock):
        self.__stock = stock

    # ===========================set methods=======================

    def set_stock(self, stock):
        self.__stock = stock

    # =====================get methods========================

    def get_stock(self):
        return self.__stock


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
