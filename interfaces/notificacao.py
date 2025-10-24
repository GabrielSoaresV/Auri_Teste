import  os
import customtkinter as ctk
from theme.colors import *  
from PIL import Image, ImageTk

class PopupNotification(ctk.CTkToplevel):
    def __init__(self, master, title="Notificação", message="Esta é uma notificação"):
        super().__init__(master)
        self.title(title)
        self.geometry("300x150")
        self.configure(fg_color=COLORS["bg_primary"])
        self.attributes("-topmost", True)

        self.label_message = ctk.CTkLabel(self, text=message, fg_color=COLORS["bg_primary"], text_color=COLORS["text_primary"])
        self.label_message.pack(expand=True)

        self._frames =[]
        self.frames = self._index = 0
        self._loop_done = 0
        self.max_loops = 5

        base_dir = os.path.dirname(os.path.abspath(__file__))
        #gif_path = os.path.abspath(os.path.join(base_dir, "assets", "nome do gif.gif"))
        gif_path = os.path.join(base_dir, "assets", "notification.gif")

        self.btn_voltar = ctk.CTkButton(self, text="Voltar", fg_color=COLORS["accent"], hover_color=COLORS["button_hover"], command=self.destroy)
        self.btn_voltar.pack(pady=20, padx=20, fill="x")

        self.center_window()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def start_detection(self):
        self.master.show_notificacao()

app = ctk.CTk()
app.show_notificacao()
app.mainloop()