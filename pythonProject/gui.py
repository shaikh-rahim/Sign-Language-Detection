import os
import tkinter as tk


def open_file():
    os.system('test.py')


# Create the main window
root = tk.Tk()
root.title("Sign Language Detection")

# Define the styling
root.configure(bg='#1E1E1E')
root.option_add('*Font', 'aerial')
root.option_add('*Button.background', '#3E3E3E')
root.option_add('*Button.foreground', 'white')
root.option_add('*Button.activeBackground', '#5E5E5E')
root.option_add('*Button.activeForeground', 'white')
root.option_add('*Label.background', '#1E1E1E')
root.option_add('*Label.foreground', 'white')

# Add widgets to the window
label = tk.Label(root, text="Sign Language Detection!")
label.pack(pady=10)

button = tk.Button(root, text="Start", command=open_file)
button.pack(pady=70)

# Run the application
root.mainloop()
