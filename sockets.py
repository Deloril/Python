import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('ctf.crikeycon.com', 23776))

def calc(data):
	ignore,question = data.split(": ")
	a,op,b,i1,i2,i3 = question.split(" ")
	a = int(a)
	b = int(b)
	if(op == "+"):
		return a + b
	elif(op == "-"):
		return a - b
	elif(op == "*"):
		return a * b
	elif(op == "/"):
		return a / b
	else:
		return "derp"
		
while 1:
    data = client_socket.recv(512)
    if ("is correct" in data):
		print "RECIEVED: " , data
    else:
		print "RECIEVED: " , data
		answer = calc(data)
		if(answer == "derp"):
			client_socket.close()
			break;
		else:
			answer = str(answer)
			print "SENDING: ", answer
			client_socket.send(answer)
			#client_socket.close()