from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import Medicine_Dashboard_Process
import subprocess
import sys
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/dashboard")
if len(sys.argv) < 2:
    print("adjust.py was opened directly. Launching main.py...")
    subprocess.Popen(["python", "Main.py"])
    sys.exit()

def relative_to_assets(path: str) -> str:
    return str(ASSETS_PATH / path)


class Medicine_Dashboard_View:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x512")
        self.window.configure(bg="#1E1E1E")
        self.canvas = Canvas(
            self.window,
            bg="#1E1E1E",
            height=512,
            width=720,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.chart_canvas = None
        self.chart_canvas_4 = None

        self.bg_image = PhotoImage(file=relative_to_assets("bg.png"))
        self.canvas.create_image(
            360.0,
            256.0,
            image=self.bg_image
        )

        # Button 1
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: Medicine_Dashboard_Process.load_and_display_medicine_stock(self),
            relief="flat"
        )
        self.button_1.place(x=210.0, y=66.0, width=92.0, height=46.0)

        # Button 2
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: Medicine_Dashboard_Process.load_and_display_top5_best_selling_bar(self),
            relief="flat"
        )
        self.button_2.place(x=360.0, y=66.0, width=92.0, height=46.0)

        # Button 3
        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: Medicine_Dashboard_Process.load_and_display_medicine_exprierd(self),
            relief="flat"
        )
        self.button_3.place(x=511.0, y=65.0, width=107.0, height=46.0)

        def open_script(script_name):
            try:
                # Pass the current window position as arguments
                x_pos = self.window.winfo_x()
                y_pos = self.window.winfo_y()
                subprocess.Popen(["python", script_name, str(x_pos), str(y_pos)])
            except Exception as e:
                print(f"Error opening {script_name}: {e}")
            finally:
                self.window.quit()
                self.window.destroy()

        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_tab5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_script("Medicine_Dashboard_View.py"),
            relief="flat"
        )
        self.button_tab5.place(x=18.5, y=430.5, width=56.8125, height=57.1139)

        self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_tab4 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_script("tracking.py"),
            relief="flat"
        )
        self.button_tab4.place(x=18.5, y=331.5, width=56.8125, height=57.1139)

        self.button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        self.button_tab3 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_script("salequantity.py"),
            relief="flat"
        )
        self.button_tab3.place(x=18.5, y=228.5, width=56.8125, height=57.1139)

        self.button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
        self.button_tab2 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_script("adjust.py"),
            relief="flat"
        )
        self.button_tab2.place(x=18.5, y=130.36, width=56.8125, height=57.2532)

        self.button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
        self.button_tab1 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_script("home.py"),
            relief="flat"
        )
        self.button_tab1.place(x=18.5, y=30.5, width=56.8125, height=57.1139)

        self.window.resizable(False, False)
        self.window.mainloop()


if __name__ == "__main__":
    Medicine_Dashboard_View()