def process(a):
    for line in range(len(a)):
        temp = ""
        for i in range(len(a[line])):
            temp += a[line][i]
            temp += f"({i})"
        a[line] = temp
    return a


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("s", type=str)
    args = parser.parse_args()
    s = args.s

    print("\n".join(process(s.split("\n"))))
