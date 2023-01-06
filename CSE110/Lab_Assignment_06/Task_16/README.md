Write a function called splitting_money that takes an “amount” of money as an argument.

Your first task is to take the “amount” of money as user input and pass the value to the function parameter.

Your second task is to implement the function and calculate how that money can be split into 500, 100, 50, 20, 10, 5, 2, and 1 taka notes.

Then print the returned value in the function call.

`Hint:` This task’s calculation is similar to Assignment-1’s seconds to hours, minutes conversion. To return the result containing multiple strings, you need to store it in a variable and return it at the end of the function.

### Test Case

Sample Input:

```
  1234
```

Function Call:

```
  splitting_money(1234)
```

Output:

```
  500 Taka: 2 note(s)
  100 Taka: 2 note(s)
  20 Taka: 1 note(s)
  10 Taka: 1 note(s)
  2 Taka: 2 note(s)
```

Sample Input:

```
  151
```

Function Call:

```
  splitting_money(151)
```

Output:

```
  100 Taka: 1 note(s)
  50 Taka: 1 note(s)
  1 Taka: 1 note(s)
```
