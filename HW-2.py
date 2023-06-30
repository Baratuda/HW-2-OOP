import re
class IntegerCoordinate:
    @staticmethod
    def validate_phone(phone):
        return phone if len(re.findall(r'^\+375\d{2}\d{7}',phone))!=0 else None
    
    @staticmethod
    def validate_email(email):
          return email if len(re.findall(r'\w@\w+.\w+',email))!=0 else None
    
    @staticmethod
    def validate_age(age):
          return age if type(age)==int else 0
    
    @staticmethod
    def validate_dispatcher(parameter):
        if type(parameter) == str and IntegerCoordinate.validate_phone(parameter)!=None: 
            return IntegerCoordinate.validate_phone(parameter)
        elif type(parameter) == str and IntegerCoordinate.validate_email(parameter)!=None:
            return IntegerCoordinate.validate_email(parameter) 
        elif type(parameter) == int and 0<=parameter<=130:
            return IntegerCoordinate.validate_age(parameter)
        else:
            return None 
            

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, self.validate_dispatcher(value))


class Point:
    age = IntegerCoordinate()
    phone = IntegerCoordinate()
    email = IntegerCoordinate()

    def __init__(self, age, phone, email):
        self.age = age
        self.phone = phone
        self.email = email


point1 = Point(25,'+375445466680', 'bra@gmail.com')
point2 = Point(-5,'+37545466680', 'bragmail.com')
print(point1.__dict__)
print(point2.__dict__)
# git remote add origin https://github.com/Baratuda/HW-2-OOP.git
# git push -u origin master