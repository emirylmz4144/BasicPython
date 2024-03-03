## Grup Kelime Karşılaştırma Projesi

Bu proje, iki grup kelime arasında karşılaştırma yapmayı ve belirli bir kelimenin diğer grupta hangi konumlarda bulunduğunu belirlemeyi amaçlamaktadır.

### Giriş Formatı

Giriş, standart giriş olarak verilir ve aşağıdaki formatta olmalıdır:

- İlk satır, iki tamsayıyı, yani grup A'nın boyutunu (n) ve grup B'nin boyutunu (m) içermelidir, boşlukla ayrılmalıdır.
- Ardından, grup A'ya ait kelimelerin bulunduğu satırlar gelir. Toplam n adet satır bulunur.
- Sonra, grup B'ye ait kelimelerin bulunduğu satırlar gelir. Toplam m adet satır bulunur.

Örnek Giriş:
````
5 2
a
a
b
a
b
a
b
c
````

### Çıktı Formatı

Çıktı, standart çıktıya yazdırılır ve aşağıdaki formatta olmalıdır:

- Çıktı, grup B'deki her kelime için bulunduğu konumları içermelidir.
- Her bir çıktı satırı, -1 veya grup A'daki belirli bir kelimenin konumlarından oluşan bir dizi içermelidir. Eğer kelime grup A'da bulunmuyorsa, -1 yazdırılmalıdır.

Örnek Çıktı:
````
1 2 4
2 5 
-1
````