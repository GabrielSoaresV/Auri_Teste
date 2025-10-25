import customtkinter as ctk
from theme.colors import COLORS

class NotificacaoPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=COLORS["bg_primary"])
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=1, column=0)

        label = ctk.CTkLabel(button_frame, text="Notificações 🔔", text_color=COLORS["text_primary"], font=("Arial", 24, "bold"))
        label.pack(pady=(0, 20))

        btn_voltar = ctk.CTkButton(button_frame, text="Voltar", fg_color=COLORS["accent"],
                                   hover_color=COLORS["button_hover"], height=50, width=250,
                                   command=lambda: controller.mostrar_tela(list(controller.frames.keys())[0]))
        btn_voltar.pack(pady=10)
