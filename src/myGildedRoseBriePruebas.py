from src.myGildedRose import *

if __name__ == '__main__':

    print('Si es un item normal')
    item = NormalItem("Aged Brie", 5, 7)
    print(item)

    item.updateQuality()
    print(item)

    print('Si es un AgedBrie se actualiza diferente')
    print('Cuando baja baja un día, se suma 1 de calidad')
    item = AgedBrie("Aged Brie", 5, 7)
    print(item)

    item.updateQuality()
    print(item)