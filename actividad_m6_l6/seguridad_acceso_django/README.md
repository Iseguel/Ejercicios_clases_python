# Proyecto: Seguridad y Acceso en Django (seguridad_acceso_django)

Este es un proyecto completo en Django enfocado en — Autenticación y Seguridad. El propósito principal es explorar cómo manejar de forma segura el acceso de los usuarios y aprender a corregir vulnerabilidades comunes en el registro, como almacenar contraseñas sin encriptar.

## Instalación y Configuración

### 1. Activar el entorno virtual
Es muy recomendable trabajar dentro de un entorno virtual para mantener aisladas las dependencias:
```bash
# En Linux o macOS:
source env/bin/activate

# En Windows:
# env\Scripts\activate
```

### 2. Instalar dependencias
Asegúrate de tener Django instalado:
```bash
pip install django
```

### 3. Aplicar las migraciones
Prepara la base de datos aplicando las migraciones necesarias del proyecto y de la aplicación:
```bash
python manage.py makemigrations 
python manage.py migrate
```

### 4. Ejecutar el servidor de desarrollo
Levanta el servidor local para probar y desarrollar el proyecto:
```bash
python manage.py runserver
```

### 5. Probar la aplicación
¡Listo! Una vez ejecutado el servidor, puedes visitar:
- **Registro de estudiantes:** http://127.0.0.1:8000/estudiantes/registro/
- **Lista de estudiantes:** http://127.0.0.1:8000/estudiantes/lista/

## Estructura de la aplicación `estudiantes`

Dentro del proyecto, la app principal tiene la siguiente estructura y funciones:

```text
estudiantes/
├── __init__.py
├── admin.py          → registro en el panel admin
├── apps.py           → configuración de la app
├── forms.py          → RegistroEstudianteForm con validaciones
├── models.py         → modelo Estudiante
├── urls.py           → rutas de la app
├── views.py          → vistas de registro y lista
└── templates/
    └── estudiantes/
        ├── registro.html   → formulario de registro (incluye botón "ojito" para ver password)
        └── lista.html      → lista que evidencia el estado de las contraseñas guardadas (⚠️/✅)
```
## 