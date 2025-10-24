import customtkinter as ctk
from theme.colors import COLORS

from interfaces.config import ConfigPage
from interfaces.popup_gif import PopupGif
from interfaces.notificacao import NotificacaoPage
from interfaces.detector import DetectorPage

class HomePage(ctk.CTkFrame):
    def _init_(self, master, controller):
        super()._init_(master, fg_color=COLORS["bg_primary"])
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=0)  

        sidemenu = ctk.CTkFrame(self, width=200, fg_color=COLORS["side_menu"])
        sidemenu.grid(row=0, column=1, sticky="ns")

        btn_config = ctk.CTkButton(
            sidemenu,
            text="Configurações ⚙",
            fg_color=COLORS["accent"],
            hover_color=COLORS["button_hover"],
            command=lambda: controller.mostrar_tela(ConfigPage)
        )
        btn_config.pack(pady=20, padx=10, fill="x")

        btn_ajuda = ctk.CTkButton(
            sidemenu,
            text="Ajuda",
            fg_color=COLORS["accent"],
            hover_color=COLORS["button_hover"],
            command=lambda: PopupGif(self)
        )
        btn_ajuda.pack(pady=20, padx=10, fill="x")

        btn_libras = ctk.CTkButton(
            sidemenu,
            text="Libras",
            fg_color=COLORS["accent"],
            hover_color=COLORS["button_hover"],
            command=lambda: controller.mostrar_tela(NotificacaoPage)
        )
        btn_libras.pack(pady=20, padx=10, fill="x")

        btn_detector = ctk.CTkButton(
            sidemenu,
            text="Detector",
            fg_color=COLORS["accent"],
            hover_color=COLORS["button_hover"],
            command=lambda: controller.mostrar_tela(DetectorPage)
        )
        btn_detector.pack(pady=20, padx=10, fill="x")

        self.container = ctk.CTkFrame(self, fg_color=COLORS["bg_primary"])
        self.container.grid(row=0, column=0, sticky="nsew")
        try:
            self.container.grid_rowconfigure(0, weight=1)
            self.container.grid_columnconfigure(0, weight=1)
        except Exception:
            pass