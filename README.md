# 🚢 Python ile Amiral Battı Oyunu

Bu proje, Python programlama dili kullanılarak nesne yönelimli programlama mantığına uygun bir şekilde geliştirilmiş dinamik bir **Amiral Battı (Battleship)** oyunudur. Kullanıcıya özel harita boyutu seçimi ve iki farklı stratejik oyun modu sunar.

## 🚀 Öne Çıkan Özellikler

* **Dinamik Oyun Alanı:** Kullanıcı minimum 10x10 olmak üzere dilediği boyutta bir oyun matrisi oluşturabilir.
* **Akıllı Gemi Yerleşimi:** Farklı boyutlardaki (1, 2, 3 ve 4 birimlik) gemiler, hem yatay hem de dikey yönlerde haritaya üst üste çakışmayacak şekilde `random` kütüphanesi yardımıyla otomatik yerleştirilir.
* **Gelişmiş Oyun Modları:**
  * **Gizli Mod (1):** Gemilerin konumları haritada gizlidir, oyuncu tamamen tahminlerine güvenerek atış yapar.
  * **Açık Mod (2):** Test veya pratik amacıyla gemilerin konumları ve boyutları harita üzerinde numaralandırılmış olarak görünür.
* **Hata Kontrol Mekanizmaları:**
  * Geçersiz matris sınırları dışına yapılan atışlar engellenir.
  * Daha önce seçilmiş koordinatlara tekrar atış yapıldığında oyuncu uyarılır ve hak kaybı yaşanmaz.
* **Puanlama Sistemi:** Kalan yanlış yapma hakkı ve yapılan toplam isabetli/isabetsiz atış sayılarına göre oyun sonunda dinamik bir kazanma puanı hesaplanır.

## 🛠️ Nasıl Çalıştırılır?

Projeyi bilgisayarınızda yerel olarak test etmek için aşağıdaki adımları takip edebilirsiniz:

1. Bu depoyu (repository) bilgisayarınıza indirin veya klonlayın.
2. Terminal ya da komut satırını açarak dosyanın olduğu dizine gidin.
3. Aşağıdaki komutu terminale yazarak oyunu başlatın:
   ```bash
   python amiral_batti.py
