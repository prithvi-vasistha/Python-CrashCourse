from city_format import format_city_country
city = None
country = None

def call_function(city, country):
    formatted = format_city_country(city, country)
    return formatted

def get_user_inputs():
    user_input = input("Enter your city name:\n")
    if user_input.isalpha:
        city = user_input
    else:
        print("invalid input")
        exit()
    user_input = input("Enter your country name:\n")
    if user_input.isalpha:
        country = user_input
    else:
        print("invalid input")
        exit()

    print_res = call_function(city, country)
    print(print_res)

if __name__ == "__main__":
    get_user_inputs()
