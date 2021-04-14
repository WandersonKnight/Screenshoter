import os
import tkinter

# Compile -> pyinstaller --onefile --noconsole --icon=icon.png screenshot1.py

root = tkinter.Tk()
root.title("Screenshoter")
root.iconbitmap("icon.ico")
root.resizable(False, False)

goodbye = tkinter.Label(root, text="Concluido!", width = 49, font=("Arial", 10))
goodbye.grid(row=0, column=0)

bar = tkinter.Entry(root, width=56, borderwidth=1, font=("Arial", 10))
bar.grid(row=0, column=0)
bar.insert(0, "Digite o caminho do diretorio desejado")


main_file = open(os.path.join(os.path.dirname(__file__), "diretorio.txt"), 'w').close()

main_file = open(os.path.join(os.path.dirname(__file__), "diretorio.txt"), 'r+')


def user_input():
    
    main_file.write(bar.get().replace("\\", "/"))
    main_file.close()

    bar.destroy()
    enter_1.destroy()

def delete_now():

    bar.delete(0, "end")

bar.bind("<Return>", lambda event: user_input())
bar.bind("<Button-1>", lambda event: delete_now())

enter_1 = tkinter.Button(root, text="Ok", width=6, command=user_input)
enter_1.grid(row=0, column=1)

root.mainloop()