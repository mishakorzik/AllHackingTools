import random
from time import sleep
from rich.progress import track

def do_step(step):
    sleep(random.uniform(000.001, 000.01))

for step in track(range(100), description="Zsh loading"):
    do_step(step)
