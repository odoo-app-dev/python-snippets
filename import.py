# check if a module is installed. If not, install it and then import it again
try:
    from zk import ZK
except:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyzk'])
    from zk import ZK
