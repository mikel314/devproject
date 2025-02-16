# Git and Github

En esta sección se explica como se realizó el setup de git y se creo el repositorio, asi como un breve tutorial de las funcionalidades de git más utilizadas. 

## Set up
Git viene instalado por defecto en Ubuntu que es el OS de la VM donde se desarrolla el proyecto. En cualquier caso su instalación ser haría con 
```console
sudo apt update && sudo apt install git -y
```

En caso de querer utilizar este repo como plantilla para desarrollar futuros proyectos, clonaríamos el repo en la carpeta deseada con:
```console
git clone https://github.com/mikel314/devproject.git
```

Si, en cambio, se desea crear un repositorio desde 0, se recomienda primero crearlo en la web de Github y clonarlo en local para editarlo despúes. Para ello:

1. **Crear un Repositorio en GitHub**
    * Accede a GitHub e inicia sesión en https://github.com.
    * Haz clic en el botón "New" 
    * Crea un nombre para tu repositorio, por ejemplo: mi-proyecto.
    * (Opcional) Agrega una descripción.
    * Elige la visibilidad (Público para usar Github pages como documentación)
    * Elige crear nn archivo README.md.
    * Elige crear nn archivo .gitignore.
    * Haz clic en "Create repository".

2. **Clonar el Repositorio en Linux**
    * Ve a la carpeta donde quieres clonar el repositorio, por ejemplo:
    ```console
        cd ~/Proyectos
    ```
    * Clona el repositorio con ``git clone``:
    ```console
        git clone https://github.com/tu-usuario/mi-proyecto.git
    ```

3. **Confirmar que el repositorio está bien clonado**
    * Para verificar que todo está correcto puedes ejecutar ``git status``
    * Si todo salió bien, verás algo como:
    ```console
        On branch main
        Your branch is up to date with 'origin/main'.

        nothing to commit, working tree clean
    ```

## Git repo structure

Aunque no existe una estructura fija para proyectos de ML, la siguiente funciona generalmente bien:

```
/project_name
│── data/                # Datos (crudos, procesados)
│   ├── raw/             # Datos sin procesar
│   ├── processed/       # Datos después de limpieza
│   └── external/        # Datos de terceros (opcional)
│
│── notebooks/           # Jupyter Notebooks
│
│── src/                 # Código fuente del proyecto
│
│── models/              # Modelos entrenados (artefacto)
│
│── reports/             # Reportes y visualizaciones
│
│── tests/               # Tests unitarias
│
│── docs/                # Documentación
│
│── config/              # Archivos de configuración
│
│── infra/               # Infra as a code
│
│── .gitignore           # Ignorar archivos (datos grandes, logs)
│── requirements.txt     # Dependencias del proyecto
│── README.md            # Descripción del proyecto
│── LICENSE              # Licencia del proyecto

```

## Commandos básicos






