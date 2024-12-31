# 파일이름 import
import Fridge

LG = Fridge.Fridge()
apple = Fridge.Food()

LG.open()
LG.put(apple)
LG.close()

elephant = Fridge.Food()

LG.open()
LG.put(elephant)
LG.close()

