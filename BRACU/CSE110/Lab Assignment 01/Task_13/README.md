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
