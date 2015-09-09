import random


def generate_fact(start=0, end=10, ops=["+", "*", "-"], nonneg=True):
    top = random.randint(start, end)
    bottom = random.randint(start, end)

    # swap facts that would result in negative numbers
    if top < bottom and nonneg:
        top, bottom = bottom, top

    op = random.choice(ops)
    display = "{0:6}\n{1}{2:5}\n----------".format(top, op, bottom)
    res = eval("{0} {1} {2}".format(top, op, bottom))
    return (res, display, [top, bottom, op])


if __name__ == "__main__":
    import sys

    try:
        count = int(sys.argv[1])
        num_correct = 0
        for idx in range(0, count):
            correct, display, values = generate_fact()
            print display
            answer = raw_input("> ")

            if int(answer) == correct:
                num_correct += 1

        print "You got {0} correct out of {1}!".format(num_correct, count)
    except Exception as e:
        print "usage: facts <n>\nwhere 'n' is the number of facts"
        print e
