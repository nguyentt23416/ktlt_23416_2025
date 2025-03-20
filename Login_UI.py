from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/login")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class LoginUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Login System")

        # Kích thước cửa sổ
        window_width = 540
        window_height = 384

        # Lấy kích thước màn hình
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Tính toán vị trí căn giữa
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Đặt kích thước và vị trí cửa sổ
        self.window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=384,
            width=540,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_bg = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(270, 192, image=self.image_bg)

        # Khung đăng nhập
        self.canvas.create_rectangle(45, 51, 495, 332, fill="#A3CD9E", outline="")

        # Chữ WELCOME
        self.canvas.create_text(270, 87, anchor="center", text="WELCOME", fill="#FFFFFF",
                                font=("Black Han Sans", 48))

        # Icon user
        self.image_user = PhotoImage(file=relative_to_assets("image_2.png"))
        self.canvas.create_image(126, 166, image=self.image_user)

        # Ô nhập username
        self.entry_bg_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.canvas.create_image(270, 166, image=self.entry_bg_1)
        self.username_entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.username_entry.place(x=180, y=144, width=180, height=43)

        # Icon password
        self.image_lock = PhotoImage(file=relative_to_assets("image_3.png"))
        self.canvas.create_image(126, 231, image=self.image_lock)

        # Ô nhập password
        self.entry_bg_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.canvas.create_image(270, 231, image=self.entry_bg_2)
        self.password_entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show="*")
        self.password_entry.place(x=180, y=209, width=180, height=43)

        # Nút SIGN UP
        self.button_signup = PhotoImage(file=relative_to_assets("button_1.png"))
        self.signup_button = Button(image=self.button_signup, borderwidth=0, highlightthickness=0, relief="flat")
        self.signup_button.place(x=162, y=266, width=95, height=25)

        # Nút LOGIN
        self.button_login = PhotoImage(file=relative_to_assets("button_2.png"))
        self.login_button = Button(image=self.button_login, borderwidth=0, highlightthickness=0, relief="flat")
        self.login_button.place(x=282, y=266, width=95, height=25)

        self.window.resizable(False, False)
