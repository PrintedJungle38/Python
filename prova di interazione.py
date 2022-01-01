import tkinter as tk

window = tk.Tk()
window.geometry("300x300")
window.title("fantastico, ci sei ruscito")
window.resizable(False, False)
window.configure(background = "black")

def first_print():
	text = "ciao mondo"
	text_output = tk.Label(window, text=text, fg= "red", font =("helvetica", 16))
	text_output.grid(row = 0, column = 1)


first_button = tk.Button(text = "OMG!", command = first_print)
first_button.grid(row = 0, column = 0)


if __name__ == "__main__":
	window.mainloop()