# mdk0101_practice4
Вариант 1. Алфавит
Описание классовой структуры
Есть Алфавит, характеристиками которого являются:
Язык
Список букв
Для Алфавита можно:
Напечатать все буквы алфавита
Посчитать количество букв
Так же есть Английский алфавит, который обладает следующими свойствами:
Язык
Список букв
Количество букв
Для Английского алфавита можно:
Посчитать количество букв
Определить, относится ли буква к английскому алфавиту
Получить пример текста на английском языке
  Задание
Класс Alphabet
Создайте класс Alphabet
Создайте метод __init__(), внутри которого будут определены два атрибута: 1) lang – язык и 2) letters – список букв. Начальные значения свойств берутся из входных параметров метода
Создайте метод print(), который выведет в консоль буквы алфавита
Создайте метод letters_num(), который вернет количество букв в алфавите
  Класс EngAlphabet
Создайте класс EngAlphabet путем наследования от класса Alphabet
Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). В качестве параметров ему будут передаваться обозначение языка (например, En) и строка, состоящая из всех букв алфавита (можно воспользоваться свойством ascii_uppercase из модуля string)
Добавьте приватный статический атрибут _letters_num, который будет хранить количество букв в алфавите.
Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
Переопределите метод letters_num() – пусть в текущем классе классе он будет возвращать значение атрибута _letters_num
Создайте статический метод example(), который будет возвращать пример текста на английском языке.
  Тесты (main)
Создайте объект класса EngAlphabet
Напечатайте буквы алфавита для этого объекта
Выведите количество букв в алфавите
Проверьте, относится ли буква F к английскому алфавиту
Проверьте, относится ли буква Щ к английскому алфавиту
Выведите пример текста на английском языке
    Пример вывода программы
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
26
True
False
English Example:
Don't judge a book by it's cover.
