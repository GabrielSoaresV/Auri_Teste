import customtkinter as ctk
from theme.colors import COLORS
from interfaces.popup_gif import PopupGif


class DetectorPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=COLORS["bg_primary"])
        self.controller = controller

        title = ctk.CTkLabel(self, text="Detector de Som", text_color=COLORS["text_primary"], font=("Arial", 24, "bold"))
        title.grid(row=0, column=0, pady=(40, 20))

        btn_alerta = ctk.CTkButton(self, text="Mostrar Alerta (GIF)", fg_color=COLORS["accent"],
                                   hover_color=COLORS["button_hover"], command=self.mostrar_alerta)
        btn_alerta.grid(row=1, column=0, pady=10)

        btn_voltar = ctk.CTkButton(self, text="Voltar", fg_color=COLORS["accent"],
                                   hover_color=COLORS["button_hover"], command=lambda: controller.mostrar_tela(list(controller.frames.keys())[0]))
        btn_voltar.grid(row=2, column=0, pady=10)

    def mostrar_alerta(self):
        PopupGif(self)
