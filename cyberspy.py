import subprocess
import time
print("instalando dependecias")

install_command1 = 'pkg update'

# Executa o comando usando subprocess
subprocess.run(install_command1, shell=True)

time.sleep(8)

install_command2 = 'pkg update'

# Executa o comando usando subprocess
subprocess.run(install_command2, shell=True)
time.sleep(8)

install_command3 = 'pkg install git'

# Executa o comando usando subprocess
subprocess.run(install_command3, shell=True)
time.sleep(8)

install_command4 = 'git clone https://github.com/Darkmux/Cyberspy.git'

# Executa o comando usando subprocess
subprocess.run(install_command4, shell=True)
time.sleep(8)

install_command5 = 'cd Cyberspy'

# Executa o comando usando subprocess
subprocess.run(install_command5, shell=True)
time.sleep(3)

install_command6 = 'bash Cyberspy.sh'

subprocess.run(install_command6, shell=True)
