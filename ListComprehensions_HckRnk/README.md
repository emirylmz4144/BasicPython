## Liste Kavramları ile Grup Koordinat Karşılaştırma Projesi

Bu proje, verilen üç boyutlu bir kübik ızgarada belirli koordinatların tüm permütasyonlarını 
bulmayı ve bu koordinatların toplamının belirli bir tamsayıdan farklı olduğu durumları listelemeyi amaçlamaktadır.

### Giriş Formatı

Giriş, standart giriş olarak verilir ve aşağıdaki formatta olmalıdır:

- İlk satır, dört tamsayıyı içermelidir: ızgaranın boyutları ve hedef toplam, boşlukla ayrılmalıdır.
- Ardından, her biri ayrı bir satırda olmak üzere üç tamsayı gelir: ızgaranın x, y ve z boyutları.
- Son olarak, hedef toplama sahip olmayan koordinatları bulmak için kullanılacak olan tamsayı gelir.

Örnek Giriş:
````angular2html
1
1
1
2
````


Bu girdi şu şekilde liste oluşturur
````angular2html
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
````

### Çıktı Formatı

Çıktı, standart çıktıya yazdırılır ve aşağıdaki formatta olmalıdır:

- Çıktı, hedef toplama sahip olmayan her bir koordinatı içermelidir.
- Her bir çıktı satırı, koordinatların bir listesi olarak verilmelidir.

Örnek Çıktı:
````angular2html
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

````


### Örnek Açıklama

Her değişken 0 veya 1 değerlerine sahip olacak ve `[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]` gibi listelerin tüm permütasyonlarını oluşturur. Toplamı olan tüm diziler kaldırılarak, yalnızca geçerli permütasyonlar bırakılır.
Bu şekilde, tüm bilgiler bir arada ve Markdown formatında verilmiş olur. Başlık ve alt başlıklar için ## ve ###, örnek giriş ve çıkışlar için üç ters tırnak kullanılmıştır.

Örnek giriş: 
````angular2html
2
2
2
2
````
Oluşturulacak Liste:
````angular2html
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
````
Örnek çıktı :
````angular2html
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
````