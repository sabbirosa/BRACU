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
