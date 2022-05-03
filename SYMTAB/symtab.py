from string import punctuation


def main():
    FileData = open(r"SYMTAB\\asmprog.asm", 'r')
    ListData = FileData.read().split('\n')
    mnemonic = ['AREG', 'BREG', 'CREG', 'ORIGIN', 'LTORG', 'ADD', 'SUB',
                'MULT', 'DIV', 'COMP', 'MOVEM', 'MOVER', 'DS', 'DC', 'STOP', 'END']
    Address, Index = 0, 0
    with open("SYMTAB\\symtab.txt", 'w') as symtab:
        symtab.write("{:<10}{:<10}{:<10}".format(
            "Index", "Symbol", "Address")+"\n")
        SymbolSet = set()
        OutputList = []
        for i in ListData:
            for j in i.split():
                if j == 'START':
                    Address = int(i.split()[-1]) - 1

                elif j in mnemonic or j.isnumeric() or j in punctuation or j.isdigit():
                    pass

                else:
                    if j not in SymbolSet:
                        SymbolSet.add(j)
                        Index += 1
                        OutputList.append([Index, j, Address])
                    else:
                        if 'DS' in i.split() or 'DC' in i.split():
                            for k in OutputList:
                                if j in k:
                                    Index = OutputList.index(k)
                                    OutputList[Index][-1] = Address
            Address += 1

        for i in OutputList:
            IndexVal, Symbol, CurrAddress = i
            symtab.write("{:<10}{:<10}{:<10}".format(
                IndexVal, Symbol, CurrAddress)+"\n")
    symtab.close()
    FileData.close()


if __name__ == "__main__":
    main()


# from string import punctuation
# from numpy import add


# def main():
#     asmprog = open(r"asmprog.asm", "r")
#     mneumonic = ['AREG', 'BREG', 'CREG', 'ORIGIN', 'LTORG', 'ADD', 'SUB',
#                  'MULT', 'DIV', 'COMP', 'MOVEM', 'MOVER', 'DS', 'DC', 'STOP', 'END']
#     listforindexing = asmprog.read().splitlines()
#     with open("symtab.txt", "w") as symtab:
#         symtab.write("{:<10} {:<10} {:<10}".format(
#             "Index", "Symbol", "Address") + "\n")
#         index, address = 0, 0
#         setdata = set()
#         for i in range(0, len(listforindexing)-1):
#             if "START" in listforindexing[i]:
#                 index += 1
#                 address = int(listforindexing[i].split()[-1])-1
#             else:
#                 progrow = listforindexing[i].replace(",", "")
#                 progrow = progrow.split(" ")
#                 for j in range(0, len(progrow)-1):
#                     if progrow[j] not in setdata:
#                         if not (progrow[j] in mneumonic or progrow[j].isdigit() or progrow[j].isdecimal() or progrow[j] in punctuation):
#                             setdata.add(progrow[j])
#                             address += 1
#                             symtab.write("{:<10} {:<10} {:<10}".format(
#                                 str(i), progrow[j], str(address)) + "\n")
#     symtab.close()
#     asmprog.close()


# if __name__ == "__main__":
#     main()
