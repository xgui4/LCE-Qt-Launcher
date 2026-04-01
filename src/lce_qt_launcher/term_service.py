from rich import print

def print_error(msg : str, header : str = "Error! :") -> None:
    print(f"[bold red]{header}[/bold red] {msg}")

def print_warning(msg : str, header : str = "Warning! :") -> None:
    print(f"[yellow bold]{header}[/yellow bold]{msg}")

def print_information(msg : str) -> None:
    print(f"[yellow]{msg}[/yellow]")

def print_pretty(msg : str) -> None:
    print(msg)

def print_success(msg : str) -> None:
    print(f"[green] {msg}")