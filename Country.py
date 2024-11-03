# Function to display the header and menu choices for the user
def display_menu():
    print("\n===== Country Management Menu =====")
    print("1. View all countries")
    print("2. View a specific country by key")
    print("3. Add a new country")
    print("4. Delete a country")
    print("5. Exit")
    print("===================================")

# Function to pre-populate a dictionary with country names
def populate_country_dict():
    countries = {
        "US": "United States",
        "CA": "Canada",
        "MX": "Mexico"
    }
    return countries

# Function to display all country keys in the dictionary
def view_countries(countries):
    print("\nCountry Keys:")
    for key in countries:
        print(key)

# Function to view a country based on the user-entered key
def view_country_by_key(countries):
    key = input("\nEnter the country key to view the corresponding country: ").upper()
    if key in countries:
        print(f"Country for key '{key}': {countries[key]}")
    else:
        print("\nInvalid key. No country found.")

# Function to add a new country to the dictionary
def add_country(countries):
    key = input("\nEnter the key for the new country: ").upper()
    if key in countries:
        print(f"\nThe key '{key}' already exists. Please enter a unique key.")
    else:
        country_name = input("Enter the name of the country: ")
        countries[key] = country_name
        print(f"\nCountry '{country_name}' has been added with key '{key}'.")

# Function to delete a country from the dictionary
def delete_country(countries):
    key = input("\nEnter the key of the country to delete: ").upper()
    if key in countries:
        deleted_country = countries.pop(key)
        print(f"\nCountry '{deleted_country}' with key '{key}' has been deleted.")
    else:
        print("\nInvalid key. No country found.")

# Main function to handle the program logic
def country_management_program():
    countries = populate_country_dict()  # Pre-populate dictionary

    while True:
        display_menu()  # Display menu choices
        try:
            choice = int(input("\nChoose an option: "))
        except ValueError:
            print("\nInvalid command. Exiting the program.")
            break

        if choice == 1:
            view_countries(countries)  # Display all country keys
        elif choice == 2:
            view_country_by_key(countries)  # Display country by key
        elif choice == 3:
            add_country(countries)  # Add a new country
        elif choice == 4:
            delete_country(countries)  # Delete a country by key
        elif choice == 5:
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid command. Exiting the program.")
            break

# Run the country management program
country_management_program()
