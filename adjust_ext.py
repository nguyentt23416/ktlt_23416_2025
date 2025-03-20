from tkinter import *
# import gui1.<class_name>
from tkinter import messagebox
import json


class ajust_process:
    @staticmethod
    def reset_button_handle(entry_1, entry_2, entry_3):
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)

    @staticmethod
    def add_button_handle(entry_1, entry_2, entry_3):
        name = entry_2.get()
        quantity = entry_1.get()
        desc = entry_3.get()
        if name == '' or quantity == '' or desc == '':
            messagebox.showerror("Warning", "Xin hãy điền đầy đủ thông tin.")
            return
        with open('data/Medicines.json', 'r+', encoding = "utf-8") as file:
            try:
                medicines = json.load(file)
            except json.JSONDecodeError:
                medicines = []
        medicines.append({
            'name': name,
            'type': desc,
            'quantity': quantity
        })
        with open('data/Medicines.json', 'r+', encoding = "utf-8") as file:
            json.dump(medicines, file, ensure_ascii= False, indent = 4)
        messagebox.showerror("Succeed", "Dữ liệu đã được thêm vào thành công.")

    @staticmethod
    def update_button_handle(entry_2, entry_1, entry_3, selected_item):
        name = entry_2.get()
        quantity = entry_1.get()
        desc = entry_3.get()
        if name == '' or quantity == '' or desc == '':
            messagebox.showerror("Warning", "Xin hãy điền đầy đủ thông tin.")
            return
        with open('data/Medicines.json', 'r', encoding="utf-8") as file:
            try:
                medicines = json.load(file)
            except json.JSONDecodeError:
                medicines = []
        for medicine in medicines:
            if medicine['name'] == selected_item:
                medicine['name'] = name
                medicine['type'] = desc
                medicine['quantity'] = quantity
                break
        with open('data/Medicines.json', 'w', encoding="utf-8") as file:
            json.dump(medicines, file, ensure_ascii=False, indent=4)
        messagebox.showerror("Succeed", "Dữ liệu đã được cập nhật thành công.")

    @staticmethod
    def delete_button_handle(entry_2, entry_1, entry_3):
        name = entry_2.get()
        quantity = entry_1.get()
        desc = entry_3.get()
        if name == '' or quantity == '' or desc == '':
            messagebox.showerror("Warning", "Xin hãy điền đầy đủ thông tin.")
            return
        with open('data/Medicines.json', 'r', encoding="utf-8") as file:
            try:
                medicines = json.load(file)
            except json.JSONDecodeError:
                medicines = []
        for medicine in medicines:
            if medicine['name'] == name:
                medicines.remove(medicine)
                break
        with open('data/Medicines.json', 'w', encoding="utf-8") as file:
            json.dump(medicines, file, ensure_ascii=False, indent=4)
        messagebox.showerror("Succeed", "Dữ liệu đã được xóa thành công.")

# lam tuong tu cho 5 nut
#     @staticmethod
#     def Tracking(self):
#         self.window.destroy()
#         app = <classname>()
#         app.window.mainloop()
#     @staticmethod
#     def Tracking(self):
#         self.window.destroy()
#         app = <classname>()
#         app.window.mainloop()
#     @staticmethod
#     def Tracking(self):
#         self.window.destroy()
#         app = <classname>()
#         app.window.mainloop()
#     @staticmethod
#     def Tracking(self):
#         self.window.destroy()
#         app = <classname>()
#         app.window.mainloop()

