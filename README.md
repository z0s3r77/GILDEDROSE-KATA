# GILDEDROSE-KATA

Los items están constantemente degradandoce en calidad a medida que se acerca su fecha de caducidad.
El sistema actualiza el inventario. 


__La tarea es añadir un nuevo tipo de item con sus metodos__

Aclaración sobre los items: 

 - Todos los items tienen un __SellIn__('fecha vencimiento') que denota el numero de dias disponibles para venderlo.
 - Todos los items tienen un __Quality__('calidad') que denota cuan valioso es el item.
 - Al final del día el sistema baja ambos valores a cada item.

Reglas:

 - Una vez se caduca, la __Quality__ baja el doble de rapido.
 - La __Quality__ de un item nunca es negativa.
 - La __Quality__ de un item nunca es mayor de 50.
 - *"Aged Bried"* aumenta __Quality__ al pasar el tiempo (aumenta __SellIn__).
 - *"Sulfuras"*, es un *item legendario*, nunca tiene que ser vendido ni bajar calida.
 - *"Backstage passes"*, como el *"Aged Bried"*, aumenta la __Quality__ a medida que se acerca el __SellIn__; La __Quality__ aumenta 2 cuando hay 10 días o menos en __SellIn__ y en 3 cuando hay menos de 5 días. 