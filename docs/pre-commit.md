# Pre-commit hooks

`pre-commit` es una herramienta que ejecuta hooks antes de realizar un commit en Git. Se utiliza para aplicar automáticamente verificaciones y formateos en el código, asegurando calidad y consistencia antes de que se guarde en el repositorio.

# Set up

Se instala fácilmente con:

```console
pip install pre-commit
```

Luego, se debe inicializar en el repositorio, ejecutando en la raiz:

```console
pre-commit install
```

Esto crea un archivo `.pre-commit-config.yaml`, donde se configuran los hooks.
Un ejemplo de archivo de configuración puede ser:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace # Elimina espacios en blanco innecesarios
      - id: end-of-file-fixer # Asegura que los archivos terminen con una línea en blanco
      - id: check-yaml # Verifica que los archivos YAML sean válidos
      - id: check-ast # Verifica que los archivos Python sean sintácticamente correctos

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black # Formatea archivos Python con Black
```

En este archivo se añaden todos los hooks que queremos ejecutar antes de hacer un commit. La versión (rev) podra ser actualizada con `pre-commit autoupdate` como se explica a continuación.

## Ejecución de los hooks

Todos los hooks serán ejecutados autoamticamente cuando se haga un `git commit` que sacará por el terminal el resultado de los tests. Si algún hook falla (por un formato incorrecto por ejemplo), no se llevará a cabo el commit.

Algunos hooks (los de formato) cambiaran el archivo problematico que tendrá que ser añadido de nuevo con `git add` ante de ejecutar de nuevo el commit.

Si se quiere ejecutar los hook antes del commit para asegurarnos manualmente de que todo esta ok, podemos hacerlo con:

```console
pre-commit run --all-files
```

La primera vez que se ejecuta un hook el sistema lo instala y tarde un rato. Además crear una carpeta cache en el repositorio, `node_modules` para ir más rapido las siguintes veces. Esta carpeta es conveniente añadirla al `.gitignore`.

## Actualización de los hooks

Para actualizar a la última versión de cada hook podemos ejecutar

```console
pre-commit autoupdate
```

Esto es especialmente útil la primera vez que añadimos un hook al archivo de configuración si no sabemos cual es la última versión.
