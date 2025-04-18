import tkinter as tk
from pet import Pet

# Create pet object
my_pet = Pet("Sport")

# GUI Functions
def update_status():
    status_text.set(
        f"Name: {my_pet.name}\n"
        f"Hunger: {my_pet.hunger}\n"
        f"Energy: {my_pet.energy}\n"
        f"Happiness: {my_pet.happiness}"
    )

def feed_pet():
    my_pet.eat()
    update_status()

def sleep_pet():
    my_pet.sleep()
    update_status()

def play_with_pet():
    my_pet.play()
    update_status()

def train_pet():
    trick = trick_entry.get()
    if trick:
        my_pet.train(trick)
        trick_entry.delete(0, tk.END)
        update_tricks()

def update_tricks():
    tricks_text.set("\n".join(my_pet.tricks) if my_pet.tricks else "No tricks yet")

# GUI Setup
root = tk.Tk()
root.title("🐾 Virtual Pet Game")

status_text = tk.StringVar()
tricks_text = tk.StringVar()

# Status Display
status_label = tk.Label(root, textvariable=status_text, font=("Arial", 14), justify='left')
status_label.pack(pady=10)

# Buttons
tk.Button(root, text="🍽️ Feed", command=feed_pet, width=20).pack()
tk.Button(root, text="😴 Sleep", command=sleep_pet, width=20).pack()
tk.Button(root, text="🎾 Play", command=play_with_pet, width=20).pack()

# Train section
tk.Label(root, text="Teach a Trick:").pack(pady=(10, 0))
trick_entry = tk.Entry(root)
trick_entry.pack()
tk.Button(root, text="🧠 Train", command=train_pet).pack()

# Tricks Display
tk.Label(root, text="Learned Tricks:").pack(pady=(10, 0))
tricks_label = tk.Label(root, textvariable=tricks_text)
tricks_label.pack()

# Initialize
update_status()
update_tricks()

# Start GUI loop
root.mainloop()
