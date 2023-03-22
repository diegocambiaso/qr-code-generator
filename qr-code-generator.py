#!/usr/bin/env python
# coding = utf8
#
# Copyright (C) 2023, Diego Cambiaso
# GNU General Public License v3.0

'''
This script is for educational purposes and will let you generate a QR-Code from an URL.
'''

import pyqrcode

__version__ = 1

try:
    url = "https://pixelcoblog.com"
    qr_code = pyqrcode.create(url)
    qr_code.png("pixelco.png", scale=6)
except ValueError:
    print("An error has occurred")
    
