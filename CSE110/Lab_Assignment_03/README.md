# Lab Assignment 2 (Loops) 📝

### Task 1

Write a Python program that takes a String as an input from the user and prints that String in reverse order.

**You cannot use the built-in reverse() function for this task.**

#### Test Case:

| Sample Input | Sample Output |
| :----------: | :-----------: |
|    CSE110    |    011ESC     |
|    Python    |    nohtyP     |
|   1576527    |    7256751    |

Solution: ⚡ [Task 1](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_02/Task_01/Task1.py)

---

### Task 2

Write a python program that takes 2 inputs from the user, where the first input is a string with length greater than 1. The second input is the index of the first given string from where you have to start reversing. After reversing the first input string from that index, print the new string back to the user. See samples below for clarification.

#### Test Case:

Sample Input:

```
  72418
  4
```

Sample Output:

```
  81427
```

`Explanation:` Our second input, index '4' is the last index of our first input String '72418', hence the entire string is reversed giving us '81427'.

Sample Input:

```
  12345
  2
```

Sample Output:

```
  32145
```

`Explanation:` The second input is '2' so we have to reverse from index 2 of our first input. The 2nd index of our first input String is '3', index 1 is '2' and index 0 is '1'. Hence, if we reverse indexes 0 to 2, we get '321'. Index 3 and 4 which is '4' and '5' respectively remains unchanged hence our final output is '32145'.

Sample Input:

```
  aBcd1234defg
  5
```

Sample Output:

```
  21dcBa34defg
```

`Explanation:` From our first input String 'aBcd1234defg',

index 0 = 'a'

index 1 = 'B'

index 2 = 'c'

index 3 = 'd'

index 4 = '1'

index 5 = '2'

index 6 = '3'

Since our second input is 5, index 0 to index 5 is reversed and we have '21dcBa' and the rest is unchanged from indexes 6 to 11 ('34defg'). Therefore, we have '21dcBa34defg' finally.

Solution: ⚡ [Task 2](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_02/Task2.py)

---

### Task 3

Write a program that takes a string as input and prints “Binary Number” if the string contains only 0s or 1s. Otherwise, print “Not a Binary Number”.

#### Test Case:

| Sample Input  |    Sample Output    |
| :-----------: | :-----------------: |
|  01101101101  |    Binary Number    |
|   12344ab0    | Not a Binary Number |
|  10127490111  | Not a Binary Number |
| Binary Number | Not a Binary Number |

Solution: ⚡ [Task 3](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_03/Task3.py)

---

### Task 4

Write a Python program that will ask the user to enter a word as an input.

- If the length of the input string is less than 4, then your program should print the same string as an output.
- If the input string’s length is greater than 3, then your program should add "er" at the end of the input string.
- If the input string already ends with "er", then add "est" instead, regardless of the length of the input string
- If the input string already ends with "est", then your program should print the same input string as an output.

#### Test Case:

Sample Input:

```
  strong
```

Sample Output:

```
  stronger
```

`Explanation:` Length of input = 6, not less than 4, greater than 3, does not end with "er" or "est", therefore "er" is added making "strong", "stronger".

Sample Input:

```
  stronger
```

Sample Output:

```
  strongest
```

`Explanation:` Input string ends with "er", therefore "er" is replaced with "est" instead so we have "strongest" from "stronger".

Sample Input:

```
  strongest
```

Sample Output:

```
  strongest
```

`Explanation:` Our input here already ends with "est" so the same input i.e. "strongest" is printed.

Sample Input:

```
  abc
```

Sample Output:

```
  abc
```

`Explanation:` Since length of input string is less than 4, the given input is printed as output.

Sample Input 5:

```
  ber
```

Sample Output 5:

```
  best
```

`Explanation:` Although the length of the input string is 3 which is less than 4, but it ends with er so we ignore the length and replace "er" with "est" regardless.

Solution: ⚡ [Task 4](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_04/Task4.py)

---

### Task 5

Write a Python program that will ask the user to input a string (containing exactly one word). Then your program should print subsequent substrings of the given string as shown in the examples below.

`Hints(1):` We may use "for loop" for this task.

`Hints(2):` We may use print() function for printing newlines.

#### Test Case:

Sample Input:

```
  BANGLA
```

Sample Output:

```
  B
  BA
  BAN
  BANG
  BANGL
  BANGLA
```

`Explanation:` The length of the string is 6 so there are 6 lines where in each line a substring of the input string, of length equal to the line number is printed i.e. substring with only the letter "B" printed in the first line, substring "BA" of length 2 printed in the 2nd line, "BAN" length of which is 3 being printed in the 3rd line and so on.

Sample Input:

```
  DREAM
```

Sample Output:

```
  D
  DR
  DRE
  DREA
  DREAM
```

