#Kullıcıdan gireceği satır miktarı
count_of_command=int(input("Lütfen kaç satır işlem yapacağınızı belirtiniz "))

our_list=[]

#Her bir key burada list üzerinde yapılacak methodu dict olarak almıştır
commands_actions_dictionary={
    "insert":our_list.insert,
    "print":print,
    "remove":our_list.remove,
    "append":our_list.append,
    "sort":our_list.sort,
    "pop":our_list.pop,
    "reverse":our_list.reverse
    
}

for i in range(count_of_command):
    # Kullanıcıdan alınan girdiler tokenlaştırıldı
    tokens=input(f"Yapacağınız {i+1}. işlemi ve işlemin parametrelerini giriniz  ").split(" ")
    # tokena göre dict'ten ilgili method alındı
    which_method=commands_actions_dictionary[tokens[0]]
    # Methoda gönderilecek parametreler tokens listesinden alındı
    values=map(int,tokens[1:])
    # Eğer printse listede işlem yapılmayacğı ve yazılacağı için buraya yazıldı
    if tokens[0]=="print":
        which_method(our_list)
    else:
        # Parametreler dict'in ilgili methodu tutan values değerine giderek listeye ilgili aksiyon eklendi
        which_method(*values)

