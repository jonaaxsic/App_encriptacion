🔐 CryptoGuard
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) 
Sistema de encriptación multicapa avanzado desarrollado con Django. CryptoGuard utiliza un algoritmo de encriptación personalizado de 4 capas para proteger tus mensajes de manera segura y eficiente.

✨ Características

🔒 Encriptación Multicapa: Algoritmo de 4 capas que combina múltiples técnicas criptográficas
🔓 Desencriptación Segura: Recupera el mensaje original usando la clave correcta
✅ Validación de Integridad: Sistema de checksum para detectar claves incorrectas o datos corruptos
🎨 Interfaz Moderna: Diseño cyberpunk con gradientes neón y animaciones suaves
📋 Copiar Resultados: Función para copiar el texto encriptado/desencriptado al portapapeles
🌐 Responsive: Diseño adaptable a diferentes dispositivos

🛠️ Tecnologías

Backend: Django 5.2.7
Frontend: HTML5, CSS3, JavaScript vanilla
Base de datos: SQLite (desarrollo)
Python: 3.x

🔐 Algoritmo de Encriptación
El sistema implementa un algoritmo de encriptación multicapa personalizado:
Capa 1: Sustitución Polialfabética

Desplaza cada letra del alfabeto según un flujo de clave generado
Convierte espacios en caracteres especiales (|)
Normaliza el texto a mayúsculas

Capa 2: Transposición Matricial

Organiza el texto en una matriz de dimensiones dinámicas
Lee los caracteres por columnas para reorganizar el mensaje
Añade padding con caracteres especiales (#)

Capa 3: Conversión Numérica

Aplica operaciones XOR con la clave
Realiza operaciones matemáticas (multiplicación y módulo)
Convierte cada carácter a un valor numérico de 2 dígitos

Capa 4: Metadatos y Checksum

Agrega checksum para validar la integridad
Incluye dimensiones de la matriz (columnas y filas)
Formato: CCRRSS[datos_encriptados]

CC: Checksum (2 dígitos)
RR: Número de filas (2 dígitos)
SS: Número de columnas (2 dígitos)



📋 Requisitos Previos

Python 3.8 o superior
pip (gestor de paquetes de Python)
Virtualenv (recomendado)

🚀 Instalación

Clonar el repositorio

bashgit clone https://github.com/tu-usuario/cryptoguard.git
cd cryptoguard

Crear y activar entorno virtual

bash# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

Instalar dependencias

bashpip install django==5.2.7

Realizar migraciones

bashpython manage.py migrate

Ejecutar el servidor de desarrollo

bashpython manage.py runserver

Acceder a la aplicación

http://localhost:8000
💻 Uso
Encriptar un mensaje

Selecciona el modo 🔒 Encriptar
Ingresa tu clave secreta (cualquier texto)
Escribe el mensaje que deseas proteger
Haz clic en 🔒 Encriptar Mensaje
Copia el resultado encriptado

Ejemplo:

Texto original: HOLA MUNDO
Clave: CLAVE123
Resultado: 200504230165826749... (texto encriptado)

Desencriptar un mensaje

Selecciona el modo 🔓 Desencriptar
Ingresa la misma clave secreta usada para encriptar
Pega el código encriptado
Haz clic en 🔓 Desencriptar Mensaje
Verifica el mensaje original recuperado

📁 Estructura del Proyecto
cryptoguard/
│
├── crypto_project/          # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py         # Configuración general
│   ├── urls.py            # URLs principales
│   ├── wsgi.py
│   └── asgi.py
│
├── encryptor/              # Aplicación principal
│   ├── templates/
│   │   └── encryptor/
│   │       └── index.html  # Interfaz web
│   ├── crypto_algorithm.py # Algoritmo de encriptación
│   ├── views.py           # Vistas de Django
│   ├── urls.py            # URLs de la app
│   └── __init__.py
│
├── manage.py              # Utilidad de Django
└── db.sqlite3            # Base de datos
🔧 Configuración
Cambiar el SECRET_KEY (Producción)
En crypto_project/settings.py, reemplaza el SECRET_KEY por uno seguro:
pythonSECRET_KEY = 'tu-clave-secreta-super-segura'
Configurar DEBUG (Producción)
pythonDEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com']
🎨 Personalización
Cambiar los colores del tema
Edita las variables de color en encryptor/templates/encryptor/index.html:
css/* Colores principales */
background: #0a0a0f;  /* Fondo oscuro */
border-color: #00ffff;  /* Cyan */
color: #ff00ff;  /* Magenta */
Modificar el algoritmo
El algoritmo está en encryptor/crypto_algorithm.py. Puedes ajustar:

Dimensiones de la matriz de transposición
Operaciones matemáticas en la Capa 3
Formato del checksum

⚠️ Consideraciones de Seguridad

Nota: Este es un proyecto educativo. Para aplicaciones en producción que requieran seguridad real, utiliza bibliotecas criptográficas probadas como:

cryptography (Python)
PyCrypto / PyCryptodome
Algoritmos estándar: AES, RSA, etc.


🤝 Contribuciones
Las contribuciones son bienvenidas. Para contribuir:

Fork el proyecto
Crea una rama para tu feature (git checkout -b feature/AmazingFeature)
Commit tus cambios (git commit -m 'Add some AmazingFeature')
Push a la rama (git push origin feature/AmazingFeature)
Abre un Pull Request

📝 Licencia
Este proyecto es de código abierto y está disponible bajo la Licencia MIT.
👤 Autor
Tu Nombre

GitHub: @tu-usuario
Email: tu-email@ejemplo.com

🙏 Agradecimientos

Django Framework
Comunidad de desarrolladores de Python
Inspiración en algoritmos criptográficos clásicos


⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!
Made with ❤️ and Python
