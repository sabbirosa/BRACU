# Lab Assignment 1 (Branching) 📝

### Task 1

Write the Python code of a program that reads two numbers from the user, and prints their `sum`, `product`, and `difference`.

`Hint:` subtract the second number from the first one

#### Test Case:

| Sample Input | Sample Output                                   |
| :----------: | ----------------------------------------------- |
|   4 <br> 5   | Sum = 9 <br> Product = 20 <br> Difference = -1  |
|  30 <br> 2   | Sum = 32 <br> Product = 60 <br> Difference = 28 |

Solution: ⚡ [Task 1](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_01/Task1.py)

---

### Task 2

Write the Python code of a program that reads the radius of a circle and prints its `circumference` and `area`.

`Hint(1):` We may import math using `import math` and then use math.pi for getting the value of pi.
For details, we can read from https://docs.python.org/3/library/math.html

`Hint(2):` We can import math and use the math function for making squares with `math.pow(number, power)` or we can simply use the power operator. For example: `S\*\*2`.

#### Test Case:

| Sample Input | Sample Output                                                      |
| :----------: | ------------------------------------------------------------------ |
|      4       | Area is 50.26548245743669 <br> Circumference is 25.132741228718345 |
|     3.5      | Area is 38.48451000647496 <br> Circumference is 21.991148575128552 |

Solution: ⚡ [Task 2](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_02/Task2.py)

---

### Task 3

Write the Python code of a program that reads two numbers from the user. The program should then print `First is greater` if the first number is greater, `Second is greater` if the second number is greater, and `The numbers are equal` otherwise.

#### Test Case:

| Sample Input | Sample Output         |
| :----------: | --------------------- |
|   7 <br> 3   | First is greater      |
|  -33 <br> 3  | Second is greater     |
|  11 <br> 11  | The numbers are equal |

Solution: ⚡ [Task 3](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_03/Task3.py)

---

### Task 4

Write the Python code of a program that reads two numbers, subtracts the smaller number from the larger one, and `prints the result`.

`Hint:` First, we may check which number is greater.

#### Test Case:

| Sample Input | Sample Output |
| :----------: | :-----------: |
| -40 <br> -4  |      36       |
|   6 <br> 2   |       4       |
|   5 <br> 5   |       0       |

`Explanation:` -4 > -40 so -4 - (-40) = -4 + 40 = 36

Solution: ⚡ [Task 4](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_04/Task4.py)

---

### Task 5

Write the Python code of a program that reads a number, and prints `The number is even` or `The number is odd`, depending on whether the number is even or odd.

`Hint(1):` We may use the `modulus (%)` operator to check for even or odd.

`Hint(2):` We can consider the number to be an integer.

#### Test Case:

| Sample Input |   Sample Output    |
| :----------: | :----------------: |
|      7       | The number is odd  |
|      10      | The number is even |
|     -44      | The number is even |

Solution: ⚡ [Task 5](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_05/Task5.py)

---

### Task 6

Write the Python code of a program that reads an integer as input from the user, and `prints the integer` if it is a multiple of 2 OR 5 and prints `Not a multiple of 2 OR 5` otherwise.

For example, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22 … i.e. This includes multiples of 2 only, multiples of 5 only and multiples of 2 and 5 both.

`Hint(1):` We may use the `modulus (%)` operator for checking the divisibility.

`Hint(2):` We can consider the number to be an integer.

#### Test Case:

| Sample Input |      Sample Output       |
| :----------: | :----------------------: |
|      5       |            5             |
|      10      |            10            |
|     -44      | Not a multiple of 2 OR 5 |

Solution: ⚡ [Task 6](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_06/Task6.py)

---

### Task 7

Write the Python code of a program that reads an integer, and `prints the integer` it is a multiple of either 2 or 5 but not both. If the number is a multiple of 2 and 5 both, then print `Multiple of 2 and 5 both`. For all other numbers, the program prints `Not a multiple we want`.

For example, 2, 4, 5, 6, 8, 12, 14, 15, 16, 18, 22 … i.e. this includes multiples of 2 only and multiples of 5 only, NOT multiples of 2 and 5 both or other numbers.

`Hint(1):` We may use the `modulus (%)` operator for checking the divisibility.

`Hint(2):` We can consider the number to be an integer.

#### Test Case:

| Sample Input |      Sample Output       |
| :----------: | :----------------------: |
|      6       |            6             |
|      15      |            15            |
|      10      | Multiple of 2 and 5 both |
|      17      |  Not a multiple we want  |

Solution: ⚡ [Task 7](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_07/Task7.py)

---

### Task 8

Write the Python code of a program that reads an integer, and `prints the integer` if it is a multiple of 2 AND 5 and prints `Not multiple of 2 and 5 both` otherwise.

For example, 10, 20, 30, 40, 50 … i.e. this only includes numbers which are multiples of both 2 and 5.

`Hint(1):` We may use the `modulus (%)` operator for checking the divisibility.

`Hint(2):` We can consider the number to be an integer.

#### Test Case:

