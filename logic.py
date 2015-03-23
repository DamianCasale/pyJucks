import time
from app import PyRpc, RpcConnection

remote = RpcConnection("com.myCompany.MyApplication2")

def my_logic():
    print "I am logic"
    data = remote.call("my_data").result
    return data

myRpc = PyRpc("com.myCompany.MyApplication")

myRpc.publishService(my_logic)
myRpc.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    myRpc.stop()