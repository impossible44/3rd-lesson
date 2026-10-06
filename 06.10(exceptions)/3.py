class BaseParser:
    def parse(self,data):
        raise NotImplementedError(
            f"Класс{self.__class__.__name__} должен реалиховать метод parse"
        )
        