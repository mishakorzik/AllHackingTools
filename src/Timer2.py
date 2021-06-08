import time
import itertools
import threading
import sys

done = False

def animate():
    for c in itertools.cycle(['33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']):
        if done:
            break
        sys.stdout.write('\Launch the tool in a few seconds ' + c)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('')

t = threading.Thread(target=animate)
t.start()

 
time.sleep(32.9)
done = True
print("")
