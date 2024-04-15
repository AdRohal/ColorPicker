import tkinter as tk
from tkinter import colorchooser, messagebox

class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker")

        # Calculate screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Set window size and position
        window_width = 400
        window_height = 300
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.color_label = tk.Label(root, text="Selected Color", font=("Arial", 12))
        self.color_label.pack(pady=10)

        self.hex_label = tk.Label(root, text="Hex Value:", font=("Arial", 12))
        self.hex_label.pack(pady=5)

        self.hex_display = tk.Label(root, text="", font=("Arial", 12))
        self.hex_display.pack(pady=5)

        self.rgb_label = tk.Label(root, text="RGB Value:", font=("Arial", 12))
        self.rgb_label.pack(pady=5)

        self.rgb_display = tk.Label(root, text="", font=("Arial", 12))
        self.rgb_display.pack(pady=5)

        self.pick_color_button = tk.Button(root, text="Pick Color", command=self.pick_color)
        self.pick_color_button.pack(pady=10)

        self.copy_hex_button = tk.Button(root, text="Copy Hex", command=self.copy_hex_color)
        self.copy_hex_button.pack(pady=5)

        self.copy_rgb_button = tk.Button(root, text="Copy RGB", command=self.copy_rgb_color)
        self.copy_rgb_button.pack(pady=5)

    def pick_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color[0]:
            self.hex_display.config(text=f"Hex Value: {color[1]}", bg=color[1], fg=self.get_text_color(color[1]))
            self.rgb_display.config(text=f"RGB Value: {color[0][0]:.0f}, {color[0][1]:.0f}, {color[0][2]:.0f}", bg=color[1], fg=self.get_text_color(color[1]))

    def copy_hex_color(self):
        color = self.hex_display.cget("text").split(": ")[1]
        if color:
            self.root.clipboard_clear()
            self.root.clipboard_append(color)
            messagebox.showinfo("Copy Success", f"Hex value '{color}' copied to clipboard!")

    def copy_rgb_color(self):
        rgb = self.rgb_display.cget("text").split(": ")[1]
        if rgb:
            self.root.clipboard_clear()
            self.root.clipboard_append(rgb)
            messagebox.showinfo("Copy Success", f"RGB value '{rgb}' copied to clipboard!")

    def get_text_color(self, color):
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        Y = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return "#FFFFFF" if Y < 0.5 else "#000000"

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
