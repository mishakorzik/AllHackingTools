import random
from time import sleep
from rich.progress import track

def do_step(step):
    sleep(random.uniform(0.001, 0.01))

for step in track(range(100), description="[cyan]Processing ..."):
    do_step(step)
