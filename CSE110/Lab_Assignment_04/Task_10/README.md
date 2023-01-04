Write a Python program that reads a string as an input from the user where multiple numbers are separated by commas. Then, make a list of numbers from the input string and print the list. Finally, remove multiple occurences of any numbers from the input list and print the modified list without duplicate values.

`Hint:` You may create a third list to store the results but you may try doing it in the same input list. You can use membership operators (in, not in) to make sure no duplicates are added.

#### Test Case:

Sample Input:

```
  0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4
```

Sample Output:

```
  Original list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
  Modified list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```
  7, 7, 7, 1, 0, 3, 3, 55, 9
```

Sample Output:

```
  Original list: [7, 7, 7, 1, 0, 3, 3, 55, 9]
  Modified list: [7, 1, 0, 3, 55, 9]
```
