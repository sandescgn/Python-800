import tkinter as tk
from tkinter import ttk

import pandas as pd

NO_OF_ROWS = 7
SEARCH_PLACEHOLDER = "Search..."


def on_focus_in(entry):
    if entry.cget("state") == "disabled":
        entry.configure(state="normal")
        entry.delete(0, "end")


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state="disabled")


# Function to filter the data based on the search term
def filter_data(event):
    search_term = search_bar.get()
    if search_term == "" or search_term == "\b":
        filtered_df = df
    else:
        filtered_df = df[
            df["name"].str.contains(search_term, case=False)
            | df["symbol"].str.contains(search_term, case=False)
        ]
    table.delete(*table.get_children())
    for index, row in filtered_df.iterrows():
        table.insert("", "end", values=list(row))


# Load data into a pandas DataFrame
data = pd.read_json("today_prices.json")
df = pd.DataFrame(data)

# Create the main window
window = tk.Tk()
window.title("NEPSE Today Price")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.state("zoomed")

# window.geometry(f"{screen_width}x{screen_height}+0+0")
# window.attributes('-fullscreen', True)

# Create a frame to hold the table
frame = tk.Frame(window)
frame.pack()

# Create the search bar
search_bar = tk.Entry(window)
search_bar.insert(0, SEARCH_PLACEHOLDER)
search_bar.place(relx=1.0, rely=0.0, anchor=tk.NE, bordermode="outside")
search_bar.configure(state="disabled")

# add / remove placeholder dynamically
search_bar.bind("<Button-1>", lambda x: on_focus_in(search_bar))
search_bar.bind("<FocusOut>", lambda x: on_focus_out(search_bar, SEARCH_PLACEHOLDER))

# Bind the filter_data function to the search bar
search_bar.bind("<Return>", filter_data)

# Create the table
table = ttk.Treeview(
    frame,
    columns=df.columns[: NO_OF_ROWS - 1],
    show="headings",
    height=screen_height,
)
table.pack()

# Set the column headings
for i, col in enumerate(df.columns[:NO_OF_ROWS]):
    table.heading(f"#{i+1}", text=col)

# Add the data to the table
for index, row in df.iterrows():
    row = list(row)[:NO_OF_ROWS]
    table.insert("", tk.END, values=row)

# Run the main loop
window.mainloop()
