import cv2
from ultralytics import YOLO

# Kamerayı başlat
cap = cv2.VideoCapture(0)  # 0. kamera endeksi
model = YOLO("yolov9c.pt")  # Resmi bir YOLOv8 modelini kullan

# Model parametrelerini ayarla
model.conf = 0.25  # NMS güven eşiği
model.iou = 0.45  # NMS IoU eşiği
model.classes = None  # (isteğe bağlı liste) sınıf filtresi

while True:
    # Kareyi yakala
    ret, frame = cap.read()
    if not ret:
        break

    # Kare üzerinde tahmin yap
    results = model.predict(frame, device='cpu')  # Cihazı burada belirt

    # Sonuçları işle
    predictions = results[0].boxes.xyxy  # Sonuçların tahminleri (koordinatlar)
    scores = results[0].boxes.conf  # Güven skorları
    categories = results[0].boxes.cls  # Sınıf kimlikleri

    # Kare üzerinde bounding box'ları çiz
    for box, score, category in zip(predictions, scores, categories):
        x1, y1, x2, y2 = map(int, box)
        label = f"{model.names[int(category)]}: % {score*100:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Sonucu göster
    cv2.imshow('YOLOv9 Nesne Tespiti', frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
