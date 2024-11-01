import tkinter as tk

# Function to update the input field when buttons are clicked
def click(button_text):
    current_text = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current_text + button_text)

# Function to evaluate the expression and display the result
def evaluate():
    try:
        expression = input_field.get()
        result = str(eval(expression))  # Evaluate the expression entered by the user
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, result)
    except:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error")

# Function to clear the input field
def clear():
    input_field.delete(0, tk.END)

# Initialize the main application window
app = tk.Tk()
app.title("Calculator")

# Input field where expressions will be entered
input_field = tk.Entry(app, width=30, borderwidth=5, font=('Arial', 16))
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons for numbers and operators
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(app, text=text, width=10, height=3, command=evaluate)
    else:
        button = tk.Button(app, text=text, width=10, height=3, command=lambda t=text: click(t))
    button.grid(row=row, column=col)

# Create 'Clear' button
clear_button = tk.Button(app, text='C', width=10, height=3, command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the application
app.mainloop()
import tkinter as tk

# Function to update the input field when buttons are clicked
def click(button_text):
    current_text = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current_text + button_text)

# Function to evaluate the expression and display the result
def evaluate():
    try:
        expression = input_field.get()
        result = str(eval(expression))  # Evaluate the expression entered by the user
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, result)
    except:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error")

# Function to clear the input field
def clear():
    input_field.delete(0, tk.END)

# Initialize the main application window
app = tk.Tk()
app.title("Calculator")

# Input field where expressions will be entered
input_field = tk.Entry(app, width=30, borderwidth=5, font=('Arial', 16))
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons for numbers and operators
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(app, text=text, width=10, height=3, command=evaluate)
    else:
        button = tk.Button(app, text=text, width=10, height=3, command=lambda t=text: click(t))
    button.grid(row=row, column=col)

# Create 'Clear' button
clear_button = tk.Button(app, text='C', width=10, height=3, command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the application
app.mainloop()
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from playsound import playsound
import nltk
from nltk import word_tokenize
import re

# Ensure that the necessary NLTK data packages are downloaded
nltk.download('punkt')

# Function to update the input field when buttons are clicked
def click(button_text):
    playsound("click_sound.mp3")  # Add sound on button press
    current_text = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current_text + button_text)

# Function to evaluate the expression and display the result
def evaluate():
    try:
        expression = input_field.get()
        result = str(eval(expression))  # Evaluate the expression entered by the user
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, result)
        # Store the expression for future predictions
        past_expressions.append(expression)
    except Exception as e:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error")
        messagebox.showerror("Calculation Error", "Invalid input!")

# Function to clear the input field
def clear():
    input_field.delete(0, tk.END)

# Function to take voice input from the user
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            messagebox.showinfo("Voice Input", "Please speak your calculation...")
            audio = recognizer.listen(source)
            speech_text = recognizer.recognize_google(audio)
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, speech_text)
        except sr.UnknownValueError:
            messagebox.showerror("Voice Recognition Error", "Sorry, I did not understand the speech!")
        except sr.RequestError:
            messagebox.showerror("Voice Recognition Error", "Could not request results from the speech recognition service!")

# Function to handle natural language input
def natural_language_input():
    input_text = input_field.get()
    tokens = word_tokenize(input_text.lower())

    # Simple pattern matching for basic arithmetic operations in natural language
    if "add" in tokens or "sum" in tokens or "plus" in tokens:
        numbers = extract_numbers(tokens)
        if numbers:
            result = sum(numbers)
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, result)
    elif "subtract" in tokens or "minus" in tokens:
        numbers = extract_numbers(tokens)
        if numbers and len(numbers) == 2:
            result = numbers[0] - numbers[1]
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, result)
    elif "multiply" in tokens or "times" in tokens:
        numbers = extract_numbers(tokens)
        if numbers:
            result = numbers[0] * numbers[1]
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, result)
    elif "divide" in tokens:
        numbers = extract_numbers(tokens)
        if numbers and len(numbers) == 2:
            result = numbers[0] / numbers[1]
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, result)
    else:
        messagebox.showinfo("NLP Error", "Sorry, I can't understand the input.")

# Function to extract numbers from the tokenized input
def extract_numbers(tokens):
    numbers = []
    for token in tokens:
        try:
            number = float(re.sub("[^0-9.-]", "", token))
            numbers.append(number)
        except ValueError:
            continue
    return numbers

# Function to analyze and predict based on past inputs
def ai_prediction():
    if past_expressions:
        messagebox.showinfo("AI Prediction", f"Last calculation was: {past_expressions[-1]}")
    else:
        messagebox.showinfo("AI Prediction", "No previous calculations available.")

# Initialize the main application window
app = tk.Tk()
app.title("AI Enhanced Calculator")
app.geometry("400x600")
app.config(bg="#2d2d2d")  # Change background color for better aesthetics

# Input field where expressions will be entered
input_field = tk.Entry(app, width=25, borderwidth=5, font=('Arial', 20), bg="#f4f4f4")
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# List to store past expressions for AI predictions
past_expressions = []

# Button layout with improved visuals
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons for numbers and operators with improved visuals
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(app, text=text, width=10, height=3, bg="#40c057", fg="white", font=('Arial', 14), command=evaluate)
    else:
        button = tk.Button(app, text=text, width=10, height=3, bg="#4c4f50", fg="white", font=('Arial', 14), command=lambda t=text: click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create 'Clear', 'Voice Input', and 'NLP Input' buttons with better layout
clear_button = tk.Button(app, text='C', width=32, height=3, bg="#ff6b6b", fg="white", font=('Arial', 14), command=clear)
clear_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

voice_button = tk.Button(app, text='Voice Input', width=10, height=3, bg="#f59f00", fg="white", font=('Arial', 14), command=voice_input)
voice_button.grid(row=5, column=3, padx=5, pady=5)

nlp_button = tk.Button(app, text='NLP Input', width=32, height=3, bg="#20c997", fg="white", font=('Arial', 14), command=natural_language_input)
nlp_button.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

ai_button = tk.Button(app, text='AI Prediction', width=10, height=3, bg="#f65e3b", fg="white", font=('Arial', 14), command=ai_prediction)
ai_button.grid(row=6, column=3, padx=5, pady=5)

# Add a footer label for better user interaction
footer_label = tk.Label(app, text="Powered by AI & Voice Technology", font=('Arial', 12), fg="#adb5bd", bg="#2d2d2d")
footer_label.grid(row=7, column=0, columnspan=4, pady=10)

# Run the application
app.mainloop()
