Write a Python program that takes an hour from the user as input and tells it is `time for which meal`.

- The user will input the number in a 24-hour format. So, 14 means 2 pm, 3 means 3 am, 18 means 6 pm, etc.
- Valid inputs are 0 to 23. Inputs less than 0 or more than 23 are invalid in 24-hour clock.
- Assume, input will be whole numbers. For example, 3.5 will NOT be given as input.

```bash
Input range: Message to be printed
4 to 6: "Breakfast"
12 to 13: "Lunch"
16 to 17: "Snacks"
19 to 20: "Dinner"
For all other valid inputs: "Patience is a virtue"
For all other invalid inputs: "Wrong time"

For example,
If the user enters 4, your program should print the message "Breakfast".
If the user enters 5, your program should print the message "Breakfast".
If the user enters 6, your program should print the message "Breakfast".
If the user enters 0, your program should print the message "Patience is a virtue".
If the user enters 1, your program should print the message "Patience is a virtue".
If the user enters 18, your program should print the message "Patience is a virtue".
If the user enters 23, your program should print the message "Patience is a virtue".
If the user enters 24, your program should print the message "Wrong Time".
If the user enters -1, your program should print the message "Wrong Time".
If the user enters 27, your program should print the message "Wrong time".
```

`Hint:` We may use nested conditionals (if-else) or chained conditions (if-elif-else) to solve this problem.

#### Test Case:

| Sample Input Range |    Sample Output     |
| :----------------: | :------------------: |
|         5          |      Breakfast       |
|         13         |        Lunch         |
|         18         | Patience is a virtue |
|         -5         |      Wrong time      |
