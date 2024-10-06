from ultralytics import YOLOv10
import cv2
import os

# YOLOv10 modelini yükle
model = YOLOv10('C:\\Users\\DoganPc\\Desktop\\Yolo\\runs\\detect\\train3\\weights\\best.pt')

# Giriş resmi ve boyutları
input_image_path = 'C:\\Users\\DoganPc\\Desktop\\Yolo\\test\\202.JPG'
input_image = cv2.imread(input_image_path)
input_image_height, input_image_width, _ = input_image.shape

# Çerçeve boyutları
frame_size = 128
overlap = 0  # Örtüşme miktarı olmadığı için 0

# Klasör adı ve oluşturulması
output_folder = "result"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Her bir çerçeve için tespit sonuçlarını al, çerçeveyi etiketlenmiş olarak kaydet ve nesne sayısını yazdır
frame_number = 1
total_onion_count = 0  # Toplam soğan sayısını saklamak için değişken
for i in range(0, input_image_height, frame_size):
    for j in range(0, input_image_width, frame_size):
        # Çerçeve başlangıç ve bitiş koordinatları
        start_x = j
        start_y = i
        end_x = min(start_x + frame_size, input_image_width)
        end_y = min(start_y + frame_size, input_image_height)

        # Çerçeve resmini al
        frame = input_image[start_y:end_y, start_x:end_x]

        # Tahminlerde bulun
        results = model(frame,conf=0.2)

        # results değişkeninin tipini kontrol et
        if isinstance(results, list):
            # Listenin ilk elemanını al
            results = results[0]

        # Nesne sayısını al
        num_objects = len(results.boxes)

        # Toplam soğan sayısını güncelle
        total_onion_count += num_objects

        # Nesne sayısını çerçevenin sol üst köşesine yazdır
        text = f"Nesne Sayisi: {num_objects}"
        font_scale = min(frame_size, frame_size) / 300  # Yazı boyutunu ayarla
        thickness = max(int(font_scale), 1)  # Yazı kalınlığını ayarla
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]  # Yazı boyutunu al
        text_x = int((frame_size - text_size[0]) / 2)  # Yazının x konumunu ayarla
        text_y = int((frame_size + text_size[1]) / 2)  # Yazının y konumunu ayarla
        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness)

        # Çerçevenin etiketlenmiş halini kaydet
        output_image_path = os.path.join(output_folder, "frame_{}.jpg".format(frame_number))
        cv2.imwrite(output_image_path, frame)  # Etiketlenmiş çerçeveyi kaydet

        # Çerçevenin numarasını ve nesne sayısını yazdır
        print("Çerçeve", frame_number, "- Nesne Sayısı:", num_objects)

        # Sonraki çerçeve için numarayı artır
        frame_number += 1

# Toplam soğan sayısını yazdır
print("Toplam soğan sayısı:", total_onion_count)
