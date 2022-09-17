a = int(input("введите число "))
b = int(input("введите число "))
c = input("Что вы хотите сделать? ")
if c =="+":
    print(a +b)
elif c =="-":
    print(a-b)
elif c =="/":
    print(a/b)
elif c =="*":
    print(a*b)
else:
    print("упс, что то пошло не так")