# TTAREA 13 – EXTENSIÓN DE MÓDULOS

Este repositorio contiene la solución para la Tarea 13: Extensión de Módulos en Odoo.

## Contenido

El proyecto consta de dos módulos de Odoo:

1.  **parent_demo**: Módulo base que define un modelo (`modelo.parent`) y su vista formulario.
2.  **extension_demo**: Módulo de extensión que hereda de `parent_demo`, modificando el modelo (cambiando una etiqueta de campo y añadiendo uno nuevo) y extendiendo la vista mediante XPath.

## Estructura de Archivos

```
/
├── parent_demo/
│   ├── models/
│   │   └── models.py       # Definición de ModeloParent
│   ├── views/
│   │   └── views.xml       # Vista Form, Tree, Acción y Menú
│   ├── __init__.py
│   └── __manifest__.py
│
└── extension_demo/
    ├── models/
    │   └── models.py       # Herencia: ModeloExtensor (_inherit)
    ├── views/
    │   └── views.xml       # Herencia de Vista con XPath
    ├── __init__.py
    └── __manifest__.py
```

## Instalación

1.  Clona este repositorio en tu carpeta de `addons` de Odoo.
2.  Actualiza la lista de aplicaciones en Odoo (modo desarrollador).
3.  Instala primero el módulo **Parent Demo**.
4.  Instala después el módulo **Extension Demo**.

## Verificación

Para verificar que la extensión funciona correctamente:
1.  Ve al menú **Parent Demo** en Odoo.
2.  Crea un nuevo registro.
3.  Verás que el campo original se llama "Nuevo Campo 1" (en lugar de "Campo 1") y aparece un campo adicional "Campo 2".

## Detalles Técnicos

### Herencia de Modelos
Se utiliza herencia de clase (`_inherit`) para modificar el modelo existente sin crear una nueva tabla en la base de datos (herencia in-place).

```python
class ModeloExtensor(models.Model):
    _inherit = "modelo.parent"
    campo1 = fields.Char(string="Nuevo Campo 1")
    campo2 = fields.Char(string="Campo 2")
```

### Herencia de Vistas
Se utiliza `xpath` para localizar el campo original e insertar el nuevo campo después de él.

```xml
<xpath expr="//field[@name='campo1']" position="after">
    <field name='campo2'/>
</xpath>
```
