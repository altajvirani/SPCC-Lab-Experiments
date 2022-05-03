def main():
    macro = open(r"MNT\\macro.asm", "r")
    listforindexing = macro.read().splitlines()
    with open('MNT\\mnt.txt', 'w') as mnt:
        mnt.write("{:<15} {:<12} {:<20} {:<10}".format(
            "Macro Number", "MACRO Name", "Number of Arguments", "MDT Index") + "\n")
        mno = 0
        for i in range(0, len(listforindexing)):
            if 'MACRO' in listforindexing[i]:
                mno += 1
                mntrow = listforindexing[i+1].replace(",", "")
                mntrow = mntrow.replace("&", "")
                mntrow = mntrow.split(" ")
                mname = mntrow[0]
                margs = mntrow[1:]
                mnt.write("{:<15} {:<12} {:<20} {:<10}".format(
                    str(mno), mname, str(len(margs)), str(i+1)) + "\n")
    mnt.close()
    macro.close()


if __name__ == "__main__":
    main()
