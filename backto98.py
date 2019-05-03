import re
import sys


def process_line(line):
    line = line.replace("nullptr", "NULL").replace(">>", "> > ").replace("cin > >", "cin >>")

    while True:
        m = re.search("map<(.+?)>", line)
        if m:
            inside = m.group(1).split(",", 1)
            left = inside[0].strip()
            right = inside[1].strip()
            line = re.sub(r"map<{},\s?{}>".format(left, right),
                          "set<pair<{}, {}> >".format(left, right), line)
        else:
            break

    return line


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        for line in f:
            print(process_line(line), end='')


if __name__ == "__main__":
    main()
    print("\nDone.")
