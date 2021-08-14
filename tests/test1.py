import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'console_widgets')))
from console_widgets import *
import traceback


TEST_NUMBER = 1


def test(t):
	global TEST_NUMBER
	
	print("---------------------------------")

	try:
		print(f"TEST {TEST_NUMBER}")
		t()
	except Exception as exc:
		print(traceback.format_exc())

	print("---------------------------------")

	TEST_NUMBER += 1


def t1():
	c = ConsoleWidget(title="NASLOV", body="tijelo.....")

	c.show()


def t2():
	c = ConsoleWidget()

	c.show()


def t3():
	c = ConsoleWidget(title="naslov", subtitle="podnaslov", body="tijelo")

	c.show()


def t4():
	c = ConsoleList(title="Lista", subtitle="borna gojsic", items=[1, 2, 3, 4, 5, 6])

	c.show()


def t5():
	c = ConsoleBox(title="naslov", subtitle="naslov2", body="tijelo....")

	c.show()


def t6():
	c = ConsoleSelection(title="Select", subtitle="Items", items=["Go right", "Go left", "Do nothing", "Go back"])

	s = c.select()


def t100S():
	print("""
		▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
		███████████████
		█   █   aaa   █
		█▀▀▀█▀▀▀▀▀▀▀▀▀█
		█   █   bbb   █
		███████████████
		█   █   aaa   █
		█   █   bb    █
		███████████████
		▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
		""")


[test(t) for t in [t1, t2, t3, t4, t5, t6]]