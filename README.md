# College_Project_netHost_Ansible
- Program work on Linux
- Administration Windows 10

## i3 arch linux screen


## What's need
- 1. Install - Ansible, winrm (via pip) - for windows
- 2. hosts - must be /etc/ansible/hosts
- 3. On windows host execute *ps1 script https://github.com/ansible/ansible/blob/devel/examples/scripts/ConfigureRemotingForAnsible.ps1
- 4. Set all file *yml - /etc/ansible/
- 5. Set all file *ps1 - /etc/ansible/scripts/
- 6. python -m venv .
- 7. source College_Project_netHost_Ansible/bin/activate
- 8. pip install -r requirements.txt
- 9. csc /target:library /out:DLL/ansible_host.dll College_Project_netHost_Ansible/AnsibleHost.cs
- 10. python main.py (or make executable file via pyinstaller)