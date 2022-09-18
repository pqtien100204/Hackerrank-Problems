if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range(N):
        try:
            name, *number = input().split()
            if name == "insert":
                str = f"List.{name}(int(number[0]), int(number[1]))"
                eval(str)        # this will go through a string and check whether it's a correct Python method, if it's correct => print it out
            elif name == "print":
                print(List)
            elif len(number) == 1:
                str = f"List.{name}(int(number[0]))"
                eval(str)
            elif len(number) == 0:
                str = f"List.{name}()"
                eval(str)
        except BaseException as a:
            print(a)