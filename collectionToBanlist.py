# Say thanks to Locorock, you ingrates
import sys

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
    with open("collection.conf", "w") as file1:
        file1.write("!Regression\n$whitelist\n")
        for card in coll:
            code = card[2]
            num = card[1]
            name = card[0]
            file1.write(code + " " + num + " --" + name.strip('"') + "\n")
        file1.write("\n")
        with open("banlist.add", "r") as file2:
            lines = file2.readlines()
            for line in lines:
                file1.write(line)
