from consolemenu import *

## TEST 1
print("TEST 1")

c = ConsoleWidget(title="IME", body="tijelo.....")

c.show()


## TEST 2
print("TEST 2")

c = ConsoleWidget()

c.show()



## TEST 3
print("TEST 3")

c = ConsoleWidget(title="Naslov", subtitle="cijena rada", body=25)

c.show()



## TEST 3
print("TEST 3")

c = ConsoleWidget(title=[1,2], subtitle=12635, body=25.1)

c.show()