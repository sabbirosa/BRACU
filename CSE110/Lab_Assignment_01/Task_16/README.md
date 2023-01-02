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
