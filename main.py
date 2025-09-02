import sys
import subprocess
from commands import COMMANDS
from utils import check_command_available, get_missing_tools, install_tools

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def display_banner():
    print(f"{YELLOW}𝙇𝙞𝙣𝙓𝙥𝙡𝙤𝙞𝙩 V0.1{RESET}")
    print(f"{GREEN}DarkShadow              Follow here: x.com/darkshadow2bd{RESET}")
    print(f"{RED}⚠️ For educational use only. Run at your own risk.{RESET}")

def main():
    display_banner()
    while True:
        print(f"\n{YELLOW}[1] I have root access{RESET}")
        print(f"{YELLOW}[2] I don't have root access{RESET}")
        print(f"{YELLOW}[3] Exit{RESET}")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Root access flow
            print("Please enter your root password to proceed.")
            if subprocess.run('sudo -v', shell=True).returncode != 0:
                print(f"{RED}Invalid password or sudo not available.{RESET}")
                continue
            root_commands = [cmd for cmd in COMMANDS if cmd['requires_root']]
            missing_tools = get_missing_tools(root_commands)
            if missing_tools:
                print(f"{RED}Missing tools: {', '.join(missing_tools)}{RESET}")
                install_choice = input("Do you want to install missing tools? (yes/no): ").strip().lower()
                if install_choice == 'yes':
                    print("Downloading tools...")
                    install_tools(missing_tools)
                    print("All are successfully downloaded.")
            available_commands = [cmd for cmd in root_commands if check_command_available(cmd)]
            if not available_commands:
                print(f"{RED}No root commands available.{RESET}")
                continue
            print(f"\n{YELLOW}Available root modules:{RESET}")
            for i, cmd in enumerate(available_commands, 1):
                print(f"[{i}] {cmd['description']}")
            module_choice = input("Enter module number to start (or 0 to go back, 000 to exit): ").strip()
            if module_choice == '000':
                sys.exit(0)
            elif module_choice == '0':
                continue
            try:
                index = int(module_choice) - 1
                selected_cmd = available_commands[index]
            except (ValueError, IndexError):
                print(f"{RED}Invalid choice.{RESET}")
                continue
            print(f"\n{YELLOW}Module: {selected_cmd['description']}{RESET}")
            print(f"What does: {selected_cmd['description']}")
            print(f"{RED}Warning: This action is irreversible and can cause serious damage.{RESET}")
            confirm = input(f"Type '{GREEN}start{RESET}' to execute, '0' to go back, '000' to exit: ").strip().lower()
            if confirm == 'start':
                subprocess.run(selected_cmd['command_string'], shell=True)
                print(f"{RED}Boom executed, alert! -any time system will be crushed.{RESET}")
                sys.exit(0)
            elif confirm == '0':
                continue
            elif confirm == '000':
                sys.exit(0)
            else:
                print(f"{RED}Invalid input.{RESET}")

        elif choice == '2':
            # Non-root access flow
            non_root_commands = [cmd for cmd in COMMANDS if not cmd['requires_root'] and 
check_command_available(cmd)]
            if not non_root_commands:
                print(f"{RED}No non-root commands available.{RESET}")
                continue
            print(f"\n{YELLOW}Available non-root modules:{RESET}")
            for i, cmd in enumerate(non_root_commands, 1):
                print(f"[{i}] {cmd['description']}")
            module_choice = input("Enter module number to start (or 0 to go back, 000 to exit): ").strip()
            if module_choice == '000':
                sys.exit(0)
            elif module_choice == '0':
                continue
            try:
                index = int(module_choice) - 1
                selected_cmd = non_root_commands[index]
            except (ValueError, IndexError):
                print(f"{RED}Invalid choice.{RESET}")
                continue
            print(f"\n{YELLOW}Module: {selected_cmd['description']}{RESET}")
            print(f"What does: {selected_cmd['description']}")
            print(f"{RED}Warning: This action can cause system instability or data loss.{RESET}")
            confirm = input(f"Type '{GREEN}start{RESET}' to execute, '0' to go back, '000' to exit: ").strip().lower()
            if confirm == 'start':
                subprocess.run(selected_cmd['command_string'], shell=True)
                print(f"{RED}Boom executed, alert! -system may become unresponsive.{RESET}")
                sys.exit(0)
            elif confirm == '0':
                continue
            elif confirm == '000':
                sys.exit(0)
            else:
                print(f"{RED}Invalid input.{RESET}")

        elif choice == '3':
            sys.exit(0)
        else:
            print(f"{RED}Invalid choice.{RESET}")

if __name__ == "__main__":
    main()
