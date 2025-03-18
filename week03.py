# 1) Ice Americano : 2000    2) Cafe Latte : 3000
drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
prices = [2000, 3000]
amount = [0, 0, 0]
total_price = 0



menu_lists = ""
for k in range(len(drinks)):
    menu_lists = menu_lists + f"{k+1}) {drinks[k]} {prices[k]}won   "
menu_lists = menu_lists + f"{len(drinks)+1}"
while True:
    menu = int(input(menu_lists))
    if len(drinks)>= menu >= 1:
        order_process(menu - 1)
        print(f"{drinks[0]} ordered. Price : {prices[0]}won")
        total_price = total_price + prices[0]
        amounts[0] = amount[0] + 1
    elif menu == "2":
        print(f"{drinks[1]} ordered. Price : {prices[1]}won")
        total_price = total_price + prices[1]
        amounts[1] = amount[1] + 1
    elif menu == "3":
        print(f"{drinks[2]} ordered. Price : {prices[2]}won")
        total_price = total_price + prices[2]
        amounts[2] = amount[2] + 1
    elif menu == "4":
        print("Finish order~")
    else:
        break
print ("Product   Price   Amount  Subtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:
    print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")
print(f"Total price : {total_price}")