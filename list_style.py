import facts


def line(idx):
    correct, display, values = facts.generate_fact()
    val = "{0}: {1:2} {2} {3:2}".format(idx, values[0], values[2], values[1])
    return val

for idx in range(0, 100):
    p0 = line(idx + 1)
    p1 = line(idx + 2)

    print "{0} = \t\t\t{1} = \n".format(p0, p1)
