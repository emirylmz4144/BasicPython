## Remote List Controller

##### Açıklama:
Bu Python betiği, bir listede çeşitli işlemler gerçekleştiren basit bir uygulamayı
simüle eder. Kullanıcılar, listedeki belirli bir konuma bir öğe ekleyebilir,
listeden belirli bir öğeyi silebilir, listenin sonuna bir öğe ekleyebilir,
listeyi sıralayabilir, listeden son öğeyi çıkarabilir veya listeyi tersine çevirebilir.

###### Giriş Formatı:

* İlk satır, komutların sayısını belirten
bir tamsayı olan N'yi içerir.


* İzleyen N satır, yukarıda belirtilen
* türdeki herhangi bir komutu içerir.


###### Örnek Girdi:
````angular2html
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
````

###### Örnek Çıktı
````angular2html
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
````