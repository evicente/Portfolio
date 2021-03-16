""" Python QR Code generator test.

    Library: pyqrcode

    This test uses SVG as output.
"""
#!/bin/env python3
import pyqrcode

url = pyqrcode.create('www.google.com')
url.svg('link_03.svg', scale=16)
