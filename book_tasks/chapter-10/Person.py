import datetime

class Person(object):
  def __init__(self, name):
    """Assumes name a string. Create a person"""
    self._name = name
    try:
      last_blank = name.rindex(' ')
      self._last_name = name[last_blank+1:]
    except:
      self._last_name = name
    self._birthday = None

  def get_name(self):
    """Returns self's full name"""
    return self._name

  def get_last_name(self):
    """Returns self's last name"""
    return self._last_name

  def set_birthday(self, birthdate):
    """Assumes birthdate is of type datetime.date
    Sets self's birthday to birthdate"""

    self._birthday = birthdate

  def get_age(self):
    """Returns self's current age in days"""
    if self._birthday == None:
      raise ValueError
    return (datetime.date.today() - self._birthday).days

  def __lt__(self, other):
    """Assumes other a Person
    Returns True if self precedes other in alphabetical
    order, and False otherwise. Comparison is based on last
    names, but if these are the same, full names are compares"""

    if self._last_name == other._last_name:
      return self._name < other._name
    return self._last_name < other._last_name

  def __str__(self):
    """Returns self's name"""
    return self._name

me = Person('Galina Erostenko')
him = Person('Barack Hussein Obama')
her = Person("Madonna")

print(him.get_last_name())
him.set_birthday(datetime.date(1961, 8, 4))
her.set_birthday(datetime.date(1958, 8, 18))

print(him.get_name(), 'is', him.get_age(), 'days old')

pList = [me, him, her]
for p in pList:
    print(p)
pList.sort()
for p in pList:
    print(p)
    

class MIT_Person(Person):
    _next_id_num = 0 #identification number
    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_Person._next_id_num
        MIT_Person._next_id_num += 1
        
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        return self._id_num < other.get_id_num()
    

p1 = MIT_Person("Mark Guttag")
p2 = MIT_Person("Billy Bob Beaver")
p3 = MIT_Person("Billy Bob Beaver")
p4 = Person("Billy Bob Beaver")

print('p1 < p2 = ', p1 < p2)
print('p3 < p2 = ', p3 < p2)
print('p4 < p1', p4 < p1)
# print('p1 < p4', p1 < p4)

print(isinstance(p4, MIT_Person))
    
        
        