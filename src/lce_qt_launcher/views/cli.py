import webbrowser
from sys import argv

from lce_qt_launcher.app import AppContext
from lce_qt_launcher import legal_str
from lce_qt_launcher.managers import mod_manager
from lce_qt_launcher.models.app_data import AppData
import lce_qt_launcher.views.term_service as term_service

MENU_STR = """
0. [bold green] Select Instance [/bold green]
1. [bold green] Play [/bold green]
2. [bold green] Install [/bold green]
3. [bold green] Marketplace  [/bold green]
4. [bold red] exit [/bold red]
"""

WARNING_LABEL = "CLI mode is currently untested and might be working correctly and will be reworked soon."
INCORRECT_CHOICE_LABEL = "Incorrect Choice! Please select from 0 to 4"
CHOOSE_CHOICE_LABEL = "Choose a option between 0 and 3 : \n"
OUT_OF_RANGE_ERROR_LABEL = "Invalid choice: Number is out of range."
INORRECT_NUMBER_VALUE_LABEL = "Invalid input: Please enter a valid integer."
CHOOSE_INST_LABEL = "Choose a instance to select : \n"
MARKETPLACE_LINK = "https://lce-hub.github.io/piston/"
SUCESS_SELECTING = "Successfully selected:"

OPTIONS : dict[str, str] = {
    "0" : "select",
    "1" : "play",
    "2" : "install",
    "3" : "marketplace",
    "4" : "exit"
}

OPTION_MARKPLACE_LABEL = "[bold green]  1. Open the marketplace (right now : LCE Emerald Marketplace) [/bold green]"
OPTION_INSTANCE_INSTALLER_LABEL = "[bold green]  2. Open the LCE Content Installer [/bold green]"
CHOOSE_MARKPLACE_LABEL = "Choose a option between 1 and 2 : \n"

def launch_cli(appContext : AppContext, appData : AppData) -> None:
    """
    _summary_ : launch the cli interface

    Args:
        instance_man : the instancer Manager object
    """

    term_service.print_warning(WARNING_LABEL)

    instanceMan = appContext.instanceMan
    instancesLists = appData.instsList

    arg_action = None
    if len(argv) > 1:
        arg_action = argv[1]

    in_menu : bool = True
    while in_menu:
        term_service.print_pretty(legal_str)
        term_service.print_pretty(MENU_STR)
        
        if arg_action:
            user_input = arg_action
            arg_action = None 
        else:
            user_input = input(CHOOSE_CHOICE_LABEL).strip()

        action = OPTIONS.get(user_input)

        if action == "select":
            for i, instance in enumerate(instancesLists, start=1):
                print(f"{i} : {instance.name} (path : {instance.installation_path})")
            user_input = input(CHOOSE_INST_LABEL)
            try:
                selected_index = int(user_input) - 1
                if 0 <= selected_index < len(instancesLists):
                    instanceMan.instance = instancesLists[selected_index]
                    term_service.print_information(f"{SUCESS_SELECTING} {instancesLists[selected_index].name}")
                else:
                    term_service.print_error(OUT_OF_RANGE_ERROR_LABEL)
            except ValueError:
                term_service.print_error(INORRECT_NUMBER_VALUE_LABEL)
            term_service.clear_console()
            
        elif action == "play":
            print(instanceMan.play())
            term_service.clear_console()
            
        elif action == "install":
            print(instanceMan.install_instance())
            term_service.clear_console()
            
        elif action == "marketplace":
            term_service.print(OPTION_MARKPLACE_LABEL)
            term_service.print(OPTION_INSTANCE_INSTALLER_LABEL)
            user_input = input(CHOOSE_MARKPLACE_LABEL)
            if user_input == "1":
                webbrowser.open(MARKETPLACE_LINK)
            if user_input == "2":
                mod_manager.main()
            term_service.clear_console()
                
        elif action == "exit":
            exit()
            
        else:
            term_service.clear_console()
            term_service.print_error(INCORRECT_CHOICE_LABEL)
