# Port Scanner

Bu proje Python ile yazılmış basit bir port tarayıcıdır. Kullanıcının bulunduğu yerel ağda tüm cihazları ve belirlenen port aralığını tarar.

## Özellikler

- Yerel IP adresini ve ağı otomatik algılar
- Belirli port aralığında tarama yapar
- Açık ve kapalı portları ayrı ayrı listeler
- Açık portları `scan_result.txt` dosyasına kaydeder

## Kullanım

Python 3 yüklü olmalıdır. Terminal veya komut istemcisine aşağıdaki komut yazılır:
python portscanner.py

Program IP aralığını otomatik belirledikten sonra sizden taramak istediğiniz port aralığını ister. Örnek giriş:
Enter port range: 20-100
