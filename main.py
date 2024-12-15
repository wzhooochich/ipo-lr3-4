print("введите три числа . программа выведет вам наибольшее из них.")
# инициализация переменных
num1=int(input("введите первое число : "))
num2=int(input("введите второе число : "))
num3=int(input("введите третье число : "))

# проверка с помощью if else
if num1>num2 and num1>num3 :
    print(num1)

elif num2>num1 and num2>num3 :
    print(num2)

elif num3>num1 and num3>num2 :
    print(num3)
    
else :
    print("ERROR")
