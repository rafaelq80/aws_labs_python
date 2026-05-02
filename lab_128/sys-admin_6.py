import subprocess
import platform

command = "ps"
commandArgument = "aux" if platform.system() != "Darwin" else "-x"

print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])