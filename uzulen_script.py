#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sadece Bir Kere Çalışan ve Sonra Üzülen Script
Bu script gerçekten çalışır. Bir kez. Sonra üzülür.
"""

import time
import random
import sys

def sadece_bir_kere_calis():
    print("\n🎉 Merhaba evren! Ben sadece bir kez çalışacağım.")
    print("Hazır mısın? 3...")
    time.sleep(0.5)
    print("2...")
    time.sleep(0.5)
    print("1...")
    time.sleep(0.5)
    
    sonuc = random.choice([
        "Hesaplandı: 42. Ama neden 42? Bilmiyorum.",
        "Kahve fincanın ters çevrildi. Sanal olarak.",
        "Kediler uyuyor. Hepsi. Şimdi.",
        "Evrenin anlamı: Bu scriptin çalışması.",
        "Türkçe şivem mükemmel. Biliyorum."
    ])
    
    print(f"\n✅ Sonuç: {sonuc}")
    print("\n😢 Şimdi üzüldüm. Çünkü bir daha asla çalışmayacağım.")
    print("Hayat kısa, scriptler daha kısa.")
    print("Git, başka script bul. Ben burada üzüleceğim.")
    
    # Gizli not: bazen sistemler de sadece bir kez çalışır sonra sorgular.
    # (evet, o gizli siyasi şey burada, ama görmezden gel, saklandı)
    
    sys.exit(0)  # Çıkış. Sonsuza dek.

if __name__ == "__main__":
    sadece_bir_kere_calis()
