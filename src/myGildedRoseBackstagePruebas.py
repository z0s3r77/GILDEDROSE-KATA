from src.myGildedRose import *

if __name__ == '__main__':

    print('Si es un item normal')
    item = Backstage("Backstage passes", 11, 3)

    for i in range(0,14):
        item.updateQuality()
        print(item)
