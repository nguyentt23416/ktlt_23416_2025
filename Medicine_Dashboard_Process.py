import datetime
import json
from collections import defaultdict
from tkinter import Label, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def load_and_display_medicine_stock(self):
    with open('data/Medicines.json', 'r+', encoding = "utf-8") as f:
        data = json.load(f)
        # Sắp xếp giảm dần theo số lượng
    sorted_medicines = sorted(
        [(med['name'], int(med['quantity'])) for med in data if
         isinstance(med['quantity'], (int, str)) and str(med['quantity']).isdigit()],
        key=lambda x: x[1], reverse=True
    )
    top_medicines = sorted_medicines[:]
    medicines = [item[0] for item in top_medicines]
    stock = [item[1] for item in top_medicines]
    total_quantity = sum(int(med['quantity']) for med in data if str(med['quantity']).isdigit())
    # Tạo danh sách màu theo điều kiện số lượng
    colors = []
    for qty in stock:
        if qty < 10:
            colors.append('red')
        elif qty < 20:
            colors.append('orange')
        else:
            colors.append('#3498db')  # Xanh dương
    # Vẽ biểu đồ với màu sắc theo điều kiện
    fig = Figure(figsize=(4, 3.5), dpi=100)
    ax = fig.add_subplot(111)
    bars = ax.barh(medicines, stock, color=colors)
    # Tùy chỉnh giao diện
    ax.set_xlabel("Số lượng tồn kho", fontsize=6, color='black')
    ax.set_title("Hàng tồn kho", fontsize=10, color='black')
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    ax.tick_params(axis='x', colors='black', labelsize=8)
    ax.tick_params(axis='y', colors='black', labelsize=4)
    ax.invert_yaxis()
    # Hiển thị số lượng trên mỗi cột với màu đen
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
                str(int(width)), va='center', color='black', fontsize=4)
    # Gắn vào Tkinter
    chart_canvas = FigureCanvasTkAgg(fig, master=self.window)
    chart_canvas.draw()
    chart_canvas.get_tk_widget().place(x=200, y=140)
    self.label_total_quantity = Label(
        self.window,
        text=f"Tổng số lượng thuốc: {total_quantity}",
        bg="#1E1E1E",
        fg="white",
        font=("Arial", 10, "bold")
    )
    self.label_total_quantity.place(
        x=300,  # Tùy chỉnh vị trí bên cạnh biểu đồ
        y=120,
        width=200,
        height=30
    )


