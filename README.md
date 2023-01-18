# GILDEDROSE-KATA
### Kata de @Emilybache
[Enlace a su repositorio](https://github.com/emilybache/GildedRose-Refactoring-Kata) 

### Kata realizado en Java por el profesor
[Enlace a su repositorio](https://github.com/dfleta/gilded-rose-kata-java)

__Se a intentado resolver el ejercicio siguiendo siguiente diagrama de clases en Java__
![diagrama_clases_UML](https://user-images.githubusercontent.com/80277545/212892060-f1d494e7-ff6d-42bb-908f-f6cca19d3deb.jpg)



Los items están constantemente degradandoce en calidad a medida que se acerca su fecha de caducidad.
El sistema actualiza el inventario. 


__La tarea es añadir un nuevo tipo de item con sus metodos__

Aclaración sobre los items: 

 - Todos los items tienen un __SellIn__('fecha vencimiento') que denota el numero de dias disponibles para venderlo.
 - Todos los items tienen un __Quality__('calidad') que denota cuan valioso es el item.
 - Al final del día el sistema baja ambos valores a cada item (*al final del día se hace un update_quality()*).
 - Una vez se caduca el __SellIn__, la __Quality__ baja el doble de rapido.


 - La __Quality__ de un item nunca es negativa.
 - La __Quality__ de un item nunca es mayor de 50.


Reglas:


 - *"Aged Bried"* aumenta __Quality__ al pasar el tiempo (disminuye __SellIn__). Aumenta el doble cuando está caducado. 

 -  El *"Backstage"* , como el Brie, incrementa su valor a medida que se caduca. Si tiene más de 10 días +1 calidad, +5 días +2 calida, +0 días +3 calidad. Si se caduca, 0 calidad.

 - El "*Sulfuras*", ni se caduca , ni se vende.

 Debemos añadir el tipo de item *"Conjured"*, que este se degrada el doble de rapido que un item Normal.
