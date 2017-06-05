import socket
import sys
import time

#Connection details
class mytarget:
  def __init__(self,host,port,channel,user,passwd,receiver):
    self.svhost = host
    self.svport = port
    self.clienthost = '210.245.30.132'
    self.channel = channel
    self.user = user
    self.passwd = passwd
    self.receiver = receiver

# Input Parametter
host = input('Host: ')
port = input('Port: ')

channel = input('Channel: ')
user = input('User: ')
passwd = input('Passwd: ')
receiver = input('Receiver: ')

#Passing parametter to class.
client = mytarget(svhost,svport,'channel,user,passwd,receiver)


#Connecting to irc server and join to channel
try:
  con = socket.socket()
  con = socket.create_connection((client.svhost, client.svport))
  print(('CONNECTING TO.. %s\r\n' % client.svhost).encode())
  con.send(('NICK %s \r\n' % client.user).encode())
  time.sleep(2)
  con.send(('USER %s %s root-me :%s \r\n' %(client.user, client.svhost, client.user)).encode())
  time.sleep(2)
  con.send(('JOIN %s \r\n' %client.channel).encode())
  print('Joined to.. %s\r\n' %client.channel)
  time.sleep(5)
  
  
  # ======= Root-me Programming Challenges ===========
  
  con.send(('PRIVMSG Candy :!ep1 \r\n').encode())
  
  #Listen respond from server
  while True:
    respond = ""
    respond = con.recv(1024).strip().decode()
    
    print(respond)

    #PRVG num is #3 and #5
    if 'Candy!Candy' in respond:
      msglist = respond.replace(':','').split()
      a = float(msglist[3])
      b = float(msglist[5])

      #calculating
      res = round(pow(a,0.5)*b,2)
      res = str(res)
      #res = (res.replace('.',','))

      print(res)
      con.send(('PRIVMSG Candy :!ep1 -rep %s \r\n' %res).encode())
      print('Sending answer successful!')
      
    #PING - PONG
    pp = respond.split()
    if pp[0] == 'PING':
      print(pp)
      con.send(('PONG %s \r\n' %pp[1]).encode())
      
except Exception as e:
  print(e)
  sys.exit(1)
  