| Sample Input |        Sample Output         |
| :----------: | :--------------------------: |
|      30      |              30              |
|      15      | Not multiple of 2 and 5 both |
|      6       | Not multiple of 2 and 5 both |

Solution: ⚡ [Task 8](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_08/Task8.py)

---

### Task 9

Write the Python code of a program that finds the number of `hours`, `minutes`, and `seconds` in a `given number of seconds`. The number of seconds is taken as input from the user.

`Hint(1):` We may consider our user input to be an integer value and use // and % operators to solve the problem.

`Hint(2):` 1 hour = 60 mins = 3600 seconds and 1 min = 60 seconds.

#### Test Case:

| Sample Input | Sample Output                    |
| :----------: | -------------------------------- |
|    10000     | Hours: 2 Minutes: 46 Seconds: 40 |
|     500      | Hours: 0 Minutes: 8 Seconds: 20  |

`Explanation:` 10000 seconds = 10000 // 3600 = 2 hours and 10000 % 3600 = 2800 seconds.
Then again, 2800 // 60 = 46 minutes and 2800 % 60 = 40 seconds.
And hence we have arrived at our answer.

Solution: ⚡ [Task 9](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_09/Task9.py)

---

### Task 10

Write a Python program to compute and display a person’s `weekly salary` as determined by the following conditions:

- If the hours worked is less than or equal to 40, then the person receives Tk 200 per hour.
- If the hours worked is greater than 40, then the person receives Tk 8000 plus Tk 300 for each hour worked over 40 hours.

The program should request the hours worked as an input from the user and display the salary as output. You need to make sure that user input is valid.
For example, a person cannot work for -5 hours or more than 168 hours in a week. So, the valid hours range is 0 to 168. For invalid hours, print outputs as given in the samples below.

`Hint:` We may consider the hour (user input) to be an integer.

#### Test Case:

| Sample Input |                 Sample Output                 |
| :----------: | :-------------------------------------------: |
|     100      |                     26000                     |
|      30      |                     6000                      |
|     -30      |            Hour cannot be negative            |
|     170      | Impossible to work more than 168 hours weekly |

`Explanation:` Since, the number of hours worked is 30 < 40, therefore salary = 30 \* 200 = 6000.

Solution: ⚡ [Task 10](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_10/Task10.py)

---

### Task 11

Suppose the following expressions are used to calculate the `values of L` for different values of S:

if 𝑆 < 100, $𝐿 = 3000 − 125𝑆^2$

if 𝑆 ≥ 100, $𝐿 = \frac{12000}{4 + 𝑆^2 / 14900}$

Write the Python code of a program that reads a value of S and then calculates the value of L.

`Hint(1):` We may import math and use math function for making squares with math.pow(number, power) or you can simply write S \*\* 2.

`Hint(2):` The value of S (user input) will be an integer.

#### Test Case:

| Sample Input |   Sample Output    |
| :----------: | :----------------: |
|     120      | 2416.2162162162163 |
|      3       |        1875        |

`Explanation:` Since S (user input) in first test case given here is 120 >= 100, so L = 12000 / (4 + (120 \* 120)/14900) = 2416.2162162162163. Similarly in second test case S (user input) given here is 3 < 100, so L = 3000 - 125 \* 3 \* 3 = 1875.

Solution: ⚡ [Task 11](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_11/Task11.py)

---

### Task 12

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

Solution: ⚡ [Task 12](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_12/Task12.py)

---

### Task 13

Write the Python code of a program that reads a student’s mark for a single subject, and prints out the `corresponding grade` for that mark. The mark ranges and corresponding grades are shown in the table below. You need to make sure that the mark is valid.<br>
For example, a student cannot receive -5 or 110 marks. So, the valid marks range is 0 to 100.

| Marks       | Grade |
| :---------- | :---: |
| 90 or Above |   A   |
| 80-89       |   B   |
| 70-79       |   C   |
| 60-69       |   D   |
| 50-59       |   E   |
| Below 50    |   F   |

`Hint(1):` We may consider the number to be an integer.

`Hint(2):` This problem can be solved in two ways: top-down (starts from A) and bottom-up (starts from F).

#### Test Case:

| Sample Input | Sample Output |
| :----------: | :-----------: |
|      93      |       A       |
|      48      |       F       |
|     102      |  Wrong mark   |

Solution: ⚡ [Task 13](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_13/Task13.py)

---

### Task 14

You are designing a robot that can calculate the temperature and guess the season. Write a Python program that takes a number as input, representing the temperature in degrees Fahrenheit, and converts it into `degrees Celsius`, and then prints `the season` based on the following table:

| Temperature (degrees Celsius)     | Season |
| :-------------------------------- | :----: |
| Less than 20 degrees              | Winter |
| Between 20 degrees and 25 degrees | Autumn |
| Between 25 degrees and 30 degrees | Spring |
| Greater than 30 degrees           | Summer |

Use the following formula to convert the temperature: `(degrees Celsius) = ((degrees Fahrenheit) - 32) * 0.56`

#### Test Case:

