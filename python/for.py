for x in range(1, 10):
    print(x)

friends = ["Ram", "Joy", "Sam"]
for x in friends:
    print(x)

def exponent(base_num, power_num):
    result=1
    for y in range(power_num):
        result = base_num * result
    return result
print(exponent(2, 4))