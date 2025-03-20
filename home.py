import json
import subprocess
import sys
from tkinter import Tk, Canvas, Label, Button, PhotoImage, Entry, Text
from pathlib import Path
from itertools import cycle

# Paths to the JSON files
DATA_DIR = Path(__file__).parent / "data"
MEDICINES_PATH = DATA_DIR / "medicines.json"
ALERT_PATH = DATA_DIR / "alert.json"
HISTORY_PATH = DATA_DIR / "history.json"

if len(sys.argv) < 2:
    print("home.py was opened directly. Launching main.py...")
    subprocess.Popen(["python", "Main.py"])
    sys.exit()  
def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def open_script(script_name):
    try:
        # Pass the current window position as arguments
        x_pos = window.winfo_x()
        y_pos = window.winfo_y()
        subprocess.Popen(["python", script_name, str(x_pos), str(y_pos)])
    except Exception as e:
        print(f"Error opening {script_name}: {e}")
    finally:
        window.quit()
        window.destroy()


def load_medicines():
    medicines = load_json(MEDICINES_PATH)
    return [medicine.get('name', 'Unknown') for medicine in medicines]


def load_expiring_medicines():
    alert = load_json(ALERT_PATH)
    return alert.get('expiring_medicines', [])


def load_recently_sold():
    history = load_json(HISTORY_PATH)
    return [entry.get('name', 'Unknown') for entry in history]


def display_scrolling_text(canvas, x, y, text_list, multiple=False, font_size=8, delay=5000):
    text_list = text_list if text_list else ["No data available"]
    label = Label(window, text="", font=("Arial", font_size), bg="#FFFFFF")
    label.place(x=x, y=y)

    def update_text():
        if multiple:
            batch_size = 5
            text_display = '\n'.join(text_list[:batch_size])
            text_list.extend(text_list[:batch_size])
            del text_list[:batch_size]
        else:
            text_display = text_list.pop(0)
            text_list.append(text_display)

        label.config(text=text_display)
        canvas.after(delay, update_text)

    update_text()


def on_button_refresh1():
    display_scrolling_text(canvas, 216, 223, load_medicines(), multiple=True, font_size=10, delay=3000)


def on_button_refresh2():
    display_scrolling_text(canvas, 468, 223, load_expiring_medicines(), multiple=True, font_size=10, delay=3000)


def on_button_refresh3():
    display_scrolling_text(canvas, 338.13, 398.7, load_recently_sold(), multiple=False, font_size=10, delay=3000)


# Initialize Tkinter window
window = Tk()
try:
    x_pos = int(sys.argv[1])
    y_pos = int(sys.argv[2])
    window.geometry(f"720x512+{x_pos}+{y_pos}")
except (IndexError, ValueError):
    window.geometry("720x512")

window.configure(bg="#FFFFFF")
canvas = Canvas(window, bg="#FFFFFF", height=512, width=720, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Load images safely
ASSETS_PATH = Path(__file__).parent / "assets/home"


def load_image(filename):
    try:
        return PhotoImage(file=ASSETS_PATH / filename)
    except Exception:
        return None


image_image_1 = load_image("image_1.png")
image_1 = canvas.create_image(363.0, 258.5, image=image_image_1)

image_image_2 = load_image("image_2.png")
image_2 = canvas.create_image(402.5, 280.0, image=image_image_2)

image_image_3 = load_image("image_3.png")
image_3 = canvas.create_image(411.0, 31.0, image=image_image_3)

button_image_4 = load_image("button_4.png")
button_image_3 = load_image("button_3.png")
button_image_5 = load_image("button_5.png")

button_refresh1 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=on_button_refresh1,
                         relief="flat")
button_refresh1.place(x=347.0, y=289.0, width=35.0, height=35.0)

button_refresh2 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=on_button_refresh2,
                         relief="flat")
button_refresh2.place(x=588.0, y=289.0, width=35.0, height=35.0)

button_refresh3 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=on_button_refresh3,
                         relief="flat")
button_refresh3.place(x=435.0, y=421.0, width=26.25, height=26.25)

button_image_1 = load_image("button_1.png")
button_tab5 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                     command=lambda: open_script("Medicine_Dashboard_View.py"), relief="flat")
button_tab5.place(x=18.5625, y=433.7088, width=56.8125, height=57.1139)

button_image_2 = load_image("button_2.png")
button_tab4 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                     command=lambda: open_script("tracking.py"), relief="flat")
button_tab4.place(x=18.5625, y=334.9494, width=56.8125, height=60.0886)

button_image_6 = load_image("button_6.png")
button_tab3 = Button(image=button_image_6, borderwidth=0, highlightthickness=0,
                     command=lambda: open_script("salequantity.py"), relief="flat")
button_tab3.place(x=18.5625, y=232.0253, width=56.8125, height=57.1139)

button_image_7 = load_image("button_7.png")
button_tab2 = Button(image=button_image_7, borderwidth=0, highlightthickness=0,
                     command=lambda: open_script("adjust.py"), relief="flat")
button_tab2.place(x=18.5625, y=133.8608, width=56.8125, height=57.1139)

button_image_8 = load_image("button_8.png")
button_tab1 = Button(image=button_image_8, borderwidth=0, highlightthickness=0, command=lambda: open_script("home.py"),
                     relief="flat")
button_tab1.place(x=18.5, y=34.0, width=56.8125, height=57.1139)

window.resizable(False, False)
window.mainloop()