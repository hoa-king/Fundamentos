productos_precio = [
    ("queso", 1500),
    ("huevos", 6500),
    ("agua", 1700)
]

for i, productos_precio in enumerate(productos_precio, start=1):
    producto = productos_precio[0]
    precio = productos_precio[1]
    print(f"{i}.{producto}- ${precio}")