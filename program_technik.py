import tkinter as tk
import random

def generate_numbers(n: int):

    return [random.randint(1, 50) for _ in range(n)]

def count_frequencies(numbers):

    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq

def find_mode(freq):

    mode = max(freq, key=freq.get)
    count = freq[mode]
    return mode, count

def draw_chart(canvas, freq, mode):

    canvas.delete("all")
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    left_pad, right_pad, bottom_pad, top_pad = 40, 20, 40, 20
    plot_w = w - left_pad - right_pad
    plot_h = h - top_pad - bottom_pad

    max_val = max(freq.values())
    bar_w = plot_w / 50

    for i in range(1, 51):
        val = freq.get(i, 0)
        x0 = left_pad + (i - 1) * bar_w
        y0 = h - bottom_pad - (val / max_val) * plot_h
        x1 = x0 + bar_w - 2
        y1 = h - bottom_pad
        color = "red" if i == mode else "blue"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        if bar_w > 10:
            canvas.create_text(x0 + bar_w/2, h - bottom_pad + 10, text=str(i), font=("Arial", 7))

def on_generate(entry, label_mode, label_count, canvas):

    try:
        n = int(entry.get())
    except ValueError:
        label_mode.config(text="Enter a valid integer!")
        label_count.config(text="")
        return

    numbers = generate_numbers(n)
    freq = count_frequencies(numbers)
    mode, count = find_mode(freq)

    label_mode.config(text=f"Mode: {mode}")
    label_count.config(text=f"Occurrences: {count}")
    draw_chart(canvas, freq, mode)

def main():
    root = tk.Tk()
    root.title("Mode Finder")

    tk.Label(root, text="Enter N:").pack()
    entry = tk.Entry(root)
    entry.pack()

    label_mode = tk.Label(root, text="Mode: —")
    label_mode.pack()
    label_count = tk.Label(root, text="Occurrences: —")
    label_count.pack()

    canvas = tk.Canvas(root, width=800, height=400, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    tk.Button(root, text="Generate", command=lambda: on_generate(entry, label_mode, label_count, canvas)).pack()

    root.mainloop()

if __name__ == "__main__":
    main()

