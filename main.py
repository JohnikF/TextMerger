import tkinter

window = tkinter.Tk()
window.title("Bla Bla Bla")
window.geometry("800x400")
window.configure(bg="silver")

def merge_format():
    text1 = text_num1.get()
    text2 = text_num2.get()
    text3 = text_num3.get()
    merged_text = f"{text1}, {text2}, {text3}"
    print(merged_text)
    label_1["text"] = "Text successfully merged!"

text_num1 = tkinter.Entry(window, width=20, bg="black", fg="gold")
text_num1.place(x=100, y=40)

text_num2 = tkinter.Entry(window, width=20, bg="black", fg="gold")
text_num2.place(x=325, y=40)

text_num3 = tkinter.Entry(window, width=20, bg="black", fg="gold")
text_num3.place(x=525, y=40)

button_merge_and_format = tkinter.Button(window, text="Merge And Format", command=merge_format, width= 20, height= 2, bg="gold")
button_merge_and_format.place(x=325, y=110)

label_1 = tkinter.Label(window, text="", bg="black", fg="gold", width= 20, height= 2)
label_1.place(x=325, y=180)

window.mainloop()