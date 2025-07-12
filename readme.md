# INSTRUCCIONES DE USO
# Clona el repositorio
git clone 

# Entra a la carpeta del proyecto
cd camilo_lovera_registro_futbol

# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual:
venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Aplica migraciones a la base de datos
python manage.py migrate

# Carga datos de prueba 
python manage.py loaddata futbol/datos_prueba.json

# Ejecuta el servidor de desarrollo
python manage.py runserver
