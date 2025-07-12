# INSTRUCCIONES DE USO
## Clona el repositorio
git clone 

## Entra a la carpeta del proyecto

---
```bash
cd camilo_lovera_registro_futbol
```

## Crea un entorno virtual
---
```bash
python -m venv venv
```

## Activa el entorno virtual:
---
```bash
venv\Scripts\activate
```

## Instala las dependencias
---
```bash
pip install -r requirements.txt
```

## Aplica migraciones a la base de datos
---
```bash
python manage.py migrate
```

## Carga datos de prueba 
---
```bash
python manage.py loaddata futbol/datos_prueba.json
```

## Ejecuta el servidor de desarrollo
---
```bash
python manage.py runserver
```
