class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

worker1 = Position('John', 'Smith', 'assistant', {'wage': 20000, 'bonus': 30000})
print(worker1.name)
print(worker1.surname)
print(worker1.position)
print(worker1._income)
print('Full name: ', worker1.get_full_name())
print('Total income: ', worker1.get_total_income())
