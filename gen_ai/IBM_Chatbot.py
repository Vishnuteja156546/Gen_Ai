import tkinter as tk
from tkinter import messagebox, simpledialog
import openai
import datetime

# Set your OpenAI API key here
openai.api_key = "your_openai_api_key"

# Define the tasks for each day
tasks = {
    "Day 1": {
        "morning": "Review basic programming concepts (variables, loops, functions)",
        "afternoon": "Practice data structures (arrays, linked lists, stacks, queues)",
        "evening": "Solve basic coding problems (arrays, strings)"
    },
    "Day 2": {
        "morning": "Study Object-Oriented Programming (OOP) principles",
        "afternoon": "Learn debugging techniques and practice",
        "evening": "Solve OOP-related coding problems"
    },
    "Day 3": {
        "morning": "Study Software Development Life Cycle (SDLC)",
        "afternoon": "Learn Git and version control systems",
        "evening": "Solve SDLC-related questions"
    },
    "Day 4": {
        "morning": "Deep dive into trees, heaps, and graphs",
        "afternoon": "Study searching and sorting algorithms",
        "evening": "Solve searching and sorting problems"
    },
    "Day 5": {
        "morning": "Prepare for mock interviews and review common IBM questions",
        "afternoon": "Study system design basics",
        "evening": "Take a mock interview and review weak areas"
    }
}

completed_tasks = []

# Function to get the current day and time
def get_current_day_and_time():
    current_time = datetime.datetime.now()
    day_of_week = current_time.weekday()  # Monday is 0, Sunday is 6
    time_of_day = "morning"  # Default to morning

    if current_time.hour >= 12 and current_time.hour < 17:
        time_of_day = "afternoon"
    elif current_time.hour >= 17:
        time_of_day = "evening"

    return day_of_week + 1, time_of_day  # Return day as Day 1 to Day 5, along with time of day

# Function to display the tasks based on the current day and time
def display_tasks():
    day, time_of_day = get_current_day_and_time()

    task_listbox.delete(0, tk.END)  # Clear current tasks
    if day <= 5:
        for period, task in tasks[f"Day {day}"].items():
            if period == time_of_day or period == "morning":  # Show current time of day and earlier tasks
                task_listbox.insert(tk.END, f"{period.capitalize()}: {task}")
    else:
        messagebox.showinfo("End of Plan", "You have completed the 5-day study plan!")

# Function to mark a task as complete
def mark_task_completed():
    task = task_listbox.get(tk.ACTIVE)
    if task:
        completed_tasks.append(task)
        task_listbox.delete(tk.ACTIVE)
        messagebox.showinfo("Task Completed", f"Task '{task}' marked as completed!")

# Function to add a new task to the list (optional if you want to add more tasks later)
def add_task():
    task = simpledialog.askstring("New Task", "Enter a new study task:")
    if task:
        task_listbox.insert(tk.END, task)
        messagebox.showinfo("Task Added", f"Task '{task}' has been added!")

# Function to display completed tasks
def view_completed_tasks():
    if not completed_tasks:
        messagebox.showinfo("Completed Tasks", "No tasks completed yet.")
    else:
        completed = "\n".join(completed_tasks)
        messagebox.showinfo("Completed Tasks", f"Completed Tasks:\n{completed}")

# Chatbot interaction using OpenAI API
def chat_with_ai():
    user_input = simpledialog.askstring("Study Chatbot", "Ask your study question:")
    if user_input:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            answer = response.choices[0].message['content'].strip()
            chat_output.insert(tk.END, f"You: {user_input}\nAI: {answer}\n\n")
        except Exception as e:
            messagebox.showerror("API Error", f"An error occurred: {str(e)}")

# Function to clear the chat history
def clear_chat():
    chat_output.delete("1.0", tk.END)

# Initialize the GUI window
root = tk.Tk()
root.title("AI Study Assistant")
root.geometry("800x600")
root.config(bg="lightgray")

# Create a frame for tasks and chat area
main_frame = tk.Frame(root, bg="lightgray")
main_frame.pack(fill=tk.BOTH, expand=True)

# Left Frame: Task List (To-Do List)
task_frame = tk.Frame(main_frame, bg="lightgray")
task_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

task_label = tk.Label(task_frame, text="Today's Study Tasks", font=("Arial", 14, "bold"), bg="lightgray")
task_label.pack(pady=10)

task_listbox = tk.Listbox(task_frame, height=20, width=40)
task_listbox.pack(pady=10)

# Insert tasks based on the current day and time
display_tasks()

# Buttons for To-Do List
add_task_button = tk.Button(task_frame, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

complete_task_button = tk.Button(task_frame, text="Mark Task as Completed", command=mark_task_completed)
complete_task_button.pack(pady=5)

view_completed_button = tk.Button(task_frame, text="View Completed Tasks", command=view_completed_tasks)
view_completed_button.pack(pady=5)

# Right Frame: Chatbot Section
chat_frame = tk.Frame(main_frame, bg="lightgray")
chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

chat_label = tk.Label(chat_frame, text="Study Chatbot", font=("Arial", 14, "bold"), bg="lightgray")
chat_label.pack(pady=10)

chat_output = tk.Text(chat_frame, height=20, width=50, wrap="word")
chat_output.pack(pady=10)

# Buttons for Chatbot
ask_chatbot_button = tk.Button(chat_frame, text="Ask AI", command=chat_with_ai)
ask_chatbot_button.pack(pady=5)

clear_chat_button = tk.Button(chat_frame, text="Clear Chat", command=clear_chat)
clear_chat_button.pack(pady=5)

# Run the GUI loop
root.mainloop()