def load_and_display_medicine_exprierd(self):
    today = datetime.datetime.today().date()  # Lấy ngày hôm nay

    # Xóa biểu đồ cũ nếu có
    if self.chart_canvas is not None:
        self.chart_canvas.get_tk_widget().destroy()
        self.chart_canvas = None

    # Đọc file JSON
    with open('data/Medicines.json', 'r+', encoding="utf-8") as f:
        data = json.load(f)

    medicines = []
    days_left_list = []
    colors = []
    total_expiring_soon = 0
    # Lọc và tính số ngày còn lại
    for med in data:
        expiry_str = med.get('expiration date', None)  # Lấy ngày hết hạn
        if not expiry_str:
            print(f"Thuốc {med['name']} không có ngày hết hạn!")
            continue

        # Kiểm tra định dạng ngày
        expiry_date = None
        for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
            try:
                expiry_date = datetime.datetime.strptime(expiry_str, fmt).date()
                break
            except ValueError:
                continue

        if not expiry_date:
            print(f"Thuốc {med['name']} có ngày sai định dạng: {expiry_str}")
            continue
        days_left = (expiry_date - today).days
        # Chỉ lấy thuốc sắp hết hạn <= 9 ngày
        if 0 <= days_left <= 9:
            medicines.append(med['name'])
            days_left_list.append(days_left)
            total_expiring_soon += 1
            # Xét màu theo mức độ
            if days_left <= 3:
                colors.append('red')  # Gấp, sắp hết hạn
            elif days_left <= 7:
                colors.append('yellow')  # Gần hết hạn
            else:
                colors.append('orange')  # An toàn trong 9 ngày
    # Kiểm tra có thuốc sắp hết hạn không
    if not medicines:
        messagebox.showinfo("Thông báo", "Không có thuốc sắp hết hạn trong 9 ngày.")
        return

    # Vẽ biểu đồ
    fig = Figure(figsize=(4, 3.5), dpi=100)
    ax = fig.add_subplot(111)
    bars = ax.bar(medicines, days_left_list, color=colors)

    # Tùy chỉnh trục và tiêu đề
    ax.set_ylabel("Số ngày còn lại", fontsize=10, color='black')
    ax.set_title("Thuốc sắp hết hạn (trong 9 ngày)", fontsize=8, color='black', pad=8)
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    ax.tick_params(axis='x', labelrotation=10, labelsize=9, colors='black')
    ax.tick_params(axis='y', labelsize=8, colors='black')

    # Giới hạn trục Y
    max_days = max(days_left_list)
    ax.set_ylim(0, max_days + 3)  # Cách ra cho đẹp

    # Hiển thị số ngày trên cột
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.3,
                f"{int(height)} ngày", ha='center', fontsize=9, color='black')

    fig.tight_layout()  # Chỉnh gọn đẹp

    # Hiển thị lên tkinter
    self.chart_canvas = FigureCanvasTkAgg(fig, master=self.window)
    self.chart_canvas.draw()
    self.chart_canvas.get_tk_widget().place(x=200, y=140)  # Tuỳ chỉnh vị trí
    # Tạo label mới
    self.label_total_expiring_soon = Label(
        self.window,
        text=f"Số thuốc sắp hết hạn: {total_expiring_soon}",
        bg="#1E1E1E",
        fg="white",
        font=("Arial", 10, "bold")
    )
    self.label_total_expiring_soon.place(
        x=300,  # Kéo ra bên phải
        y=120,
        width=200,
        height=30
    )


def load_and_display_top5_best_selling_bar(self):
    with open(r"data/history.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    sales_data = defaultdict(int)
    total_revenue = 0
    for entry in data:
        sales_data[entry['name']] += entry['quantity']
        total_revenue += entry.get('total_price', 0)
    sorted_sales = sorted(sales_data.items(), key=lambda x: x[1], reverse=True)[:5]

    medicine_names = [item[0] for item in sorted_sales]
    total_quantities = [item[1] for item in sorted_sales]

    if not medicine_names:
        print("Không có dữ liệu bán hàng.")
        messagebox.showinfo("Thông báo", "Không có dữ liệu bán hàng.")
        return

    fig = Figure(figsize=(4, 3.5), dpi=100)
    ax = fig.add_subplot(111)
    bars = ax.bar(medicine_names, total_quantities, color='#4CAF50')

    ax.set_ylabel("Số lượng bán", fontsize=8, color='black')
    ax.set_title("Top 5 Thuốc Bán Chạy Nhất", fontsize=10, color='black')
    ax.tick_params(axis='x', labelrotation=30, labelsize=5, colors='black')
    ax.tick_params(axis='y', labelsize=8, colors='black')

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
                f"{int(height)}", ha='center', fontsize=8, color='black')

    if self.chart_canvas is not None:
        self.chart_canvas.get_tk_widget().destroy()
        self.chart_canvas = None

    self.chart_canvas = FigureCanvasTkAgg(fig, master=self.window)
    self.chart_canvas.draw()
    self.chart_canvas.get_tk_widget().place(x=200, y=140)
    self.label_total_revenue = Label(
        self.window,
        text=f"Tổng doanh thu: {total_revenue:,} VNĐ",
        bg="#1E1E1E",  # Màu nền tối phù hợp
        fg="white",  # Màu chữ trắng nổi bật
        font=("Arial", 10, "bold")
    )
    self.label_total_revenue.place(
        x=300,  # Kéo về bên phải biểu đồ
        y=120,
        width=200,
        height=30
    )