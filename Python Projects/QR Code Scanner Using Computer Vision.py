import cv2
from pyzbar.pyzbar import decode
from warnings import filterwarnings
filterwarnings('ignore')


capture = cv2.VideoCapture(0)
recieved_data = None
while True:
    _, frame = capture.read()
    # Decoding the QR Code 
    decoded_data = decode(frame)
    try:
        data = decoded_data[0][0]
        if data != recieved_data:
            recieved_data = data
            print("\n", data, "\n")
    except:
        pass
    
   
    cv2.imshow("QR CODE Scanner", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break