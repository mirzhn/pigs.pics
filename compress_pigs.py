from PIL import Image
import os

# Укажите путь к папке с изображениями
directory = "/mnt/c/repo/pigs.pics/pics"  # Замените на путь к вашей папке

compression_quality = 50  # Попробуйте снизить до 70 или ниже

# Функция для получения размера файла в килобайтах
def get_file_size(file_path):
    return os.path.getsize(file_path) / 1024  # размер в КБ

# Перебор всех файлов в указанной директории
for filename in os.listdir(directory):
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
        img_path = os.path.join(directory, filename)
        
        # Получаем размер файла до сжатия
        original_size = get_file_size(img_path)

        img = Image.open(img_path)
        # Сжимаем и сохраняем изображение с указанным качеством и прогрессивным сжатием
        img.save(img_path, "JPEG", optimize=True, quality=compression_quality, progressive=True)

        # Получаем размер файла после сжатия
        compressed_size = get_file_size(img_path)

        # Выводим размер файла до и после сжатия
        print(f"Файл: {filename}")
        print(f"Размер до сжатия: {original_size:.2f} КБ")
        print(f"Размер после сжатия: {compressed_size:.2f} КБ")
        print(f"Экономия: {original_size - compressed_size:.2f} КБ")
        print("-" * 40)

print("Все изображения успешно сжаты.")