def show_palindrome(num):
    str_ = ""
    for i in range(1, num+1):
      str_ += str(i)
    for j in range(num-1, 0, -1):
      str_ += str(j)
    
    return str_

print(show_palindrome(5))