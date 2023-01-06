sentence = input()
position = int(input())

def str_machine(sentence, position):
    new_str = ""
    end_str = ""
    
    for i in range(len(sentence)):
        if i == 0:
            new_str += sentence[i]
        elif i % position != 0:
            new_str += sentence[i]
        else:
            end_str += sentence[i]
    result = new_str + end_str
    return result

print(str_machine(sentence, position))