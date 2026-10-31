
## 1. City codes and country codes

city_codes = {
    "Tehran": "021",
    "Qom": "025",
    "Isfahan": "031",
    "Alborz": "026",
    "East Azerbaijan": "041",
    "West Azerbaijan": "044",
    "Ardabil": "045",
    "Bushehr": "077",
    "Chaharmahal": "038",
    "Fars": "071",
    "Gilan": "013",
    "Golestan": "017",
    "Hamadan": "081",
    "Hormozgan": "076",
    "Ilam": "084",
    "Kerman": "034",
    "Kermanshah": "083",
    "Khorasan Razavi": "051",
    "North Khorasan": "058",
    "South Khorasan": "056",
    "Khuzestan": "061",
    "Kohgiluyeh": "074",
    "Kurdistan": "087",
    "Lorestan": "066",
    "Markazi": "086",
    "Mazandaran": "011",
    "Qazvin": "028",
    "Semnan": "023",
    "Sistan": "054",
    "Yazd": "035",
    "Zanjan": "024"
}

country_codes = {
    "Turkey": "90",
    "Germany": "49",
    "England": "44",
    "Iraq": "964",
    "UAE": "971",
    "Afghanistan": "93"
}


## 2. Input function
## Enter 0 to go back or cancel

def get_input(message):

    answer = input(message)

    if answer == "0":
        return None

    return answer


## 3. Get phone number

def get_phone_number():

    while True:

        print("\n1. Iranian mobile")
        print("2. Iranian city phone")
        print("3. Foreign phone")
        print("4. Service number")
        print("0. Back")

        choice = get_input("Choose phone type: ")

        if choice is None:
            return None

        ## Iranian mobile

        if choice == "1":

            number = get_input("Enter mobile number: ")

            if number is None:
                continue

            if number.isdigit() and len(number) == 11 and number.startswith("09"):
                return number

            print("Invalid mobile number! Try again.")


        ## Iranian city phone

        elif choice == "2":

            while True:

                print("\nDo you know the city code?")
                print("1. Yes")
                print("2. No")
                print("0. Back")

                answer = get_input("Choose 1 or 2: ")

                if answer is None:
                    break

                if answer == "1":

                    city_code = get_input("Enter city code with 0: ")

                    if city_code is None:
                        continue

                    if city_code in city_codes.values():
                        break

                    print("Invalid city code!")

                elif answer == "2":

                    print("\nCity codes:")

                    i = 1

                    for city, code in city_codes.items():
                        print(i, ".", city, "-", code)
                        i += 1

                    city_choice = get_input("Choose city number: ")

                    if city_choice is None:
                        continue

                    city_code = ""

                    i = 1

                    for city, code in city_codes.items():

                        if city_choice == str(i):
                            city_code = code

                        i += 1

                    if city_code != "":
                        break

                    print("Invalid choice!")

                else:
                    print("Invalid choice!")

            if answer is None:
                continue

            while True:

                number = get_input("Enter local phone number: ")

                if number is None:
                    break

                if number.isdigit() and len(number) == 8:
                    return city_code + number

                print("Invalid phone number!")

        ## Foreign phone

        elif choice == "3":

            while True:

                print("\nDo you know the country code?")
                print("1. Yes")
                print("2. No")
                print("0. Back")

                answer = get_input("Choose 1 or 2: ")

                if answer is None:
                    break

                if answer == "1":

                    country_code = get_input("Enter country code without +: ")

                    if country_code is None:
                        continue

                    if country_code in country_codes.values():
                        break

                    print("Invalid country code!")

                elif answer == "2":

                    print("\nCountry codes:")

                    i = 1

                    for country, code in country_codes.items():
                        print(i, ".", country, "-", "+" + code)
                        i += 1

                    country_choice = get_input("Choose country number: ")

                    if country_choice is None:
                        continue

                    country_code = ""

                    i = 1

                    for country, code in country_codes.items():

                        if country_choice == str(i):
                            country_code = code

                        i += 1

                    if country_code != "":
                        break

                    print("Invalid choice!")

                else:
                    print("Invalid choice!")

            if answer is None:
                continue

            while True:

                number = get_input("Enter phone number without country code: ")

                if number is None:
                    break

                if number.isdigit() and 6 <= len(number) <= 12:
                    return "+" + country_code + number

                print("Invalid phone number!")

        ## Service number

        elif choice == "4":

            number = get_input("Enter service number: ")

            if number is None:
                continue

            if number.isdigit() and 3 <= len(number) <= 5:
                return number

            print("Invalid service number!")

        else:
            print("Invalid choice!")


