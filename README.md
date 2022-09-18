# College_Project_netHost_Ansible
- Program work on Linux
- Administration Windows 10

## i3 arch linux screen
![nethostLinux](https://user-images.githubusercontent.com/80000258/190925481-758db023-09b5-493d-8007-ca4e180306c8.png)

## What's need
- Install - Ansible, winrm (via pip) - for windows
- hosts - must be /etc/ansible/hosts
- On windows host execute *ps1 script https://github.com/ansible/ansible/blob/devel/examples/scripts/ConfigureRemotingForAnsible.ps1
- Set all file *yml - /etc/ansible/
- Set all file *ps1 - /etc/ansible/scripts/
- python -m venv .
- source College_Project_netHost_Ansible/bin/activate
- pip install -r requirements.txt
- csc /target:library /out:DLL/ansible_host.dll College_Project_netHost_Ansible/AnsibleHost.cs
- python main.py (or make executable file via pyinstaller)
