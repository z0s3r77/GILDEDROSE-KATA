# Desglozando y entendiendo el GildedRose de Dfleta
# Tenemos la clase Item, común a todos los Items
class Item:
    # Este es el constructor de un item
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    #Al crear la instancia y poner (print(instancia), nos devolverá esto
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# class Interfaz para añadir comportamientos de las clases que estás han de tener
# De ahí viene a que se llame un "contrato", en la interfaz y la clase.
class Interfaz():
    #Todas las clases que usen la interfaz, deben tener este metodo
    def update_quality(self):
        pass


class NormalItem(Item, Interfaz):
    #Herencia multiple de item e Interfaz

    #Cuando instanciamos un NormalIntem, hereda las propiedades de Item y Interfaz,
    # al igual que sus metodos 
    def __init__(self, name, sell_in, quality): #Aquí, le pasamos los parametros item = NormalItem("Aged Brie", 5, 0)
        Item.__init__(self, name, sell_in, quality)

    #Este metodo es solo para NormalItem, setSellIn, es que se aproxima su fecha de caducidad cada vez
    #que se ejecuta la función, comportamiento "base" en todos los items Normales.
    def setSell_in(self):
        self.sell_in = self.sell_in - 1


    #El metodo de las reglas basicas de un NormalItem
    def setQuality(self, valor): 
        #La calidad no puede ser mayor a 50, 50 es el limite
        if self.quality + valor > 50:
            self.quality = 50
        
        #Se suma la calidad normal, este metodo puede cambiar dependiendo el objeto
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor 
        
        #La calidad nunca puede ser negativa
        else:
            self.quality = 0


    # Sobreescribe el metodo update_quality de la Interfaz
    def update_quality(self):
        #Si aún no se ha caducado se resta uno a la calidad
        if self.sell_in > 0:
            self.setQuality(-1)
        
        else:
        #Si ya se ha caducado degrada al doble
            self.setQuality(-2)
        self.setSell_in()
        




if __name__ == '__main__':

    item = NormalItem("Aged Brie", 2 ,8)
    item.update_quality()    
    item.update_quality()
    item.update_quality()
    item.update_quality()
    item.update_quality()


    print(item)