## 4. Get and check email

def get_email():

    while True:

        email = get_input("Enter email address use @gmail.com in the end  (0 to cancel): ")

        if email is None:
            return None

        if email == "":
            print("Email cannot be empty!")
            continue

        if (
            email.count("@") == 1
            and "." in email.split("@")[1]
            and " " not in email
            and not email.startswith("@")
            and not email.endswith(".")
        ):
            return email

        print("Invalid email address! Try again.")


## 5. Get address

def get_address():

    while True:

        address = get_input("Enter address (0 to cancel): ")

        if address is None:
            return None

        address = address.strip()

        if address != "":
            return address

        print("Address cannot be empty!")


## 6. Phonebook and file

phonebook = {}

file_name = "phonebook.txt"


## 7. Load contacts from file

try:

    file = open(file_name, "r")

    for line in file:

        line = line.strip()

        parts = line.split("|", 3)

        if len(parts) == 4:

            name = parts[0]
            number = parts[1]
            email = parts[2]
            address = parts[3]

            phonebook[name] = [number, email, address]

    file.close()

except FileNotFoundError:
    pass


## 8. Save contacts in file

def save_phonebook():

    file = open(file_name, "w")

    for name, details in phonebook.items():

        file.write(
            name + "|" +
            details[0] + "|" +
            details[1] + "|" +
            details[2] + "\n"
        )

    file.close()


## 9. Check duplicate phone numbers

def phone_exists(number, old_name=None):

    for name, details in phonebook.items():

        if details[0] == number and name != old_name:
            return True

    return False


## 10. Show full contact details

def show_contact(name):

    print("\nContact details:")
    print("Name:", name)
    print("Phone:", phonebook[name][0])
    print("Email:", phonebook[name][1])
    print("Address:", phonebook[name][2])


## 11. Main menu

