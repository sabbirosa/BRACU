def individul_bonus_calculation(player, earning, total_goal, bonus):
  total_earning = int(total_goal * (bonus / 100 * earning))
  
  if total_goal > 30:
     total_earning += 10000
  
  elif 20 < total_goal <= 30:
    total_earning += 5000

  print(f"{player} earned a bonus of {total_earning} Taka for {total_goal} goals.")

individul_bonus_calculation('Luis', 80000, 25, 10)