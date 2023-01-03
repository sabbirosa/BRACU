start = int(input())
end = int(input())
divisor = int(input())
product_list = []

for i in range(start, end+1):
  product = 1
  for j in str(i):
    product *= int(j)
  product_list.append(product)

for num in product_list:
  if int(num) % divisor == 0:
    print(num, end = " ")
print()
