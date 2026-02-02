import customtkinter as ctk
from theme.colors import COLORS


class ConfigPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=COLORS["bg_primary"])
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)

        # ===== TÍTULO =====
        title = ctk.CTkLabel(
            self,
            text="CONFIGURAÇÕES",
            font=("Arial", 28, "bold"),
            text_color=COLORS["text_primary"]
        )
        title.grid(row=0, column=0, pady=(30, 10))

        # ===== TEXTO EXPLICATIVO =====
        description = ctk.CTkLabel(
            self,
            text=(
                "Texto explicando sobre as configurações...\n"
                "talvez mais texto"
            ),
            font=("Arial", 14),
            text_color=COLORS["text_secondary"],
            justify="center"
        )
        description.grid(row=1, column=0, pady=(0, 30))

        # ===== CATEGORIAS =====
        cat_label = ctk.CTkLabel(
            self,
            text="SELECIONAR CATEGORIAS:",
            font=("Arial", 14, "bold"),
            text_color=COLORS["text_primary"]
        )
        cat_label.grid(row=2, column=0, sticky="w", padx=80, pady=(0, 10))

        categories_frame = ctk.CTkFrame(self, fg_color="transparent")
        categories_frame.grid(row=3, column=0, padx=80, sticky="w")

        categories = [
            "Campainha",
            "Explosão",
            "Campanha",
            "Outro",
            "Outro 2"
        ]

        for i, cat in enumerate(categories):
            btn = ctk.CTkButton(
                categories_frame,
                text=cat,
                fg_color=COLORS["text_primary"],
                hover_color=COLORS["text_primary"],
                text_color=COLORS["text_primary"],
                width=120,
                height=36
            )
            btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)

        # ===== CHECKBOX =====
        self.notify_var = ctk.BooleanVar(value=True)
        notify_check = ctk.CTkCheckBox(
            self,
            text="Ativar notificações",
            variable=self.notify_var,
            text_color=COLORS["text_primary"]
        )
        notify_check.grid(row=4, column=0, sticky="w", padx=80, pady=(30, 40))

        # ===== BOTÕES =====
        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.grid(row=5, column=0, pady=(0, 30))

        btn_save = ctk.CTkButton(
            actions,
            text="SALVAR",
            width=160,
            height=40,
            fg_color=COLORS["accent"],
            hover_color=COLORS["button_hover"]
        )
        btn_save.grid(row=0, column=0, padx=15)

        btn_back = ctk.CTkButton(
            actions,
            text="VOLTAR",
            width=160,
            height=40,
            fg_color=COLORS["bg_secondary"],
            text_color=COLORS["text_primary"],
            hover_color=COLORS["bg_secondary"],
            command=lambda: controller.mostrar_tela(list(controller.frames.keys())[0])
        )
        btn_back.grid(row=0, column=1, padx=15)
