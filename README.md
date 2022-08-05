### Description:
A script to sync your session list in SecureCRT with AWS EC2 instances. If you have ephemeral instances, and you would like to use SecureCRT, this script may be a good idea. I'm using this script as a "Command" in SecureCRT, in order to refresh all session list for an environment.
This scripted was tested using:
- Windows 10 Pro
- SecureCRT 9.2.2
- Python 3.10.6

### Steps:
- Install Python 3, and install Boto3 library ([more details here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html))
- Download this script and replace variables:
- - template_session_config - this variable should be replaced with a file config that you're using. Configuration folder is C:\Users\ionutgavrilut\AppData\Roaming\VanDyke\Config, or you can check in SecureCRT -> Options -> Global Options -> Configuration Paths. Choose a file that you want to use as a template, and copy it to another folder. This should be this variable.
- - sessions_directory - this directory is where to save sessions. This is used by SecureCRT and you should set the correct directory.
- - aws_region - AWS Region
- - aws_key - AWS Access Key ID
- - aws_secret - AWS Secret access key

##### Thank you! Any contribution will be appreciated!
