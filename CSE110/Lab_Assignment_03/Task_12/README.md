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
