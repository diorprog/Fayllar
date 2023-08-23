import subprocess

usb_path = "/dev/sdX"  # Usb manzili (X o'rniga qo'yilgan harfni qo'llang)

try:
    subprocess.run(["sudo", "umount", usb_path + "*"], check=True)
    subprocess.run(["sudo", "mkfs.fat", "-F32", usb_path], check=True)
    print("Usb muvaffaqiyatli formatlandi.")
except subprocess.CalledProcessError as e:
    print("Xatolik yuz berdi:", e)




'''
Terminalda: 
lsblk
sudo su
python format_usb.py

'''