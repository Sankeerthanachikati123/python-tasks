import paramiko
def ssh_connect(host, username, password, port):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password, port=port)
        print("connection is succesfully established")
    except Exception as e:
        print(f"Error: {e}")

ssh_connect("localhost", "root", "password",port=22)