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
