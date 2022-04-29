
class Hotel:
     info = {}
     def __init__(self,name,price,capacity):
          self.name = name
          self.price = price
          self.capacity = capacity
          self.info = {'Name':name,'Price':price,'Capacity':capacity}
     @classmethod
     def search(cls,name):
          return cls.info.get(name,'Topilmadi')
     def __str__(self):
             return self.info
a= Hotel('Hilton',1500,300)
b = Hotel("Zarafshan",500,100)

print(Hotel.info)

          