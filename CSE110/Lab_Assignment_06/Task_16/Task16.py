def splitting_money(amount):
    notes = (500, 100, 50, 20, 10, 5, 2, 1)
    remainder = amount
    results = []
    
    for i in notes:
      n, remainder = divmod(remainder, i)
      if n > 0:
        results += [f'{i} taka {n} note(s)']

    print('\n'.join(results)) 


amount = int(input())
splitting_money(amount)