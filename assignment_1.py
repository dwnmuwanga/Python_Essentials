# Question 1: Demonstrating OOP concepts
# Parent Class
class Country:
  def __init__(self, name, capital, population):
    self.name = name
    self.capital = capital
    self.population = population

def display_info(self):
  print(f"Country: {self.name}")
  print(f"Capital: {self.capital}")
  print(f"Population: {self.population}")

# Inheritance / Child Class
class AfricanCountry(Country):
  def __init__(self, name, capital, population, president):
    super().__init__(name, capital, population)
    self.president = president

  # Polymorphism (Method Overriding)
  def display_info(self):
    print(f"Country: {self.name}")
    print(f"Capital: {self.capital}")
    print(f"Population: {self.population}")
    print(f"President: {self.president}")

# Objects
Uganda = AfricanCountry("Uganda", "Kampala", 49000000, "Yoweri Museveni" )
Kenya = AfricanCountry("Kenya", "Nairobi", 55000000, "William Ruto")

# Calling the passed methods
Uganda.display_info()
print("-----------------")
Kenya.display_info()















# Question 2 : From objects to real outcomes
# Approach
# Using OOP to create a country management system  that displays for us countries with their corresponding details

class Country:
    def __init__(self, name, capital, population, currency):
        self.name = name
        self.capital = capital
        self.population = population
        self.currency = currency

    def display_details(self):
        print(f"Country: {self.name}")
        print(f"Capital: {self.capital}")
        print(f"Population: {self.population:,}")
        print(f"Currency: {self.currency}")
        print("-" * 30)


# Creating objects
a = Country("Uganda", "Kampala", 49000000, "Uganda Shilling")
b = Country("Kenya", "Nairobi", 55000000, "Kenyan Shilling")
c = Country("Tanzania", "Dodoma", 67000000, "Tanzanian Shilling")

# Store objects in a list
countries = [a, b, c]

# Display all countries
print("EAST AFRICAN COUNTRIES")
print("=" * 30)

for country in countries:
    country.display_details()