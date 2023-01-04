Write a Python program that takes a single string as an input from the user where few numbers are separated by commas. Now, make a list with the numbers of the given string.Then your task is to remove multiple occurences of any number and then finally print the list `without any duplicate values`.

`Hint(1):` For obtaining the numbers from the string, use split(). For cleaning the data, use strip().

`Hint(2):` You may create a third list to store the results. You can use membership operators (in, not in) to make sure no duplicates are added.

#### Test Case:

Sample Input:

```
  0, 0, 1, 2, 3, 4,      4, 5, 6, 6, 6,      7, 8, 9, 4,         4
```

Sample Output:

```
  Given numbers in list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
  List without any dupliacte values: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Sample Input:

```
  7, 7, 7, 1,           0, 3, 3,   55, 9
```

Sample Output:

```
  Given numbers in list: [7, 7, 7, 1, 0, 3, 3, 55, 9]
  List without any dupliacte values: [7, 1, 0, 3, 55, 9]
```
