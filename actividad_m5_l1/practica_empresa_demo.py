import sqlite3

conn = sqlite3.connect("empresa_demo.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre  TEXT    NOT NULL,
        cargo   TEXT    NOT NULL,
        salario REAL
    )
""")

cursor.executemany(
    "INSERT INTO empleados (nombre, cargo, salario) VALUES (?, ?, ?)",
    [
        ("Ana Torres",   "Desarrolladora",  1800000),
        ("Pedro López",  "Diseñador",       1500000),
        ("Carla Muñoz",  "Project Manager", 2100000),
    ]
)

conn.commit()

cursor.execute("SELECT * FROM empleados")
filas = cursor.fetchall()

print(f"{'ID':<4} {'Nombre':<20} {'Cargo':<20} {'Salario':>12}")
print("-" * 58)
for fila in filas:
    print(f"{fila[0]:<4} {fila[1]:<20} {fila[2]:<20} {fila[3]:>12,.0f}")

conn.close()
print("\nBase de datos 'empresa_demo.db' creada correctamente.")
