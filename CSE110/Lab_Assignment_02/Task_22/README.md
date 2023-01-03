Write a python program that converts a decimal integer number to a binary number.

`Hint:` A decimal can be converted to a binary number by keeping track of the remainders after each division of that number by 2.

For example, to convert 11 to a binary number, we can try the following approach.

```
11 // 2 = 5 (Remainder 1)
5 // 2 = 2 (Remainder 1)
2 // 2 = 1 (Remainder 0)
1 // 2 = 0 (Remainder 1)
```

Now, taking the remainders from bottom to top gives us the binary number which is 1011. Binary of 11 is 1011.

#### Test Case:

| Sample Input | Sample Output |
| :----------: | :-----------: |
|      11      |     1011      |
|      13      |     1101      |
