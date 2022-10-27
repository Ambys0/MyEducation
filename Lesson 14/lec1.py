class Human:
    def __init__(self, name_par, age_par, phone_par, country_par, city_par):
        self.name = name_par
        self.age = age_par
        self.phone = phone_par
        self.country = country_par
        self.city = city_par

    def hello(self):
        return "Hello my name is " + self.name

    print(self.age)