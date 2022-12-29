# check if a module is installed. If not, install it and then import it again
import logging
try:
    from getkey import getkey, key
    logging.info('getkey imported properly!')
except:
    try:
        import subprocess
        subprocess.run(['pip', 'install', 'getkey'])
        from getkey import getkey, key
        logging.info('getkey imported after installation!')
    except Exception as e:
        logging.error(f'import getkey error:{e}')
