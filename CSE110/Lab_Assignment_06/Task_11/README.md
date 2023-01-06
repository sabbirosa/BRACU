Write a function called rem_duplicate that takes a tuple in the parameter and return a tuple removing all the duplicate values. Then print the returned tuple in the function call.

**[Cannot use remove() or removed() for this task]**

`Hint:` Unlike lists, tuples are immutable, so the tuple taken as an argument cannot be modified. But the list can be modified and lastly for returning the result use type conversion. You need to use membership operators (in, not in) for preventing adding any duplicates values.

### Test Case

Function Call:

```
  rem_duplicate((1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 4, 0, 0, 0))
```

Output:

```
  (1, 2, 3, 4, 5, 6, 0)
```

Function Call:

```
  rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))
```

Output:

```
  ('Hi', 1, 2, 3, 'a', [1, 2])
```
