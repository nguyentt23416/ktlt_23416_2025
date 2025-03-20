import sys
from pathlib import Path
import json
import subprocess
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk
from adjust_ext import ajust_process as gp
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/adjust")
if len(sys.argv) < 2:
    print("adjust.py was opened directly. Launching main.py...")
    subprocess.Popen(["python", "Main.py"])
    sys.exit()
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
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
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=512,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    363.0,
    258.5,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    411.0,
    31.0,
    image=image_image_2
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_tab5 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_script("Medicine_Dashboard_View.py"),
    relief="flat"
)
button_tab5.place(x=18.5, y=434.0, width=56.8125, height=57.1139)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_tab4 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_script("tracking.py"),
    relief="flat"
)
button_tab4.place(x=18.5, y=335.0, width=56.8125, height=57.1139)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_tab3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_script("salequantity.py"),
    relief="flat"
)
button_tab3.place(x=18.5, y=232.0, width=56.8125, height=57.1139)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_tab2 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_script("adjust.py"),
    relief="flat"
)
button_tab2.place(x=18.5, y=133.86, width=56.8125, height=57.1139)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_tab1 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_script("home.py"),
    relief="flat"
)
button_tab1.place(x=18.5, y=34.0, width=56.8125, height=57.1139)

canvas.create_rectangle(
    128.5,
    99.0,
    683.125,
    462.74627685546875,
    fill="#C7EDC1",
    outline="")

canvas.create_rectangle(
    368.0,
    174.5,
    625.0,
    335.5,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    259.5,
    255.75,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=181.5,
    y=242.0,
    width=156.0,
    height=25.5
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    259.5,
    189.75,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=181.5,
    y=176.0,
    width=156.0,
    height=25.5
)

canvas.create_text(
    182.5,
    223.5,
    anchor="nw",
    text="Quantity",
    fill="#000000",
    font=("Bitter Bold", 15 * -1)
)

canvas.create_text(
    184.5,
    158.5,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Bitter Bold", 15 * -1)
)

canvas.create_text(
    182.5,
    289.5,
    anchor="nw",
    text="Description",
    fill="#000000",
    font=("Bitter Bold", 15 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    259.5,
    321.75,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=181.5,
    y=308.0,
    width=156.0,
    height=25.5
)

# Tạo Treeview
columns = ("Name", "Type", "Quantity")
tree = ttk.Treeview(window, columns=columns, show='headings', height=5)

# Định nghĩa tiêu đề cột
tree.heading("Name", text="Name")
tree.heading("Type", text="Type")
tree.heading("Quantity", text="Quantity")

# Định nghĩa kích thước cột
tree.column("Name", width=80)
tree.column("Type", width=140)
tree.column("Quantity", width=50)

tree.place(x=368.0, y=174.5, width=257.0, height=161.0)

# Load dữ liệu vào Treeview
def load_medicines():
    with open("data/Medicines.json", "r", encoding="utf-8") as file:
        return json.load(file)

medicines = load_medicines()

for medicine in medicines:
    tree.insert("", "end", values=(medicine["name"], medicine["type"], medicine["quantity"]))

# Update dữ liệu vào Treeview
def update_medicines():
    tree.delete(*tree.get_children())
    medicines = load_medicines()
    for medicine in medicines:
        tree.insert("", "end", values=(medicine["name"], medicine["type"], medicine["quantity"]))

# Thêm click_event cho Treeview
def on_treeview_select(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        values = item['values']
        if values:
            entry_1.delete(0, "end")
            entry_1.insert(0, values[2])  # Quantity
            entry_2.delete(0, "end")
            entry_2.insert(0, values[0])  # Name
            entry_3.delete(0, "end")
            entry_3.insert(0, values[1])  # Type

tree.bind("<<TreeviewSelect>>", on_treeview_select)

def selected_item():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        values = item['values']
        if values:
            return values[0]

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (gp.update_button_handle(entry_2, entry_1, entry_3, selected_item()), update_medicines(), gp.reset_button_handle(entry_2, entry_1, entry_3)),
    relief="flat"
)
button_6.place(
    x=445.5,
    y=367.5,
    width=35.0,
    height=35.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (gp.delete_button_handle(entry_2, entry_1, entry_3), update_medicines(), gp.reset_button_handle(entry_1, entry_2, entry_3)),
    relief="flat"
)
button_7.place(
    x=502.0,
    y=366.0,
    width=35.0,
    height=35.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (gp.reset_button_handle(entry_1, entry_2, entry_3), update_medicines()),
    relief="flat"
)
button_8.place(
    x=556.5,
    y=366.0,
    width=35.0,
    height=35.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (gp.add_button_handle(entry_1, entry_2, entry_3), update_medicines(), gp.reset_button_handle(entry_1, entry_2, entry_3)),
    relief="flat"
)
button_9.place(
    x=388.5,
    y=367.5,
    width=35.0,
    height=35.0
)

canvas.create_text(
    463.0,
    153.5,
    anchor="nw",
    text="Thống kê",
    fill="#000000",
    font=("Bitter Bold", 15 * -1)
)

window.resizable(False, False)
window.mainloop()