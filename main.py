from tkinter import *
from deep_translator import GoogleTranslator

def translate_text():
    try:
        text = input_text.get("1.0", END).strip()

        translated = GoogleTranslator(
            source='auto',
            target=target_lang.get()
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {e}")

root = Tk()
root.title("Language Translator")
root.geometry("700x500")

Label(root, text="Enter Text", font=("Arial", 12)).pack()

input_text = Text(root, height=8, width=70)
input_text.pack(pady=5)

Label(root, text="Target Language Code").pack()

target_lang = Entry(root)
target_lang.insert(0, "ur")
target_lang.pack()

Button(
    root,
    text="Translate",
    command=translate_text
).pack(pady=10)

Label(root, text="Translated Text").pack()

output_text = Text(root, height=8, width=70)
output_text.pack(pady=5)

root.mainloop()
