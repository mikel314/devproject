# Logging using `loguru` package

## Introduction

Loguru is a Python logging library designed to make logging in Python more intuitive, flexible, and user-friendly. It provides a simple and powerful API for logging, eliminating much of the boilerplate code required by the standard logging module.

## Built-in Features:

- **File Rotation**: Automatically rotates log files based on size, time, or both.
- **Colorful Output**: Logs are colored by default for better readability in the console.
- **Structured Logging**: Supports JSON and other structured formats for easier log parsing.
- **Exception Handling**: Automatically captures and logs exceptions with tracebacks.
- **Customizable Formatting**: Easily customize log message formats.

## Example of use case

```python
from loguru import logger

# Add a file sink with rotation
logger.add("app.log", rotation="10 MB", level="INFO")

# Log some messages
logger.info("Starting the application...")
logger.debug("This is a debug message (won't be logged due to level=INFO)")
logger.warning("Something might be wrong!")
logger.error("An error occurred!")

# Log an exception
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Division by zero error!")
```
