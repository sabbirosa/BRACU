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
