import json
from datetime import datetime, timedelta

class Alert:
    def __init__(self):
        self.medicines = self.load_medicines()
        self.expiring_medicines = self.check_expiring_medicines()

    def load_medicines(self):
        try:
            with open("data/Medicines.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                # Nếu dữ liệu là danh sách, trả về trực tiếp
                if isinstance(data, list):
                    return data
                # Nếu là dictionary, cố gắng lấy key "medicines"
                return data.get("medicines", [])
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu thuốc: {e}")
            return []

    def check_expiring_medicines(self):
        expiring = []
        today = datetime.today()
        six_months_later = today + timedelta(days=180)

        for medicine in self.medicines:
            try:
                exp_date = datetime.strptime(medicine["expiration date"], "%d/%m/%Y")
                if today <= exp_date <= six_months_later:
                    expiring.append(medicine["name"])
            except KeyError:
                print(f"Thiếu thông tin trong thuốc: {medicine}")
            except ValueError:
                print(f"Định dạng ngày sai: {medicine.get('expiration date')}")

        return expiring
