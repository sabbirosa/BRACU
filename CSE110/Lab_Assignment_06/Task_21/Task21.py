def individul_bonus_calculation(player, earning, total_goal, bonus):
  total_earning = int(total_goal * (bonus / 100 * earning))
  
  if total_goal > 30:
     total_earning += 10000
  
  elif 20 < total_goal <= 30:
    total_earning += 5000

  print(f"{player} earned a bonus of {total_earning} Taka for {total_goal} goals.")


def cal_bonus(*infos):
  for i in range(0, len(infos), 4):
    individul_bonus_calculation(infos[i], infos[i+1], infos[i+2], infos[i+3])
  
cal_bonus("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10)