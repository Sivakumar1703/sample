import math
name = input("enter your name he or she")
i = 1
print("hi..." + name + "..."+"i am sivakumar python developer you do simple basic calc here")
value1 =int(input("enter first value"))
value2 =int(input("enter second value"))
print("entered value1=",value1)
print("entered value2=",value2)
while i < 2:
    a=int(input("1=add,2=sub,3=multiple 4=input another value,5=sqrt,6=stop"))
    if a == 1:
        add_Value = value1 + value2
        print(add_Value)
        j = 0
        while j < 1:
            b = int(input("enter 1 to contine add, 2 to go back"))
            if b == 1:
                print(add_Value)
                value3 = int(input("+"))
                value5 = add_Value + value3
                print(value5)
                value4 = int(input("+"))
                add_Value = value5 + value4
                print(add_Value)
            else :
                j += 1
    elif a == 2:
        sub_value = value1 - value2
        print(sub_value)
    elif a == 3:
        mul_value = value1 * value2
        print(mul_value)
    elif a == 4:
        value1 = int(input("enter another value"))
        value2 = int(input("enter another value"))
        print("entered values are",value1,value2)
    elif a == 5:
        sq1 = math.sqrt(value1)
        sq2 = math.sqrt(value2)
        print(sq1,sq2)
    elif a == 6:
        i += 1

    else:
        print("enter valied number")















