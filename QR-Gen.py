import qrcode  

print('QR-Code Generator\n')
qr_img = qrcode.make(input('Enter the data to be converted to QR : '))  
qr_img.save("QR.jpg")  
print('QR Code saved as QR.jpg')