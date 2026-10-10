x = float(input())
y = float(input())


if x >= 0:
    if x**2 + y**2 <= 1:
        print("Да")
    else:
        print("Нет")

else:
  
    if y >= 0:
        if x**2 + y**2 <= 1:
            print("Да")
        else:
            print("Нет")
    else:
        if x + y >= -2:
            print("Да")
        else:
            print("Нет")
