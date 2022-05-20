import os, subprocess, signal

try:
    os.kill(
        int(
            subprocess.Popen(
                'netstat -ano | findstr 0.0.0.0:15215', 
                stdout = subprocess.PIPE, 
                stderr = subprocess.PIPE, 
                shell = True
        ).communicate()[0].decode().strip().split(' ')[-1]), 
        signal.CTRL_C_EVENT
    )
    print('Server terminated')
except:
    print('Failed on terminate the server')