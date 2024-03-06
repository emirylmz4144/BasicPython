def count_substring(string, sub_string):
    startIndex = 0
    count = 0
    while string.find(sub_string, startIndex) != -1:
        startIndex = string.find(sub_string, startIndex) + 1
        count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)