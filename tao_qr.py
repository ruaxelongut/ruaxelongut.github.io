# -*- coding: utf-8 -*-
"""Tao ma QR cho cac kenh cua Rua Xe Long Ut — mau theo thuong hieu tung kenh."""
import os
import sys

import segno

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "qr")
os.makedirs(OUT, exist_ok=True)

# ten file : (noi dung, mau QR)
MA = {
    "qr-youtube":  ("https://www.youtube.com/@RuaXeLongUt", "#FF0000"),
    "qr-facebook": ("https://www.facebook.com/ruaxelongut", "#1877F2"),
    "qr-tiktok":   ("https://www.tiktok.com/@ruaxelongut105", "#111111"),
    "qr-maps":     ("https://www.google.com/maps/search/?api=1&query=R%E1%BB%ADa+xe+%C3%B4+t%C3%B4+xe+m%C3%A1y+Long+%C3%9At+105+T%C3%A2y+Th%E1%BA%A1nh", "#188038"),
    "qr-goi":      ("tel:0765333324", "#E32227"),
    "qr-zalo":     ("https://zalo.me/0765333324", "#0068FF"),
}

for ten, (noi_dung, mau) in MA.items():
    qr = segno.make(noi_dung, error="h")
    duong_dan = os.path.join(OUT, ten + ".png")
    qr.save(duong_dan, scale=12, border=3, dark=mau, light="#FFFFFF")
    print(f"{ten}.png  <-  {noi_dung[:60]}")

print("\nXONG:", OUT)
