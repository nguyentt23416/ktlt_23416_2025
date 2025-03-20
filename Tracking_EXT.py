import json
from tkinter import messagebox

class Tracking:
    def __init__(self, entry_medicine, entry_quantity):
        self.entry_medicine = entry_medicine
        self.entry_quantity = entry_quantity
        self.medicines = self.load_medicines()
        self.selected_medicine = None
        self.tree = None

    def set_tree(self, tree):
        self.tree = tree

    def load_medicines(self):
        try:
            with open("data/Medicines.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải dữ liệu: {str(e)}")
            return []

    def display_medicines(self, tree):
        tree.delete(*tree.get_children())
        for medicine in self.medicines:
            tree.insert("", "end", values=(medicine['name'], medicine['type'], medicine['quantity']))

    def select_medicine(self, event, tree):
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            values = item['values']
            if values:
                self.entry_medicine.delete(0, "end")
                self.entry_medicine.insert(0, values[0])  # Name
                self.entry_quantity.delete(0, "end")
                self.entry_quantity.insert(0, str(values[2]))  # Quantity
                self.selected_medicine = values[0]

    def update_quantity(self, amount):
        if not self.selected_medicine:
            messagebox.showwarning("Lỗi", "Vui lòng chọn thuốc trước!")
            return

        try:
            current_quantity = self.entry_quantity.get()
            if not current_quantity.isdigit():
                messagebox.showerror("Lỗi", "Số lượng không hợp lệ!")
                return

            new_quantity = int(current_quantity) + amount
            if new_quantity < 0:
                messagebox.showerror("Lỗi", "Số lượng không thể âm!")
                return

            self.entry_quantity.delete(0, "end")
            self.entry_quantity.insert(0, str(new_quantity))

        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng không hợp lệ!")

    def save(self):
        """Lưu cập nhật vào file JSON mà không cần chọn thuốc"""
        try:
            medicine_name = self.entry_medicine.get().strip()
            new_quantity = self.entry_quantity.get()

            if not medicine_name:
                messagebox.showwarning("Lỗi", "Vui lòng nhập tên thuốc!")
                return

            if not new_quantity.isdigit():
                messagebox.showerror("Lỗi", "Số lượng không hợp lệ!")
                return

            new_quantity = int(new_quantity)
            updated = False
            for medicine in self.medicines:
                if medicine["name"].lower() == medicine_name.lower():
                    medicine["quantity"] = new_quantity
                    updated = True
                    break

            if not updated:
                messagebox.showwarning("Lỗi", "Tên thuốc không tồn tại trong danh sách!")
                return

            with open("data/Medicines.json", "w", encoding="utf-8") as file:
                json.dump(self.medicines, file, indent=4, ensure_ascii=False)
            messagebox.showinfo("Thành công", "Cập nhật số lượng thành công!")

            if self.tree:
                self.display_medicines(self.tree)  # ✅ Làm mới danh sách thuốc
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {str(e)}")

    def update_all(self):
        """Cập nhật lại toàn bộ dữ liệu hiển thị trên Treeview"""
        self.medicines = self.load_medicines()  # Tải lại dữ liệu từ file JSON
        if self.tree:
            self.display_medicines(self.tree)  # Cập nhật Treeview với dữ liệu mới
        messagebox.showinfo("Thành công", "Danh sách thuốc đã được làm mới!")
