# домашняя задания 1
class SuperHero:
    people='people'
    fly = True
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def nameHero(self):
        print("Name hero is", self.name)
    
    def myltyhealth_points(self):
        print("Health_points: ",self.health_points * 2)

    def __str__(self) -> str:
        return f"Status hero:\nNikname hero - {self.nickname}\nSuperpower hero - {self.superpower}\nhealth_points hero - {self.health_points}"
        
    def __len__(self):
        return len(self.catchphrase)
# hero = SuperHero("Toni Stark", "Ironman", "Inventor", 100, "I'm just Ironman")
# hero.nameHero()
# hero.myltyhealth_points()
# print(hero)
# print(len(hero))
# print(SuperHero.people())

# домашка 2

class classSuperHero_1(SuperHero): 
    people ="Sadir Japarov"
    def myltyhealth_points(self):
        print(self.health_points**2)
    def __init__(self, name, nickname, superpower, health_points, catchphrase , fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly= fly
    def __str__(self) -> str:
        return f"Status hero:\nNikname hero - {self.nickname}\nSuperpower hero - {self.superpower}\nhealth_points hero - {self.health_points}\nfly {self.fly}"
        
    def new_metod(self):
        self.fly = True
        print(f"fly in the True_phrase: {self.fly }")


class classSuperHero_2(classSuperHero_1):
    people = "Sadir Japarov"
    def new_metod(self):
        self.fly= False
        print(f"fly in the True_phrase: {self.fly }")

class classSuperHero_3(classSuperHero_2):
   people = "people"



hero_1 = classSuperHero_1("Thor" , "Thor","Thunder" ,250,"Death will soon overtake you anyway")
print(hero_1)
hero_1.myltyhealth_points()
hero_1.new_metod()

hero_2 = classSuperHero_2("Arthur Curry","Aquaman","King of the underwater kingdom",220,"I'm a Aquman")
print(hero_2)
hero_2.myltyhealth_points()
hero_2.new_metod()


hero_3 = classSuperHero_3("Peter Benjamin Parker","Spider-Man","web",100,"The greater the power, the greater the responsibility")
print(hero_3)
hero_3.myltyhealth_points()
hero_3.new_metod()