`Explanation:` TSimply, no of lines = length of the input string and no of letters in each line = line number.

Solution: ⚡ [Task 5](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_05/Task5.py)

---

### Task 6

Write a Python program that will ask the user to input a string (containing exactly one word). Then print the ASCII code for each character in the String using the ord() function.

To check if your program is working correctly or not, you can find a list of all correct values from the following website. You may look at “Dec” and “Char” columns only and ignore the other columns for this problem.
link: http://www.asciitable.com

#### Test Case:

Sample Input:

```
  Programming
```

Sample Output:

```
  P : 80
  r : 114
  o : 111
  g : 103
  r : 114
  a : 97
  m : 109
  m : 109
  i : 105
  n : 110
  g : 103
```

`Explanation:` Each line prints a letter sequentially from the given string and its corresponding ASCII value separated by " : ".

Sample Input:

```
  hunger
```

Sample Output:

```
  h : 104
  u : 117
  n : 110
  g : 103
  e : 101
  r : 114
```

Solution: ⚡ [Task 6](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_06/Task6.py)

---

### Task 7

Write a Python program that takes a string as an input from the user containing all small letters and then prints the next alphabet in sequence for each alphabet in the input.

`Hint:` You may need to use the functions ord() and chr(). The ASCII value of ‘a’ is 97 and ‘z’ is 122.

#### Test Case:

| Sample Input | Sample Output |
| :----------: | :-----------: |
|     abcd     |     bcde      |
|   the cow    |    uif!dpx    |
|    xyzabc    |    yzabcd     |

Solution: ⚡ [Task 7](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_07/Task7.py)

---

### Task 8

Write a Python program that takes a String as input from the user, removes the characters at even index and prints the resulting String in uppercase without using the built-in function upper().

#### Test Case:

| Sample Input | Sample Output |
| :----------: | :-----------: |
|    String    |      TIG      |
|     abcd     |      BD       |

`Explanation:` The characters in first input 'S', 'r' and 'n' are at index positions 0, 2, and 4 respectively. Hence they are removed and the remaining characters 'tig' are capitalized giving us output 'TIG'.

Solution: ⚡ [Task 8](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_08/Task8.py)

---

### Task 9

Write a python program that splits a given string on a given split character. The first input is a String and the second input is the character that will be used to split the first String.

**[You cannot use the built-in split function for this task]**

#### Test Case:

Sample Input:

```
  This-is-CSE110
  -
```

Sample Output:

```
  This
  is
  CSE110
```

`Explanation:` The second input which is the character '-', is used to split or divide the first input String 'This-is-CSE110' into 'This', 'is' and 'CSE110' which are printed individually in separate lines.

Sample Input:

```
  tom@gmail,harry@yahoo,bob@gmail,mary@gmail
  ,
```

Sample Output:

```
  tom@gmail
  harry@yahoo
  bob@gmail
  mary@gmail
```

Solution: ⚡ [Task 9](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_09/Task9.py)

---

### Task 10

Given a string, create a new string with all the consecutive duplicates removed.

`Hint:` You may make a new string to store the result. You can check whether the current character and the next character are the same, then add that character to the new string.

`Note:` Only consecutive letters are removed not all duplicate occurences of a letter. You may try doing this alternative i.e. removing all duplicate letters from a given string, for your own practice.

#### Test Case:

Sample Input:

```
  AAABBBBCDDBBECE
```

Sample Output:

```
  ABCDBECE
```

`Explanation:` From the 3 consecutive "A"s, 2 are removed and we have 'A' only. Then from the 4 consecutive 'B's, 3 are removed and only one is added to the new string giving us "AB". Since we have only one 'C' next, it is added making the resulting string "ABC" now and so on.

Sample Input:

```
  Jupyter Notebook is better. Case sensitivity check AAaaaAaaAAAa.
```

Sample Output:

```
  Jupyter Notebok is beter. Case sensitivity check AaAaAa.
```

`Explanation:` Just the 2 consectutive 'o's and 't's are changed to one at first and the uppercase 'A' and lowercase 'a' are treated separately i.e. case sensitive when checking for consecutive duplicates.

Solution: ⚡ [Task 10](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_10/Task10.py)

---

### Task 11

Write a python program that takes 2 inputs from the user. The first input is a string and the second input is a letter. The program should remove all occurences of the letter from the given string and print the output. If the letter is not found in the string and the length of string is greater than 3, then remove the first letter and last letter of the given string and print it. Otherwise print the string as it is. You can assume that all the input will be in lowercase letter.

#### Test Case:

Sample Input:

```
  tanjiro kamado
  a
```

Sample Output:

```
  tnjiro kmdo
```

`Explanation:` All 3 instances of the character 'a' is removed from the input String 'tanjiro kamado' to give us output 'tnjiro kmdo'.

