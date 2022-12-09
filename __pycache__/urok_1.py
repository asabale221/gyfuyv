# # # def ptinte(name):
# # #     print(f'{name} its may name')



# # # ptinte('Beka')



# class Human:
#     #
#     head=1
#     hand=2
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age


#     #Функция внутри класаб метод классаб функция
#     def pritt(self):
#         print(self.name, 'is runn')


# beka=Human('beka',19)
# beka.pritt()
# hum2=Human('Nurbek',20)
# hum2.pritt()
# # Обьект класса
# human=Human('Beka',19)
# print(human.name,human.age)
# print(human.head)
# human2=Human('jumabek',20)
# print(human2.name,human2.age)
# print(human2.head)




class Car:
    motor=1
    def __init__(self,model,age,marka):
        self.model=model
        self.age=age
        self.mark=marka
    def __str__(self):
        return f'model is {self.model}\n' \
               f'age is {self.age}\n' \
               f'mark is {self.mark}'

car1=Car('BMW',2010,'x5')
print(car1)       


car2=Car('Mercedes',2018,'S')
print(car2)



