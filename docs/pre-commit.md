Se instala fácilmente con:

bash
Copiar
Editar
pip install pre-commit
Luego, se debe inicializar en el repositorio con:

bash
Copiar
Editar
pre-commit install
Esto crea un archivo .pre-commit-config.yaml, donde se configuran los hooks.

pre-commit run --all-files

pre-commit autoupdate

rm -rf node_modules