| Sample Input |      Sample Output       |
| :----------: | :----------------------: |
|      82      | 28 degrees C <br> Spring |
|      32      | 0 degrees C <br> Winter  |

`Explanation:` The temperature in Celsius is (82 - 32) \* 0.56 = 28 degrees, which is printed. This is between 25 and 30 degrees, so “Spring” is printed after that.

Solution: ⚡ [Task 14](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_14/Task14.py)

---

### Task 15

Suppose, your friend is building an automated car called “Besla”. He needs to fix the programming of the car so that it runs at a proper speed.<br>
Now, write a python program that takes 2 inputs (distance in meters and time in seconds). The program should then print the velocity in kilometers per hour of that car. Also, it should print whether the car is working properly based on the following chart.

| Velocity                   | Information to be printed                    |
| -------------------------- | -------------------------------------------- |
| Less than 60 km/h          | Too slow. Needs more changes.                |
| Between 60 km/h to 90 km/h | Velocity is okay. The car is ready!          |
| Greater than 90 km/h       | Too fast. Only a few changes should suffice. |

#### Test Case:

|   Sample Input   |                   Sample Output                    |
| :--------------: | :------------------------------------------------: |
| 160000 <br> 7200 | 80.0 km/h <br> Velocity is okay. The car is ready! |
| 25400 <br> 3600  |    25.4 km/h <br> Too slow. Needs more changes.    |

`Explanation:` In the first test casen after the conversion of distance and time, the velocity is (160/2) km/h = 80 km/h. So the velocity is okay. And in the second test case After the conversion of distance and time, the velocity is (25.4/1) km/h = 25.4 km/h. So the speed is too slow.

Solution: ⚡ [Task 15](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_15/Task15.py)

---

### Task 16

Write a python program that takes the CGPA and no of credits completed by a student and prints whether the student is eligible for a waiver and of `what percentage`.
<br>
To be eligible for a waiver, a student must have completed at least 30 credits and earned a CGPA greater or equal to 3.8. If not, please print "The students is not eligible for a waiver".

| CGPA        | Waiver percentage |
| ----------- | ----------------- |
| 3.80 - 3.89 | 25 percent        |
| 3.90 - 3.94 | 50 percent        |
| 3.95 - 3.99 | 75 percent        |
| 4.00        | 100 percent       |

#### Test Case:

| Sample Input |                    Sample Output                    |
| :----------: | :-------------------------------------------------: |
| 3.93 <br> 78 | The student is eligible for a waiver of 50 percent. |
| 3.79 <br> 24 |      The students is not eligible for a waiver      |

Solution: ⚡ [Task 16](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_16/Task16.py)

---

### Task 17

Write the Python code of a program that reads an integer, and prints the integer if it is a `multiple of NEITHER 2 NOR 5`.
<br>
For example, 1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39 …

`Hint(1):` We may use the `modulus (%)` operator for checking the divisibility.

`Hint(2):` We can consider the number to be an integer.

#### Test Case:

| Sample Input | Sample Output |
| :----------: | :-----------: |
|      3       |       3       |
|      19      |      19       |
|      5       |      No       |
|      12      |      No       |

Solution: ⚡ [Task 17](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_17/Task17.py)

---

### Task 18

Write the Python code of a program that reads an integer, and prints the integer if it is `NOT a multiple of 2` OR `NOT a multiple of 5`.
<br>
For example, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22

`Hint(1):` We may use the `modulus (%)` operator for checking the divisibility.

`Hint(2):` We can consider the number to be an integer.

#### Test Case:

| Sample Input | Sample Output |
| :----------: | :-----------: |
|      3       |       3       |
|      15      |      15       |
|      20      |      No       |
|      14      |      14       |

Solution: ⚡ [Task 18](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_18/Task18.py)

---

### Task 19

Fiona has recently started acrylic painting and she is planning to order a few canvases and paints from an online stationery shop. The price of each 10 x 10 sized canvas is 120 tk and the price of each 25 ml paint tube is 75 tk. Depending on the total amount ordered from the shop, she will get some discounts. The table below shows the discount she will get on her total amount.

| Total Amount (TK) | Discount (TK) |
| ----------------- | :-----------: |
| 0 - 299           |  No Discount  |
| 300 - 499         |      10       |
| 500 - 749         |      20       |
| 750 - 999         |      50       |
| >= 1000           |      150      |

Write a python program and take two inputs from the user. The first input will be the number of canvases and the second input will be the number of paint tubes ordered. Based on the price of each item, calculate the `total amount` that Fiona needs to pay including the discount.

#### Test Case:

| Sample Input |                      Sample Output                       |
| :----------: | :------------------------------------------------------: |
|   5 <br> 8   | Previous total: 1200 <br> New total after discount: 1050 |
|   0 <br> 3   |  Previous total: 225 <br> New total after discount: 225  |

`Explanation:` 5 \* 120 + 8 \* 75 = 1200 Tk was her bill without discount. For 1200 Tk, the discount amount is 150 Tk. So, her new bill with a discount is (1200 - 150) = 1050 Tk.

Solution: ⚡ [Task 19](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_01/Task_19/Task19.py)