while True:

    print("\n========== PHONEBOOK ==========")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Edit contact")
    print("4. Search by name")
    print("5. Show all contacts")
    print("6. Search by phone number")
    print("7. Show number of contacts")
    print("8. Delete all contacts")
    print("9. Show recent contacts")
    print("10. Show contact details")
    print("11. Exit")

    choice = input("Choose an option: ")


    ## 12. Add contact

    if choice == "1":

        while True:

            name = get_input("Enter first and last name (0 to go back): ")

            if name is None:
                break

            name = name.strip()

            if len(name.split()) < 2:
                print("Please enter first and last name!")
                continue

            if name in phonebook:
                print("This contact already exists!")
                continue

            number = get_phone_number()

            if number is None:
                continue

            if phone_exists(number):
                print("This phone number already exists!")
                continue

            email = get_email()

            if email is None:
                continue

            address = get_address()

            if address is None:
                continue

            phonebook[name] = [number, email, address]

            save_phonebook()

            print("Contact added successfully!")
            break


    ## 13. Delete contact

    elif choice == "2":

        while True:

            name = get_input("Enter contact name (0 to go back): ")

            if name is None:
                break

            name = name.strip()

            if name not in phonebook:
                print("Contact not found! Try again.")
                continue

            print("Are you sure you want to delete this contact?")
            print("1. Yes")
            print("2. No")
            print("0. Back")

            answer = get_input("Choose 1 or 2: ")

            if answer is None:
                break

            if answer == "1":

                del phonebook[name]
                save_phonebook()

                print("Contact deleted successfully!")
                break

            elif answer == "2":
                print("Delete cancelled!")
                break

            else:
                print("Invalid choice!")


    ## 14. Edit contact

    elif choice == "3":

        while True:

            name = get_input("Enter contact name (0 to go back): ")

            if name is None:
                break

            name = name.strip()

            if name not in phonebook:
                print("Contact not found!")
                continue

            print("\n1. Edit name")
            print("2. Edit phone number")
            print("3. Edit email")
            print("4. Edit address")
            print("0. Back")

            answer = get_input("Choose an option: ")

            if answer is None:
                break

            ## Edit name

            if answer == "1":

                new_name = get_input("Enter new first and last name: ")

                if new_name is None:
                    continue

                new_name = new_name.strip()

                if len(new_name.split()) < 2:
                    print("Please enter first and last name!")
                    continue

                if new_name in phonebook:
                    print("This name already exists!")
                    continue

                phonebook[new_name] = phonebook[name]
                del phonebook[name]

                save_phonebook()

                print("Name changed successfully!")

            ## Edit phone

            elif answer == "2":

                while True:

                    number = get_phone_number()

                    if number is None:
                        break

                    if phone_exists(number, name):
                        print("This phone number already exists!")
                        continue

                    phonebook[name][0] = number
                    save_phonebook()

                    print("Phone number changed successfully!")
                    break

            ## Edit email

            elif answer == "3":

                email = get_email()

                if email is not None:

                    phonebook[name][1] = email
                    save_phonebook()

                    print("Email changed successfully!")

            ## Edit address

            elif answer == "4":

                address = get_address()

                if address is not None:

                    phonebook[name][2] = address
                    save_phonebook()

                    print("Address changed successfully!")

            else:
                print("Invalid choice!")


    ## 15. Search by part of name

    elif choice == "4":

        while True:

            search_name = get_input("Enter part of name (0 to go back): ")

            if search_name is None:
                break

            search_name = search_name.strip().lower()

            if search_name == "":
                print("Please enter a name!")
                continue

            found = False

            for name in phonebook:

                if search_name in name.lower():

                    print(name, ":", phonebook[name][0])
                    found = True

            if not found:
                print("No matching contact found!")
            else:
                break


    ## 16. Show all contacts sorted by last name

    elif choice == "5":

        if len(phonebook) == 0:
            print("Phonebook is empty!")

        else:

            print("\nAll contacts:")
            print("Total contacts:", len(phonebook))

            for name in sorted(phonebook, key=lambda x: x.split()[-1].lower()):

                print(name, ":", phonebook[name][0])


    ## 17. Search by part of phone number

    elif choice == "6":

        while True:

            search_number = get_input("Enter part of phone number (0 to go back): ")

            if search_number is None:
                break

            if not search_number.isdigit():
                print("Please enter numbers only!")
                continue

            found = False

            for name, details in phonebook.items():

                if search_number in details[0]:

                    print(name, ":", details[0])
                    found = True

            if not found:
                print("No matching phone number found!")
            else:
                break


    ## 18. Show number of contacts

    elif choice == "7":

        print("Total contacts:", len(phonebook))


    ## 19. Delete all contacts

    elif choice == "8":

        if len(phonebook) == 0:
            print("Phonebook is already empty!")

        else:

            print("Are you sure you want to delete ALL contacts?")
            print("1. Yes")
            print("2. No")
            print("0. Back")

            answer = get_input("Choose an option: ")

            if answer == "1":

                phonebook.clear()
                save_phonebook()

                print("All contacts deleted!")

            elif answer == "2":
                print("Delete cancelled!")

            elif answer is None:
                print("Back to main menu!")

            else:
                print("Invalid choice!")


    ## 20. Show recent contacts

    elif choice == "9":

        if len(phonebook) == 0:
            print("Phonebook is empty!")

        else:

            print("\nRecent contacts:")

            recent_names = list(phonebook.keys())

            for name in recent_names[-5:][::-1]:
                print(name, ":", phonebook[name][0])


    ## 21. Show full contact details

    elif choice == "10":

        while True:

            name = get_input("Enter contact name (0 to go back): ")

            if name is None:
                break

            name = name.strip()

            if name in phonebook:

                show_contact(name)
                break

            print("Contact not found! Try again.")


    ## 22. Exit program with confirmation

    elif choice == "11":

        print("Are you sure you want to exit?")
        print("1. Yes")
        print("2. No")

        answer = get_input("Choose 1 or 2: ")

        if answer == "1":

            save_phonebook()

            print("Goodbye. Come back soon!")
            break

        elif answer == "2":
            print("Back to main menu!")

        else:
            print("Invalid choice!")


    ## 23. Invalid menu choice

    else:
        print("Invalid choice! Please try again.")
