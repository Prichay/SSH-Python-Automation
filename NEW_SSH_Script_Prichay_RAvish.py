import paramiko
import time
import pandas as p
print("*"*70)
print("Before Running This Script Make sure that system has 'Paramiko' Lib installed in it")
print("*"*70)
print('To add new server in automation just simply add in existing excell file')
df=p.read_excel('C:\\Users\\Prichay\\Desktop\\Input.xlsx')
loop=len(df.index)
for i in range (loop):
    d=df.iloc[i]#Extract row data
    cred=[]#empty list to append credential to read by ssh
    for a in d:
        cred.append(a)
    localtime = time.asctime( time.localtime(time.time()) )
    path="C:\\Users\\Public\\Documents\\Prichay.txt"
    ssh=paramiko.SSHClient()
    print("SSHClient connection successfull\n")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Added the Host Missing Key to avoid being questioned for authorisation\n")
    ssh.connect(hostname=str(cred[0]),username=str(cred[1]),password=str(cred[2]))
    print("SSh is Connected\n")
    stdin,stdout,stderr = ssh.exec_command(str(cred[3])+"\n")
    print("Executed the command to change the name 'prichay' in the 2nd line of a test file in the dir '/usr/ravish/ravish.ini'\n")
    print("Now writing the changes in the file for logging and you will find the file in above given DIR\n")
    msg="\n\n\t\t"+localtime+"\n\nThis is a test file\nIt will contain the ip address and what changes took place in server\nip address is "+cred[0]+"\nCommand executedon server host is"+cred[3]+"\nlogges the changes in this file\n"
    with open(path, 'a+') as f:
        f.write(msg)
