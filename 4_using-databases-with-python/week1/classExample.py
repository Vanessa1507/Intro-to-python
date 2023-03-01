class PartyAnimal:
  x = 0
  name = ""

  def __init__(self, z):
    self.name= z
    print("I am constructed", self.name)

  def party(self):
    self.x = self.x +1
    print(self.name, "So far", self.x)

  # def __del__(self):
  #   print("I am destructed", self.x)

ramon = PartyAnimal("Ramón")

ramon.party()
ramon.party()

mateo = PartyAnimal("Mateo")

mateo.party()
mateo.party()
mateo.party()
mateo.party()
mateo.party()

class FootballFan(PartyAnimal):
  points = 0
  def touchDown(self):
    self.points = self.points + 7
    self.party()
    print(self.name, "points", self.points)

fan = FootballFan("Jim")
fan.party()
print(fan.touchDown())

# print("Type", type(ramon)) # Type <class '__main__.PartyAnimal'>
# print("Dir", dir(ramon)) # Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'party', 'x']

# an2 = PartyAnimal()

# an2.party()
# an2.party()
# an2.party()
# an2.party()
# an2.party()