# class H:
#     atribyt=1
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def run(self):
#         print('run')


# g=H('name',19)


# g.run()


#Обьектно ориентированное программирование
#наследование полиморфизм инкапсуляция
# инкапсуляция
#git


class Human:  # супер класс == главный класс 
    head=1
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'name is {self.name}\n'\
            f'age is {self.age}\n'\
            f'lastname is {self.lastname}\n'
            


# hum=Human('Sadir',36)
# print(hum)


class Student(Human):  #дочерный класс
    def __init__(self, name, age, lastname):
        super().__init__(name, age)
        Human.__init__(self,name,age)
        self.lastname=lastname
    def fly(self):
        print(self.name, 'is fly in True')
    def __str__(self):
        return super().__str__()
    
        
        
    


student=Student('Daniyel',60, 'Ermekov')
# print(student)
print(student.lastname)

# student.fly()
# student.lastname()





# class Teacher(Student):   # дочерный класс
#     def fly(slef):
#         print(f'{self.name} is ')
# teach=Teacher('Beka',55,'Dgj')
# teach.fly()



# class Robot:
#     def noSleep(a):
#         print(f'{a} funkchun no Sleep True')
 
# class Robot2(Robot):...

# Robot.noSleep(student.name)


