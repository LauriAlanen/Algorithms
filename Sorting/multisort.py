import random
import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.options = ["Bubble Sort",
                        "Insertion Sort",
                        "Selection Sort",
                        "Heap Sort"]


        self.resizable(0, 0)
        self.canvas = tk.Canvas(self, width=1500, height=800)

        self.var = tk.StringVar(self)
        self.var.set(self.options[0])
        self.choice = tk.OptionMenu(self, self.var, *self.options)
        self.choice.config(width=10)
        self.choice.place(x=0, y=0)

        self.activation_btn = tk.Button(self, text="Activate Sort", command=self.sorting_method)
        self.activation_btn.place(x=105, y=2)
        self.reset_btn = tk.Button(self, text="Reset", command=self.draw)
        self.reset_btn.place(x=185, y=2)
        self.draw()

    def sorting_method(self):
        choice = self.var.get()
        if choice == "Bubble Sort":
            self.bubble_sort(self.height)
        if choice == "Insertion Sort":
            self.insertion_sort(self.height)
        if choice == "Selection Sort":
            self.selection_sort(self.height)
        elif choice == "Heap Sort":
            self.heap_sort(self.height)

    def draw(self):
        self.height = [random.randrange(250, 750) for i in range(334)]
        self.canvas.delete("all")
        for i in range(len(self.height)):
            x1 = (i * 4.5) - 2.5
            x2 = i * 4.5
            self.canvas.create_rectangle(x1, 800, x2, self.height[i], fill="#0000FF")
            self.canvas.grid(column=0, row=3, sticky=tk.SW, padx=1)
        return self.height

    def update_draw(self, array):
        self.canvas.delete("all")
        for i in range(len(array)):
            x1 = (i * 4.5) - 2.5
            x2 = i * 4.5
            self.canvas.create_rectangle(x1, 800, x2, array[i], fill="#0000FF")
            self.canvas.grid(column=0, row=4, sticky=tk.SW, padx=1)
        self.update_idletasks()

    def bubble_sort(self, array):
        n = len(array)
        for i in range(n):
            already_sorted = True
            self.update_draw(array)
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    already_sorted = False

            if already_sorted:
                break

    def insertion_sort(self, array):
        for i in range(len(array)):
            key = array[i]
            var = i - 1
            while var >= 0 and array[var] > key:
                array[var + 1] = array[var]
                var -= 1
            array[var + 1] = key
            self.update_draw(array)

    def selection_sort(self, array):
        for i in range(len(array)):
            lowest_value_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[lowest_value_index]:
                    lowest_value_index = j
            array[i], array[lowest_value_index] = array[lowest_value_index], array[i]
            self.update_draw(array)

    def heapify(self, array, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and array[left_child] > array[largest]:
            largest = left_child

        if right_child < heap_size and array[right_child] > array[largest]:
            largest = right_child

        if largest != root_index:
            array[root_index], array[largest] = array[largest], array[root_index]
            self.heapify(array, heap_size, largest)

    def heap_sort(self, array):
        n = len(array)

        for i in range(n, -1, -1):
            self.heapify(array, n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
            self.update_draw(array)


if __name__ == "__main__":
    App = Window()
    App.mainloop()
