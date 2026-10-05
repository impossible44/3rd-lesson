from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self, data):  # ИСПРАВЛЕНО: date изменено на data
        self.data = data

    # ИСПРАВЛЕНО: Все методы ниже теперь сдвинуты внутрь класса DataProcessor
    @abstractmethod
    def process(self):
        pass

    @staticmethod
    def validate_data(data):
        # ИСПРАВЛЕНО: Заменена точка на запятую в isinstance(data, list)
        return isinstance(data, list) and len(data) > 0

    @staticmethod
    def format_output(result):
        return f"Результат: {result}"


class NumberProcessor(DataProcessor):
    def process(self):
        # ИСПРАВЛЕНО: Исправлено имя метода на validate_data
        if not self.validate_data(self.data):
            return "Некорректные данные" # ИСПРАВЛЕНО: лучше возвращать строку, а не просто принтить
        return sum(self.data)

# Проверяем работу кода:
processor = NumberProcessor([1, 2, 3, 4, 5])
result = processor.process()

# ИСПРАВЛЕНО: Добавлена точка при вызове статического метода
print(NumberProcessor.format_output(result)) 
