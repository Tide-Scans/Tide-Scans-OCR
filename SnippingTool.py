import tkinter as tk
from PIL import ImageGrab
from screeninfo import get_monitors

class SnippingTool:
    def __init__(self, master):
        self.master = master
        self.master.attributes("-alpha", 0.3)
        self.master.attributes("-topmost", True)
        self.master.overrideredirect(True)  # Remove window decorations (title bar, borders)
        self.screen_width, self.screen_height = self.get_screen_resolution()
        self.canvas = tk.Canvas(master, bg="black", width=self.screen_width, height=self.screen_height)
        self.canvas.pack()
        self.rect = None
        self.start_x = self.start_y = self.end_x = self.end_y = 0
        self.master.bind("<ButtonPress-1>", self.on_button_press)
        self.master.bind("<B1-Motion>", self.on_motion)
        self.master.bind("<ButtonRelease-1>", self.on_button_release)
        self.master.bind("<Escape>", self.cancel_snip)

    def get_screen_resolution(self):
        monitor = get_monitors()[0]  # Assuming the first monitor is the primary one
        return monitor.width, monitor.height

    def on_button_press(self, event):
        self.end_x, self.end_y = event.x, event.y
        self.start_x, self.start_y = event.x, event.y
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    def on_motion(self, event):
        self.end_x, self.end_y = event.x, event.y
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_button_release(self, event):
        self.master.withdraw()
        x1 = min(self.start_x, self.end_x)
        y1 = min(self.start_y, self.end_y)
        x2 = max(self.start_x, self.end_x)
        y2 = max(self.start_y, self.end_y)
        self.screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        self.master.quit()

    def cancel_snip(self, event):
        self.master.withdraw()
        self.master.quit()

def getImage():
    root = tk.Tk()
    app = SnippingTool(root)
    root.mainloop()
    try:
        return app.screenshot
    except:
        return None

def getAndShowImage():
    image = getImage()
    image.show()
    return image