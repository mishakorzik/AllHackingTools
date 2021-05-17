import time
import itertools
import threading
import sys

done = False

def animate():
    for c in itertools.cycle(['|', '/', '—', '\\']):
        if done:
            break
        sys.stdout.write('\rWait a moment AdminHack loading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('')

t = threading.Thread(target=animate)
t.start()

 
time.sleep(3)
done = True
print("")
