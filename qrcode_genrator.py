import pyqrcode

from pyqrcode import QRCode

#Text or url to encode
s="https://chatgpt.com/"

#create the qrcode
url=pyqrcode.create(s)

#save as svg
# url.svg("myqr.svg",scale=8)

#save as png
url.png("myqr.png",scale=6)