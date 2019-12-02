class Country:

    #Inicialización de un objeto Country
    def __init__(self, name: str, population: int, area: int):
        self.name = name
        self.population = population
        self.area = area

    #Comprobación del tamaño del area
    def is_larger(self, country):
        return self.area > country.area

    #Calculo de la densidad de población
    def population_density(self):
        return self.population/self.area

    #Imprimir string con todos los datos
    def __str__(self):
        return '{} has a population of {} and is {} square km.'.format(
            self.name, self.population, self.area)

    #Imprimir un string con los datos de un objeto Country, debe hacerse desde el terminal de python
    def __repr__(self):
        return "Country('{0}', {1}, {2})".format(self.name, self.population, self.area)


canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 124, 555)



