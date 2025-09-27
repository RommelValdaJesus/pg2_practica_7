# Auto Parts Manager

**Auto Parts Manager** es una librería en Python orientada a objetos (POO) para la **gestión de repuestos de autos**, que permite administrar **inventarios, proveedores y ventas** de forma sencilla y reutilizable.

## 🚀 Características

- Gestión de repuestos con categorías, precios y stock.
- Administración de proveedores y sus productos.
- Registro de ventas con actualización automática de inventario.
- Generación de reportes simples de inventario y ventas.
- Estructura modular y orientada a objetos (POO).

## 🔧 Ejemplo de uso

```python
from autoparts.inventario import Inventario
from autoparts.proveedor import Proveedor
from autoparts.repuesto import Repuesto
from autoparts.venta import Venta
from autoparts.reporte import Reporte

# Crear inventario y proveedor
inv = Inventario()
prov = Proveedor(1, "Repuestos La Paz", "777-1234", "ventas@lapaz.com")

# Crear repuesto y agregar al inventario
r1 = Repuesto(101, "Filtro de aceite", "Motor", 50, 20, prov)
inv.agregar_repuesto(r1)
prov.agregar_producto(r1)

# Registrar venta
venta = Venta(1, "2025-09-25", "Carlos Pérez")
venta.agregar_item(r1, 2)

print("Total venta:", venta.calcular_total())

# Reporte de inventario
print("Stock bajo:", inv.stock_bajo(minimo=5))
print("Resumen inventario:", Reporte.resumen_inventario(inv)) 

```


##  🛠 Requisitos

- Python 3.8 o superior


## 📦 Instalación

```bash
pip install auto-parts-manager

```

## 📁 Estructura del proyecto

```text
auto_parts_manager/
│── src/
│   └── autoparts/
│       ├── __init__.py
│       ├── repuesto.py
│       ├── proveedor.py
│       ├── inventario.py
│       ├── venta.py
│       └── reporte.py
│
├── setup.cfg
├── pyproject.toml
└── README.md
```


## 📜 Licencia
Este proyecto está bajo la licencia MIT — consulta el archivo LICENSE para más detalles.