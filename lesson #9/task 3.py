class Worker():
    def __init__(self,name,surname,position,income):

        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}, {self.position}'

    def get_income(self):
        return str(self._income_wage + self._income_bonus)


a = Position('Bill','Gates','Founder',{'wage': 200000,'bonus': 100000})
print(a.get_full_name())
print(a.get_income() + '$')