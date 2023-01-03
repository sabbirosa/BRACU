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
