# My Shop

## Módulo de Odoo para gestionar una tienda de videojuegos.
***
### RESUMEN

El módulo consiste en poder controlar los movimientos de los videojuegos que se presten y saber en cada momento si están prestados o no. Además controla el proceso el cual no deja prestar un videojuego en caso de que no estea disponible o esté prestado ya en ese momento.

### KANBAN

Dispone de una vista kanban sin grupos, es decir, sin poder desplazar los videojuegos a etapas de vida. Los grupos se pueden utilizar para en un futuro ordenarlos de forma que si compras uno por internet lo puedas mover en varias situaciones (**interesado**, **solicitado**, **en camino**, **retraso**,**tienda**). Ahora mismo está implementado para una mejor visualización de los productos.

### REGISTROS

A los videojuegos se les puede asignar **Creadores** y **Géneros**: acción, deporte, aventura... Por defecto el módulo ya genera algúnos géneros y creadores más famosos y/o usados. Además se pueden añadir manualmente y cuando quieras, tando creadores como géneros.

### HERENCIA

Se utiliza la herencia con *res.partner* . Es decir se utilizan Socios para la creación de clientes.

### FIELDS

Se utilizan fields **data** para el manejo de fechas y **relacionales** para el control de los creadores de un videojuegos (por ejemplo).
