import exercies_generator
import time

EQUATION_NUM = 10

def main():
    Flag = 0
    while True:
        if Flag == 0:
            game()   
        choice = input(f"Would you like to continue playing or to exit?\n\t1. proceed\n\t2.exit\n")
        if choice == "1":
            Flag = 0
        elif choice == "2":
            print("Thank you! Bye bye :-)")
            quit()
        else:
            print("Please input a valid number.")
            Flag = 1

def game():
    start = time.time()
    wrong_ex = []
    for i in range(EQUATION_NUM):
        exercise = exercies_generator.ex_gen()
        result = eval(exercise)
        ans = input(f"The number {i+1} is: {exercise}\n")
        try:
            ans = int(ans)
        except ValueError:
            print("You didn't even try to insert a number...\n")
            wrong_ex.append(exercise + "="+str(result))
            continue
        if ans != result:
            wrong_ex.append(exercise + "="+str(result))
        print("Thanks!\n")
    stop = time.time()
    delta_time = stop-start
    print(f"Total time: {round(delta_time,2)} seconds.")
    if len(wrong_ex) == 0:
        print("Lesgosky! You got everything right!")
    else:
        print(f"You got {10-len(wrong_ex)} answers correct!")
        print("The following are the questions you got wrong with the correct answer.\n")
        for i in wrong_ex:
            print(i)
            
if __name__ == "__main__":
    main()