print('Welcome to the BMI(Body Mass Index) calculator')
print("--------------------------------------------")
print('--------Select code for Operation----------')
ch=input('101: Calculate BMI\n102: View BMI Calculate\n103: Exit\n')
match ch:
    case '101':
        weight=float(input("Enter Weight in Kg: "))
        height=float(input("Enter Height in mit: "))
        bmi=weight/height**2
        print("-----------------------------------------------")
        print('Your BMI is: ',bmi)
        if bmi<=18.5:
            print('Category: Underweight')
            print('--------Health Tips----------')
            print('Eat Caloric-rice food\nEat Nuts\nEat dairy product \n Strength Training')
        elif bmi<=24.9:
            print('Category: Normal')
            print('---------Health Tips-----------')
            print('Maintain a balanced diet,\n exercise for at least 30 minutes daily, \n drink plenty of water,\n and get 7–9 hours of sleep.')
        elif bmi<=29.9:
            print('Category: Overweight')
            print('---------Health Tips-----------')
            print('Reduce sugary and fried foods,\n eat more fruits and vegetables,\n walk or exercise 45–60 minutes daily,\n and control portion sizes.')
        elif bmi<=30.0:
            print('Category: Obese')
            print('---------Health Tips-----------')
            print('Follow a healthy eating plan,\n exercise regularly,\n avoid junk food and sugary drinks,\n and consult a doctor or dietitian for a personalized weight-loss plan.')
    case '102':
        print('Category\t\tBMI range')
        print('---------------------------------')
        print('Underweight\t\t<18.5')
        print(' Normal\t\t<24.9')
        print('Overweight\t\t<29.9')
        print('Obese\t\t<30.0')
    case '103':
        print('Invalid Choice')