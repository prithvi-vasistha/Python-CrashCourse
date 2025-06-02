def format_city_country(city, country, population = ''):
    if population:
        if population >= 1:
            value = f"{city.title()}, {country.title()} - population {population}"
        else:
            return("invalid population value")
    else:
        value = f"{city.title()}, {country.title()}"
    return value
