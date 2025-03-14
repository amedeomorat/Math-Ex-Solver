from exercies_generator import gen_ex

EQUATION_NUM = 10

def main():
    Flag = 0
    while True:
        if Flag == 0:
            game()   
        choice = input(f"Would you like to continue playing or to exit?\n\t1. proceed\n\t2.exit\n")
        if choice == "1":
            Flag = 0
        elif choice == "0":
            print("Thank you! Bye bye :-)")
            quit()
        else:
            print("Please input a valid number.")
            Flag = 1

def game():
    wrong_ex = []
    for i in range(EQUATION_NUM):
        exercise = gen_ex()
        result = eval(exercise)
        ans = int(input(f"The number {i+1} is: {exercise}\n"))
        if ans != result:
            wrong_ex.append(exercise + "="+str(result))
        print("Thanks!\n")
    print("The following are the questions you got wrong with the correct answer.\n")
    if len(wrong_ex) == 0:
        print("Lesgosky! You got everything right!")
    else:    
        for i in wrong_ex:
            print(i)