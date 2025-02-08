def permut(string, answer=""):
    if len(string) == 0:
        print(answer)
    else:
        for i in range(len(string)):
            permut(string[:i] + string[i+1:], answer + string[i])

user_input = input("Enter a string: ")
permut(user_input)