
from datetime import datetime
import factory, factory.fuzzy, string
from factory.django import DjangoModelFactory

class PersonFactory(DjangoModelFactory):
    
    # Factory-boy wybierze nazwe użytkownika oraz 
    # imie i nazwisko oraz hasło przy użyciu modułu Faker
    pesel = factory.fuzzy.FuzzyText(length=11, chars=string.digits)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    gender = factory.fuzzy.FuzzyChoice(choices=('F','M'))
    birthdate = factory.fuzzy.FuzzyDate(datetime.date(1980, 1, 1), datetime.date(2003, 1,1))


class UsersFactory(DjangoModelFactory):

    person = factory.SubFactory(Person)
    hireDate = factory.fuzzy.FuzzyDate(datetime.date(1998, 1, 1), datetime.date(2003, 1,1))
    username = factory.Faker('user_name')
    password = factory.Faker('password')
    
    @factory.lazy_attribute
    def fireDate(self):
        return factory.fuzzy.FuzzyDate(self.hireDate, datetime.date(2002,12,31)).fuzz
