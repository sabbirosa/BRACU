# Lab Assignment 5 (Dictionary & Tuple) 📝

### Task 1

Assume, you have been given a tuple.

```
  a_tuple = ("The Institute", ("Best Mystery & Thriller", "The Silent Patient", 68821), 75717, [1, 2, 3, 400, 5, 6, 7], ("Best Fiction", "The Testaments", 98291))
```

Write one line of Python code to access and print the value 400.

`Output:`

```
  400
```

Solution: ⚡ [Task 1](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_01/Task1.py)

---

### Task 2

Assume, you have been given a tuple. Write a Python program that creates a new tuple excluding the first and last two elements of the given tuple and prints the new tuple.

`Hint:` You may use tuple slicing.

#### Test Case:

| Sample Input                 | Sample Output |
| :--------------------------- | :------------ |
| (10, 20, 24, 25, 26, 35, 70) | (24, 25, 26)  |
| (-10, 20, 30, 40)            | ()            |
| (-10, 20, 25, 30, 40)        | (25,)         |

Solution: ⚡ [Task 2](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_02/Task2.py)

---

### Task 3

Assume, you have been given a tuple.

```
  book_info = (("Best Mystery & Thriller","The Silent Patient",68,821), ("Best Horror","The Institute",75,717), ("Best History & Biography","The five",31,783 ), ("Best Fiction","The Testaments",98,291))
```

Write a Python program that prints the size of the tuple and all its elements as shown below.

Output:

```
  Size of the tuple is: 4
  ('Best Mystery & Thriller', 'The Silent Patient', 68, 821)
  ('Best Horror', 'The Institute', 75, 717)
  ('Best History & Biography', 'The five', 31, 783)
  ('Best Fiction', 'The Testaments', 98, 291)
```

Solution: ⚡ [Task 3](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_03/Task3.py)

---

### Task 4

Assume, you have been given a tuple with details about books that won the Good Reads Choice Awards.

```
  book_info = ( ("Best Mystery & Thriller","The Silent Patient",68821), ("Best Horror","The Institute",75717), ("Best History & Biography","The five",31783 ), ("Best Fiction","The Testaments",98291) )
```

Write a Python program that prints the award category, the book name, and its total votes earned as shown below.

**[Must use Tuple unpacking for printing and need to handle the quotation marks as a part of the output]**

Output:

```
  The Silent Patient won the 'Best Mystery & Thriller' category with 68821 votes
  The Institute won the 'Best Horror' category with 75717 votes
  The five won the 'Best History & Biography' category with 31783 votes
  The Testaments won the 'Best Fiction' category with 98291 votes
```

Solution: ⚡ [Task 4](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_04/Task4.py)

---

### Task 5

Write a python program that takes an input from the user and finds the number of times that the input is present in a given tuple.

```
  Given tuple: (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
```

#### Test Case:

| Sample Input | Sample Output                  |
| :----------: | :----------------------------- |
|      8       | 8 appears 4 times in the tuple |
|      1       | 1 appears 0 times in the tuple |

Solution: ⚡ [Task 5](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_05/Task5.py)

---

### Task 6

Write a Python program to reverse a given tuple.

**[You are not allowed to use tuple slicing]**

`Note:` Unlike lists, tuples are immutable. So, in order to reverse a tuple, we may need to convert it into a list first, then modify the list, and finally convert it back to a tuple.

#### Test Case:

| Given Tuple                              | Output                                   |
| :--------------------------------------- | :--------------------------------------- |
| ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') | ('h', 'g', 'f', 'e', 'd', 'c', 'b', 'a') |
| (10, 20, 30, 40, 50, 60)                 | (60, 50, 40, 30, 20, 10)                 |

Solution: ⚡ [Task 6](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_06/Task6.py)

---

### Task 7

Suppose you are given two dictionaries. Now create a new dictionary "marks", merging the two dictionaries, so that the original two dictionaries remain unchanged.

**Note: You can use dictionary functions.**

Given Dictionaries:

```
  {'Harry':15, 'Draco':8, 'Nevil':19}
  {'Ginie':18, 'Luna': 14}
```

Output:

