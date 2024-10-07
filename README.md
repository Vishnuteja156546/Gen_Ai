# Gen_Ai
---

## **Project Overview:**

This Python project creates a **Language Translator** application with additional **text-to-speech (TTS)** and **speech-to-text (STT)** features. The app uses **Tkinter** to build the graphical user interface (GUI), **OpenAI GPT** for translating text between languages, and various libraries like **gTTS** and **SpeechRecognition** for audio conversion. 

The app allows users to input text, translate it between different languages, and also convert that text to speech. Additionally, users can provide audio input and convert it to text for translation.

---

### **Components and Their Functionalities:**

### 1. **Core Libraries:**

- **tkinter**: Used to create the GUI.
- **ttk**: Provides enhanced widgets for dropdowns and buttons.
- **openai**: Used to access the OpenAI GPT model for language translation.
- **gTTS (Google Text-to-Speech)**: Converts text into audio.
- **SpeechRecognition**: Converts speech to text.

--- 

### 2. **Language Translation Logic:**

The main functionality for language translation is handled by the `translate_text()` function. 

**Steps:**

- **User Input**: The user inputs text to be translated into the `Text` widget. 
- **Language Selection**: Users can choose a source language (e.g., English) and a target language (e.g., Hindi) using `Combobox` widgets.
- **Translation Request**: A prompt is generated and sent to the OpenAI API, which responds with the translated text. This response is then displayed in the output text box.

```python
prompt = f"Translate this text from {src_lang} to {dest_lang}: {source_text}"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
translated_text = response.choices[0].message['content'].strip()
```

--- 

### 3. **Speech-to-Text (STT) Functionality:**

The speech-to-text functionality allows the user to input spoken language, which is converted to text. The **SpeechRecognition** library is used for this.

**Key Steps:**

- **Speech Input**: Using the system’s microphone, the user speaks, and the `recognize_google()` method converts the audio to text.
  
```python
with sr.Microphone() as source:
    audio_data = recognizer.listen(source)
    text = recognizer.recognize_google(audio_data)
```

The recognized text is placed into the input text box for translation.

---

### 4. **Text-to-Speech (TTS) Functionality:**

After translation, users can convert the translated text to speech using the **gTTS** library.

**Key Steps:**

- **Generate Speech**: The translated text is passed to the `gTTS` function, which converts it to audio.
  
```python
tts = gTTS(translated_text, lang=target_lang_code)
tts.save("translated_audio.mp3")
```

- **Play Audio**: The `playsound` library is used to play the generated audio file.

```python
playsound("translated_audio.mp3")
```

---

### 5. **Graphical User Interface (GUI):**

The GUI is built using the **Tkinter** library.

- **Input Area**: A `Text` widget where users can type the text they want to translate.
- **Source and Target Languages**: Two `Combobox` widgets allow users to choose the source and target languages.
- **Translate Button**: When clicked, it calls the translation logic and displays the result.
- **Output Area**: Displays the translated text.
- **Speech-to-Text Button**: Activates the microphone to capture speech and convert it to text.
- **Text-to-Speech Button**: Converts the translated text to audio and plays it.

---

### **Conclusion:**

This project demonstrates a powerful and user-friendly tool for language translation combined with audio input/output capabilities. Users can translate text between multiple languages, convert speech to text for translation, and listen to the translated text using text-to-speech conversion. The application uses OpenAI's GPT model for text translation and integrates Python libraries for audio functionalities.

--- 
