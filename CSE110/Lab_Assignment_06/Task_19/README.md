Write a python function which will take a string as an argument.

Your first task is to take a string as user input and pass the value to the function.

Your second task is to implement a function which will check whether all the alphabets from a to j (convert all the alphabets to lowercase) have appeared at least once in the given string or not.

- If all of these alphabets (a to j) appear at least once, then the result will be 5.
- If any one of the alphabets (a to j) is not in the given string, then the result will be 6.

Return this result and print the statement, "PSG will win the Champions League this season" that many times.

### Test Case

Sample Input:

```
  "A black jackal is hunting a full grown deer"
```

Function Call:

```
  function_name("A black jackal is hunting a full grown deer")
```

Output:

```
  PSG will win the Champions League this season
  PSG will win the Champions League this season
  PSG will win the Champions League this season
  PSG will win the Champions League this season
  PSG will win the Champions League this season
```

Explaination:

```
  "A black jackal is hunting a full grown deer"
  Here all the alphabets from A to J are present at least once. So, the function will return 5 and
  will print the statement 5 times.
```

Sample Input:

```
  "ABBCDEFEFGHI"
```

Function Call:

```
  function_name("ABBCDEFEFGHI")
```

Output:

```
  PSG will win the Champions League this season
  PSG will win the Champions League this season
  PSG will win the Champions League this season
  PSG will win the Champions League this season
  PSG will win the Champions League this season
  PSG will win the Champions League this season
```
