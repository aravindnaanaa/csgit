class Flight():
 def __init__(self,capacity):
  self.capacity = capacity
  self.passanger=[]
  self.add = 0

 def add_passanger(self,name):
  if not self.open_seat():
   return False
  self.passanger.append(name)
  self.add = self.add + 1
  return True
  
 def open_seat(self):
  return self.capacity - len(self.passanger)

flightA = Flight(3)

name = ["Aravind", "deepi", "mark", "donald"]

for i in name:
 
 if flightA.add_passanger(i):
  print(f"Passanger {i} added")
 else:
  print(f"Passanger {i} seat is not available")
print(type(flightA.capacity))
print(type(flightA.passanger))
print(type(Flight(3)))
