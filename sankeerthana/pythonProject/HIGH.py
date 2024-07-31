import paramiko
def ssh_connect(host,username,password,port=22):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host,username=username,password=password,port=port)

        print("Connection is successful")
    except Exception as e:
        print(f"Error: {e}")
ssh_connect("192.168.29.185","root","Sanki123@")


