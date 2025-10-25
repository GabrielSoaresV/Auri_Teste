import customtkinter as ctk
from theme.colors import COLORS
from interfaces.home import HomePage
from interfaces.config import ConfigPage
from interfaces.detector import DetectorPage
from interfaces.notificacao import NotificacaoPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Auri - Sistema")
        self.geometry("862x490")
        self.configure(fg_color=COLORS["bg_primary"])

        self.container = ctk.CTkFrame(self, fg_color=COLORS["bg_primary"])
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, ConfigPage, DetectorPage, NotificacaoPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(HomePage)

    def mostrar_tela(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()
