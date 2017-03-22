import urllib2

baseSite = "https://api.qrserver.com/v1/read-qr-code/?fileurl=http://tunnel.web.easyctf.com/images/"
QR = "P75hn0VCl8sU969U80My"

#easyctf{y0u_sh0uld_b3_t1r3d_tr4v3ll1ng_all_th1s_w4y!!!!!}
while 1==1:
	print ("Requesting: " + baseSite + QR)
	proc = urllib2.urlopen(baseSite + QR)
	data = proc.read()
	data = data.split("data\":\"")
	QR = data[1].split("\",")[0]