"""Module providing a function printing text."""


def main():
    """Function printing text."""
    print("Hello world!")


if __name__ == "__main__":
    main()
 язакатаю, 
# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
A = "www.my_site.com#about"
print(A.replace("#", "/"))

# Напишите программу, которая добавляет ‘ing’ к словам
B = "word"
print(B + "ing")

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
C = "Ivanou Ivan"
C1 = C.split()
print(C1[1] + " " + C1[0])

# Напишите программу которая удаляет пробел в начале, в конце строки
# // написала для случая удаления и в начале, и в конце
D = " Тестовая строка с пробелами "
print(D.strip())

# Имена собственные всегда начинаются с заглавной буквы,
# за которой следуют строчные буквы.
# Исправьте данное имя собственное так,
# чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"у
E = "pARiS"
print(E.capitalize())
