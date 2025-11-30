import tkinter as tk
import random

def generate_numbers(n: int):
    return [random.randint(1, 50) for _ in range(n)]

def count_frequencies(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq

def find_modes(freq):
    if not freq:
        return [], 0
    max_count = max(freq.values())
    modes = [num for num, c in freq.items() if c == max_count]
    return modes, max_count

def draw_chart(canvas, freq, modes):
    canvas.delete("all")
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    left_pad, right_pad, bottom_pad, top_pad = 40, 20, 40, 20
    plot_w = w - left_pad - right_pad
    plot_h = h - top_pad - bottom_pad

    max_val = max(freq.values()) if freq else 1
    bar_w = plot_w / 50

    # Axes
    canvas.create_line(left_pad, h - bottom_pad, w - right_pad, h - bottom_pad)  # X-axis
    canvas.create_line(left_pad, h - bottom_pad, left_pad, top_pad)  # Y-axis

    for i in range(1, 51):
        val = freq.get(i, 0)
        x0 = left_pad + (i - 1) * bar_w
        y0 = h - bottom_pad - (val / max_val) * plot_h
        x1 = x0 + bar_w - 2
        y1 = h - bottom_pad
        color = "red" if i in modes else "blue"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        if bar_w > 10:
            canvas.create_text(x0 + bar_w/2, h - bottom_pad + 10, text=str(i), font=("Arial", 7))

def on_generate(entry, label_modes, label_count, canvas):
    try:
        n = int(entry.get())
        if n < 1:
            label_modes.config(text="Enter N ≥ 1")
            label_count.config(text="")
            canvas.delete("all")
            return
    except ValueError:
        label_modes.config(text="Enter a valid integer!")
        label_count.config(text="")
        canvas.delete("all")
        return

    numbers = generate_numbers(n)
    freq = count_frequencies(numbers)
    modes, max_count = find_modes(freq)

    if not modes:
        label_modes.config(text="Modes: —")
        label_count.config(text="Occurrences: —")
        canvas.delete("all")
        return

    label_modes.config(text=f"Modes: {', '.join(map(str, sorted(modes)))}")
    label_count.config(text=f"Occurrences (each): {max_count}")
    draw_chart(canvas, freq, modes)

def main():
    root = tk.Tk()
    root.title("Mode Finder")

    tk.Label(root, text="Enter N:").pack()
    entry = tk.Entry(root)
    entry.pack()

    label_modes = tk.Label(root, text="Modes: —")
    label_modes.pack()
    label_count = tk.Label(root, text="Occurrences: —")
    label_count.pack()

    canvas = tk.Canvas(root, width=800, height=400, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    tk.Button(root, text="Generate",
              command=lambda: on_generate(entry, label_modes, label_count, canvas)).pack()

    root.mainloop()

if __name__ == "__main__":
    main()