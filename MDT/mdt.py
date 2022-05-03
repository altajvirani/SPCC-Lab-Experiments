def main():
    macro = open(r"MDT\\macro.asm", "r")
    listforindexing = macro.read().splitlines()
    with open('MDT\\mdt.txt', 'w') as mdt:
        mdt.write("{:<15} {:<20} {:<10}".format(
            "Macro Number", "Card", "Index") + "\n")
        mflag = False
        mno = 0
        for i in range(0, len(listforindexing)):
            if 'MACRO' in listforindexing[i]:
                mflag = True
                mno += 1
                continue

            if mflag == True:
                mdt.write("{:<15} {:<20} {:<10}".format(
                    str(mno), str(listforindexing[i]), str(i+1)) + "\n")
                if 'MEND' in listforindexing[i]:
                    mflag = False
    mdt.close()
    macro.close()


if __name__ == "__main__":
    main()
