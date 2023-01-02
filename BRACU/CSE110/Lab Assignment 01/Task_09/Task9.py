input_sec = int(input())

hours = input_sec // 3600
remaining_sec = input_sec % 3600
minutes = remaining_sec // 60
seconds = remaining_sec % 60

print("Hours:", hours, "Minutes: ", minutes, "Seconds: ", seconds)