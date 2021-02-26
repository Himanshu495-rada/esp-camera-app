import cv2
import urllib.request
import numpy as np
url = "http://192.168.43.237/cam-hi.jpg"


while True:
    imgResponse = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    cv2.imshow("Streaming", img)
    if cv2.waitKey(1) == ord(" "):
        cv2.destroyAllWindows()
        break
