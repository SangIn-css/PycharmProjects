# 1) Ice Americano : 2000    2) Cafe Latte : 3000
drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
prices = [2000, 3000]
amount = [0, 0]
total_price = 0
# order_list = ''
while True:
    menu = input(f"1) {drinks[0]} {prices[0]}won  2) {drinks[1]} {prices[1]}  3) {drinks[2]} {prices[2]}")
    if menu == "1":
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
        break

#print(f"{drinks[0]} {prices[0]} x{amounts[0]} {prices[0]*amounts[0]}")
#print(f"{drinks[1]} {prices[1]} x{amounts[1]} {prices[1]*amounts[1]}")
#print(f"{drinks[2]} {prices[2]} x{amounts[2]} {prices[2]*amounts[2]}")
print ("Product   Price   Amount  Subtotal")
for i in range(len(drinks)):
    print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")
print(f"Total price : {total_price}")