from colorama import Fore, init
class Debuger:
    def __init__(self):
        self.debug = True
        init(autoreset=True)

    def print_ready(self):
        if self.debug:
            print(Fore.BLUE + "BOT IS READY TO USE!")

    def print_update(self, update):
        if self.debug:
            print(Fore.GREEN + str(update.type))

    def user_registered(self, username):
        if self.debug:
            print(Fore.YELLOW +f"USER REGISTRED BY NAME {username}")

    def error_reply(self):
        print(Fore.RED + f"ERROR RESPONDING MAYBE INTERNAL")
