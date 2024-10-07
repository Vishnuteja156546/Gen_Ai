import tkinter as tk
from tkinter import ttk, messagebox
import openai

# Set your OpenAI API key here
openai.api_key =  "API key"
# Function to translate the text using OpenAI
def translate_text():
    try:
        source_text = input_text.get("1.0", tk.END).strip()
        if not source_text:
            messagebox.showerror("Input Error", "Please enter text to translate")
            return

        # Get the selected languages
        src_lang = src_lang_combo.get()
        dest_lang = dest_lang_combo.get()

        # Create the translation prompt
        prompt = f"Translate this text from {src_lang} to {dest_lang}: {source_text}"

        # Call OpenAI API for translation
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use your desired model
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract translated text from the response
        translated_text = response.choices[0].message['content'].strip()

        # Clear previous translation and insert the new one
        output_text.delete("1.0", tk.END)  # Clear previous translation
        output_text.insert(tk.END, translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x400")
root.config(bg="lightblue")

# Heading
title_label = tk.Label(root, text="Language Translator", font=("Arial", 18, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Input text area
input_label = tk.Label(root, text="Enter text:", font=("Arial", 12), bg="lightblue")
input_label.pack(pady=5)
input_text = tk.Text(root, height=5, width=40)
input_text.pack(pady=5)

# Source language
src_lang_label = tk.Label(root, text="Source Language:", font=("Arial", 12), bg="lightblue")
src_lang_label.pack(pady=5)
src_lang_combo = ttk.Combobox(root, values=["English", "Hindi", "Kannada", "Tamil"], state="readonly")
src_lang_combo.set("English")  # Default source language
src_lang_combo.pack(pady=5)

# Destination language
dest_lang_label = tk.Label(root, text="Target Language:", font=("Arial", 12), bg="lightblue")
dest_lang_label.pack(pady=5)
dest_lang_combo = ttk.Combobox(root, values=["Hindi", "Telugu", "Tamil", "Kannada","Germany","French"], state="readonly")
dest_lang_combo.set("Hindi")  # Default target language
dest_lang_combo.pack(pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", font=("Arial", 12, "bold"), command=translate_text)
translate_button.pack(pady=10)

# Output text area
output_label = tk.Label(root, text="Translated text:", font=("Arial", 12), bg="lightblue")
output_label.pack(pady=5)
output_text = tk.Text(root, height=5, width=40)
output_text.pack(pady=5)

# Run the application
root.mainloop()