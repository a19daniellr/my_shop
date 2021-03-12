# My Shop

### Módulo de Odoo para gestionar una tienda de videojuegos.

#### RESUMEN

El módulo consiste en poder controlar los movimientos de los videojuegos que se presten y saber en cada momento si están prestados o no. Además controla el proceso el cual no deja prestar un videojuego en caso de que no estea disponible o esté prestado ya en ese momento.
***
#### KANBAN

Dispone de una vista kanban. Te permite mover los videojuegos por sus etápas.
***
#### REGISTROS

A los videojuegos se les puede asignar **Creadores** y **Géneros**: acción, deporte, aventura... Por defecto el módulo ya genera algúnos géneros y creadores más famosos y/o usados. Además se pueden añadir manualmente y cuando quieras, tando creadores como géneros.
***
#### HERENCIA

Se utiliza la herencia con *res.partner*. Es decir se utilizan Socios para la creación de clientes.
***
#### FIELDS

Se utilizan fields **data** para el manejo de fechas y **relacionales** para el control de los creadores de un videojuegos (por ejemplo).
***
#### AMPLIACIONES FUTURAS Y DEMÁS
Como ya hemos mencionado anteriormente se pretende utilizar un kanban para poder **ordenar los videojuegos** según su estado. Se tendría que mejorar el apartado de prestamo de videojuegos para poder **venderlos** y además añadir un **stock** y **precios** de los mismos. Si se añade un préstamo al libro automaticamente se pone el nombre del libro prestado al préstamo, pudiendo cambiarlo.
***
#### VISTA CALENDAR AÑADIDA
Se ha añadido una vista Calendar para los préstamos de los videojuegos.

