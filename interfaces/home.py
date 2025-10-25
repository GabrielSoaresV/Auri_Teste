import os
from PIL import Image
import customtkinter as ctk
from theme.colors import COLORS
from interfaces.popup import PopupGif
from interfaces.config import ConfigPage
from interfaces.notificacao import NotificacaoPage
from interfaces.detector import DetectorPage
from customtkinter import CTkImage

class HomePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=COLORS["bg_primary"])
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=0)

        sidemenu = ctk.CTkFrame(self, width=400, fg_color=COLORS["side_menu"])
        sidemenu.grid(row=0, column=1, sticky="nsew")
        sidemenu.grid_rowconfigure(0, weight=1)
        sidemenu.grid_rowconfigure(2, weight=1)

        button_frame = ctk.CTkFrame(sidemenu, fg_color="transparent")
        button_frame.grid(row=1, column=0)

        button_font = ("Arial", 18, "bold")

        btn_config = ctk.CTkButton(button_frame, text="⚙️ Configurações", fg_color=COLORS["accent"],
                                   hover_color=COLORS["button_hover"], corner_radius=27,
                                   font=button_font, height=50, width=230,
                                   command=lambda: controller.mostrar_tela(ConfigPage))
        btn_config.pack(pady=20, padx=10)

        btn_ajuda = ctk.CTkButton(button_frame, text="❓ Ajuda", fg_color=COLORS["accent"],
                                  hover_color=COLORS["button_hover"], corner_radius=27,
                                  font=button_font, height=50, width=230,
                                  command=lambda: PopupGif(self))
        btn_ajuda.pack(pady=20, padx=10)

        btn_libras = ctk.CTkButton(button_frame, text="🖐️ Libras", fg_color=COLORS["accent"],
                                   hover_color=COLORS["button_hover"], corner_radius=27,
                                   font=button_font, height=50, width=230,
                                   command=lambda: controller.mostrar_tela(NotificacaoPage))
        btn_libras.pack(pady=20, padx=10)

        btn_detector = ctk.CTkButton(button_frame, text="🎯 Detector", fg_color=COLORS["accent"],
                                     hover_color=COLORS["button_hover"], corner_radius=27,
                                     font=button_font, height=50, width=230,
                                     command=lambda: controller.mostrar_tela(DetectorPage))
        btn_detector.pack(pady=20, padx=10)

        logo_frame = ctk.CTkFrame(self, fg_color=COLORS["bg_primary"])
        logo_frame.grid(row=0, column=0, sticky="nsew")
        logo_frame.grid_rowconfigure(0, weight=0)
        logo_frame.grid_rowconfigure(1, weight=1)
        logo_frame.grid_columnconfigure(0, weight=1)

        titulo_label = ctk.CTkLabel(
            logo_frame,
            text="AURI",
            text_color="#005EB5",
            font=ctk.CTkFont(size=36, weight="bold")
        )
        titulo_label.grid(row=0, column=0, pady=(50, 20), sticky="n")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        LOGO_PATH = os.path.join(base_dir, "..", "assets", "LogoAuri.png")

        try:
            img = Image.open(LOGO_PATH)
            self.logo_img = CTkImage(light_image=img, dark_image=img, size=(355, 234))
            logo_label = ctk.CTkLabel(logo_frame, image=self.logo_img, text="")
            logo_label.grid(row=1, column=0, sticky="n")
        except Exception as e:
            print("Erro ao carregar a logo:", e)
            logo_label = ctk.CTkLabel(logo_frame, text="Logo não encontrada",
                                      text_color=COLORS["text_primary"],
                                      font=("Arial", 24))
            logo_label.grid(row=1, column=0, sticky="n")
