from sqlalchemy import except_


def filter_list():
    a=[]
    b=[]
    try:
        n = int(input("введите количество элементов"))
    except ValueError:
         print("ВВЕДИТЕ ЧИСЛО")
         return filter_list()
    for i in range(n):
        element = input(f"введите элементы списка{i + 1}:  ")
        a.append(element)
    print("список:", a)


    for element in a:
        if element.endswith("http://"):
            b.append(element)
    print(b)

filter_list()




