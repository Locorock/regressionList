# Say thanks to Locorock, you ingrates
import datetime
import errno
import os
import random
import sys
from os.path import dirname, abspath
from time import sleep

if __name__ == '__main__':
    coll = []
    with open(sys.argv[1], "r") as collection:
        lines = collection.readlines()
        first = True
        for line in lines:
            if not first:
                quoted = False
                line = list(line)
                for i in range(len(line)):
                    letter = line[i]
                    if letter == '"':
                        if quoted:
                            quoted = False
                        else:
                            quoted = True
                    if quoted and letter == ",":
                        line[i] = "|"
                line = "".join(line)

                split = line.split(",")
                split = split[:3]
                split[0] = split[0].replace("|", ",", 3)
                if int(split[1]) > 3:
                    split[1] = "3"
                coll += [split]
            else:
                first = False
    print(coll)
    try:
        filename = "C:\\ProjectIgnis\\oldlist\\foo"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open("C:\\ProjectIgnis\\lflists\\collection.conf", "r") as old:
            with open("C:\\ProjectIgnis\\oldlist\\collection-" + str(datetime.date.today()) + "#" + str(
                    random.randint(1, 100)) + ".conf", "w") as postold:
                print("BREAK")
                for line in old.readlines():
                    print(line, end="")
                    postold.write(line)
    except Exception as e:
        print(e)

    try:
        with open("C:\\ProjectIgnis\\lflists\\0_collection.conf", "w+") as file1:
            file1.write("!Regression\n$whitelist\n")
            for card in coll:
                code = card[2]
                num = card[1]
                name = card[0]
                file1.write(code + " " + num + " --" + name.strip('"') + "\n")
            file1.write("\n")
            with open(str(dirname(abspath(__file__))) + "\\banlist.add", "r") as file2:
                lines = file2.readlines()
                for line in lines:
                    file1.write(line)
    except Exception as e:
        print(e)

    input("\nI DONE DID IT")