Sample Input:

```
  eren yeager
  k
```

Sample Output:

```
  ren yeage
```

`Explanation:` The character 'k' is absent in the first input String 'eren yeager' and it's length is 11 which is greater than 3 therefore the first character 'e' and the last character 'r' is removed. Hence, the final String is 'ren yeage'.

Sample Input:

```
  hi
  a
```

Sample Output:

```
  hi
```

`Explanation:` The letter 'a' is not found in our first input 'hi', the length of which is 2. Since the character is not present and the length is less than 3, we print the String 'hi' as it is.

Solution: ⚡ [Task 11](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_11/Task11.py)

---

### Task 12

Write a Python program that will take one input from the user made up of two strings separated by a comma and a space (see samples below). Then create a mixed string with alternative characters from each string. Any leftover chars will be appended at the end of the resulting string.

`Hint:` For adding the leftover characters you may use string slicing.

`Note:` Please do not use lists for this task.

#### Test Case:

Sample Input:

```
  ABCD, efgh
```

Sample Output:

```
  AeBfCgDh
```

`Explanation:` At first, the two strings divided by ", " should be separated. Then the first character of the first string 'A' is concatenated with the first character of the second string 'e' which in turn is concatenated to the second character of the first string 'B', the second character of the second string f and so on since the strings are of equal length.

Sample Input:

```
  ABCDENDFGH, ijkl
```

Sample Output:

```
  AiBjCkDlENDFGH
```

`Explanation:` Here, since the length of the first string is greater than the length of the second string, after separation, the characters are concatenated alternatively as in sample input/output 1, till the length of the second string i.e. ijkl. Since, there are no more characters in the second string after that, the remaining characters if the first string i.e. ENDFGH in this case are concatenated at the end of the final string.

Sample Input:

```
  ijkl, ABCDENDFGH
```

Sample Output:

```
  iAjBkClDENDFGH
```

`Explanation:` This time, the length of the second string is greater than the length of the first string therefore the first letters of the 2 strings 'i' and 'A', then the second letters 'j' and 'B' and so on are being concatenated until there are no more letters in the first shorter string following which the remaining letters i.e. ENDFGH again in this case too (this may be different for other different string inputs) are added at the end giving us the resulting output string.

Solution: ⚡ [Task 12](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_12/Task12.py)

---

### Task 13

Suppose you are given two strings, s1, and s2. Now, print a new string made up of the last characters and then the first characters of the input strings.

#### Test Case:

Sample Input:

```
  new
  string
```

Sample Output:

```
  gwsn
```

`Explanation:` The last character of the String s2 is 'g'. The last character of the String s1 is 'w'. The first character of the String s2 is 's'. The first character of the String s1 is 'n'. Together they give us the ouput we want 'gwsn'.

Sample Input:

```
  abcd
  efgh
```

Sample Output:

```
  hdea
```

`Explanation:` The last characters of the Strings s2 and s1 is 'h' and 'd' respectively while the first characters of the Strings is 'e' and 'a' respectively. Together they give us the ouput we want 'gwsn'.

Solution: ⚡ [Task 13](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_13/Task13.py)

---

### Task 14

Write a python program that takes two inputs. The first input is a string and the second input is a number. If the number is even then concatenate the given string two times the given number and if the number is odd then concatenate the given string three times the given number.

#### Test Case:

Sample Input:

```
  CSE110
  4
```

Sample Output:

```
  CSE110CSE110CSE110CSE110CSE110CSE110CSE110CSE110
```

`Explanation:` The second input which is the number 4 is even, therefore the first string input 'CSE110' is concatenated(joined together) 4\*2 = 8 times.

Sample Input:

```
  CSE110
  3
```

Sample Output:

```
  CSE110CSE110CSE110CSE110CSE110CSE110CSE110CSE110CSE110
```

Solution: ⚡ [Task 14](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_14/Task14.py)

---

### Task 15

Write a python program that takes a string as an input from the user and then modifies the string in such a way that the string always starts with an uppercase letter and the case of each subsequent letter is the opposite of the previous letter (uppercase character followed by a lowercase character followed by an uppercase character and so on). Finally the modified string is printed to show the user.

`Hint:` Flags/counters can be used to manage uppercase-lowercase.

#### Test Case:

|          Sample Input           |          Sample Output          |
| :-----------------------------: | :-----------------------------: |
| Python programming is very easy | PyThOn PrOgRaMmInG iS vErY eAsY |
|    I love Python Programming    |    I lOvE pYtHoN pRoGrAmMiNg    |
|          CSE110 Course          |          CsE110 cOuRsE          |
|                c                |                C                |

Solution: ⚡ [Task 15](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_03/Task_15/Task15.py)
