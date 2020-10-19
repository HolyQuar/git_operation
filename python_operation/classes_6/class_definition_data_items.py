class Employee:
    pass
john = Employee()
# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
print('john_object:{}'.format(john.__str__))
print('john_attribute:{}'.format(john.__dict__))
