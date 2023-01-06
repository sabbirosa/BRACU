You have been hired as an app developer for the company. The company plans to make an app for a grocery store where the user can order groceries and see the total amount to be paid in the cart section.

To build this feature, you have to write a function that takes 2 arguments. They are:

- order_items (must be a list)
- location (default value should be set to "Dhanmondi")

Your first task is to take a list of items from the user. Pass the list into the function parameter along with the optional location (Use default argument technique). (Also, no need to take location as input, pass this any value you want.)

Your second task is to implement the function. In the function, create a dictionary for the items shown in the table. Calculate the total price of the items passed as a list to the function.

Additionally, add a delivery fee of 30 taka if the location is Dhanmondi. Otherwise, add a delivery fee of 70 taka. Finally, return the value and print it.

|  Item   | Price (Tk) |
| :-----: | :--------: |
|  Rice   |    105     |
| Potato  |     20     |
| Chicken |    250     |
|  Beef   |    510     |
|   Oil   |     85     |

`Hint:` The keys are the items and values are the corresponding price. Iterate the items in the list
and check if the items in the list are available in the dictionary keys or not. If it is available, add
the price.

### Test Case

Sample Input:

```
  ["Rice", "Beef", "Rice"]
```

Function Call:

```
  function_name(["Rice", "Beef", "Rice"], "Mohakhali")
```

Output:

```
  790
```

Explaination:

```
  function_name(["Rice", "Beef", "Rice"], "Mohakhali")
  total = 105 + 510 + 105 = 720 (Take the price of each item and add them.)
  total = 720 + 70 = 790 (Finally, add the delivery fee based on the location.)
```

Sample Input:

```
  ["Rice", "Beef", "Rice"]
```

Function Call:

```
  function_name(["Rice", "Beef", "Rice"])
```

Output:

```
  750
```

Explaination:

```
  function_name(["Rice", "Beef", "Rice"])
  total = 105 + 510 + 105 = 720 (Take the price of each item and add them.)
  total = 720 + 30 = 750 (Since no location is passed in the parameter, it will use the default location-"Dhanmondi". For Dhanmondi, delivery fee of 30 taka)
```
