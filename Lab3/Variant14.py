import math  

class Shape:
    def __init__(self, shape_id):
        self._shape_id = shape_id  # Защищённый (protected, но доступен в наследниках)
        self.__shape_type = "Undefined"  # Приватный (private, доступен только внутри класса)

    def get_shape_id(self):
        return self._shape_id
    
    def set_shape_id(self, shape_id):
        print(f"Устанавливаем ID: {shape_id}")
        self._shape_id = shape_id
    
    def get_shape_type(self):
        return self.__shape_type
    
    def move(self, dx, dy):
        raise NotImplementedError("Метод move() должен быть реализован в подклассе")  

    def area(self):
        raise NotImplementedError("Метод area() должен быть реализован в подклассе")  

    def compare(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Сравнение возможно только между объектами Shape")  
        
        diff = self.area() - other.area()  
        return diff

    def is_intersect(self, other):
        raise NotImplementedError("Метод is_intersect() должен быть реализован в подклассе")  


class Quad(Shape):
    def __init__(self, shape_id, sideLen):
        super().__init__(shape_id)
        if sideLen <= 0:
            raise ValueError("Длина стороны квадрата должна быть положительной")  
        self._side_length = sideLen  
        self._Shape__shape_type = "Quad"

    def get_side_length(self):
        return self._side_length  

    def set_side_length(self, sideLength):
        if sideLength <= 0:
            print("Попытка установки некорректной длины")
            raise ValueError("Длина стороны квадрата должна быть положительной")  
        self._side_length = sideLength  
        

    def move(self, dx, dy):
        shift_x, shift_y = dx, dy
        print(f"Квадрат {self.get_shape_id()} перемещен на ({shift_x}, {shift_y})")  

    def area(self):
        return self._side_length ** 2  

    def is_intersect(self, other):
        if not isinstance(other, Quad):
            print("Ошибка типа: ожидался объект Quad")
            raise TypeError("Пересечение возможно только между объектами Quad")  
        return False  


class Pentagon(Shape):
    def __init__(self, shape_id, sideLength):
        super().__init__(shape_id)
        if sideLength <= 0:
            raise ValueError("Длина стороны пятиугольника должна быть положительной")  
        self._side_length = sideLength  
        self._Shape__shape_type = "Pentagon"

    def get_side_length(self):
        return self._side_length  

    def set_side_length(self, sLength):
        if sLength <= 0:
            raise ValueError("Длина стороны пятиугольника должна быть положительной")  
        self._side_length = sLength  
        print(f"Значение обновлено: {sLength}")

    def area(self):
        return (5 / 4) * (self._side_length ** 2) * (1 / math.tan(math.pi / 5))  

    def move(self, dx, dy):
        print(f"Пятиугольник {self.get_shape_id()} перемещен на ({dx}, {dy})")  

    def is_intersect(self, other):
        if not isinstance(other, Pentagon):
            raise TypeError("Пересечение возможно только между объектами Pentagon")  
        return False  


try:
    quad = Quad("Quad1", 5)  
    pentagon = Pentagon("Pentagon1", 4)  

    print(f"Тип квадрата: {quad.get_shape_type()}")  
    print(f"Тип пятиугольника: {pentagon.get_shape_type()}")  

    comparison = quad.compare(pentagon)  
    if comparison > 0:
        print(f"Площадь квадрата {quad.get_shape_id()} больше площади пятиугольника {pentagon.get_shape_id()}")  
    elif comparison < 0:
        print(f"Площадь квадрата {quad.get_shape_id()} меньше площади пятиугольника {pentagon.get_shape_id()}")  
    else:
        print(f"Площади квадрата {quad.get_shape_id()} и пятиугольника {pentagon.get_shape_id()} равны")  

    if quad.is_intersect(pentagon):
        print(f"Квадрат {quad.get_shape_id()} и пятиугольник {pentagon.get_shape_id()} пересекаются")  
    else:
        print(f"Квадрат {quad.get_shape_id()} и пятиугольник {pentagon.get_shape_id()} не пересекаются")  

except ValueError as e:
    print(f"Ошибка: {e}")  
except TypeError as e:
    print(f"Ошибка: {e}")  
except Exception as e:
    print(f"Неизвестная ошибка: {e}")  
