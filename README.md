<h1 align="center">
   𝙇𝙞𝙣𝙓𝙥𝙡𝙤𝙞𝙩
</h1>

**𝙇𝙞𝙣𝙓𝙥𝙡𝙤𝙞𝙩** — a next-generation, all-in-one Python framework designed for exploiting, testing, and fully controlling Linux environments in **authorized penetration tests**.  
- 🔒 Version: 0.1
- 🐍 Built with: Python 3
- ⚠️ Disclaimer: For educational use only. Run at your own risk—may cause system damage or instability. Not for malicious intent!
**~DarkShadow**

## 📋 Features

- 🛡️ Root & non-root modules for system testing (e.g., fork bombs, disk overwrites, CPU exhaustion).
- 🔧 Auto-checks for required tools like bash, dd, rm.
- 📦 Installs missing tools via package managers (apt, yum, dnf) if root access granted.
- ⚡ Interactive menu with warnings before execution.
- 📜 Commands include: Fork bombs, data wipes, permission changes, and more—see commands.py for full list.

## 🛠️ Installation
```
pip3 install linxploit
```

## 🚀 Usage
Run the tool:
```
linxploit
```
- Choose root (1) or non-root (2) access.
- Select a module from the list.
- Confirm with 'start' to execute (or '0' back, '000' exit).

## 🛑 Important Notes

- 🔍 Requires Linux tools (e.g., bash, dd)—checks availability automatically.
- 📁 Code structure: main.py (core logic), utils.py (tool checks/installs), commands.py (exploit list).
- 🌐 Follow: x.com/darkshadow2bd
- ❗ Use in isolated environments only. Author not liable for misuse.

**⭐ Star the repo if useful.**
