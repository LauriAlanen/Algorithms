import tkinter as tk
import numpy
import random


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(0, 0)
        self.title("PathFinder")
        self.geometry("1002x1000")
        self.config(bg="#000080")

        self.colors = [
            "#F5F5F5",
            "#000000"
        ]

        self.CANVAS_X = 1000
        self.CANVAS_Y = 800
        self.canvas = tk.Canvas(self, width=self.CANVAS_X, height=self.CANVAS_Y)
        self.canvas.config(bg="#000000")
        self.canvas.place(x=0, y=200)

        self.generate_button = tk.Button(self, text="Generate", command=lambda: self.generate(10000))
        self.generate_button.place(x=0, y=0)

    def generate(self, block_count):
        self.counter = 0
        self.canvas.delete("all")
        for y in range(100):
            block_height = self.CANVAS_Y / (
                    block_count / 100)  # Change the division to 10 if the block count is < 10000
            y1 = y * block_height
            y2 = y1 + block_height

            for x in range(100):
                block_width = self.CANVAS_X / (
                        block_count / 100)  # Change the division to 10 if the block count is < 10000
                x1 = x * block_width
                x2 = x1 + block_width
                block_state = random.randrange(0, 2)
                self.counter += 1
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.colors[block_state])

                # print(f"Generated rectangle ({x1}, {y1}) ({x2}, {y2})")
        print(f"Generated {self.counter} rectangles.")


if __name__ == "__main__":
    Display = Window()
    Display.mainloop()
