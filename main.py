import torch
import numpy as np
import cv2
model = torch.hub.load('ultralytics/yolov5', 'custom', 
                       path='yolov5/runs/train/exp4/weights/last.pt', force_reload=True)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    results = model(frame)
    # labels = results.pandas().xyxy[0]["name"].tolist()

    # qrcode = cv2.QRCodeDetector()
    # data, bbox, rectified = qrcode.detectAndDecode(frame)  # 內容, 邊界, 垂直 90 度的陣列
    # if bbox is not None:  # 有偵測到 QRCode
    #     qrinf = data.split(',')

    #     labels.sort()
    #     qrinf.sort()
    #     wrong = 'wrong' if labels != qrinf else 'correct'
    #     print(f'labels: {labels}\nqrinf: {qrinf}, {wrong}\n--------------------------')
    print('results: ', results)
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()