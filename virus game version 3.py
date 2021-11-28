#Taran Singh
#24/11/2021
#Virus Simulator Version 3


#Stores input from user
country_list = []
num_infected = []
max_length_list = 3
country_name = ""

#Data Collection
while len(country_name) < max_length_list:
    country_name = str(input("Please enter a name of a country you will like to add. ")).upper()
    country_list.append(country_name)
    infected_percent = int(input("What percent fo the country is infected? "))
    num_infected.append(infected_percent)


#Function to print details
def print_details(self):
    details = "" + self.country_name + "has " + str(self.infected_percent) + " percent infected, and "
    if self.is_in_lockdown == True:
        details += "is in lockdown."
    else:

        details += "is not in lockdown."
    return details
    

#Function to ask user which country to help
def ask_which_country_to_help():
    help_country = "Which country would you like to help? "
    for country_name in country_list:
        help_country += "\n" + country.country_name
    #See if country name is vaild
    
    
print_details(
    )
