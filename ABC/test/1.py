import sys

def main(lines):
    for i, v in enumerate(lines):
        print("Hello {s}!".format(s=v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)