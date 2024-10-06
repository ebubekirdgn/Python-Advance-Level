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

# Kayıt klasörünü oluştur
output_dir = './result'
os.makedirs(output_dir, exist_ok=True)

# Toplam soğan sayısını saklamak için değişkeni tanımla
total_onion_count = 0

# Her bir çerçeve için tespit sonuçlarını al ve soğan sayılarını topla
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
        results = model(frame, conf=0.2)
        
        # results değişkeninin tipini kontrol et
        if isinstance(results, list):
            # Listenin ilk elemanını al
            results = results[0]

        # Çerçeve numarasını hesapla
        cerceve_numarasi = (i // frame_size) * (input_image_width // frame_size) + (j // frame_size) + 1

        # Çerçeve numarasını ve tespit edilen soğan sayısını yazdır
        onion_count = len(results.boxes)
        print(f"Çerçeve {cerceve_numarasi}: {onion_count} soğan")

        # Soğan sayısını topla
        total_onion_count += onion_count

        # Tespit edilen nesnelerle birlikte çerçeveyi kaydet
        annotated_frame = results.plot()
        cv2.imwrite(os.path.join(output_dir, f'cerceve{cerceve_numarasi}.jpg'), annotated_frame)

# Toplam soğan sayısını yazdır
print("Toplam soğan sayısı:", total_onion_count)
