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
