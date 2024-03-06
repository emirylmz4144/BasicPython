def count_substring(string, sub_string):
    startIndex = 0 #burası kelime eşleşirse başlangıç noktasıdır 
    count = 0
    while string.find(sub_string, startIndex) != -1:#daha fazla istenilen kelimeyi bulamayana kadar aramaya devam et
        startIndex = string.find(sub_string, startIndex) + 1#bulursa kelimenin başlangıcından bir sonrakine gider ki bulduğu kısım içersinden sonra var mı kontrol edebilsin
        count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
