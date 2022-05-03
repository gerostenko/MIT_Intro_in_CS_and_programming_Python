class Int_set(object):
  """An Int_set is a set of integers"""
  # Information about the implementation (not the abstraction):
  # Value of a set is represented by a list of ints, self._vals
  # Each int in a set occurs in self._vals exactly once.
  def __init__(self):
    """Create an empty set of integers"""
    self._vals = []

  def insert(self, e):
    """Assumes e is an integer and inserts e into self"""
    if e not in self._vals:
      self._vals.append(e)

  def member(self, e):
    """Assumes e is an integer
    Returns True if e is in self._vals, and False otherwise"""
    return e in self._vals

  def remove (self, e):
    """Assumes e is an integer and removed e from self
    Raises ValueError if e is not in self._vals"""
    try:
      self._vals.remove(e)
    except:
      raise ValueError(str(e) + ' not found')

  def get_members(self):
    """Returns a list containing the elements of self._vals.
    Nothing can be assumed about the order of elements"""
    return self._vals[:]

  def __str__(self):
    """Returns a string representation of self._vals"""

  def __add__(self, other):
    """other is an Int_set
    mutates self so that it contains exactly the elements in self plus the elements in other"""
    for other_e in other.get_members():
      if self.member(other_e):
        continue
      else:
        self.insert(other_e)

    if self._vals == []:
      return '{}'
    self._vals.sort()
    result = ''
    for e in self._vals:
      result = result + str(e) + ','
    return result[:-1]

# my_set = Int_set()

# my_set.insert(3)
# my_set.insert(4)

# print(my_set.get_members())
# other_set = Int_set()
# other_set.insert(4)
# other_set.insert(5)
# print(other_set.get_members())

# my_set + other_set
# print(my_set.get_members())
# print(other_set.get_members())