# 1. import diablo2
import diablo2

print(diablo2.basic_energy) # 10
print(diablo2.sing())       # lalala~~~

jane = diablo2.Amazon()
print(jane.strength)        # 20
print(jane.attack())        # => Jab Jab

eve = diablo2.Amazon()
print(eve.vitality)         # 20
eve.exercise()
print(eve.vitality)         # 21

# 2. from diablo2 import * (좋은 방법 아님)
from diablo2 import *

print(basic_energy) # 10
print(sing()) # lalala~~~

lee = Amazon()
print(lee.attack()) # => Jab Jab
lee.exercise()
print(lee.strength) # 22

# 3. from diablo2 import Amazon
from diablo2 import Amazon, sing
print(sing())   # lalala~~~

kim = Amazon()
kim.exercise()
kim.exercise()
print(kim.strength)  # 24
