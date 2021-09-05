from time import sleep
from rich.console import Console

console = Console()
tasks = [f"data {n}" for n in range(1, 4)]

with console.status("[bold green]I perform the task ...[/bold green]") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} done!")

console1 = Console()
tasks1 = [f"data {n}" for n in range(1, 4)]

with console1.status("[bold green]I perform the task ...[/bold green]") as status:
    while tasks1:
        task = tasks.pop(0)
        sleep(1)
        console1.log(f"{task} done!")

