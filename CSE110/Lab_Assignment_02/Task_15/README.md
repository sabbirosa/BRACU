Write a Python program that takes a number as input from the user and tells if it is a perfect number or not.

`Perfect Number:` An integer number is said to be a perfect number if its factors, including 1 but not the number itself, sum to the number.

#### Test Case:

| Sample Input |       Sample Output        |
| :----------: | :------------------------: |
|      6       |   6 is a perfect number    |
|      28      |   28 is a perfect number   |
|      33      | 33 is not a perfect number |

`Explanation:` In first test case 6 has 4 divisors: 1, 2, 3, and 6. If we add all factors except 6 itself, 1 + 2 + 3 = 6. The sum of the factors excluding the number itself sum up to the number therefore "6 is a perfect number" is printed. And in third test case 33 has 4 divisors: 1, 3, 11, and 33. If we add all factors except itself, 15 = 1 + 3 + 11. The sum is not equal to the number, therefore 33 is not a perfect number.
