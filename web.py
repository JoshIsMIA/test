import socket
import hashlib
import threading
import logging

s=socket.socket(socket.AF_INET,socket.SOCK_RAW)

x=hashlib.sha512(b"audsooisfiojsdiojfsodijfiojsdoifisojfodsjfijdsijifjsiojfiosjfiojsdijfsoijfiojsijfiosj i was here sfoijfosjdfijdsoifisodjfio")

ip=("10.0.0.115",8080)



def send():

    s.connect(ip)
    
    s.sendall(x)

    s.close()
send()


threads = list()
for index in range(5):
    logging.info("Main    : create and start thread %d.", index)
    x = threading.Thread(target=send, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    logging.info("Main    : before joining thread %d.", index)
    thread.join()
    logging.info("Main    : thread %d done", index)