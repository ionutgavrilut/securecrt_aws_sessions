#$language = "Python"
#$interface = "1.0"

import os
import boto3
import sys
import shutil

def get_tag(tags, key='Name'):
    if not tags: return ''
    for tag in tags:
        if tag['Key'] == key:
            return tag['Value']
    return ''

def Main():

 template_session_config = 'D:\\Work\\aws-vm-template.ini'
 sessions_directory = 'C:\\Users\\ionutgavrilut\\AppData\\Roaming\\VanDyke\\Config\\Sessions\\My Project\\My Environment'
 aws_region = 'aws_region'
 aws_key = 'aws_key'
 aws_secret = 'aws_secret'
 
 for file in os.scandir(sessions_directory):
   os.remove(file.path)
	 
 ec2 = boto3.resource('ec2', region_name=aws_region, aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)
 
 for instance in ec2.instances.all():
   instance_name = get_tag(instance.tags) 

   if instance.private_ip_address is not None:
     shutil.copyfile(template_session_config, sessions_directory + "\\" + instance_name + '-' + instance.private_ip_address + ".ini")
     # opening the file in read mode
     file = open(sessions_directory + "\\" + instance_name + '-' + instance.private_ip_address + ".ini", "r")
     replacement = ""
     # using the for loop
     for line in file:
       line = line.strip()
       changes = line.replace("S:\"Hostname\"=", "S:\"Hostname\"=" + instance.private_ip_address)
       replacement = replacement + changes + "\n"

     file.close()
     # opening the file in write mode
     fout = open(sessions_directory + "\\" + instance_name + '-' + instance.private_ip_address + ".ini", "w")
     fout.write(replacement)
     fout.close()

Main()
