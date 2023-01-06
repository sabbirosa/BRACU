Write a function which will take 2 arguments. They are:

- Sentence
- Position

Your first task is to take these arguments as user input and pass these values to the function parameters.

Your second task is to implement the function and remove the characters at the index number which is divisible by the position (Avoid the index number 0 as it will always be divisible by the position, so no need to remove the index 0 character).

Finally, add the removed characters at the end of the new string. Return the value and then finally, print the new string at the function call.

**[Cannot use remove() or removed() for this task]**

### Test Case

Sample Input:

```
  "I love programming."
  3
```

Function Call:

```
  function_name("I love programming.", 3)
```

Output:

```
  I lveprgrmmngo oai.
```

Sample Input:

```
  "Python is easy to learn. I love python."
  6
```

Function Call:

```
  function_name("Python is easy to learn. I love python.", 6)
```

Output:

```
  Pythonis eay to earn.I lov pythn. sl eo
```
