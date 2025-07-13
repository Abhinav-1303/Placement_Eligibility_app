is_male = True

if(is_male):
    print("You are male")

is_male = True
is_tall = False

if(is_male or is_tall):
    print("You are male or tall")

else:
    print("You are not male")

if(is_male and is_tall):
    print("You are male or tall")

else:
    print("You are not male")

if(is_male and is_tall):
    print("You are tall male")
elif(is_male) and not(is_tall):
    print("You are short male")
elif(not(is_male) and is_tall):
    print("You are not male and tall")
else:
    print("You are nothing")


def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
print(max_num(200, 256, 322))