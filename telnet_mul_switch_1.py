import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnt username: ")
password = getpass.getpass()

#f=open("myswitches")

for IP in open("myswitches").strip():
    IP=IP.strip()
    print("Get Running Config from Switch  "+str(IP))
    HOST=IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"term len 0\n")
    tn.write(b"show run\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    readoutput=tn.read_all()
    savedoutput=open("switch"+HOST,'w+')
    savedoutput.write(readoutput.decode('ascii'))
    savedoutput.write("\n")
    savedoutput.close
    print(tn.read_all().decode("ascii"))