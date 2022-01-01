import tkinter as tk
import requests

window = tk.Tk()
window.geometry("900x550")
window.title("ASCII ART DOWNLOADER")
window.grid_columnconfigure(0, weight = 1)
window.configure(background = "black")

def download_ascii():
	if text_input.get():
		user_input = text_input.get()
		payload = {"text": user_input}
		response = requests.get("http://artii.herokuapp.com/make", params = payload)
		text_response = response.text
	else:
		text_response = "metti una parola altrimenti non posso fare nulla"

	textwidget = tk.Text()
	textwidget.insert(tk.END, text_response)
	textwidget.grid(row = 3, column = 0, sticky = "WE", padx = 10)

	credit_label = tk.Label(window, text = "ascii art by artii.herokuapp.com")
	credit_label.grid(row = 4, column = 0, sticky = "S", pady = 10)

welcome_label = tk.Label(window, text = "welcome! Aggiungi una parola o una frase:",  font = ("Hervetica", 15))
welcome_label.grid(row = 0, column = 0, sticky = "N", padx = 20, pady = 10 )
welcome_label.configure(background = "gray")

text_input = tk.Entry()
text_input.grid(row = 1, column = 0, sticky = "WE", padx = 10)

download_button = tk.Button(text = "download ascii art", command = download_ascii)
download_button.grid(row = 2, column = 0, sticky = "WE", pady = 10, padx = 10)
download_button.configure(background = "gray")

if __name__ == "__main__":
	window.mainloop()