
def unit_convertor():
    print("Welcome to the Unit Convertor.")
    print("1.Length(meters to kilometers,inches to centimeters)")
    print("2.Weight(kilograms to pounds,grams to ounces)")
    print("3.Temperature(Celsius to Fahrenheit,Fahrenhit to Celsius)")
    print("4.Exit.")

def enter_choice():
    choice = int(input("Enter your choice from (1-4) :"))
    return(choice)

def length_convertor():
    print("Choose a Conversion: ")
    print("1.Length(meter to kilometer )")
    print("2.Length(inches to centimeter )")
    choice = int(input("Enter your choice (1-2) :"))
    if (choice == 1):
        meter = float(input("Enter any value in meter :"))
        print(f"{meter}in meter = {meter/1000} in kilometer")
    elif (choice == 2):
        inches = float(input("Enter any value in inches :"))
        print(f"{inches}in inches = {2.54*inches} in centimeter")
    else:
        print("Value can't be converted.")

def weight_convertor():
    print("Choose a Convertor :")
    print("1.Weight(kilograms to pounds)")
    print("2.Weight(grams to ounces )")
    choice = int(input("Enter your choice (1-2) :"))
    if (choice == 1):
        kilograms = float(input("Enter any value in kilogram :"))
        print(f"{kilograms}in kilograms = {kilograms*2.20462}in pounds.")
    elif (choice == 2):
        grams = float(input("Enter any value in grams:"))
        print(f"{grams}in grams = {grams*0.035274} in ounces.")
    else:
        print("Value can't be converted.")

def temperature_convertor():
    print("Choose a Convertor")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenhit to Celsius")
    choice = int(input("Enter your choice (1-2): "))
    if (choice == 1):
        celsius = float(input("Enter any value in celsius: "))
        fahrenhit = (celsius*9/5)+32
        print(f"{celsius} in celsius = {fahrenhit}in fahrenhit")
    elif (choice == 2):
        fahrenhit = float(input("Enter any value in fahrenhit"))
        celsius = (fahrenhit*5/9)-32
        print(f"{fahrenhit}in fahrenhit = {celsius}in celsius")
    else:
        print("Value can't be converted")


def main():
    while True:
        unit_convertor()
        choice = enter_choice()
        if (choice == 1):
            length_convertor()
        elif (choice == 2):
            weight_convertor()
        elif (choice == 3):
            temperature_convertor()
        elif (choice == 4):
            ("Thank you for providing us this oppertunity to help you out.")
            break
        else:
            ("Entered choice is not valid.")
            break

main()
