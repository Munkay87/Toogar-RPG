import tkinter
import sys

from main import start_game

class TextRedirector:
    def __init__(self, text_box):
        self.text_box = text_box
        self.current_text = ""


    def write(self, message):

            self.text_box.config(state="normal")
            self.text_box.insert("end", message)
            self.text_box.config(state="disabled")
            self.text_box.see("end")

    def write_tagged(self, message,tag):
        self.text_box.config(state="normal")
        self.text_box.insert("end", message, tag)
        self.text_box.config(state="disabled")
        self.text_box.see("end")

    def flush(self):
        pass

    def clear(self):
        self.text_box.config(state="normal")
        self.text_box.delete("1.0", "end")
        self.text_box.config(state="disabled")

class InputRedirector:
    def __init__(self, input_box):
        self.input_box = input_box
        self.result = None
        self.input_ready = tkinter.BooleanVar(value=False)        

    def get_input(self):
        self.result = None
        self.input_ready.set(False)
        self.input_box.focus()
        self.input_box.wait_variable(self.input_ready)
        return self.result

def submit_input(event):
    input_handler.result = input_box.get()
    input_box.delete(0, "end")
    input_handler.input_ready.set(True)

def game_input(prompt):
    print(prompt, end="")
    return input_handler.get_input()

def game_heading(text):
    output.write_tagged(text + "\n", "heading")

window = tkinter.Tk()

window.title("Toogar RPG")
window.geometry("800x600")
window.minsize(500, 400)

text_box = tkinter.Text(
    window,
    state="disabled",
    font=("Consolas", 12)
    )

text_box.tag_configure(
    "heading",
    font=("Consolas", 16, "bold")
)

command_frame = tkinter.Frame(window)
command_frame.pack(
    side="bottom",
    fill="x",
    padx=10,
    pady=5
    )

input_label = tkinter.Label(
    command_frame,
    text="Enter your command:"
)
input_label.pack(anchor="w")

input_box = tkinter.Entry(
    command_frame,
    font=("Consolas", 12),
    relief="solid",
    bd=1
    )
input_box.pack(fill="x")

text_box.pack(fill="both", expand=True)

input_handler = InputRedirector(input_box)

input_box.bind("<Return>", submit_input)
output = TextRedirector(text_box)
sys.stdout = output

start_game(game_input, output.clear, game_heading)

window.mainloop()

