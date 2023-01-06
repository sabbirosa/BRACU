items = input()
item_list = []

for i in items[1:-1].split(","):
  item_list.append(i.strip()[1:-1])

def price_cal(order_items, location = "Dhanmondi"):
    item_dict = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}
    total_price = 0
    for i in order_items:
        total_price += item_dict[i]
    if location == "Dhanmondi":
        total_price += 30
    else:
        total_price += 70
    return total_price

print(price_cal(item_list, "Mohakhali"))