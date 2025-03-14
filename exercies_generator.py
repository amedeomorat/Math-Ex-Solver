import random

MIN_NUM_OPERATORS = 3
MAX_NUM_OPERATORS = 5
MIN_NUM = 0
MAX_NUM = 100

operators = ["+","-","*","/"]

def ex_gen():
    number = random.randint(MIN_NUM,MAX_NUM)
    exercise = str(number)
    N = random.randint(MIN_NUM_OPERATORS,MAX_NUM_OPERATORS)
    for i in range(N):
        sign = random.choice(operators)
        if sign == "/":
            divisors = find_divisors(number)
            number = random.choice(divisors)
            exercise = exercise + "/" + str(number)
        else:
            number = random.randint(MIN_NUM,MAX_NUM)
            exercise = exercise + sign + str(number)
    return exercise
        
        
def find_divisors(num):
    divisors = [num]
    for i in range(1,num):
        if num%i == 0:
            divisors.append(i)
    random.shuffle(divisors)
    if len(divisors)>2:
        divisors.remove(1)
        divisors.remove(num)
    return divisors