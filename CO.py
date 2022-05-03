def main():
    code = []
    result = {}
    toBeReplaced = {}
    nol = int(input("Enter number of lines of code: "))
    for i in range(nol):
        loc = input("Enter line: ")
        code.append(loc)
    print("Before code optimization:")
    for i in code:
        print(i)
    for i in range(len(code)):
        line = code[i].split("=")
        if not (any(char.isalpha() for string in line[1] for char in string)):
            toBeReplaced[line[0]] = line[1]
        else:
            result[line[0]] = line[1]
    for i in range(len(code)):
        line = code[i].split("=")
        for j in toBeReplaced:
            if line[0] == j:
                pass
            elif j in line[1].split():
                result[line[0]] = line[1].replace(j, toBeReplaced[j])
    print("\nAfter code optimization:")
    for i in result:
        print(i, "=", result[i])


if __name__ == "__main__":
    main()


# def main():
#     code = []
#     result = {}
#     toBeReplaced = {}
#     nol = int(input("Enter number of lines of code: "))
#     for i in range(nol):
#         loc = input("Enter line: ")
#         code.append(loc)
#     print("Before code optimization:")
#     for i in code:
#         print(i)
#     for i in range(len(code)):
#         line = code[i].split("=")
#         if not (any(char.isalpha() for string in line[1] for char in string)):
#             toBeReplaced[line[0]] = line[1]
#         else:
#             result[line[0]] = line[1]
#     for i in range(len(code)):
#         for j in toBeReplaced:
#             line = code[i].split("=")
#             if line[0] == j:
#                 pass
#             elif j in line[1].split():
#                 result[line[0]] = line[1].replace(j, toBeReplaced[j])
#     print("\nAfter code optimization:")
#     for i in result:
#         print(i, "=", result[i])


# if __name__ == "__main__":
#     main()
