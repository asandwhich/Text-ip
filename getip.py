import socket, struct, fcntl
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd = sock.fileno()
SIOCGIFADDR = 0x8915
import urllib2
def get_ip(iface = 'eth0'):
	ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
	try:
		res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
	except:
		return None
	ip = struct.unpack('16sH2x4s8x', res)[2]
	return socket.inet_ntoa(ip)

def getpubip():
	pub_ip = urllib2.urlopen("http://automation.whatismyip.com/n09230945.asp").read()
	return pub_ip
