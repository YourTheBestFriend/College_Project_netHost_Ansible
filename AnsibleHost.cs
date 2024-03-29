﻿using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace CSharpAnsible
{
    public class AnsibleHost
    {
         // default parametrs
        public Process proc; // for execute program (shell)
        private string command;  // command for shell
        private string hostIpV4;
        private string hostname;
        private string password;
        // private string os;
        
        // assetors
        public string HostIpV4
        {
            set { hostIpV4 = value; } 
            get { return hostIpV4; }
        }
        public string Hostname
        {
            set { hostname = value; }
            get { return hostname; }
        }
        public string Password
        {
            set { password = value; }
            get { return password; }
        }
        public string Command 
        {
            set { command = value; }
            get { return command;}
        }
        // In the future 1/0 - windows or linux remote host
        // (because for windows you need use winrm on host and start PWSH script on remote host)
        public AnsibleHost() {}
        public AnsibleHost(string hostIpV4, string hostname, string password/*, string os*/)
        {
            proc = new Process();
            // paramets for Proccess
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.FileName = "bash"; // ApplicationName= !(bash)
            proc.StartInfo.RedirectStandardOutput = true;
            
            // in assetors write exception for verify data
            HostIpV4 = hostIpV4;
            Hostname = hostname;
            Password = password;
        }
        public string CreateNodeAnsible() => $"\n[{Hostname}]\n{HostIpV4}\n[{Hostname}:vars]\nansible_user = {Hostname}\nansible_password = {Password}\nansible_port = 5986\nansible_connection = winrm\nansible_winrm_server_cert_validation = ignore"; // may change port in the future, 5986 - default

        public void WriteOnAnsibleHostFile()
        {
            // >> add, rewrite > ////// echo '{CreateNodeAnsible()}' >> /etc/ansible/hosts
            Command = $"echo '{CreateNodeAnsible()}' >> /etc/ansible/hosts"; // pattern for write string - $"echo /"WritePattern/" > /etc/ansible/hosts" // !!! NEED to get access chmod 777 hosts
            proc.StartInfo.Arguments = " -c \" " + Command + " \"";
            proc.Start();
        }
        // check all hosts
        public string GetListHosts()
        {
            Command = $"ansible all --list-host"; 
            proc.StartInfo.Arguments = " -c \" " + Command + " \"";
            proc.Start();
            return proc.StandardOutput.ReadToEnd();
        }
        public string PingHost(string host_name)
        {
            Command = $"ansible {host_name} -m win_ping"; 
            proc.StartInfo.Arguments = " -c \" " + Command + " \"";
            proc.Start();
            return proc.StandardOutput.ReadToEnd();
        }
        public string PrintSystemInfo(string host_name)
        {
            Command = $"ansible {host_name} -m win_shell -a \"systeminfo\"";
            proc.StartInfo.Arguments = " -c \" " + Command + " \"";
            proc.Start();
            return proc.StandardOutput.ReadToEnd();
        }
        public string PrintProgram_x32(string host_name)
        {
            Command = $"ansible-playbook -l {host_name} /etc/ansible/mytask.yml";
            proc.StartInfo.Arguments = " -c \" " + Command + " \"";
            proc.Start();
            proc.WaitForExit();
            proc.StartInfo.Arguments = " -c \" " + "cat /tmp/log_programs_x32.txt" + " \""; // Command,
            proc.Start();
            return proc.StandardOutput.ReadToEnd();
        }
        public string PrintProgram_x64(string host_name)
        {
            Command = $"ansible-playbook -l {host_name} /etc/ansible/mytask2.yml";
            proc.StartInfo.Arguments = " -c \" " + Command + " \"";
            proc.Start();
            proc.WaitForExit();
            proc.StartInfo.Arguments = " -c \" " + "cat /tmp/log_programs_x64.txt" + " \""; // Command,
            proc.Start();
            return proc.StandardOutput.ReadToEnd();
        }
        public string Proccess_(string host_name)
        {
            Command = $"ansible-playbook -l {host_name} /etc/ansible/mytask3.yml";
            proc.StartInfo.Arguments = " -c \" " + Command + " \"";
            proc.Start();
            proc.WaitForExit();
            proc.StartInfo.Arguments = " -c \" " + "cat /tmp/log_process.txt" + " \""; // Command,
            proc.Start();
            return proc.StandardOutput.ReadToEnd();
        }
        public string MyCommand(string command) // host_name
        {
            // Command = $"ansible {host_name} -m win_shell -a \"{command}\"";
            proc.StartInfo.Arguments = " -c \" " + $"{command}" + " \""; // Command,
            proc.Start();
            proc.WaitForExit();
            return proc.StandardOutput.ReadToEnd();
        }
    } 
}