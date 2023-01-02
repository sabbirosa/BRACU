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
