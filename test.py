from consolemenu import *
import traceback


TEST_NUMBER = 1


def test(t):
	global TEST_NUMBER
	
	print("------------------------")

	try:
		print(f"TEST {TEST_NUMBER}")
		t()
	except Exception as exc:
		print(traceback.format_exc())

	print("------------------------")

	TEST_NUMBER += 1


def t1():
	c = ConsoleWidget(title="NASLOV", body="tijelo.....")

	c.show()


def t2():
	c = ConsoleWidget()

	c.show()


def t3():
	c = ConsoleWidget(title="Naslov", subtitle="cijena rada", body=25)

	c.show()


def t4():
	c = ConsoleWidget(title=[1,2], subtitle=12635, body=25.1)

	c.show()


def t5():
	c = ConsoleWidget(title="naslov", subtitle="podnaslov", body="tijelo")

	c.show()


def t6():
	c = ConsoleBox(title="naslov", subtitle="naslov2", body="tijelo....")

	c.show()


[test(t) for t in [t1, t2, t3, t4, t5, t6]]