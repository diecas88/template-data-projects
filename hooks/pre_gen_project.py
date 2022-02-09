import os
import sys

folder = "{{ cookiecutter.folder }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if folder.startswith("x"):
   print(f"{ERROR_COLOR}ERROR: {folder=} Nombre no valido para la carpeta.{RESET_ALL}")

   sys.exit(1)

print(f"{MESSAGE_COLOR}construyendo!")
print(f"Se ha creado el proyecto en la ruta: => { os.getcwd() }{RESET_ALL}")