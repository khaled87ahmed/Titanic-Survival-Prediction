import tkinter as tk
from tkinter import ttk
import pickle
from PIL import Image, ImageTk

# List to store the chosen values
chosen_values_list = []

with open('../Code/servivedPerson', 'rb') as model_file:
    model = pickle.load(model_file)

def predict():

    pclass_value = combobox_pclass.get()
    age_value = entry_age.get()
    sibsp_value = entry_sibsp.get()
    parch_value = entry_parch.get()
    fare_value = entry_fare.get()
    embarked_value = combobox_embarked.get()
    gender_value = combobox_gender.get()

    chosen_values_list = [pclass_value, age_value, sibsp_value, parch_value, fare_value, embarked_value, gender_value]

    embarked_dic = {"Cherbourg": 0,
                    "Queenstown": 1,
                    "Southampton": 2}

    gender_dic = {"Male": 1,
                  "Female": 0}

    try:
        chosen_values_list[0] = int(chosen_values_list[0])
        chosen_values_list[1] = float(chosen_values_list[1])
        chosen_values_list[2] = int(chosen_values_list[2])
        chosen_values_list[3] = int(chosen_values_list[3])
        chosen_values_list[4] = float(chosen_values_list[4])
        chosen_values_list[5] = embarked_dic[embarked_value]
        chosen_values_list[6] = gender_dic[gender_value]

    except:
        result_label.config(text='Invalid input. Please enter values.',background="red")


    prediction = model.predict([chosen_values_list])

    prediction_dic = {0:"Is Death",
                      1:"Is Alive"}

    prediction = prediction_dic[prediction[0]]

    if prediction == "Is Alive":
        result_label.config(text=prediction+" :)))))))))", background="green")
    else:
        result_label.config(text=prediction+" :(((((((((", background="red")




# Dark mode color palette
dark_mode_palette = {
    "background": "#1E1E1E",
    "foreground": "#FFFFFF",
    "highlightBackground": "#333333",
    "highlightColor": "#FFFFFF",
    "selectBackground": "#404040",
    "selectColor": "#FFFFFF",
}

# Create the main GUI window
root = tk.Tk()
root.title('Titanic predictor')

# Configure the window background color
root.configure(bg=dark_mode_palette["background"])



# Calculate screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position
window_width = int(0.6 * screen_width)
window_height = int(0.7 * screen_height)
root.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

# Lock the window sizes
root.resizable(False, False)

original_image = Image.open("Titanic.png")

# Resize the image to fit the window
resized_image = original_image.resize((window_width, window_height), Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# Create a Canvas widget for the background image
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Create a single frame for all Entry widgets with a transparent background
frame = ttk.Frame(root, style="My.TFrame")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

frame2 = ttk.Frame(root, style="My.TFrame")
frame2.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

combobox_pclass_label = ttk.Label(frame, text="Pclass", foreground="#000000", style="My.TLabel")
combobox_pclass_label.grid(row=0, column=0, padx=5, pady=5)
combobox_values_pclass = ['1', '2', '3']
combobox_pclass = ttk.Combobox(frame, values=combobox_values_pclass, state='readonly')
combobox_pclass.grid(row=1, column=0, padx=5, pady=5)
combobox_pclass.set(combobox_values_pclass[0])  # Set default value

label_age = ttk.Label(frame, text=f"Age", foreground="#000000", style="My.TLabel")  # Set foreground color to black
label_age.grid(row=0, column=1, padx=5, pady=5)
entry_age = ttk.Entry(frame)
entry_age.grid(row=1, column=1, padx=5, pady=5)

label_sibsp = ttk.Label(frame, text=f"SibSp", foreground="#000000", style="My.TLabel")  # Set foreground color to black
label_sibsp.grid(row=0, column=2, padx=5, pady=5)
entry_sibsp = ttk.Entry(frame)
entry_sibsp.grid(row=1, column=2, padx=5, pady=5)

label_parch = ttk.Label(frame, text=f"Parch", foreground="#000000", style="My.TLabel")  # Set foreground color to black
label_parch.grid(row=0, column=3, padx=5, pady=5)
entry_parch = ttk.Entry(frame)
entry_parch.grid(row=1, column=3, padx=5, pady=5)

label_fare = ttk.Label(frame, text=f"Fare", foreground="#000000", style="My.TLabel")  # Set foreground color to black
label_fare.grid(row=0, column=4, padx=5, pady=5)
entry_fare = ttk.Entry(frame)
entry_fare.grid(row=1, column=4, padx=5, pady=5)

combobox_embarked_label = ttk.Label(frame, text="Embarked", foreground="#000000", style="My.TLabel")
combobox_embarked_label.grid(row=0, column=5, padx=5, pady=5)
combobox_values_embarked = ['Cherbourg', 'Queenstown', 'Southampton']
combobox_embarked = ttk.Combobox(frame, values=combobox_values_embarked, state='readonly')
combobox_embarked.grid(row=1, column=5, padx=5, pady=5)
combobox_embarked.set(combobox_values_embarked[0])  # Set default value

combobox_gender_label = ttk.Label(frame, text="Gender", foreground="#000000", style="My.TLabel")
combobox_gender_label.grid(row=0, column=6, padx=5, pady=5)
combobox_values_gender = ['Male', 'Female']
combobox_gender = ttk.Combobox(frame, values=combobox_values_gender, state='readonly')
combobox_gender.grid(row=1, column=6, padx=5, pady=5)
combobox_gender.set(combobox_values_gender[0])  # Set default value

# Style configuration for frames
style = ttk.Style()
style.configure("My.TFrame", background=dark_mode_palette["background"])

# Define styles for labels, entry widgets, and combobox
style.configure("My.TLabel", foreground="#000000", font=('Helvetica', 10, 'bold'))  # Adjust font and color
style.configure("My.TEntry", background="#303030", foreground="#FFFFFF", bordercolor=dark_mode_palette["background"])  # Adjust colors
style.configure("My.TCombobox", background="#303030", foreground="#FFFFFF", bordercolor=dark_mode_palette["background"])  # Adjust colors

# Create a button to trigger prediction
predict_button = ttk.Button(frame2, text='Predict', command=predict, style="My.TLabel")
predict_button.grid()  # Use grid instead of pack for proper placement

# Create a label to display the prediction result
result_label = ttk.Label(frame2, foreground="white", style="My.TLabel")
result_label.grid()  # Use grid instead of pack for proper placement


# Create a button to toggle dark mode

# Start the GUI main loop
root.mainloop()
