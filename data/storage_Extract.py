import json

# Đọc dữ liệu từ file Medicines.json
input_file = "Medicines.json"
output_file = "Medicines_storage.json"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Trích xuất dữ liệu cần thiết
medicines_storage = []
for medicine in data.get("medicines", []):
    medicines_storage.append({
        "name": medicine["name"],
        "type": medicine["type"],
        "quantity": "0"  # Giá trị mặc định là 0
    })

# Ghi dữ liệu vào file mới
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(medicines_storage, file, indent=4, ensure_ascii=False)

print(f"Dữ liệu đã được trích xuất và lưu vào {output_file}")
