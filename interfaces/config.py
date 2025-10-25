import customtkinter as ctk
from theme.colors import COLORS

class ConfigPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=COLORS["bg_primary"])
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(self, text="Configurações ⚙️", text_color=COLORS["text_primary"], font=("Arial", 24, "bold"))
        label.grid(row=0, column=0, pady=(40, 20), padx=20, sticky="n")

        btn_voltar = ctk.CTkButton(self, text="Voltar", fg_color=COLORS["accent"],
                                   hover_color=COLORS["button_hover"],
                                   command=lambda: controller.mostrar_tela(list(controller.frames.keys())[0]))
        btn_voltar.grid(row=1, column=0, pady=10)
