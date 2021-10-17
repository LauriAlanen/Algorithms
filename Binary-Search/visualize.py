import tkinter as tk
from time import sleep
from tkinter import messagebox


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x465")
        self.resizable(False, False)
        self.title("Binary Search Algorithm")

        self.int_list = [i for i in range(96)]
        self.target = 0
        self.pillars = []

        self.create_button = tk.Button(self, text="Start Visualization", width=240, height=15,
                                       command=self.button_func)
        self.create_button.place(x=0, y=0)

        self.interval_label = tk.Label(text="Interval in seconds (0.0)")
        self.interval_label.place(x=10, y=180)
        self.interval_entry = tk.Entry()
        self.interval_entry.place(x=0, y=200)

        self.target_label = tk.Label(text="Target number (0-95)")
        self.target_label.place(x=10, y=140)
        self.target_entry = tk.Entry()
        self.target_entry.place(x=0, y=160)

        self.target_entry.insert(0, 50)
        self.interval_entry.insert(0, 0.5)

        for i in range(96):
            pillar = tk.Label(self, text=f"{self.int_list[i]}", bg="grey", height=15, width=2, font=("Arial", 10),
                              borderwidth=2,
                              relief="solid")
            pillar.place(x=20 * i, y=220)
            self.pillars.append(pillar)

    def button_func(self):
        try:
            self.target = int(self.target_entry.get())
        except ValueError:
            messagebox.showerror("Value Error!", "Make sure the target value was between 0-95")


        if self.target < 0 or self.target > 95:
            messagebox.showerror("Value Error!", "Make sure the target value was between 0-95")
            return False

        elif float(self.interval_entry.get()) < 0.0000001 or float(self.interval_entry.get()) < 0.0000001 \
                or self.interval_entry.get() == "":
            messagebox.showerror("Value Error!", "Make sure the interval value was between 0.0000001s and 10s")
            return False

        for i in range(len(self.pillars)):
            self.pillars[i].config(bg="grey")

        self.activate_binary_search()

    def activate_binary_search(self):
        lower = 0
        upper = len(self.int_list) - 1

        if self.int_list[0] == self.target:
            self.pillars[0].config(bg="green")
            return print("Found it :)")

        elif self.int_list[-1] == self.target:
            self.pillars[-1].config(bg="green")
            return print("Found it :)")

        self.pillars[lower].config(bg="black")
        self.pillars[upper].config(bg="black")

        while lower <= upper:
            mid_val = (lower + upper) // 2
            self.pillars[mid_val].config(bg="red")
            sleep(float(self.interval_entry.get()))
            self.update()

            if self.int_list[mid_val] == self.target:
                self.pillars[mid_val].config(bg="green")
                return print("Found it :)")

            else:
                self.pillars[mid_val].config(bg="grey")
                if self.int_list[mid_val] < self.target:
                    self.pillars[lower].config(bg="grey")
                    lower = mid_val + 1
                    self.pillars[lower].config(bg="black")

                else:
                    self.pillars[upper].config(bg="grey")
                    upper = mid_val - 1
                    self.pillars[upper].config(bg="black")

        return print("Didn't find it :/")


if __name__ == "__main__":
    Display = MainWindow()
    Display.mainloop()
