You have been hired by the Abahani football club to write a function that will calculate the total bonus on the yearly earnings of each player for the total goals they have scored.

Since the number of players will vary, you decide to use the "\*args" technique that you learned in your CSE110 class.

For each player: pass the name, yearly earning, the total goal scored this season, bonus percent per goal. Additionally,

- If the goal scored is above 30, add an extra bonus of 10000 taka.
- If it is between 20 and 30 inclusive, add an extra 5000 taka.

**[For this task, there is no need to take any input from the user. Call the functions and print the values inside the function.]**

**[Must reuse the individul_bonus_calculation() function of the previous task]**

### Test Case

Function Call:

```
  cal_bonus("Neymar", 1200000, 35, 5)
```

Output:

```
  Neymar earned a bonus of 2110000 Taka for 35 goals.
```

Explaination:

```
  cal_bonus("Neymar", 1200000, 35, 5)
  bonus = 35 * (5 / 100 * 1200000) + 10000 = 2110000
```

Function Call:

```
  cal_bonus("Neymar", 1200000, 30, 10, "Jamal", 700000, 19, 5)
```

Output:

```
  Neymar earned a bonus of 3605000 Taka for 30 goals.
  Jamal earned a bonus of 665000 Taka for 19 goals.
```

Function Call:

```
  cal_bonus("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10))
```

Output:

```
  Neymar earned a bonus of 2110000 Taka for 35 goals.
  Jamal earned a bonus of 1064000 Taka for 19 goals.
  Luis earned a bonus of 205000 Taka for 25 goals.
```
