import json
import sys

from salequantity_ext import salequantity as sq
from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/salequantity")
if len(sys.argv) < 2:
    print("salequantity.py was opened directly. Launching main.py...")
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
    bg = "#FFFFFF",
    height = 512,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
    402.5,
    280.0,
    image=image_image_2
)

canvas.create_text(
    231.0,
    119.0,
    anchor="nw",
    text="SỐ LƯỢNG THUỐC BÁN RA",
    fill="#000000",
    font=("Bitter Bold", 25 * -1)
)

canvas.create_text(
    471.0,
    162.0,
    anchor="nw",
    text="Thuốc khả dụng",
    fill="#000000",
    font=("Bitter Bold", 16 * -1)
)

canvas.create_text(
    199.0,
    162.0,
    anchor="nw",
    text="Thuốc muốn bán",
    fill="#000000",
    font=("Bitter Bold", 16 * -1)
)

canvas.create_text(
    155.0,
    191.0,
    anchor="nw",
    text="Tên thuốc muốn bán:",
    fill="#000000",
    font=("Bitter Bold", 16 * -1)
)

canvas.create_text(
    155.0,
    242.0,
    anchor="nw",
    text="Số lượng muốn bán:",
    fill="#000000",
    font=("Bitter Bold", 16 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    411.0,
    31.0,
    image=image_image_3
)



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
button_tab3.place(x=18.5, y=231.9999, width=56.8125, height=57.1139)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_tab2 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_script("adjust.py"),
    relief="flat"
)
button_tab2.place(x=18.5, y=133.8607, width=56.8125, height=57.1139)

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
    414.0,
    188.0,
    660.0,
    392.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    153.0,
    301.0,
    388.0,
    392.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    270.5,
    226.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=153.0,
    y=212.0,
    width=235.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    270.5,
    277.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=153.0,
    y=263.0,
    width=235.0,
    height=26.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sq.sell_medicine(entry_1, entry_2, tree, canvas, load_sales_history),  # Gọi hàm bán thuốc
    relief="flat"
)
button_6.place(
    x=153.0,
    y=410.0,
    width=95.25,
    height=25.5
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sq.reset_button_handle(entry_1, entry_2),  # Gọi hàm xóa dữ liệu
    relief="flat"
)
button_7.place(
    x=293.0,
    y=410.0,
    width=95.25,
    height=25.5
)
canvas.create_rectangle(
    414.0,
    188.0,
    660.0,
    392.0,
    fill="#FFFFFF",
    outline=""
)

# Thêm bảng Treeview vào vùng trên
columns = ("Name", "Quantity", "Price")
tree = ttk.Treeview(window, columns=columns, show='headings', height=5)

# Định nghĩa tiêu đề cột
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")

# Định nghĩa kích thước cột
tree.column("Name", width=50)
tree.column("Quantity", width=50)
tree.column("Price", width=50)

# Đặt bảng vào trong vùng canvas đã tạo
tree.place(x=414, y=190, width=246, height=200)

def load_medicines():
    with open(r"data\Medicines.json", "r", encoding="utf-8") as file:
        return json.load(file)
medicines = load_medicines()

for medicine in medicines:
    tree.insert(
        "", "end",
        values=(
            medicine.get("name", "N/A"),
            medicine.get("quantity", 0),
            medicine.get("price", 0)  # Nếu không có "price", mặc định là 0
        )
    )
# Update dữ liệu vào Treeview
def update_medicines():
    tree.delete(*tree.get_children())
    medicines = load_medicines()
    for medicine in medicines:
        tree.insert("", "end", values=(medicine["name"], medicine["quantity"], medicine["price"]))

# Thêm bảng lịch sử bán thuốc
history_columns = ("Tên thuốc", "Tổng số lượng", "Tổng tiền")
history_tree = ttk.Treeview(window, columns=history_columns, show="headings", height=5)

# Định nghĩa tiêu đề cột
history_tree.heading("Tên thuốc", text="Tên thuốc")
history_tree.heading("Tổng số lượng", text="Tổng số lượng")
history_tree.heading("Tổng tiền", text="Tổng tiền")

# Định nghĩa kích thước cột
history_tree.column("Tên thuốc", width=75)
history_tree.column("Tổng số lượng", width=90)
history_tree.column("Tổng tiền", width=60)

# Đặt bảng vào cửa sổ
history_tree.place(x=153, y=301, width=235, height=100)

def load_sales_history():
    """Load dữ liệu từ history.json và hiển thị lên Treeview"""
    try:
        with open("C:\\KTLT\\Đồ Án Cuối Kỳ\\SoLuongThuocBanRa\\data\\history.json", "r", encoding="utf-8") as file:
            history_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history_data = []

    # Xóa dữ liệu cũ
    history_tree.delete(*history_tree.get_children())

    # Thêm dữ liệu từ history.json vào bảng
    for record in history_data:
        history_tree.insert("", "end", values=(record["name"], record["quantity"], record["total_price"]))

# Gọi hàm khi khởi động chương trình
load_sales_history()


# Thêm click_event cho Treeview
def on_treeview_select(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        values = item['values']
        if values:
            entry_1.delete(0, "end")
            entry_1.insert(0, values[0])  # Name

            entry_2.focus_set()  # Chuyển con trỏ về entry_2 để người dùng nhập số lượng
tree.bind("<<TreeviewSelect>>", on_treeview_select)

def selected_item():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        values = item['values']
        if values:
            return values[0]
window.resizable(False, False)
window.mainloop()
