import customtkinter as ctk
from theme.colors import COLORS
import csv, json
import os

class ConfigPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=COLORS["bg_primary"])
        self.controller = controller

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.assets_dir = os.path.join(base_dir, "assets")
        
        class_names = []
        cat_path = os.path.join(self.assets_dir, "yamnet_class_map.csv")
        if os.path.exists(self.config_path):
            with open(cat_path, "r", newline="", encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                next(reader)   # Skip header
                class_names = [display_name for (_, _, display_name) in reader]

        self.config_data = {}
        self.config_path = os.path.join(self.assets_dir, "config.json")
        if os.path.exists(self.config_path):
            with open("config.json", "r") as f:
                try:
                    self.config_data = json.load(f)
                except Exception:
                    self.config_data = {}

        label = ctk.CTkLabel(self, text="Configurações ⚙", text_color=COLORS["text_primary"], font=("Arial", 24, "bold"))
        label.grid(row=0, column=0, pady=(40, 20))

        btn_voltar = ctk.CTkButton(self, text="Voltar", fg_color=COLORS["accent"], hover_color=COLORS["button_hover"], command=lambda: controller.mostrar_tela(list(controller.frames.keys())[0]))
        btn_voltar.grid(row=1, column=0, pady=10)

        btn_salvar = ctk.CTkButton(self, text="Salvar", fg_color=COLORS["accent"], hover_color=COLORS["button_hover"], command=self.salvar_configs())
        btn_salvar.grid(row=1, column=1, pady=10)
        
        categories_checklist = ctk.CTkScrollableFrame(self, width=300, height=200)
        categories_checklist.grid(row=2, column=0, pady=20)

        self.category_vars = {}

        for i, category in enumerate(class_names):
            value = self.config_data.get(category, 0)
            checkbox_var = ctk.IntVar(value=value)
            self.category_vars[category] = checkbox_var
            checkbox = ctk.CTkCheckBox(categories_checklist, text=category, variable=self.category_vars[category], onvalue=1, offvalue=0, text_color=COLORS["text_primary"])
            checkbox.grid(row=i, column=0, sticky="w", padx=10, pady=2)


    def salvar_configs(self):
        config = {item: var.get() for item, var in self.checkbox_vars.items()}
        os.makedirs(self.assets_dir, exist_ok=True)
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)
        #app.destroy() Voltar para o home?