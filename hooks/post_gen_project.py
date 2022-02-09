import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Creando repo de GIT...{RESET_ALL}")

subprocess.call(['pip', 'install', '-r', "requeriments.txt"])

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}Se ha creado el repositorio, ya puedes iniciar tu proyecto!{RESET_ALL}")