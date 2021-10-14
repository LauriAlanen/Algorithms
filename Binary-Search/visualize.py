import tkinter as tk
from time import sleep


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x465")
        self.resizable(False, False)
        self.title("Binary Search Algorithm")
        self.int_list = [i for i in range(96)]
        self.target = 87
        self.create_button = tk.Button(self, text="Start Visualization", width=240, height=15,
                                       command=self.activate_binary_search)
        self.create_button.place(x=0, y=0)

        self.pillars = []
        for i in range(96):
            pillar = tk.Label(self, text=f"{self.int_list[i]}", bg="grey", height=15, width=2, font=("Arial", 10),
                              borderwidth=2,
                              relief="solid")
            pillar.place(x=20 * i, y=220)
            self.pillars.append(pillar)

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
            self.pillars[mid_val].config(bg="blue")
            self.update()
            sleep(0.5)


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
