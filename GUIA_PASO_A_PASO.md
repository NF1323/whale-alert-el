# Guía de Extracción de Datos: Whale Alert EL

Este instructivo detalla el proceso paso a paso para configurar el entorno, desarrollar el script de scraping y gestionar el repositorio del proyecto.

## 1. Configuración del Entorno de Desarrollo

Desde la terminal de PowerShell en la raíz del proyecto:

```powershell
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Instalar las librerías necesarias
pip install requests pandas beautifulsoup4
```

## 2. Estructura del Proyecto

Asegúrate de tener la siguiente estructura de carpetas:
- `src/`: Carpeta para el código fuente.
- `data/`: Carpeta donde se guardarán los archivos CSV generados.
- `.gitignore`: Para evitar subir archivos innecesarios.

## 3. Desarrollo del Script (`src/whale_alert.py`)

El script realiza las siguientes tareas:
1. Petición HTTP a `whale-alert.io`.
2. Extracción de datos con `BeautifulSoup`.
3. Procesamiento y limpieza con `pandas`.
4. Registro de eventos en un archivo `logs.log`.
5. Guardado de los resultados en `data/whales_YYYY-MM-DD.csv`.

## 4. Configuración de Git e Ignorado de Archivos

Configura tu `.gitignore` para no subir archivos basura:
```text
.env
venv/
__pycache__/
data/*.csv
*.log
```

Configura tu identidad de Git (solo la primera vez):
```powershell
git config --global user.email "nicofarina1323@gmail.com"
git config --global user.name "Nicolas Farina"
```

## 5. Control de Versiones (Commit)

Para guardar tus cambios:
```powershell
git add .
git commit -m "feat: implementar script de whale alert"
```

## 6. ¿Cómo volver al pasado? (Git Revert/Reset)

Si cometes un error o quieres volver a una versión anterior después de haber hecho commits, tienes varias opciones:

### A. Ver el historial
Primero, identifica a qué punto quieres volver:
```powershell
git log --oneline
```

### B. Volver temporalmente (Explorar)
Si solo quieres ver cómo estaba el código antes sin borrar nada:
```powershell
git checkout <codigo-del-commit>
# Para volver al presente:
git checkout feature/init-repo
```

### C. Volver permanentemente (Borrar lo nuevo)
**⚠️ Cuidado:** Esto borrará todos los cambios realizados después de ese commit.
```powershell
git reset --hard <codigo-del-commit>
```

### D. Deshacer un commit con uno nuevo (Más seguro)
Crea un nuevo commit que hace exactamente lo opuesto al commit que quieres deshacer. Es la opción recomendada si ya subiste los cambios a GitHub:
```powershell
git revert <codigo-del-commit>
```

## 7. Versiones Maestras (Git Tags)

Para marcar versiones importantes (hitos) y no depender de códigos extraños de commits, usamos **Tags**.

### A. Crear un hito (versión)
He marcado la versión actual como el punto de partida antes de MinIO:
```powershell
git tag -a v1.0-pre-minio -m "Version base antes de MinIO"
git push origin --tags
```

### B. ¿Cómo volver a esta versión exacta?
Si en el futuro rompes algo con MinIO y quieres volver a este estado exacto:
```powershell
# 1. Ver todas las versiones disponibles
git tag

# 2. Volver a la versión v1.0
git checkout v1.0-pre-minio
```

---
**Nota:** El script está diseñado para ejecutarse siempre con el entorno virtual activo.
