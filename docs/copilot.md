# GitHub Copilot para Visual Studio Code

_documentación generada con copilot y editada manualmente_

## Introducción

En la guia [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview) se describe como instalar Copilot en VS code y las funcionalidades principales. Es muy recomendable leerlo.

## Instalación

Para instalar GitHub Copilot en Visual Studio Code, sigue estos pasos:

1. Abre Visual Studio Code.
2. Ve a la extensión de Marketplace haciendo clic en el icono de extensiones en la barra lateral izquierda.
3. Busca "GitHub Copilot".
4. Haz clic en "Instalar" en la extensión de GitHub Copilot.
5. Una vez instalada, inicia sesión con tu cuenta de GitHub para activar la extensión.

## Funcionalidades Principales

### Autocompletado de Código

GitHub Copilot sugiere líneas completas de código y bloques de código basados en el contexto del archivo en el que estás trabajando.

### Generación de Código

Puedes generar código a partir de comentarios en lenguaje natural. Simplemente escribe un comentario describiendo lo que quieres que haga el código y GitHub Copilot generará el código correspondiente. Por ejemplo, unit tests, optimización de funciones o repositorios enteros.

### Refactorización de Código

GitHub Copilot puede ayudarte a refactorizar tu código sugiriendo mejoras y optimizaciones basadas en las mejores prácticas.

### Inline chat

With Copilot Chat, you can start a chat conversation with Copilot in VS Code to ask specific tasks about your code by using natural language. Simply press `Ctrl+I` on your keyboard to bring up Copilot Inline Chat.

Copilot Inline Chat gives you a chat interface that lets you ask questions about the code in the active editor.

This work in any file opened or even in the **terminal**.

### Explicacion de Código

Copilot generates natural language descriptions of the code's functionality and purpose. This can be useful if you want to understand the code's behavior or for non-technical stakeholders who need to understand how the code works.

### Documentación Automática

Genera automáticamente documentación para tus funciones y clases basándose en el código y los comentarios existentes.

## Comandos Principales de GitHub Copilot

GitHub Copilot ofrece varios comandos útiles que puedes usar para mejorar tu flujo de trabajo en Visual Studio Code.
Basta con seleccionar un trozo de codigo, abrir el Inline chat con `Ctrl+I` y escribir el comando con `/command`
Aquí hay una lista de los comandos principales.

### /doc

El comando `/doc` genera documentación para la función o clase seleccionada. Esto es útil para crear comentarios de documentación automáticamente basados en el código existente.

### /explain

El comando `/explain` proporciona una explicación en lenguaje natural del código seleccionado. Esto puede ayudarte a entender mejor el propósito y funcionamiento del código.

### /fix

El comando `/fix` sugiere correcciones para el código seleccionado. Esto puede incluir la corrección de errores, la mejora del rendimiento o la refactorización del código según las mejores prácticas.

### /test

El comando `/test` genera pruebas unitarias para la función o clase seleccionada. Esto es útil para asegurarte de que tu código funciona correctamente y para prevenir futuros errores.

### /optimize

El comando `/optimize` sugiere optimizaciones para el código seleccionado. Esto puede incluir mejoras en el rendimiento, la reducción de la complejidad del código o la adopción de mejores prácticas.
