#Taran Singh
#21/11/2021
#Virus Simulator Version 2



#List to hold all the countrys
country_list = []



NZ = ("New Zealand")
IND = ("India")
AUS = ("Australia")
country_list.append(NZ)
country_list.append(IND)
country_list.append(AUS)



#Function to ask user which country to add
def add_country():
    #Loop keeps adding country's until the user is done
    while True:
        country = input("Which country would you like to add? ")
        if country != "done":
            infected = int(input("What percent of the country is infected? "))
        #If user is done adding country's break out of function
        else:
            break
        newlist = country
        i = country_list.append(newlist)
        for i in country_list:
            print(i)

#Function to ask user if they will want to add a country
def main():
    country = input("If you would like to add in a country type in \"add\" or type in \"done\" and click enter ")
    if country.lower() == "add":
        add_country()
    elif country.lower() == "done":
        help()


if __name__ == "__main__":
    main()
