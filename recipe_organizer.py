
import mysql.connector
from tkinter import Tk, Label, Button, Entry, Listbox, END, messagebox, Toplevel, StringVar, OptionMenu
from tkinter import font as tkFont
from PIL import Image, ImageTk  # Import Pillow

# Define the size and background for the windows
WINDOW_WIDTH = 800  # Set the width for all windows
WINDOW_HEIGHT = 600  # Set the height for all windows
BACKGROUND_IMAGE_PATH = "C:/Users/Dedge/Desktop/Sanji_MESHI!/one_piece_background.jpg"  # Path to the background image

# Function to create a window with the background and fixed size
def create_window_with_background(title, window_geometry=(WINDOW_WIDTH, WINDOW_HEIGHT), bg_color="#ffe700", is_main=False):
    if is_main:
        window = Tk()  # Use Tk only for the main window
    else:
        window = Toplevel()  # Use Toplevel for secondary windows

    window.title(title)
    window.geometry(f"{window_geometry[0]}x{window_geometry[1]}")  # Set fixed window size
    window.config(bg=bg_color)

    # Load and set the background image
    background_image = Image.open(BACKGROUND_IMAGE_PATH)
    background_image = background_image.resize((window_geometry[0], window_geometry[1]), Image.LANCZOS)  # Resize
    background_image = ImageTk.PhotoImage(background_image)

    background_label = Label(window, image=background_image)
    background_label.image = background_image  # Prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the window

    # Store the image reference to prevent garbage collection
    window.background_image = background_image

    return window, background_label


