import customtkinter as ctk
from theme.colors import COLORS
import csv
import os

class ConfigPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=COLORS["bg_primary"])
        self.controller = controller

        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, '..', "assets", "yamnet_class_map.csv")
        with open(path, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)   # Skip header
            class_names = [display_name for (_, _, display_name) in reader]

        label = ctk.CTkLabel(self, text="Configurações ⚙", text_color=COLORS["text_primary"], font=("Arial", 24, "bold"))
        label.grid(row=0, column=0, pady=(40, 20))

        btn_voltar = ctk.CTkButton(self, text="Voltar", fg_color=COLORS["accent"], hover_color=COLORS["button_hover"], command=lambda: controller.mostrar_tela(list(controller.frames.keys())[0]))
        btn_voltar.grid(row=1, column=0, pady=10)
        
        categories_checklist = ctk.CTkScrollableFrame(self, width=300, height=200)
        categories_checklist.grid(row=2, column=0, pady=20)

        self.category_vars = {}

        for i, category in enumerate(class_names):
            self.category_vars[category] = ctk.BooleanVar(value=True)
            checkbox = ctk.CTkCheckBox(categories_checklist, text=category, variable=self.category_vars[category], text_color=COLORS["text_primary"])
            checkbox.grid(row=i, column=0, sticky="w", padx=10, pady=2)