print("\n\t==========BMI calculator==========\n")
print("\nTO calculate BMI(Body Mass Index) please give these details: \n \n")

a = int(input("Enter Age : "))

try:
    h =float(input("\n\nEnter Height(m) : "))
    
        
except:
    print("Please enter Numeric Value only!!")

try:
    w = float(input("\n\nEnter Weigth(kg) : "))
    
except:
    print("Please enter Numeric Value only!!")


if(h != 0 and h<2.5 and w > 0):
    bmi = float(w/h**2)
    print(f"BMI = {bmi:.2f}")

    if(bmi < 18.5):
     print("Underweight")
    elif(18.5 <= bmi < 25):
     print("Normal Weight")
    elif(25<= bmi <30):
     print("Overweight")
    else:
     print("Obese")

else:
    if(h == 0 or h>2.5):
        print("\nInvalid Input of height !!!")
        print("Please enter height in meters only")
    if(w <= 0):
        print("\nInvalid Input of weight !!!")

    print("\n\nCouldn't calculate BMI")
    print("\nTry Again\n\n")


