Write the python programs, which prints the following sequences of values in loops:

a) 24, 18, 12, 6, 0, -6

b) -10, -5, 0, 5, 10, 15, 20

c) 18, 27, 36, 45, 54, 63

d) 18, -27, 36, -45, 54, -63

`Hint(1):` We may use a while loop for solving these problems.

`Hint(2):` We are already familiar with the print() function. But, when we use it to print any value, it automatically adds an additional newline after each print statement.

For example:

```
  print(1)
  print(2)
```

Output:

```
  1
  2
```

`Hint(3):` To solve this problem, in Python3, we can add an extra argument (end = " ") in the print function which tells the program to skip printing the additional newline.

For example:

```
  print(1, end ="")
  print(2)
```

Output: (prints the next output right to the previous one)

```
  12
```

`Hints for 1(d):` To print negative integer we may use `string concatenation` or `multiply the integer with -1`.

For example:

```
  print(5 * (-1))
  print("-" + str(5))
```

Output:

```
  print(5 * (-1))
  print("-" + str(5))
```

`Explaination:` In Task-1(a), the loop counter may be initialized at 24 and then the loop should terminate when the loop counter reaches -6. The difference between the first two values is 24 - 18 = 6. So the loop counter value is getting decremented by 6 in every iteration for the given sequence here.
