def main():
    Expression = str(input("Enter Expression: "))
    post = []
    ExpGenList = []
    Precedence = {'+': 1, '-': 1, "*": 2, '/': 3}
    OperatorList = []
    for i in Expression:
        if i.isalpha():
            post.append(i)
        elif not OperatorList or Precedence[i] > Precedence[OperatorList[-1]]:
            OperatorList.append(i)
        else:
            y = OperatorList.pop()
            post.append(y)
            OperatorList.append(i)
    ReverseOpList = OperatorList[::-1]
    post.extend(ReverseOpList)

    i = 1
    for z in post:
        if z.isalpha():
            ExpGenList.append(z)
        else:
            right = ExpGenList.pop()
            left = ExpGenList.pop()
            print('t'+str(i), '=', left, z, right)
            ExpGenList.append('t' + str(i))
            i += 1

if __name__ == "__main__":
    main()
