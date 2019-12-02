from Ejercicio1 import Country

class Continent:
    def __init__(self, name: str, countries: list):
        self.name = name
        self.countries = countries

    #Calculo del total de la poblacion del array countries
    def total_population(self):
        totalpopulation = 0
        for country in countries:
            totalpopulation += country.population
        return totalpopulation

    #String con todos los datos
    def __str__(self):
        res = self.name
        for country in self.countries:
            res = res + '\n' + str(country)
        return res


canada = Country('Canada', 3, 970)
usa = Country('United States of America', 124, 555)
mexico = Country('Mexico', 4, 55)

countries = [canada, usa, mexico]
north_america = Continent('North America', countries)

print(north_america)

