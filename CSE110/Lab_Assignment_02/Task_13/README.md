Write a Python program that takes a number from the user and prints its digits **from left to right**.

**[Consider the input number to be an INTEGER. You are not allowed to use String indexing for solving this task]**

Example: if the user gives 32768, then print 3, 2, 7, 6, 8

`Hint(1):` The input() function takes the input data as String data type by default. Please convert it to an integer before starting your code for the task.

`Hint(2):` First, count how many digits. Then, calculate 10 to the power (number of digits - 1). Say, the input given by the user as in our example, 32768 has 5 digits, so calculating 10 to the power 4 gives us 10000. Then floor dividing 32768 by 10000, we can get 3. Proceeding further, the remainder of 32768 by 10000 (32768 % 10000) gives us 2768. This time to get 2 we need to floor divide 2768 by 1000 which is basically our 10000/10. Again, taking remainder of 2768 by 1000 gives us 768 which we then divide by 100 (i.e. 1000/10) and keep on doing this until there are no more digits left (zero).

**To summarize and clarify:**

- Loop 1: First, we count digits like our Task 12, say 5 in this case for 32768
- Loop 2: Then, we calculate 10 to the power 4 (5-1), that is 10000.
- Loop 3: Then we keep repeating the three steps of floor dividing, modulus and dividing by 10 as demonstrated below.

```
32768 // 10000 = 3
32768 % 10000 = 2768
10000 // 10 = 1000

2768 // 1000 = 2
2768 % 1000 = 768
1000 // 10 = 100

768 // 100 = 7
768 % 100 = 68
100 // 10 = 10

68 // 10 = 6
68 % 10 = 8
10 // 10 = 1

8 // 1 = 8
8 % 1 = 0
1 // 10 = 0
```

Done. Loop ends as number has become 0.

#### Test Case:

| Sample Input |  Sample Output   |
| :----------: | :--------------: |
|    32768     |  3, 2, 7, 6, 8   |
|    132929    | 1, 3, 2, 9, 2, 9 |
