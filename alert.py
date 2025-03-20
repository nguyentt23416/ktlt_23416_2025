from pathlib import Path
from tkinter import Tk, Canvas, Entry, Label, PhotoImage, font
import json
from alert_ext import Alert
import sys
import subprocess
if len(sys.argv) < 2:
    print("alert.py was opened directly. Launching main.py...")
    subprocess.Popen(["python", "Main.py"])
    sys.exit()
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_alert_window(medicine_name, callback):
    print(f"Creating alert for: {medicine_name}")  # Debugging print

    window = Tk()
    window.geometry("480x217")
    window.configure(bg="#A3CD9E")

    canvas = Canvas(
        window,
        bg="#A3CD9E",
        height=217,
        width=480,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(240.0, 23.0, image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(43.0, 125.0, image=image_image_2)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.create_image(240.0, 125.0, image=image_image_3)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(213.0, 123.0, image=entry_image_1)

    custom_font = font.Font(family="Bitter", size=8, weight="bold")
    label_1 = Label(
        window,
        text=medicine_name,
        bg="#FFFFFF",
        fg="#000716",
        font=custom_font
    )
    label_1.place(x=169.0, y=113.0)

    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window, callback))
    window.mainloop()


def on_close(window, callback):
    window.destroy()
    callback()


def save_expiring_medicines(expiring_medicines):
    print(f"Saving expiring medicines: {expiring_medicines}")  # Debugging print
    data_path = Path("data/alert.json")
    data_path.parent.mkdir(parents=True, exist_ok=True)
    with open(data_path, "w", encoding="utf-8") as file:
        json.dump({"expiring_medicines": expiring_medicines}, file, indent=4, ensure_ascii=False)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/alert")

alert = Alert()
print(f"Expiring medicines: {alert.expiring_medicines}")  # Debugging print
expiring_medicines = alert.expiring_medicines.copy()


def show_next_alert():
    if expiring_medicines:
        create_alert_window(expiring_medicines.pop(0), show_next_alert)
    else:
        save_expiring_medicines(alert.expiring_medicines)


show_next_alert()
