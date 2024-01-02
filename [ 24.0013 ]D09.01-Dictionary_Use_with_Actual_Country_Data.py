
programming_dictionary = world_cities = {
    "New York": {"country": "USA", "population": 8419000},
    "Los Angeles": {"country": "USA", "population": 3971000},
    "Chicago": {"country": "USA", "population": 2716000},
    "Houston": {"country": "USA", "population": 2313000},
    "Phoenix": {"country": "USA", "population": 1686000},
    "Philadelphia": {"country": "USA", "population": 1584000},
    "San Antonio": {"country": "USA", "population": 1547000},
    "San Diego": {"country": "USA", "population": 1424000},
    "Dallas": {"country": "USA", "population": 1343000},
    "San Jose": {"country": "USA", "population": 1035000},
    "London": {"country": "UK", "population": 8982000},
    "Birmingham": {"country": "UK", "population": 1142000},
    "Leeds": {"country": "UK", "population": 793100},
    "Glasgow": {"country": "UK", "population": 633100},
    "Sheffield": {"country": "UK", "population": 584800},
    "Bradford": {"country": "UK", "population": 539800},
    "Liverpool": {"country": "UK", "population": 494800},
    "Edinburgh": {"country": "UK", "population": 488100},
    "Manchester": {"country": "UK", "population": 547600},
    "Bristol": {"country": "UK", "population": 467900},
    "Tokyo": {"country": "Japan", "population": 13960000},
    "Yokohama": {"country": "Japan", "population": 3765000},
    "Osaka": {"country": "Japan", "population": 2723000},
    "Nagoya": {"country": "Japan", "population": 2305000},
    "Sapporo": {"country": "Japan", "population": 1952000},
    "Fukuoka": {"country": "Japan", "population": 1592000},
    "Kobe": {"country": "Japan", "population": 1538000},
    "Kyoto": {"country": "Japan", "population": 1475000},
    "Kawasaki": {"country": "Japan", "population": 1513000},
    "Saitama": {"country": "Japan", "population": 1300000}
}


for key in programming_dictionary:
    print(f"The world cities' Keys are: {key}")
print(" ")

user_input = int(input("Please type a number: "))

keys_list = list(world_cities.keys())
print(f'This is the Key list: {keys_list}')

# Check if the user input is within the range of the dictionary
if user_input < len(keys_list):
    city_key = keys_list[user_input]
    print(f"The world city at index {user_input} is: {city_key}. It is city #{user_input+1} in the actual list.\n")
    # print(programming_dictionary[key])

x=0
y=1
z=2

print(f"The {x} character place is {city_key[x]}")
print(f"The {y} character place is {city_key[y]}")
print(f"The {z} character place is {city_key[z]}")

if user_input < len(keys_list):
    city_key = keys_list[user_input]
    city_info = world_cities[city_key]
    country = city_info["country"]
    population = city_info["population"]
    print(f"The world city at index {user_input} is: {city_key}, Country: {country}, Population: {population}")
