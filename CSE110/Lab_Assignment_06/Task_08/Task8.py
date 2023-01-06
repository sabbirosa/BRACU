def show_palindrome(num):
    str_ = ""
    for i in range(1, num+1):
      str_ += str(i)
      str_ += " "
    for j in range(num-1, 0, -1):
      str_ += str(j)
      str_ += " "

    return str_

def palindrome_triangle(num):
  for i in range(1, num+1):
    for j in range((num-1)*2):
      print(end=" ")
    num -= 1
    print(show_palindrome(i))

palindrome_triangle(7)