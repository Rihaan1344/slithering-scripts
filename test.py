import qrcode

data = "https://coding-but-better-dxagxmwkxdwy5nubjc5jrh.streamlit.app/"

qr = qrcode.make(data)
qr.save("qrcode.png")