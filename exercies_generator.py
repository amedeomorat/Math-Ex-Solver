import random

MIN_NUM_OPERATORS = 3
MAX_NUM_OPERATORS = 5
MIN_NUM = 0
MAX_NUM = 100

operators = ["+","-","*","/"]

def ex_gen():
    exercise = str(random.randint(MIN_NUM,MAX_NUM))
    N = random.randint(MIN_NUM_OPERATORS,MAX_NUM_OPERATORS)
    for i in range(N):
        sign = random.choice(operators)
        if sign == "/":
            divisors = find_divisors
            exercise = exercise + "/" + str(random.choice(divisors))
        else:
            exercise = exercise + sign + str(random.randint(MIN_NUM,MAX_NUM))
        
        
def find_divisors(num):
    divisors = [num]
    for i in range(1,num/2):
        if num%i == 0:
            divisors.append(i)
    return divisors