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
