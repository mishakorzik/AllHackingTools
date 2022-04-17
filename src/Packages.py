from time import sleep
from rich.console import Console

console = Console()
tasks = [f"data {n}" for n in range(1, 4)]

with console.status("[bold green]I perform the task ...[/bold green]") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(0.7)
        console.log(f"{task} done!")
