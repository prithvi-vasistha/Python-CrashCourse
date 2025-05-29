import city_country 
import city_format 

def test_santiago_chile():
    format = city_country.call_function("Santiago", "Chile")
    assert format == 'Santiago, Chile'

def test_newyork_manhattan():
    format = city_format.format_city_country("new york", "manhattan")
    assert format == 'New York, Manhattan'
