height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in kg"))
height=height/100
bmi=weight/(height**2)
print("Your BMI is", bmi)
if bmi>0:
    if bmi<=16:
        print("You are severly underweight")
    elif bmi<=18.5:
        print("You are underweight")
    elif bmi<=25:
        print("You are healthy")
    elif bmi<=30:
        print("You are overweight")
    else:
        print("You are severly overweight")
else:
    pring("Enter valid details")