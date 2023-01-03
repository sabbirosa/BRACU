Write a Python program that will ask the user to enter a word as an input.

- If the length of the input string is less than 4, then your program should print the same string as an output.
- If the input string’s length is greater than 3, then your program should add "er" at the end of the input string.
- If the input string already ends with "er", then add "est" instead, regardless of the length of the input string
- If the input string already ends with "est", then your program should print the same input string as an output.

#### Test Case:

Sample Input:

```
  strong
```

Sample Output:

```
  stronger
```

`Explanation:` Length of input = 6, not less than 4, greater than 3, does not end with "er" or "est", therefore "er" is added making "strong", "stronger".

Sample Input:

```
  stronger
```

Sample Output:

```
  strongest
```

`Explanation:` Input string ends with "er", therefore "er" is replaced with "est" instead so we have "strongest" from "stronger".

Sample Input:

```
  strongest
```

Sample Output:

```
  strongest
```

`Explanation:` Our input here already ends with "est" so the same input i.e. "strongest" is printed.

Sample Input:

```
  abc
```

Sample Output:

```
  abc
```

`Explanation:` Since length of input string is less than 4, the given input is printed as output.

Sample Input 5:

```
  ber
```

Sample Output 5:

```
  best
```

`Explanation:` Although the length of the input string is 3 which is less than 4, but it ends with er so we ignore the length and replace "er" with "est" regardless.
