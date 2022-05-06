import subprocess

data = subprocess.check_output(['top'])
print(data)
