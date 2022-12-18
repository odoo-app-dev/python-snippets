import os
import platform
import subprocess
import logging

def ping(machine_ip):
    if platform.system() == 'Linux':
        response = os.system("ping -c 1 " + machine_ip)
        if response == 0:
          logging.warning("Biometric Device is Up/Reachable.")
            logging.warning("Biometric Device is Up/Reachable.")
        else:
            logging.warning("Biometric Device is Down/Unreachable.")
    else:
        prog = subprocess.run(["ping", machine_ip], stdout=subprocess.PIPE)
        if 'unreachable' in str(prog):
            logging.warning("Biometric Device is Down/Unreachable.")
        else:
            logging.warning("Biometric Device is Up/Reachable.")
