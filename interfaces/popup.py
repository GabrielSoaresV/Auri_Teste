import os
import customtkinter as ctk
from theme.colors import COLORS
from PIL import Image, ImageSequence, ImageTk, UnidentifiedImageError

class PopupGif(ctk.CTkToplevel):
    def _init_(self, master):
        super()._init_(master)
        self.title("Alerta!")
        self.geometry("600x400")
        self.configure(fg_color="black")
        self.attributes("-topmost", True)

        self.label = ctk.CTkLabel(self, text="")
        self.label.pack(expand=True)

        self._frames = []
        self._frame_index = 0
        self._loops_done = 0
        self._max_loops = 3

        base_dir = os.path.dirname(__file__)
        gif_path = os.path.abspath(os.path.join(base_dir, "..", "assets", "alerta.gif"))

        try:
            gif = Image.open(gif_path)
        except (FileNotFoundError, UnidentifiedImageError, OSError):
            self.label.configure(text="Alerta (GIF) não disponível", fg_color=COLORS.get("bg_primary", "#000"))
            self.after(2000, self.destroy)
            return

        try:
            for frame in ImageSequence.Iterator(gif):
                img = frame.convert("RGBA")
                photo = ImageTk.PhotoImage(img)
                self._frames.append(photo)
        except Exception:
            self.label.configure(text="Erro ao processar GIF")
            self.after(2000, self.destroy)
            return

        self._play_next_frame()

    def _play_next_frame(self):
        if not self._frames:
            self.destroy()
            return

        frame = self._frames[self._frame_index]
        try:
            self.label.configure(image=frame, text="")
            self.label.image = frame
        except Exception:
            self.destroy()
            return

        self._frame_index += 1
        if self._frame_index >= len(self._frames):
            self._frame_index = 0
            self._loops_done += 1
            if self._loops_done >= self._max_loops:
                self.destroy()
                return

        self.after(70, self._play_next_frame)