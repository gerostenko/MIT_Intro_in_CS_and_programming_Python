class Info_Hiding(object):
  def __init__(self):
    self.visible = "Look at me"
    self.__also_visible__ = "Look at me too"
    self.__invisible = "Don't look at me directly"

  def print_visible(self):
    print(self.visible)

  def print_invisible(self):
    print(self.__invisible)

  def __print_invisible(self):
    print(self.__invisible)

  def __print_invisible__(self):
    print(self.__invisible)

test = Info_Hiding()
# print(test.visible)
# print(test.__also_visible__)
# print(test.__invisible) # throws an error

# test.print_invisible()
# test.__print_invisible__()
# test.__print_invisible() # throws an error

class Sub_Class(Info_Hiding):
  def new_print_invisible(self):
    print(self.__invisible)

test_sub = Sub_Class()
# test_sub.new_print_invisible() # throws an error