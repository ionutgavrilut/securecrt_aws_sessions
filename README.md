### Description:
A script to sync your session list in SecureCRT with AWS EC2 instances. If you have ephemeral instances, and you would like to use SecureCRT, this script may be a good idea. I'm using this script as a "Command" in SecureCRT, in order to refresh all session list for an environment.
This scripted was tested using:
- Windows 10 Pro
- SecureCRT 9.2.2
- Python 3.10.6

### Steps:
- Install Python 3, and install Boto3 library with *pip install boto3* ([more details here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html))
- Download these scripts and replace variables in refresh-AWS-instances.py script:
- - *template_session_config* - this variable will be a file that you will create. Copy a current file from an existing session and use it as a template.
You can find session files in C:\Users\ionutgavrilut\AppData\Roaming\VanDyke\Config (or you can check in SecureCRT -> Options -> Global Options -> Configuration Paths) Choose a file that you want to use as a template, and copy it to another folder. You have to change one line in this file. Search for **S:"Hostname"=x.y.z.w** and replace this line with **S:"Hostname"=**

- - *sessions_directory* - this directory is where to save sessions. This is used by SecureCRT and you should set the correct directory. You can see an example in the script.
- - *aws_region* - AWS Region
- - *aws_key* - AWS Access Key ID
- - *aws_secret* - AWS Secret access key

- Create 2 commands in SecureCRT. We will have 2 commands with 2 different scripts: first one will delete all the sessions and create the new ones; second script will refresh the list in SecureCRT.

- - **First command:**
- - - Script: refresh-AWS-instances.py
- - - Create a command that run your main script
- - - Command function: Launch Application (python executable)
- - - Command arguments: Script; make sure you will double quote this string, because it can contain spaces.

![SecureCRT Screenshot](https://i.imgur.com/9wteqj1.png)

- - **Second command (optional):**
- - - Script: refresh-session-list.py
- - - This command will refresh the session manager, to not restart the SecureCRT everytime you recreate sessions.
- - - Command function: Run Script

![SecureCRT Screenshot](https://i.imgur.com/n8DFfws.png)
