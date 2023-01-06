Write a python function that takes a list as an argument. Your task is to create a new list where each element can be present at max 2 times. Inside the function, print the number of elements removed from the given list. Finally, return the new list and print the result.

`Hint:` You may use list_name.count(element) to count the total number of times an element is in a list. list_name is your new list for this problem.

### Test Case

Function Call:

```
  function_name([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])
```

Output:

```
  Removed: 2
  [1, 2, 3, 3, 4, 5, 8, 8]
```

Function Call:

```
  function_name([10, 10, 15, 15, 20])
```

Output:

```
  Removed: 0
  [10, 10, 15, 15, 20]
```
