""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Pokemon Information")

# Create the frames

frame_input = ttk.Frame(root)
frame_input.grid(row=0, column=0, columnspan=2, pady=(20,10))

frame_info = ttk.LabelFrame(root, text = "Info")
frame_info.grid(row=1, column = 0, padx = (20 , 10), pady= (10 , 20), sticky = N)

frame_stats = ttk.LabelFrame(root, text = "Stats")
frame_stats.grid(row=1, column = 1, padx = (10 , 20), pady= (10 , 20), sticky = N)

Label_name = ttk.Entry(frame_input, text="Pokemon Name")
Label_name.grid(row = 0, column = 0, padx = (10,5), pady = (10))

enter_name = ttk.Entry(frame_input)
enter_name.insert(0,'mew')
enter_name.grid(row = 0, column = 1)
# Define the labels for pokemon data

label_pokemon_name = ttk.Label(frame_info)
label_pokemon_name.grid(row=0, column=0, sticky=W)

label_pokemon_type = ttk.Label(frame_info)
label_pokemon_type.grid(row=1, column=0, sticky=W)

label_pokemon_height = ttk.Label(frame_info)
label_pokemon_height.grid(row=2, column=0, sticky=W)

label_pokemon_weight = ttk.Label(frame_info)
label_pokemon_weight.grid(row=3, column=0, sticky=W)

label_pokemon_stats = ttk.Label(frame_stats)
label_pokemon_stats.grid(row=0, column=0, sticky=W)

def handle_button_get_info():
    pokemon_name = enter_name.get()
    try:
        pokemon_data = get_pokemon_info(pokemon_name)
        
        # Updating the labels with the fetched data

        label_pokemon_name.configure(text=f"Name: {pokemon_data['name']}")
        label_pokemon_type.configure(text=f"Type: {', '.join(pokemon_data['types'])}")
        label_pokemon_height.configure(text=f"Height: {pokemon_data['height']}")
        label_pokemon_weight.configure(text=f"Weight: {pokemon_data['weight']}")
        label_pokemon_stats.configure(text=f"Stats: {pokemon_data['stats']}")
    
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))

# Add the button
button_get_info = ttk.Button(frame_input, text="Get Info", command=handle_button_get_info)
button_get_info.grid(row=0, column=2, padx=(5,10))

# Start the GUI loop
root.mainloop()
