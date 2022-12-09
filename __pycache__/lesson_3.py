#инкапсуляция
#git clone


# инкапсуляция заключение в одно место (класс) для работы с ними 2 предаставление пользователя публичного интерсейфа




#public без нижны почедчеркований
#публичный
#защищеный
# скрытый


class Human:
    atribyt=1
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def run(self):
        print(f'{self.__name} is running')

h=Human('Азиреть', 20)
# h.name='gyuy'
# h._name='Daniel'
# print(h.name,h._name)
# print(_Human_.__name)



