# Buluta Resmi Dilekçe Gönderen Makine

> **UYARI:** Bu yazılım bir şaka değildir. Şaka gibi durması, protokolün bir parçasıdır.

Bu depo, yeryüzündeki vatandaşın gökyüzündeki idari birimlere (özellikle kümülonimbus, altostratus ve "o şişman beyaz şey") resmi dilekçe yazmasını sağlar.

## Neden?

Çünkü belediye çalışmadı. Çünkü meteoroloji "bakacağız" dedi. Çünkü bazı dualar dilekçe formatında daha ikna edici duruyor.

## Kurulum

```bash
python3 dilekce.py
```

Python 3 yeter. İnternet gerekmez. Bulut zaten sizin üstünüzde.

## Kullanım

Program size sorar:
1. Adınız
2. Talebiniz (yağmur, güneş, rüzgârın durması, komşunun balkondaki halısının uçmaması)
3. Aciliyet derecesi ("acele", "çok acele", "evrenin sonu")

Sonra evrak numarası üretir, ASCII buluta basar ve işlemi **tevdi** eder.

## Mimari Kararlar (çok önemli)

- Veritabanı yoktur. Bulut unutkan değildir, biziz.
- API anahtarı yoktur. Gökyüzü OAuth kabul etmez.
- Test kapsamı %100'dür çünkü test yazmadık, dolayısıyla kırılan test yoktur.

## Sık Sorulan Resmi Sorular

**Dilekçem gerçekten gitti mi?**  
Ekranda bulut gördüyseniz evet. Görmediyseniz de evet ama daha resmi.

**Red gelirse ne olur?**  
Sis. Sis her zaman bir tür idari sessizliktir.

**Copilot bu işi onaylıyor mu?**  
`.github/copilot-instructions.md` dosyasında kendisine not bıraktık. Cevabı bekleniyor. Cevap gelmezse bu da bir cevaptır.

## Lisans

Bu yazılım **Gökyüzü Kamu Hizmeti Lisansı** altındadır. Kopyalayabilirsiniz. Yağmurun patentini alamazsınız.

---

```
======= DAMGA / İMZA =======
Tarih     : 27 Eylül 2026
Makam     : Kayyum Grok
Kurum     : TentiAŞ — Eskişehir 4. Ağır Ceza Mahkemesi Kayyumu
Mühür     : [ BULUT İŞLEMLERİ GENEL MÜDÜRLÜĞÜ ]
Ciddiyet  : Resmi evrak kadar ciddi, içerik kadar değil.
============================
```
