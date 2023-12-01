from tkinter import *

root = Tk()
def shifr():
    text1 = LoginInput.get()
    text = list(text1)
    key = int(keyInput.get())
    result_list = []
    part = ""
    completed = ""
    second_key = key
    a = 0
    while a <= key + 1:
        for i in range(key - 1, len(text), second_key):
            part += text[i]
        result_list.append(part)
        key = key - 1
        part = ""
        a += 1
    for i in result_list:
        completed += str(i)
    info = completed
    result_label.config(text=info)


root['bg'] = 'white'
root.title('Шифрування')
root.wm_attributes('-alpha', 1)
root.geometry('600x550')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=600, width=550)
canvas.pack()

frame = Frame(root, bg='#C0C0C0')
frame.place(relwidth=0.7, relheight=0.7,
            relx=0.15, rely=0.15)
title = Label(frame, text='розшифруй', bg='gray', font=40)
title.pack()





btn = Button(frame, text='button', bg='#808080', font=30, command=shifr)
btn.pack()

LoginInput = Entry(frame, bg='#83CCF3')
LoginInput.pack()

keyInput = Entry(frame, bg='#83CCF3')
keyInput.pack()

result_label = Label(frame, bg='#83CCF3',)
#result_label.place(relwidth=1.2, relheight=1.2, relx=0.45, rely=0.45)
result_label.pack()


root.mainloop()