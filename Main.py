import json
import subprocess
from tkinter import Tk, messagebox
from Login_UI import LoginUI  # Import từ file giao diện

class LoginApp(LoginUI):
    def __init__(self, window):
        super().__init__(window)

        self.login_button.config(command=self.handle_login)
        self.signup_button.config(command=self.handle_signup)

    def load_users(self):
        """Load danh sách tài khoản từ file JSON."""
        try:
            with open("data/users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self, users):
        """Lưu danh sách tài khoản vào file JSON."""
        with open("data/users.json", "w") as file:
            json.dump(users, file, indent=4)

    def handle_login(self):
        """Xử lý đăng nhập."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        users = self.load_users()

        if not username:
            messagebox.showwarning("Warning", "Tên đăng nhập không được để trống.")
            return
        if not password:
            messagebox.showwarning("Warning", "Mật khẩu không được để trống.")
            return

        if username not in users and not any(user["password"] == password for user in users.values()):
            messagebox.showwarning("Warning", "Tài khoản chưa tồn tại, vui lòng đăng ký.")
        elif username not in users:
            messagebox.showwarning("Warning", "Tên đăng nhập sai. Vui lòng thử lại!")
        elif users[username]["password"] != password:
            messagebox.showwarning("Warning", "Mật khẩu sai. Vui lòng thử lại!")
        else:
            messagebox.showinfo("Success", f"Đăng nhập thành công! Xin chào, {username}")
            self.window.destroy()  # Đóng cửa sổ đăng nhập
            self.open_home_gui()

    def handle_signup(self):
        """Xử lý đăng ký tài khoản mới."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Tên đăng nhập và mật khẩu không được để trống!")
            return

        users = self.load_users()

        if username in users:
            messagebox.showwarning("Warning", "Tên đăng nhập đã tồn tại! Vui lòng chọn tên khác.")
        #elif any(user["password"] == password for user in users.values()):
            #messagebox.showwarning("Warning", "Mật khẩu này đã được sử dụng! Vui lòng chọn mật khẩu khác.")
        else:
            users[username] = {"password": password}
            self.save_users(users)
            messagebox.showinfo("Success", "Đăng ký tài khoản thành công! Bạn có thể đăng nhập ngay bây giờ.")

    def open_home_gui(self):
        """Mở giao diện home.py."""
        try:
            subprocess.Popen(["python", "home.py", "from_main"])  # Pass an argument
        except Exception as e:
            messagebox.showerror("Error", f"Không thể mở home.py: {e}")


if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
