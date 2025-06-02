class My_Employee:
:q
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, *amount):
        if amount:
            self.salary += amount[0]

        else:
            self.salary += 5000

        return self.salary
