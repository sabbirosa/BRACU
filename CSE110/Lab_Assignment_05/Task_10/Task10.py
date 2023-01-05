given_dict = {'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure': 9}
largest_num = given_dict['sci fi']
genre = ""

for i in given_dict:
  if given_dict[i] > largest_num:
    largest_num = given_dict[i]
    genre = i

print("The highest selling book genre is" +" '"+ genre +"' "+ "and the number of books sold are", largest_num)