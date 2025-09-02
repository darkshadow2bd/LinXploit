import shutil
import subprocess

def check_tool(tool):
    return shutil.which(tool) is not None

def check_command_available(command):
    return all(check_tool(tool) for tool in command['required_tools'])

def get_missing_tools(commands_list):
    all_required_tools = set()
    for cmd in commands_list:
        all_required_tools.update(cmd['required_tools'])
    missing = [tool for tool in all_required_tools if not check_tool(tool)]
    return missing

def install_tools(tools):
    package_managers = [('apt', 'apt install'), ('yum', 'yum install'), ('dnf', 'dnf install')]
    for pm, install_cmd in package_managers:
        if check_tool(pm):
            install_command = f"sudo {install_cmd} {' '.join(tools)}"
            subprocess.run(install_command, shell=True)
            break
    else:
        print("No supported package manager found.")
