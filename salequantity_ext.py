import json
from tkinter import messagebox


class salequantity:
    @staticmethod
    def reset_button_handle(entry_1, entry_2):
        """Xóa nội dung của entry_1 và entry_2"""
        entry_1.delete(0, "end")
        entry_2.delete(0, "end")

    @staticmethod
    def sell_medicine(entry_1, entry_2, tree, canvas, load_sales_history):
        """Trừ số lượng thuốc từ Medicines.json khi bán và hiển thị thông tin"""
        medicine_name = entry_1.get().strip()
        try:
            sell_quantity = int(entry_2.get().strip())
        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng phải là số nguyên!")
            return

        file_path = r"data\Medicines.json"
        history_path = r"data\history.json"

        # Đọc dữ liệu từ Medicines.json
        with open(file_path, "r", encoding="utf-8") as file:
            medicines = json.load(file)

        for medicine in medicines:
            if medicine["name"].lower() == medicine_name.lower():
                current_quantity = int(medicine.get("quantity", 0))
                price = int(medicine.get("price", 0))  # Lấy giá thuốc

                if sell_quantity > current_quantity:
                    messagebox.showerror("Lỗi", "Số lượng bán vượt quá tồn kho!")
                    return

                total_price = sell_quantity * price  # Tính tổng giá tiền
                medicine["quantity"] = current_quantity - sell_quantity

                # Ghi lại vào Medicines.json
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(medicines, file, ensure_ascii=False, indent=4)

                # Cập nhật lại bảng Treeview
                salequantity.update_treeview(tree)

                # Hiển thị dữ liệu lên canvas
                canvas.create_rectangle(153, 301, 388, 392, fill="#FFFFFF", outline="")
                canvas.create_text(160, 310, anchor="nw", text=f"Tên thuốc: {medicine_name}", fill="#000000",
                                   font=("Arial", 12))
                canvas.create_text(160, 330, anchor="nw", text=f"Số lượng bán: {sell_quantity}", fill="#000000",
                                   font=("Arial", 12))
                canvas.create_text(160, 350, anchor="nw", text=f"Tổng tiền: {total_price} VND", fill="#000000",
                                   font=("Arial", 12))

                # Lưu lịch sử bán vào history.json
                history_data = []
                try:
                    with open(history_path, "r", encoding="utf-8") as file:
                        history_data = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    pass  # Nếu file chưa tồn tại hoặc bị lỗi, tiếp tục với danh sách trống

                history_data.append({
                    "name": medicine_name,
                    "quantity": sell_quantity,
                    "total_price": total_price
                })

                with open(history_path, "w", encoding="utf-8") as file:
                    json.dump(history_data, file, ensure_ascii=False, indent=4)

                messagebox.showinfo("Thành công",
                                    f"Đã bán {sell_quantity} {medicine_name}!\nTổng tiền: {total_price} VND")
                load_sales_history()  # Cập nhật bảng sau khi bán thuốc

                return

        messagebox.showerror("Lỗi", "Không tìm thấy thuốc!")

    @staticmethod
    def update_treeview(tree):
        """Cập nhật lại bảng Treeview sau khi thay đổi dữ liệu"""
        file_path = r"data\Medicines.json"

        with open(file_path, "r", encoding="utf-8") as file:
            medicines = json.load(file)

        tree.delete(*tree.get_children())  # Xóa dữ liệu cũ trong bảng
        for medicine in medicines:
            tree.insert("", "end", values=(
                medicine.get("name", "N/A"),
                medicine.get("quantity", 0),
                medicine.get("price", 0)  # Mặc định là 0 nếu không có giá
            ))
