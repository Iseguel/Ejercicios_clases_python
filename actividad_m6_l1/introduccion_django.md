# Introducción a Django

## 1. ¿Qué es Django?

**¿Qué tipo de framework es Django?**
Django es un framework web de alto nivel para Python. Está diseñado para que los desarrolladores puedan construir sitios web de forma rápida y con poco código repetitivo. Incluye muchas herramientas listas para usar desde el principio.

**¿Qué tipo de aplicaciones permite construir?**
Con Django se pueden construir todo tipo de aplicaciones web como tiendas online, redes sociales, paneles de administración, APIs, plataformas educativas y sistemas de gestión, entre otros.

**Tres ventajas de usar Django sobre Python puro:**
1. Incluye un panel de administración.
2. Trae un sistema para manejar la base de datos sin escribir SQL directamente (ORM).
3. Tiene protecciones de seguridad integradas contra ataques comunes como XSS o CSRF.

---

## 2. Entornos virtuales en Python

**¿Qué es un entorno virtual y para qué sirve?**
Un entorno virtual es un espacio aislado dentro de tu computador donde se instalan las librerías de un proyecto específico. Sirve para que cada proyecto tenga sus propias versiones de paquetes sin interferir con otros proyectos.

**Ventajas para un proyecto Django:**
Permite tener una versión de Django específica para ese proyecto sin afectar otros. Facilita compartir el proyecto con otros, ya que pueden instalar exactamente las mismas librerías. Evita conflictos entre versiones de paquetes. aislamiento 

**Explicación del comando `python -m venv venv`:**
Este comando crea una carpeta llamada `venv` en el directorio actual. Dentro de esa carpeta se guarda una copia aislada de Python con sus propias librerías. A partir de ese momento, todo lo que se instale en el entorno activado no afecta al resto del sistema.

---

## 3. Estructura y diseño de Django

**¿Qué es el patrón MVC y cómo se aplica en Django (MTV)?**
MVC (Modelo-Vista-Controlador) es una forma de organizar el código separando los datos, la lógica y la presentación. Django usa una variante llamada MTV (Model-Template-View) que cumple el mismo objetivo pero con nombres distintos.

**Tabla comparativa MVC vs MTV:**

| Concepto tradicional (MVC) | Nombre en Django (MTV) | Función |
|---------------------------|------------------------|---------|
| Model | Model | Gestiona los datos y la estructura de la base de datos |
| View | Template | Define cómo se muestra la información al usuario (HTML) |
| Controller | View | Contiene la lógica que conecta los datos con la presentación |

**¿Qué es el enrutador de Django?**
El enrutador es el archivo `urls.py` que actúa como una central de tráfico. Cuando el navegador pide una URL, Django la compara con una lista de patrones y decide qué función o vista debe encargarse de responder esa petición.

---

## 4. Principios del desarrollo con Django

**¿Qué significa el principio DRY ("Don't Repeat Yourself")?**
Significa "no te repitas": si algo ya está escrito, no hay que volver a escribirlo. Django lo aplica ofreciendo componentes reutilizables como formularios, vistas genéricas y el ORM, para que no tengas que programar desde cero cosas que ya existen.

**¿Qué significa que Django tenga una "estructura flexible y minimalista"?**
Significa que Django no te obliga a usar todas sus funciones si no las necesitas. Puedes empezar con algo simple e ir agregando componentes según el proyecto crezca. No impone una estructura rígida que hay que seguir al pie de la letra.

**¿Qué son los Templates en Django?**
Los Templates son archivos HTML que incluyen etiquetas especiales de Django. Cuando el servidor procesa una petición, rellena esas etiquetas con datos reales (como el nombre de un usuario o una lista de productos) y envía el HTML final al navegador del usuario.
