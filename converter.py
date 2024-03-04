miles_to_km = 1.609
farenheit_offset = 32
farenheit_factor = 9/5
kelvin = 273.15

pg = input("Which converter do you want to use?? \n (1) Miles to Km: \n (2) Degrees to Farenheit: \n (3) Degrees to Kelvin: ")

if pg == "1":
    try:
        question_miles = float(input("How many miles? "))
        total_kms = question_miles * miles_to_km
        print("{} miles equals {:.1f} kms".format(question_miles, total_kms))

    except ValueError:
        print("Please, enter a valid number for Miles!")

elif pg == "2":
    try:
        question_degrees = float(input("How  many degress? "))
        result = (question_degrees * farenheit_factor) + farenheit_offset
        print("{} degrees equals {:.1f} farenheit".format(question_degrees, result))

    except ValueError:
        print("Please, enter a valid number for Degrees!")

elif pg == "3":
    try:
        question_kelvin = float(input("How  many degress? "))
        result = question_kelvin + kelvin
        print("{} degrees equals {:.2f} kelvin".format(question_kelvin, result))

    except ValueError:
        print("Please, enter a valid number for Degrees!")

else:
    print("Please, choose option 1, 2 or 3!")