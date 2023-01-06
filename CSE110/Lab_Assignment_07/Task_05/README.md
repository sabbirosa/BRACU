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
