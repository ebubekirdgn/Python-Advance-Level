from ultralytics import YOLOv10
import cv2
import os
import numpy as np

# YOLOv10 modelini yükle
model = YOLOv10('C:\\Users\\DoganPc\\Desktop\\Yolo\\runs\\detect\\train3\\weights\\best.pt')

# Giriş resmi ve boyutları
input_image_path = 'C:\\Users\\DoganPc\\Desktop\\Yolo\\test\\202.JPG'
input_image = cv2.imread(input_image_path)
input_image_height, input_image_width, _ = input_image.shape

# Çerçeve boyutları ve çakışma oranı
frame_size = 128
overlap = 64  # %50 çakışma

# Klasör adı ve oluşturulması
output_folder = "result"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def non_max_suppression(boxes, overlap_thresh):
    if len(boxes) == 0:
        return []

    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    pick = []
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    conf = boxes[:, 4]
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(conf)[::-1]

    while len(idxs) > 0:
        i = idxs[0]
        pick.append(i)
        xx1 = np.maximum(x1[i], x1[idxs[1:]])
        yy1 = np.maximum(y1[i], y1[idxs[1:]])
        xx2 = np.minimum(x2[i], x2[idxs[1:]])
        yy2 = np.minimum(y2[i], y2[idxs[1:]])
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        overlap = (w * h) / area[idxs[1:]]

        idxs = np.delete(idxs, np.concatenate(([0], np.where(overlap > overlap_thresh)[0] + 1)))

    return boxes[pick].astype("int")

# Her bir çerçeve için tespit sonuçlarını al, çerçeveyi etiketlenmiş olarak kaydet ve nesne sayısını yazdır
all_detections = []

for i in range(0, input_image_height - frame_size + overlap, overlap):
    for j in range(0, input_image_width - frame_size + overlap, overlap):
        # Çerçeve başlangıç ve bitiş koordinatları
        start_x = j
        start_y = i
        end_x = min(start_x + frame_size, input_image_width)
        end_y = min(start_y + frame_size, input_image_height)

        # Çerçeve resmini al
        frame = input_image[start_y:end_y, start_x:end_x]

        # Tahminlerde bulun
        results = model(frame, conf=0.18)

        # results değişkeninin tipini kontrol et
        if isinstance(results, list):
            # Listenin ilk elemanını al
            results = results[0]

        # Tespit edilen nesneleri çerçevele ve etiketle
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)  # Tensörü numpy arrayine çevirip int'e dönüştür
            x1 += start_x
            y1 += start_y
            x2 += start_x
            y2 += start_y
            conf = box.conf.item()  # Güven skorunu al
           
            all_detections.append([x1, y1, x2, y2, conf])

# Toplam tespit edilen nesne sayısı
total_detections = len(all_detections)

# NMS uygulama
all_detections = np.array(all_detections)
nms_detections = non_max_suppression(all_detections, 0.25)

# Tespit edilen nesneleri orijinal resimde işaretleme ve etiketleme
for (x1, y1, x2, y2, conf) in nms_detections:
    confidence_percentage = conf * 100  # Güveni yüzdeye çevir
    label = f"onion {confidence_percentage:.2f}%"  # Yüzdeyi etiket olarak kullan
    cv2.rectangle(input_image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Kırmızı çerçeve

# Toplam soğan sayısını yazdır
total_onion_count = len(nms_detections)
print("Toplam soğan sayısı:", total_onion_count)

# Etiketlenmiş resmi kaydet
output_image_path = os.path.join(output_folder, "annotated_image.jpg")
cv2.imwrite(output_image_path, input_image)  # Etiketlenmiş resmi kaydet
