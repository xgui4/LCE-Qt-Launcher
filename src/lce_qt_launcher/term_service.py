from rich import print

def print_error(msg : str, header : str = "Error! :"):
    print(f"[bold red]{header}[/bold red] {msg}")

def print(msg : str, header : str = "Warning! :"):
    print(f"[yellow bold]{header}[/yellow bold]{msg}")

def print_information(msg : str):
    print(f"[yellow]{msg}[/yellow]")

def print_pretty(msg : str):
    print(msg)

def print_success(msg : str):
    print(f"[green] {msg}")

def show_image(path : str):
    from term_image.image import from_file
    image = from_file(path)
    image.draw()