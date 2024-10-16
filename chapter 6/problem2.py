marks1=int(input("Enter Marks 1: "))
marks2=int(input("Enter Marks 2: "))
marks3=int(input("Enter Marks 3: "))

# check for total percentage
total_percentag=(100*(marks1+marks2+marks3))/300

if(total_percentag>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed :",total_percentag)

else:
    print("You failed,try again next year:",total_percentag)

