#Taran Singh
#28/11/2021
#Virus Game Simulator Version 4

#List to hold all country objects
name_of_countrys = []
infected_percents = []
in_lockdown = []

#Function which gets input for country names form user
def add_countrys_to_game():
    add_country = ""
    #Loop allows user to keep adding countrys
    while True:
        add_country = input("Write down the country you will like to add and press enter, when you are done adding countrys type DONE and press enter. ")
        #If the user has input a valid country, add it to the list
        if add_country != "DONE":
            while len(add_country) == 0:
                print("You haven't typed anything, try again")
                add_country = input()
                infected_percent = validate_data
            infected_percent = int(input(
                ("What is the current percent of infected for? " + add_country + " and press enter. ")))
            name_of_countrys.append(add_country)
            infected_percents.append(infected_percent)
            in_lockdown.append(False)
        #If the user is done, break out of the function
        else:
            break

#Function to print the infected percent and if its in lockdown or not
def paste_data(name_of_countrys, infected_percent, in_lockdown):
    data = "" + name_of_countrys + " currently has " + str(infected_percent) + " percent infected, and "
    if infected_percent >= 80:
        in_lockdown = True
        data += "is in LOCKDOWN."
    else:
        data += "is not in LOCKDOWN."
    return data
            
#Function which asks the user which country to support
def ask_which_country_to_support():
    #String will display options for the user
    which_country = "Which country would you like to support? Choose from these options"
    for country in name_of_countrys:
        which_country += "\n" + country
    #Check if chosen option is valid
    while True:
        country_to_support = input(which_country) 
        for country in name_of_countrys:
            if country_to_support == country:
                #Return the country name if its valid
                return country_to_support
        #Error message and return to the top of the loop if the input is invalid
        print("Input is invalid, try again")



#Function runs new days. Country to support is an required argument 
def new_day(country_to_help):
    print("NEW DAY")
    list_index = 0
    for country in name_of_countrys:
        #Country chosen by the user to support will get deducted 40% of infected 
        #If chosen country is at 40% or below, it cant go less than 0% of infected
        if country == country_to_help:
            if infected_percents[list_index] >= 40:
                infected_percents[list_index] = infected_percents[list_index] - 40
            else:
                infected_percents[list_index] = 0
        #If the chosen country is at 80% or above, it cant go over 100% infected
        else:
            if infected_percents[list_index] >= 80:
                infected_percents[list_index] = 100
            else:
                infected_percents[list_index] = infected_percents[list_index] + 20
        #Print status of each countrys     
        print(paste_data(name_of_countrys[list_index], infected_percents[list_index],
                            in_lockdown[list_index]))
        list_index += 1
    print("END DAY")

add_countrys_to_game()
for i in range(0, 5):
    new_day(ask_which_country_to_support())
