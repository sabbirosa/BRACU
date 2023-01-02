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
