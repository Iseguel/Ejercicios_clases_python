# Proyecto: miapp

Este es el proyecto principal **miapp**, desarrollado utilizando el framework Django.

## Requisitos

- Python 3.x
- Django

## Instalación y Configuración

### 1. Activar el entorno virtual
Es muy recomendable trabajar dentro de un entorno virtual para mantener aisladas las dependencias de este proyecto.
```bash
# En Linux o macOS:
source env/bin/activate

# En Windows:
# env\Scripts\activate
```

### 2. Instalar dependencias
Si aún no has instalado Django en tu entorno virtual, hazlo con el siguiente comando:
```bash
pip install django
```

### 3. Aplicar las migraciones
Prepara la base de datos aplicando las migraciones necesarias del proyecto:
```bash
python manage.py migrate
```

### 4. Ejecutar el servidor de desarrollo
Levanta el servidor local para probar y desarrollar el proyecto:
```bash
python manage.py runserver
```

¡Listo! El proyecto debería estar funcionando y disponible ingresando a http://127.0.0.1:8000/ desde tu navegador web.

### RESPONDER A LAS PREGUNTAS
• ¿Qué aprendiste sobre el flujo entre formulario, vista y template? 
R: Aprendí que trabajan en ciclo continuo: el **template** muestra el formulario al usuario (en HTML). Al enviarlo, la **vista** captura esos datos (generalmente mediante POST), se apoya en el **formulario** de Django para validarlos y, si son correctos, los guarda y redirige. Si hay errores, la vista vuelve a enviar el formulario al template para que el usuario los corrija.

• ¿Cuál es la ventaja de usar ModelForm?
R: La ventaja principal es el ahorro de código y tiempo (aplicando el principio DRY). Al usar `ModelForm`, Django genera automáticamente los campos y las validaciones del formulario basándose directamente en un modelo de la base de datos, evitando que tengamos que definirlos y configurarlos todos de nuevo de forma manual.