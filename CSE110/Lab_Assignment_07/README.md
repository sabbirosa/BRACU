# Lab Assignment 7 (Searching & Sorting) 📝

### Task 1

Suppose you have a list named my_list as given below.

```
  my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
```

Now use bubble sort to sort my_list into ascending order.

Output:

```
  [1, 2, 2, 3, 5, 6, 10, 11, 12, 14, 15, 17, 18, 20, 29]
```

Solution: ⚡ [Task 1](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_01/Task1.py)

---

### Task 2

Suppose you have a list named my_list as given below

```
  my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
```

Now use bubble sort to sort my_list into ascending order.

Output:

```
  [1, 2, 2, 3, 5, 6, 10, 11, 12, 14, 15, 17, 18, 20, 29]
```

Solution: ⚡ [Task 2](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_02/Task2.py)

---

### Task 3

Suppose you have a list named my_list as given below

```
  my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
```

Now use any of the two sorting techniques you have used above to sort the list in descending order.

Output:

```
  [29, 20, 18, 17, 15, 14, 12, 11, 10, 6, 5, 3, 2, 2, 1]
```

Solution: ⚡ [Task 3](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_03/Task3.py)

---

### Task 4

Suppose you have a sitting arrangement of the students who will give the final exam in a list. The list contains the last two digits of their student ID as given below.

```
  sitting_list = [10, 30, 20, 70, 11, 15, 22, 16, 58, 100, 12, 56, 70, 80]
```

Now you want to organize the sitting arrangement of the students in your own way. You decide to sort all the students in the even indices of the list in ascending order and all the students in the odd indices of the list in descending order.

So, write a python program that organizes the list for you in this way.

Output:

```
  [10, 100, 11, 80, 12, 70, 20, 56, 22, 30, 58, 16, 70, 15]
```

Solution: ⚡ [Task 4](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_04/Task4.py)

---

### Task 5

Suppose a list contains marks earned in the courses CSE110, PHY111, and MAT110 of each student consecutively in a nested list form. Your task is to take a course name as input from the user and sort the list based on the marks obtained in that course to finally print the names of the students in descending order of marks obtained i.e. from the student who earned the highest marks to the student who earned the lowest.

For example, the list may look like

```
  lst = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]
```

where for each nested list, 1st index holds the name of the student, 2nd index is total marks earned in the CSE110 course, 3rd index is PHY111 marks and 4th index is MAT110 marks.

`Hint:` You may create a function for sorting, then call it whenever needed instead of rewriting the code. And you may get the data in the individual lists from the given nested list.

### Test Case:

Sample Input:

```
  MAT110
```

Sample Output:

```
  Alan
  Musk
  Turing
  Elon
```

`Explanation:` Here the user gives us "MAT110" as the course name. Now, the students Alan, Turing, Elon, and Musk earned 91, 83, 80, and 90 marks respectively in this course. If we sort it, Alan got the highest marks of 91 followed by Musk with 90 marks and Turing with 83 marks. Among these 4 students, Elon obtained the lowest marks in the MAT110 course with 80 marks. All of these have been illustrated in our sample output.

Sample Input:

```
  PHY111
```

Sample Output:

```
  Musk
  Elon
  Turing
  Alan
```

Solution: ⚡ [Task 5](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_05/Task5.py)

---

### Task 6

Suppose you have a list named my_list as given below. Your task is to sort the list in ascending order and print the count of numbers that have changed their positions in the process of sorting.

```
  my_list = [4, 2, 3, 1, 6, 5]
```

The sorted list would be `[1, 2, 3, 4, 5, 6]` where 4 numbers `(4, 1, 6, 5)` have changed their positions.

Therefore our sample output here would be 4. Please check if your code is working correctly by changing the above list and using the knowledge given here to verify whether your code gives the correct output for all different lists.

Output:

```
  4
```

Solution: ⚡ [Task 6](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_06/Task6.py)

---

### Task 7

Write a python program that takes two lists from the user, merges the two lists, sorts the resulting list, and then finds the median of the elements in the two lists.

### Test Case

Sample Input:

```
  list_one = [1, 2, 1, 4]
  list_two = [5, 4, 1]
```

Sample Output:

```
  Sorted list = [1, 1, 1, 2, 4, 4, 5]
  Median = 2
```

Sample Input:

```
  list_one = [1, 7, 9, 10]
  list_two = [2, 7, 6, 5]
```

Sample Output:

```
  Sorted list = [1, 2, 5, 6, 7, 7, 9, 10]
  Median = 6.5
```

Solution: ⚡ [Task 7](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_07/Task7.py)

---

### Task 8

Write a python program that takes a list from a user containing both positive and negative numbers. The program then finds two pairs of values whose summation is closest to zero.

### Test Case

Sample Input:

```
  list_one = [-10, 15, 2, 4, -4, 7, -8]
```

Sample Output:

```
  Two pairs which have the smallest sum = 4 and -4
```

Sample Input:

```
  list_one = [1, -8, 4, -7, -20, 26, 70, -85]
```

Sample Output:

```
  Two pairs which have the smallest sum = 4 and -7
```

Solution: ⚡ [Task 8](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_08/Task8.py)

---

### Task 9

You will be given a list of tuples where each tuple indicates a point i.e. (x, y) in a 2-dimensional coordinate system.

You need to write a python program to find the minimum distance and the point that is closest to the origin i.e. (0, 0)

`Hint:` The formula of distance = $√((Δx)^2 + (Δy)^2)$

As you are calculating the distance from the origin (0, 0), you can simply use distance = $√(x^2 + y^2)$

You can create a list of distances from each point and sort that list using your personal favorite sorting algorithm.

### Test Case

Sample Input:

```
  points = [(5,3), (2,9), (-2,7), (-3,-4), (0,6), (7,-2)]
```

Sample Output:

```
  Minimum distance = 5.0
  Here the closest point is (-3, -4) which has a distance of 5.0 from the origin.
```

Sample Input:

```
  points = [(1,7), (4,5), (-1,7), (-2,0), (1,1), (5,-1)]
```

Sample Output:

```
  Minimum distance = 1.4142135623730951
  Here the closest point is (1, 1) which has a distance of 1.4142135623730951 from the origin.
```

Solution: ⚡ [Task 9](https://github.com/sabbirosa/BRACU/tree/main/CSE110/Lab_Assignment_07/Task_09/Task9.py)
