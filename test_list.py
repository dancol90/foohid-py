import foohid

for i in range(1, 10):
    foohid.create("FooHID {0}".format(i), "xxx", "SN%d" % i, 2, 3)

print(foohid.list())

for i in range(1, 10):
    foohid.destroy("FooHID {0}".format(i))
