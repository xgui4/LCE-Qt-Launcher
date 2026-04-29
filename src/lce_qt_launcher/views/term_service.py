from rich import print

def print_error(msg : str, header : str = "Error! :") -> None:
    """_summary_ Print an pretty error msg

    Args:
        msg (str): _description_ : the error msg to show
        header (_type_, optional): Defaults to "Error! :"  _description_ The header to replace the default Error" 
    """
    print(f"[bold red]{header}[/bold red] {msg}")

def print_warning(msg : str, header : str = "Warning! :") -> None:
    """_summary_ Print an pretty warning msg

    Args:
        msg (str): _description_ the warning msg to show
        header (_type_, optional):  Defaults to "Warning! : " _description_ :  The header to replace the default Warning.
    """
    print(f"[yellow bold]{header}[/yellow bold]{msg}")

def print_information(msg : str) -> None:
    """_summary_ Print a pretty an colorful msg

    Args:
        msg (str): _description_ : the mssage to show
    """
    print(f"[yellow]{msg}[/yellow]")

def print_pretty(msg : str) -> None:
    """_summary_ Print a pretty msg , no default color
    Args:
        msg (str): _description_ : the mssage to show
    """
    print(msg)

def print_success(msg : str) -> None:
    """_summary_ Print an success green msg

    Args:
        msg (str): _description_  the success msg to show
    """
    print(f"[green] {msg}")