def split_and_join(line):
    return '-'.join(map(str,line))

if __name__ == '__main__':
    line = input().split()
    result = split_and_join(line)
    print(result)
