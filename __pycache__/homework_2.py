class SuperHero:    

    def __init__(self,name,nickname,superpower,health_points):
        self.name = name
        self.nicname = nickname
        self.superpower = superpower
        self.health_points = health_points


    def __mul__(self):
        return Hero(self.health_points * 2) 

      


    def __str__(self):
        return f'{self.name}\n' \
               f'{self.nicname}\n' \
               f'{self.superpower}\n' \
               f'{self.health_points}'

a = SuperHero('Tony Stark','stark','iron man',100)
print(a)

class Hero:     

    def printt(name):
        print(f'{name} its his name')
    printt('Tony Stark')   
   



    def __len__(self):
            return len(self) 
    print(len(a.name)) 



class Hero1(SuperHero):
    h = 1
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False):
        SuperHero.__init__(self,name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
    def print_name_hero(self):
        print(f'{self.health_points **2}')
        self.fly=
     