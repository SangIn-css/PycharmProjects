# 1) Ice Americano : 2000    2) Cafe Latte : 3000
while True:
    menu = input("1) Ice Americano  2) Cafe Latte  3) Exit : ")
    if menu == "1":
        print("Ice Americano ordered. Price : 2000 won")
    elif menu == "2":
        print("Cafe Latte ordered. Price : 3000 won")
    elif menu == "3":
        print("Order Finished")
        break
print("2주차 업데이트")