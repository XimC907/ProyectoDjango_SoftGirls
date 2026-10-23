# 💜 STEAM Girls Comunnity

> **Visibilizando, conectando e impulsando el talento femenino en la industria tecnológica de Medellín.**

---

## 🌟 Nuestra Visión & Sentimiento
La industria del desarrollo de software y las áreas STEAM (*Ciencia, Tecnología, Ingeniería, Arte y Matemáticas*) han sido históricamente lideradas por hombres. Sin embargo, en **Medellín**, una fuerza transformadora de mujeres apasionadas por la tecnología está cambiando esa narrativa día a día.
Descubrimos que una de las herramientas más potentes para acortar la brecha de género y fomentar la participación femenina son los **grupos de estudio, mentorías y comunidades de apoyo**. 

**STEAM Girls Comunnity** nace con el corazón en la comunidad: una plataforma web concebida para ser la vitrina y el punto de encuentro de todas estas increíbles iniciativas. Queremos que cada estudiante, profesional o apasionada por la tecnología encuentre su espacio, conozca la misión de cada grupo, asista a sus eventos y sepa que **no está sola en este camino**.

---

## 🚀 Funcionalidades Principales
- 📁 **Directorio de Iniciativas STEAM:** Un espacio centralizado donde cada comunidad visibiliza su misión, visión, historia y canales de contacto.
- 📅 **Agenda de Eventos y Participaciones:** Calendario interactivo con talleres, meetups, conferencias y eventos en los que las comunidades participan o lideran en la ciudad.
- 📍 **Mapeo de Sedes y Eventos:** Ubicación geográfica de los puntos de encuentro en Medellín (universidades, centros de innovación como Ruta N, etc.).
- 👩‍💻 **Perfiles e Integrantes:** Conecta a estudiantes, líderes, mentoras, directivas y aliadas del ecosistema local.
- 🖼️ **Galería Comunitaria:** Registro fotográfico de los eventos y momentos memorables compartidos.

---

## 🛠️ Arquitectura y Tecnologías
El proyecto está desarrollado con el framework web **Django** en el backend, siguiendo una arquitectura MVC (Modelo-Vista-Controlador) limpia y escalable.

### 📊 Modelo de Datos (6 Entidades Principales)
El sistema se fundamenta en un esquema relacional enfocado en la flexibilidad y la integridad de los datos:

1. **`Iniciativa`**: Registra la información institucional de cada comunidad (Misión, Visión, Universidad de Origen, Número de estudiantes).
2. **`Miembro`**: Gestiona las usuarias registradas con sus diferentes roles (*Líder/Organizadora, Estudiante, Mentora, Directiva/Aliada*).
3. **`UbicacionSede`**: Almacena las sedes físicas habituales de las iniciativas.
4. **`RedSocial`**: Centraliza las vías de contacto y redes de cada iniciativa (Instagram, LinkedIn, GitHub, Discord, etc.).
5. **`Evento`**: Registra las actividades organziadas o participaciones externas, indicando lugar, fecha e importancia.
6. **`GaleriaEvento`**: Guarda las memorias fotográficas de los eventos desarrollados.

---

## 💻 Instalación y Configuración Local
+ Sigue estos pasos para ejecutar el proyecto en tu entorno local:

```bash
### 1. Crear una carpeta en el que se desee guardar el proyecto y abrirla

### 2. Clonar el repositorio y abrir una CMD en la carpeta o en Visual Studio Code
git clone https://github.com/XimC907/ProyectoDjango_SoftGirls.git

### 3. Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate

### 4. Actualiza pip e instalar dependencias:
python -m pip install --upgrade pip 
pip install django

### 5. Ejecutar migraciones de base de datos
python manage.py makemigrations
python manage.py migrate

### 6. Crear superusuario (Admin)
python manage.py createsuperuser

### 7. Levantar el servidor de desarrollo
python manage.py runserver

+ Visita http://127.0.0.1:8000/ en tu navegador para ver la aplicación funcionando.
```
---
## 💜 Contribuciones y Comunidad
Este proyecto es hecho por y para la comunidad. Si eres desarrolladora, diseñadora, mentora o simplemente quieres aportar con ideas, ¡todas las contribuciones son bienvenidas!

Comunícate con nosotras al siguiente correo: softgirls@pascualbravo.edu.co
