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
        self.geometry("800x600")
        self.configure(fg_color=COLORS["bg_primary"])

        self.frames = {}

        container = ctk.CTkFrame(self, fg_color=COLORS["bg_primary"])
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (HomePage, ConfigPage, DetectorPage, NotificacaoPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            try:
                frame.grid_rowconfigure(0, weight=1)
                frame.grid_columnconfigure(0, weight=1)
            except Exception:
                pass

        self.mostrar_tela(HomePage)

    def mostrar_tela(self, page_class):
        """Mostra a tela (frame) correspondente à classe passada."""
        frame = self.frames[page_class]
        frame.tkraise()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()
