def announce(fun):
 def inno():
  print("The process start to pump")
  fun()
  print("Mission completed succussfully")
 return inno

@announce
def bab():
 print("Let's go... jik jik jik")

bab()