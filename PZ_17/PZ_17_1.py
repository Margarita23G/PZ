import tkinter as tk


def minimal_product():
    input_str = entry.get()
    a = input_str.split(' ')

    sg = []
    sm = []

    for i in range(1, 6):
        sg.append(int(a[i]))

    for j in range(7, len(a)):
        sm.append(int(a[j]))

    slg = {a[0]: sg}
    slm = {a[6]: sm}

    result_text.insert(tk.END, f"Минимальная продажа груш составляет: {min(slg['груши'])} кг\n")
    result_text.insert(tk.END, f"Минимальная продажа моркови составляет: {min(slm['морковь'])} кг\n")


root = tk.Tk()
root.title("Минимальные продажи")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_label = tk.Label(frame, text="Введите строку:")
entry_label.grid(row=0, column=0)

entry = tk.Entry(frame, width=50)
entry.grid(row=0, column=1)

button = tk.Button(frame, text="Найти минимальные продажи", command=minimal_product)
button.grid(row=1, columnspan=2, pady=(5, 0))

result_text = tk.Text(root, width=50, height=5)
result_text.pack(pady=(10, 0))

root.mainloop()
