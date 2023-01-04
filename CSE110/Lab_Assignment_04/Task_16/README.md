Write a python program to take a list as a string input from the user and print it back to the user as a list. Please look at the examples below for clarification.

**[Must use string split() and strip() functions]**

#### Test Case:

Sample Input:

```
  '1,        2 ,            3, 50, 4'
```

Sample Output:

```
  Original data: '1,        2 ,            3, 50, 4'
  After removing square brackets: 1,        2 ,            3, 50, 4
  Numbers in string format with extra white spaces: ['1', '       2' ,'            3', '50', '4']
  Final data (numbers in list format): [1, 2, 3, 50, 4]
```

Sample Input:

```
  '[1,      2   ,            3, 50, 4]'
```

Sample Output:

```
  Original data: [1,      2   ,            3, 50, 4]
  fter removing square brackets: 1,      2   ,            3, 50, 4
  umbers in string format with extra white spaces: ['1', '      2   ', '            3', '50', '4']
  inal data (numbers in list format): [1, 2, 3, 50, 4]
```

Sample Input:

```
  "      [1,   2   ,         3,   50,   4]         "
```

Sample Output:

```
  Original data:       1,   2   ,         3,   50,   4
  After removing square brackets: 1,   2   ,         3,   50,   4
  Numbers in string format with extra white spaces: [' 1', '   2   ', '         3', '   50', '   4']
  Final data (numbers in list format): [1, 2, 3, 50, 4]
```
