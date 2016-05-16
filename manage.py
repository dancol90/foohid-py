import foohid
import sys

def help():
	print("Destroy all foohid devices, or just the one specified.\n")
	print("Usage: clean.py interface")
	print("       clean.py -a\n")

names = foohid.list()

if len(sys.argv) != 2:
	help()
else:
	arg = sys.argv[1]

	if arg == '-l':
		print("Available interfaces are:")

		for n in names:
			print("\t%s" % n)
	elif arg == '-a':
		for n in names:
			foohid.destroy(n)
	elif arg in names:
		foohid.destroy(arg)
	else:
		print("Invalid device name: %s" % arg)
		help()
		sys.exit()

