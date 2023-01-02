# -*- coding=utf-8 -*-
import subprocess
import platform

def ping_test(ip='8.8.8.8'):
    import subprocess, platform, time
    # Ping parameters as function of OS
    linux = True if platform.system().lower()!="windows" else False
    ping_str = "-c 1 -W 1" if  linux else "-n 1 -w 1000"
    args = "ping " + " " + ping_str + " " + ip
    need_sh = True if  linux else False
    # Ping
    out = subprocess.run(args,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=need_sh).stdout.decode('utf-8')

    res = out.find(' 0% packet loss') > 0 if linux else out.find('Received = 1') > 0
    if res:
        if linux:
            time_index = out.find('max/mdev = ') + 11
            res = ip + ',' + str(round(float(out[time_index: time_index + 15].split('/')[0]), 2)) + ',ms'
        else:
            time_index = out.find('Average = ') + 10
            res = ip + ',' + str(round(int(out[time_index: time_index + 15].split('ms')[0]), 2)) + ',ms'

    return res
  
# ping_test('amazon.com') -> 'amazon.com,172,ms'
