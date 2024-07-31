import paramiko
def ssh_connect(host, username, password, port=22):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddpolicy())
        client.connect(host=host, username=username, password=password, port=port)
        print("connection is succesfully established")
    except Exception as e:
        print(f"Error: {e}")

ssh_connect("192.168.29.185", "root", "Sanki123@")