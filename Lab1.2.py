s = (input("Введите ваше имя "))
t = int(input("Введите ваш возраст "))
i = input("Вы праздновали День Рождения в этом году?")
n = (input("В каком городе вы проживаете? "))
g = (input("В какой стране вы проживаете? "))
if i == "да":
    i = 2023
else:
    i = 2022
e = (-t + i)
print("Уважаемый",s, "!",
      "На сегодняшний день Вы проживаете в стране",g,"в городе",n ,
      "и вы родились в",e,"году" )