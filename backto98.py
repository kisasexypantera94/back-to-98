import sys
import re


def process_line(line):
    line = line.replace("nullptr", "NULL").replace(">>", "> >").replace(
        ">>", "> >")

    while True:
        m = re.search("map<(.+?)>", line)
        if m:
            inside = m.group(1).split(",", 1)
            left = inside[0].strip()
            right = inside[1].strip()
            line = re.sub("map<{},\s?{}>".format(left, right),
                          "set<pair<{}, {}> >".format(left, right), line)
        else:
            break

    return line


def main():
    filename = sys.argv[1]
    out = open("98" + filename, mode="w")
    with open(filename) as f:
        for line in f:
            out.write(process_line(line))

    out.close()


if __name__ == "__main__":
    main()
    print("Done.")
