class Person:
    def __str__(self):
        return ",".join([f"{k} ---> {v} " for k, v in self.__dict__.items()])

class PersonBuilder:
    def __init__(self):
        self.name = None
        self.age = None
        self.place = None

    def build_name(self, name):
        self.name = name
        return self #returns PersonBuilder object so that it can perform chaining

    def build_age(self, age):
        self.age = age
        return self #returns PersonBuilder object so that it can perform chaining

    def build_place(self, place):
        self.place = place
        return self #returns PersonBuilder object so that it can perform chaining

    def build_person(self):
        person = Person()
        person.name = self.name
        person.age = self.age
        person.place = self.place
        return person # returns Person object for representation

if __name__ == "__main__":
    pb = PersonBuilder()
    print(pb.build_person()) # name ---> None ,age ---> None ,place ---> None
    person = pb.build_name("Saumya").build_age(27).build_place("Mujafarpur").build_person()
    print(person) # name ---> Saumya ,age ---> 27 ,place ---> Mujafarpur
    # In future if we want to add more instance variable for Person, we can directly add new varible in
    # PersonBuilder init method and add build method and at last in build_person method, just one extra 
    # will be added