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
