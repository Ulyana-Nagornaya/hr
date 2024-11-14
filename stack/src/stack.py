'''
Создание стека

Цель: Создать класс для реализации ограниченного стека с использованием наследования в Python. 
Стек должен поддерживать основные операции и обеспечивать обработку ошибок.
'''

class StackError(Exception):
    """
    Класс для обработки ошибок стека.
    """
    pass

class Stack:
    """
    Базовый класс для стека.
    """
    
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def size(self):
        """
        Возвращает количество элементов в стеке.
        """
        return len(self.items)

    def empty(self):
        """
        Проверяет, пуст ли стек.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Добавляет элемент на вершину стека.
        """
        if not isinstance(item, int):  
            raise StackError("Ошибка: только целые числа могут быть добавлены в стек.") # Проверка на тип данных
        if self.size() >= self.capacity:
            raise StackError("Ошибка: стек переполнен.") # Переполнение стека
        self.items.append(item)

    def pop(self):
        """
        Удаляет элемент с вершины стека и возвращает его.
        """
        if self.empty():
            raise StackError("Ошибка: стек пуст.") # Пустой стек
        return self.items.pop()

    def top(self):
        """
        Возвращает элемент на вершине стека без его удаления.
        """
        if self.empty():
            raise StackError("Ошибка: стек пуст.")
        return self.items[-1]

class LimitedStack(Stack):
    """
    Класс для ограниченного стека с наследованием от Stack.
    """
    
    def __init__(self, capacity=10):
        super().__init__(capacity)

# Пример использования
if __name__ == "__main__":
    stack = LimitedStack(19)
    
    # Пример добавления элементов в стек
    try:
        for i in range(20):  # Попробуем добавить 12 элементов
            stack.push(i)
            print(f"Добавлено: {i}, размер стека: {stack.size()}")
        
        # # Попробуем добавить неверный тип данных
        # stack.push("строка")
    except StackError as e:
        print(e)

    # # Попробуем удалить элементы из стека
    # try:
    #     while not stack.empty():
    #         print(f"Удалено: {stack.pop()}, размер стека: {stack.size()}")
        
    #     # Попробуем удалить элемент из пустого стека
    #     stack.pop()
    # except StackError as e:
    #     print(e)

    # # Попробуем получить верхний элемент из пустого стека
    # try:
    #     stack.top()
    # except StackError as e:
    #     print(e)