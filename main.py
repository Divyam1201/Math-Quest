from random import randint

def main():
    print("\n\t\t*****___Welcome to the Math Quest :) ___*****")
    print("\n_*_Instructions:_*_")
    print("1: There are three levels in this game level 1,2 and 3 each with increasing difficulty")
    print("2: All four basic operations such as +,-,*,/ are supported")
    print("3: There are total 10 question with one points each ")
    print("4: If you answer the question correctly u will get 1 point but if u get it wrong you will get 3 tries if you cannot answer correctly 1 point will be deducted and game will over \n")

# getting the level 
    level=get_level()

    # getting the operator
    operator=get_operator()

    again=0
    score=0
#no of tries 
    tries=3

    problems=0
    # generating 10 random problems with selected operator 
    while problems<3:

        # generating random integers 
        x ,y=generate_integer(level)
     
        inp_res=0

        # selecting the operation to be performed on the basis of selected operator 
        if operator=="+":
            res=x + y
        elif operator== "-":
            res=x - y
        elif operator== "*":
            res=x * y
        elif operator=="/":
            res=x / y
            
        while tries!=0:
            if tries==-1:
                tries=1
                break
            if tries==4:
                tries=3
                break
            try:
                inp_res=int(input(f"{x} {operator} {y} = "))
            except ValueError:
                pass
# checking that the result is equal to the result input by user 
            if res==inp_res:
                score=score+1
                break

            
                # if not equal printing error and reducing the number of tries
            if tries>1:
                print(f"Careful {tries-1}/3 tries left !!!")
            else:
                print("\nno tries left")
                print("\nThe correct answer is :")
                print(f"{x} {operator} {y} = ",res)
            tries=tries-1


            # if user is not able to get the right answer displaying the result and ending the game
            if tries==0:
                if score!=0:
                    score=score-1
                 
                print("\nYou lose :( ")
                if again==0:
                    while True:
                        tryagain=input("Press T to Try again or R to restart or e to exit : ").lower()
                        if tryagain=="t":
                            print("You have gained one try make sure to make it count 🦾")
                            tries=-1
                            again=1
                            break 
                        elif tryagain=="r":
                            tries=4
                            problems=-1
                            again=1
                            score=0
                            break
                        elif tryagain=="e":
                            problems=10
                            break


        problems=problems+1

# printing final score achieved by the user 
    if 9<=score<=10:
        print(f"!! Well Done Shining Star!! Your Score is: {score}/10")
    elif 6<=score<=8:
        print(f"Keep up the hard work you will shine one day Your score is:{score}/10")
    elif 3<=score<=5:
        print(f"Practice everyday Your score is :{score}/10")
    else:
        print(f"Work hard you scored: {score}/10")
    





# function asking for level if level entered is not 1,2,3 again prompting the user for level  
def get_level():
        while True:
            num=[1,2,3]
            try:
                i=int(input("Level: "))
            except ValueError:
                pass
            else:
                if i in num:
                    return i

# function asking for operator if operator entered is not +,-,*,/ again prompting the user for the same 
def get_operator():
        while True:
            operators=["+","-","*","/"]
            o=input("operation: ")
            if o in operators:
                return o


# function generating random numbers with the number of digits based on the level,level 1 for 1 digit and so on 
def generate_integer(level):

        if level ==1:
            x=randint(0,9)
            y=randint(0,9)
        elif level==2:
            x=randint(10,99)
            y=randint(10,99)
        elif level==3:
            x=randint(100,999)
            y=randint(100,999)
        return x,y



main()





