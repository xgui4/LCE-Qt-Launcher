from rich import print

def print_error(msg : str):
    print(f"[bold red]Error![/bold red] {msg}")

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