# Database Setup
def setup_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sanji_db"
    )
    cursor = connection.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        name VARCHAR(255) NOT NULL,
        ingredients TEXT NOT NULL,
        instructions TEXT NOT NULL,
        prep_time INT,
        rating INT,
        category VARCHAR(50),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )''')

    # Insert sample data
    cursor.execute("INSERT IGNORE INTO users (id, username, password) VALUES (1, 'test_user', 'password123')")

    connection.commit()
    connection.close()

# User Authentication Functions
def register_user(username, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sanji_db"
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        connection.close()
        return True
    except mysql.connector.Error:
        return False

def authenticate_user(username, password):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sanji_db"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    connection.close()
    return user

# Recipe Management Functions
def add_recipe(user_id, name, ingredients, instructions, prep_time, category, rating):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sanji_db"
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO recipes (user_id, name, ingredients, instructions, prep_time, category, rating) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (user_id, name, ingredients, instructions, prep_time, category, rating))
    connection.commit()
    connection.close()

def get_recipes(search_text=""):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sanji_db"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, rating FROM recipes WHERE name LIKE %s", (f"%{search_text}%",))
    recipes = cursor.fetchall()
    connection.close()
    return recipes

def get_recipe_details(recipe_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sanji_db"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT name, ingredients, instructions, prep_time, rating, category FROM recipes WHERE id = %s", (recipe_id,))
    recipe = cursor.fetchone()
    connection.close()
    return recipe

# GUI Functions
def login_screen():
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        user = authenticate_user(username, password)
        if user:
            messagebox.showinfo("Login Success", f"Welcome back, {username}!")
            root.destroy()
            recipe_manager_screen(user[0])
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_register_screen():
        def handle_register():
            reg_username = reg_username_entry.get()
            reg_password = reg_password_entry.get()
            if not reg_username or not reg_password:
                messagebox.showerror("Error", "Please fill out all fields.")
                return

            if register_user(reg_username, reg_password):
                messagebox.showinfo("Success", "Registration successful! You can now log in.")
                register_window.destroy()
            else:
                messagebox.showerror("Error", "Registration failed. Username might already exist.")

        register_window, background_label = create_window_with_background("Register", window_geometry=(WINDOW_WIDTH, WINDOW_HEIGHT), bg_color="#ffe700")

        Label(register_window, text="Username:", font=("Comic Sans MS", 12), bg="#ffe700").pack(pady=10)
        reg_username_entry = Entry(register_window, font=("Comic Sans MS", 12))
        reg_username_entry.pack(pady=5)

        Label(register_window, text="Password:", font=("Comic Sans MS", 12), bg="#ffe700").pack(pady=10)
        reg_password_entry = Entry(register_window, show="*", font=("Comic Sans MS", 12))
        reg_password_entry.pack(pady=5)

        Button(register_window, text="Register", font=("Comic Sans MS", 12), bg="#FF9800", fg="white", command=handle_register).pack(pady=20)

    root, background_label = create_window_with_background("Login", window_geometry=(WINDOW_WIDTH, WINDOW_HEIGHT), bg_color="#ffe700")

    title_label = Label(root, text="Sanji, MESHIIIIII!", font=("Comic Sans MS", 18, "bold"), fg="#d32f2f", bg="#ffe700")
    title_label.pack(pady=20)

    Label(root, text="Username:", font=("Comic Sans MS", 12), bg="#ffe700").pack(pady=10)
    username_entry = Entry(root, font=("Comic Sans MS", 12))
    username_entry.pack(pady=5)

    Label(root, text="Password:", font=("Comic Sans MS", 12), bg="#ffe700").pack(pady=10)
    password_entry = Entry(root, show="*", font=("Comic Sans MS", 12))
    password_entry.pack(pady=5)

    Button(root, text="Login", font=("Comic Sans MS", 12), bg="#4CAF50", fg="white", command=handle_login).pack(pady=20)
    Button(root, text="Register", font=("Comic Sans MS", 12), bg="#2196F3", fg="white", command=open_register_screen).pack(pady=10)

    root.mainloop()

def recipe_manager_screen(user_id):
    def load_recipes(search_text=""):
        recipe_list.delete(0, END)
        recipes = get_recipes(search_text)
        if not recipes:
            messagebox.showinfo("No Recipes", "No recipes found.")
        else:
            for recipe in recipes:
                recipe_list.insert(END, f"{recipe[0]}: {recipe[1]} (Rating: {recipe[2] if recipe[2] else 'N/A'})")

    def handle_add_recipe():
        def save_recipe():
            name = name_entry.get()
            ingredients = ingredients_entry.get()
            instructions = instructions_entry.get()
            prep_time = prep_time_entry.get()
            rating = rating_entry.get()
            category = category_var.get()

            if not name or not ingredients or not instructions or not prep_time.isdigit() or not rating.isdigit():
                messagebox.showerror("Input Error", "Please fill out all fields correctly.")
                return

            add_recipe(user_id, name, ingredients, instructions, int(prep_time), category, int(rating))
            messagebox.showinfo("Success", "Recipe added successfully!")
            add_recipe_window.destroy()
            load_recipes()

        add_recipe_window, background_label = create_window_with_background("Add Recipe", window_geometry=(WINDOW_WIDTH, WINDOW_HEIGHT), bg_color="#ffcc80")

        Label(add_recipe_window, text="Recipe Name:", font=("Comic Sans MS", 12), bg="#ffcc80").pack(pady=10)
        name_entry = Entry(add_recipe_window, font=("Comic Sans MS", 12))
        name_entry.pack(pady=5)

        Label(add_recipe_window, text="Ingredients:", font=("Comic Sans MS", 12), bg="#ffcc80").pack(pady=10)
        ingredients_entry = Entry(add_recipe_window, font=("Comic Sans MS", 12))
        ingredients_entry.pack(pady=5)

        Label(add_recipe_window, text="Instructions:", font=("Comic Sans MS", 12), bg="#ffcc80").pack(pady=10)
        instructions_entry = Entry(add_recipe_window, font=("Comic Sans MS", 12))
        instructions_entry.pack(pady=5)

        Label(add_recipe_window, text="Preparation Time (minutes):", font=("Comic Sans MS", 12), bg="#ffcc80").pack(pady=10)
        prep_time_entry = Entry(add_recipe_window, font=("Comic Sans MS", 12))
        prep_time_entry.pack(pady=5)

        Label(add_recipe_window, text="Rating (1-5):", font=("Comic Sans MS", 12), bg="#ffcc80").pack(pady=10)
        rating_entry = Entry(add_recipe_window, font=("Comic Sans MS", 12))
        rating_entry.pack(pady=5)

        Label(add_recipe_window, text="Category:", font=("Comic Sans MS", 12), bg="#ffcc80").pack(pady=10)
        categories = ["Main Course", "Dessert", "Appetizer"]
        category_var = StringVar(add_recipe_window)
        category_var.set(categories[0])
        category_menu = OptionMenu(add_recipe_window, category_var, *categories)
        category_menu.pack(pady=5)

        Button(add_recipe_window, text="Save Recipe", font=("Comic Sans MS", 12), bg="#FF5722", fg="white", command=save_recipe).pack(pady=20)

    def show_recipe_details(event):
        selected_recipe = recipe_list.get(recipe_list.curselection())
        recipe_id = int(selected_recipe.split(":")[0])
        recipe_details = get_recipe_details(recipe_id)
        if recipe_details:
            details_window, background_label = create_window_with_background(f"Recipe Details: {recipe_details[0]}", window_geometry=(WINDOW_WIDTH, WINDOW_HEIGHT), bg_color="#f3e5f5")

            Label(details_window, text=f"Name: {recipe_details[0]}", font=("Comic Sans MS", 12), bg="#f3e5f5").pack(pady=10)
            Label(details_window, text=f"Ingredients: {recipe_details[1]}", font=("Comic Sans MS", 12), bg="#f3e5f5").pack(pady=10)
            Label(details_window, text=f"Instructions: {recipe_details[2]}", font=("Comic Sans MS", 12), bg="#f3e5f5").pack(pady=10)
            Label(details_window, text=f"Prep Time: {recipe_details[3]} mins", font=("Comic Sans MS", 12), bg="#f3e5f5").pack(pady=10)
            Label(details_window, text=f"Rating: {recipe_details[4]} / 5", font=("Comic Sans MS", 12), bg="#f3e5f5").pack(pady=10)
            Label(details_window, text=f"Category: {recipe_details[5]}", font=("Comic Sans MS", 12), bg="#f3e5f5").pack(pady=10)

    root, background_label = create_window_with_background("Recipe Manager", window_geometry=(WINDOW_WIDTH, WINDOW_HEIGHT), bg_color="#ffcc80")

    title_label = Label(root, text="Welcome to Sanji's Recipe Manager!", font=("Comic Sans MS", 16, "bold"), fg="#d32f2f", bg="#ffcc80")
    title_label.pack(pady=20)

    search_entry = Entry(root, font=("Comic Sans MS", 12))
    search_entry.pack(pady=5)
    search_entry.bind("<KeyRelease>", lambda event: load_recipes(search_entry.get()))

    recipe_list = Listbox(root, font=("Comic Sans MS", 12), width=50, height=15)
    recipe_list.pack(pady=10)
    recipe_list.bind("<Double-1>", show_recipe_details)

    load_recipes()

    Button(root, text="Add Recipe", font=("Comic Sans MS", 12), bg="#FF9800", fg="white", command=handle_add_recipe).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    setup_database()
    login_screen()
