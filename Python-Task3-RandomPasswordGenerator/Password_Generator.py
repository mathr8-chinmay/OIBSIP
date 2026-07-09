import random
import string
spcl_characters = "!@#$&*_"
while True :
    print("\n==============================================================================================================")
    print(("\t\t\t\t\t   Password Generator"))
    print("==============================================================================================================")
    while True:
        try:
            length = int(input("Enter password length : "))

            if(length>7):
                break
            elif(length <8):
                print("\nPassword lenght must be grearater than 7\n")
            else:
                print("\n!!Please Enter Valid Length!!\n")

        except:
            print("\nInvalid Input. Please Enter Numeric Value Only!!!\n\n")

    print("\nEnter character set prefrence for the password :")




    while True:
        print("\n1. Uppercase letters Password  ")
        print("\n2. Lowercase letters Password  ")
        print("\n3. Numeric Password ")
        print("\n4. special Characters password")
        try:
            print("\nEnter any two choices :- ")
            n1= int(input("\nEnter your choice (1-4) : ")) 
            n2 = int(input("\nEnter another choice (1-4) : "))


            if(n1>0 and n1<=4 and n2>0 and n2 <=4):
                break
            else:
                print("\nInvalid Choice !")
                print("\n!!Pease enter a number between 1-4 only!!\n")
                continue
        
        except:
            print("\nInvalid Input. Please Enter a Valid Number !!!\n\n")

    characters1 = ""
    characters2 = ""

    if(n1==1):
        characters1 =string.ascii_uppercase

    elif(n1==2):
        characters1 = string.ascii_lowercase

    elif(n1==3):
        characters1 = string.digits

    elif(n1==4):
        characters1 = spcl_characters


    if(n2==1):
        characters2 =string.ascii_uppercase

    elif(n2==2):
        characters2 = string.ascii_lowercase

    elif(n2==3):
        characters2 = string.digits

    elif(n2==4):
        characters2 = spcl_characters

    character_set = characters1 + characters2 

    password = ""
    for i in range(1,length+1):
        password+= random.choice(character_set)

    print("\n\n\n-------------------------------------------------------")
    print("\nPassword Generated Successfully !!!")
    print("\n\nGenerated Password : ", password , "\n")
    print("-------------------------------------------------------\n")

    print("\nEnter 1 to generate another password. ")
    print("Enter 0 to Exit. ")
    n = int(input("\nEnter here : "))


    if(n==1):
        continue
    if(n==0):
        break