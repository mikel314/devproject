# Github pages y Jekyll

## Introducción

GitHub Pages es un servicio de alojamiento de sitios web estáticos proporcionado por GitHub. Permite publicar páginas web directamente desde un repositorio de GitHub sin necesidad de servidores adicionales. Además permite crear todo el contenido de la página usando archivos Markdown que son editables y visualizables desde el VS Code.

En este proyecto se usuaran muy pocas de las funcionalidades de Githubpagesc con Jekyll, para una documentación completa se puede visitar el tuturial [Setting up a GitHub Pages site with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)


## Setup

No es necesario isntalar nada ni en local ni en la VM para trabajar con Github pages. Todo se ejecuta en el reposistorio de Github en la nube. Para habilitarlo basta con:

* Ve a Settings → Pages dentro de tu repositorio en GitHub.
* En la sección "Source", selecciona la rama main y la carpeta docs/ y haz clic en "Save".
* GitHub generará automáticamente tu sitio en https://tu-usuario.github.io/tu-repositorio/.

## Set up Jekyll
Crea y modifica el archivo _config.yml de la carpeta docs/ para personalizar el sitio web.
Ejemplo de configuración básica:

```yaml
title: "Mi Blog con Jekyll"
description: "Documentación generado con Jekyll y alojado en GitHub Pages"
theme: jekyll-theme-minimal
```
Para cambiar el diseño, puedes usar temas compatibles con GitHub Pages:
[Lista de temas soportados](https://pages.github.com/themes/)

## Crear documentación
Una vez activado, todos los archivos .md de la carpeta ``docs/`` seran transformados en htmls visualizables en la url https://tu-usuario.github.io/tu-repositorio/ de forma totalmente transparente al usuario.

Es recomendable crear un [index.md](index.md) con la estructura de la documentación y los links al resto de páginas.

Los archivos de documentación estan escritos en Markdowns, este [tutorial para principiantes](https://hackernoon.com/a-beginners-guide-to-markdown-everything-you-need-to-know-to-get-started) está bien para aprender lo básico. También es útil leer [cómo crear code bloks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks) ya que es algo que usaremos mucho en una documentación de un proyecto de desarrollo.


