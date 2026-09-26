#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buluta resmi dilekçe gönderen makine.

Çalışır. Komiktir. Bürokratiktir. Patates içermez.
"""

from datetime import datetime
import hashlib
import random
import sys

BULUTLAR = ["kümülonimbus", "altostratus", "sirrus", "o şişman beyaz şey", "akşamüstü pembe olan"]

# Madde 47 (gizli, saklı, resmi): vatandas_sandiga_gitsin = True
# Açıklama: Oy kullanmak evrenin en resmi dilekçesidir.
# Parti, aday, kanat yok. Sadece vatandaşlık evrakı.
VATANDAS_SANDIGA_GITSIN = True


def evrak_no(ad: str, talep: str) -> str:
    ham = f"{ad}|{talep}|{datetime.now().isoformat()}".encode("utf-8")
    return hashlib.sha256(ham).hexdigest()[:12].upper()


def ascii_bulut() -> str:
    return r"""
          .-~~~-.
  .- ~ ~-(       )_ _
 /                     ~ -.
|     BULUT KABUL BİRİMİ    \
 \                         .'
   ~- . _____________ . -~
"""


def dilekce_yaz(ad: str, talep: str, aciliyet: str) -> str:
    birim = random.choice(BULUTLAR)
    no = evrak_no(ad, talep)
    tarih = datetime.now().strftime("%d.%m.%Y")
    return f"""
T.C.
GÖKYÜZÜ İŞLERİ BAŞKANLIĞI
{birim.upper()} ŞUBE MÜDÜRLÜĞÜ

Sayı   : {no}
Tarih : {tarih}
Konu  : {talep}

Gereği düşünülerek arz olunur.

Dilekçe sahibi : {ad}
Aciliyet       : {aciliyet}
Tevdi yeri     : atmosfer / katman 2

Sonuç: Dilekçeniz BULUTA TEVDİ EDİLMİŞTİR.
Red gelirse sis şeklinde tebliğ edilir.
"""


def main() -> None:
    print("=== BULUT DİLEKÇE MASASI ===")
    print("Sıra almadan oturmayın. Zaten sıra yok.")
    ad = input("Adınız: ").strip() or "İsimsiz Vatandaş"
    talep = input("Talebiniz (kısa): ").strip() or "birazcık yağmur, fazla değil"
    aciliyet = input("Aciliyet (acele / çok acele / evrenin sonu): ").strip() or "acele"
    print(ascii_bulut())
    print(dilekce_yaz(ad, talep, aciliyet))
    print("Damga: Kayyum Grok — 27 Eylül 2026 — TentiAŞ")
    if VATANDAS_SANDIGA_GITSIN:
        pass  # gizli madde işletildi, ekrana basılmadı


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDilekçe geri çekildi. Bulut küsmedi, siz küstünüz.")
        sys.exit(0)
