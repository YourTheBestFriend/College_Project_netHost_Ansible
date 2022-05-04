using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WPF_app_for_admin
{
    public partial class MainWindow : Window
    {
        // Список или много создавать не надо т.к я чисто в файл записываю и оно там храниться, но я вот думаю может смылка моего класса нету, хотя это для переноса на Linux
        AnsibleHost remotehost;
        // get acces via terminal linux (wsl on linux)
        Process proc = new Process();
        public MainWindow()
        {
            InitializeComponent();
            proc.StartInfo.FileName = "wsl";
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.RedirectStandardOutput = true;
        }

        // get data (host ipv4, hostname, password) via textbox
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            remotehost = new AnsibleHost(this.TextBoxHosIpV4.Text, this.TextBoxHostName.Text, this.TextBoxPassword.Text);
            remotehost.WriteOnAnsibleHostFile();
            TextBox_Logs.AppendText(remotehost.CreateNodeAnsible());
        }

        // return all 
        public string GetListHosts()
        {
            // check all hosts
            proc.StartInfo.Arguments = $"ansible all --list-host"; // Только тут надо выводить названия
            proc.Start();
            return proc.StandardOutput.ReadToEnd();
        }

        // print all remote host on machine
        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            TextBoxAllRemoteHost.Text = GetListHosts();
        }
        // ping host
        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            // ping host
            proc.StartInfo.Arguments = $"ansible {this.TextBoxtHostnameOrAll.Text} -m win_ping";
            proc.Start();
            OutputTextBox.Text = proc.StandardOutput.ReadToEnd();
        }
        // systeminfo
        private void Button_Click_3(object sender, RoutedEventArgs e)
        {
            proc.StartInfo.Arguments = $"ansible {this.TextBoxtHostnameOrAll.Text} -m win_shell -a \"systeminfo\"";
            proc.Start();
            OutputTextBox.Text = proc.StandardOutput.ReadToEnd();
        }
    }
}
