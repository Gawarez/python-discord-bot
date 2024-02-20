import os
from paramiko import SSHClient, AutoAddPolicy
from dotenv import load_dotenv

def runCommandSSH(command):
  load_dotenv()
  HOST = os.getenv('HOST')
  USER = os.getenv('USER')
  PASS = os.getenv('PASS')

  client = SSHClient()
  client.set_missing_host_key_policy(AutoAddPolicy())
  client.connect(hostname=HOST, username=USER, password=PASS)

  _stdin, _stdout, _stderr = client.exec_command(command)
  return _stdout.read().decode()
  client.close()