```
  {'Harry': 15, 'Draco': 8, 'Nevil': 19, 'Ginie': 18, 'Luna': 14}
```

Given Dictionaries:

```
  {'A':90, 'B': 0}
  {'C':50}
```

Output:

```
  {'A': 90, 'B': 0, 'C': 50}
```

Solution: ⚡ [Task 7](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_07/Task7.py)

---

### Task 8

Write a Python program that takes a dictionary as an input from the user and then prints the average of all the values in the dictionary.

**[You are not allowed to use len() and sum()]**

`Hint(1):` For taking dictionary input

- Approach(1): For taking dictionary as an input from the user, you may take the whole dictionary as a string using the input() function. Then you can use the split(), strip() functions and conditions to get the keys and values from the string. Finally, you can make the dictionary using the obtained data.

- Approach(2): If the first approach seems too difficult you can create an empty dictionary and then just run a simple loop. For each iteration ask the user for a key and a value using the input() function and keep updating the dictionary with the key and value.

`Hint(2):` After you have a dictionary, you can use dictionary functions to get all the values from it, run loop to calculate the sum and the total number of values in the dictionary in order to find out the average.

#### Test Case:

| Sample Input                                 |  Sample Output  |
| :------------------------------------------- | :-------------: |
| {'Jon': 100, 'Dan':200, 'Rob':300}           | Average is 200. |
| {'Jon': 100, 'Dan':200, 'Rob':30, 'Ned':110} | Average is 110. |

Solution: ⚡ [Task 8](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_08/Task8.py)

---

### Task 9

Suppose there is a dictionary named exam_marks as given below.

```
exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
```

Write a Python program that takes an input from the user and creates a new dictionary with only those elements from 'exam_marks' whose keys have values higher than the user input (inclusive).

#### Test Case:

| Sample Input | Sample Output                                                  |
| :----------: | :------------------------------------------------------------- |
|     190      | {'Alden Cantrell': 200, 'Pierre Cox': 190}                     |
|     170      | {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Pierre Cox': 190} |

Solution: ⚡ [Task 9](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_09/Task9.py)

---

### Task 10

Write a Python program that finds the largest value with its key from a given dictionary.

**[You are not allowed to use the max() function for this task]**

`Note:` You do not need to take the dictionaries as an input from the user but your code should work for any given dictionary. Also, you need to handle the quotation marks as a part of the output.

`Hint:` Think of membership operators (in and not in). You can use dictionary functions to get the values.

### Test Case

Given Dictionary:

```
  {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
```

Output:

```
  The highest selling book genre is 'mystery' and the number of books sold are 15
```

Given Dictionary:

```
  {'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure':9}
```

Output:

```
  The highest selling book genre is 'horror' and the number of books sold are 14.
```

Solution: ⚡ [Task 10](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_10/Task10.py)

---

### Task 11

Write a Python program that takes a String as an input from the user and counts the frequency of each character using a dictionary. For solving this problem, you may use each character as a key and its frequency as values.

**[You are not allowed to use the count() function]**

`Hint:` You can create a new dictionary to store the frequencies. You may ignore case for simplicity (i.e. may consider P and p to be the same).

#### Test Case:

Sample Input:

```
  Python programming is fun
```

Sample Output:

```
  {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 3, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 's': 1, 'f': 1, 'u': 1}
```

Solution: ⚡ [Task 11](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_11/Task11.py)

---

### Task 12

Suppose you are given the following dictionary where the values are lists.

```
  dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
```

Write a Python program that counts the total number of items in a dictionary’s values and prints it. **[Without using sum(), len(), count() functions]**

`Note:` Make changes to the above dictionary and see if your code works properly for other dictionaries as well.

Output:

```
  9
```

Solution: ⚡ [Task 12](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_12/Task12.py)

---

### Task 13

Suppose you have been given the following list of tuples.

```
  list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
```

Write a Python program that converts this list of tuples into a dictionary and then prints the dictionary.

**[You are not allowed to use set]**

`Hint:` Think of membership operators (in and not in).

Output:

```
  {'a': [1, 3, 2], 'b': [2, 1], 'c': [1]}
```

Solution: ⚡ [Task 13](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_05/Task_13/Task13.py)
