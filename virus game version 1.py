#Taran Singh
#19/11/2021
#Version 1 of Virus Simulator Game

#These will collect the country and percent infected from the user
country = str(input("What country will you like to add? "))
cases = int(input("What percentage of the chosen country is infected? "))


#Function that will receive all the data from the user and check if the cases are over 50 and print if the country is in lockdown or open.
def details():
    print(cases)
    print(country)
    if cases > 50:
        print( country + " is in Lockdown")
    else:
        print("Country is Open")


details()
