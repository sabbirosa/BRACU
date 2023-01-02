canvases = int(input())
paint_tube = int(input())

total_price = (canvases*120) + (paint_tube*75)

if total_price > 0 and total_price <= 299:
    print("Previous tota:", total_price)
    print("New total after discount: ", total_price - 0)
elif total_price > 300 and total_price <= 499:
    print("Previous total:", total_price)
    print("New total after discount: ", total_price - 10)
elif total_price > 500 and total_price <= 749:
    print("Previous total:", total_price)
    print("New total after discount: ", total_price - 20)
elif total_price > 750 and total_price <= 999:
    print("Previous total:", total_price)
    print("New total after discount: ", total_price - 50)
else:
    print("Previous total:", total_price)
    print("New total after discount: ", total_price - 150)