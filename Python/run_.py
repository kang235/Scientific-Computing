# run_.py
from subprocess import Popen, PIPE
import shlex
def run_(cmd, input=None):
    p = Popen(shlex.split(cmd), stdin=PIPE, stderr=PIPE,
              universal_newlines=True)
    err = p.communicate(input=input)[1]
    print(err, end='')
    if err:
        print('return code =', p.returncode)
    elif p.returncode < 0:
        print('return code =', - p.returncode)
        if not input:
            print('Enter "'+cmd+'" to see error message.')
    return p.returncode
