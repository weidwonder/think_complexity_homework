import string


def alphanum_circle():
    while True:
        for num in string.digits:
            for alpha in string.ascii_lowercase:
                yield alpha + num

def test():
    t = 1000
    for s in alphanum_circle():
        print s
        t -= 1
        if t < 0:
            break

if __name__ == '__main__':
    test()