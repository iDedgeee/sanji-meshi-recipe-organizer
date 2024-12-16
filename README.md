# Sanji, MESHI! Recipe Organizer

## Overview

Sanji, MESHI! is a Python-based recipe organizer application designed to help users manage, search, and share recipes. It features user authentication, a database-driven backend using MySQL via XAMPP, and a GUI built with Tkinter. The app aims to streamline meal planning, reduce food waste, and support healthy eating by making it easier for individuals, particularly students and those with limited cooking experience, to organize their recipes.

## Features

- **User Authentication**: Allows users to register, log in, and securely manage their account.
- **Recipe Management**: Users can add, view, and search for recipes.
- **Ingredients Search**: Users can search recipes by ingredients.
- **Rating System**: Recipes can be rated on a scale of 1-5.
- **Categories**: Recipes are categorized into different sections (Main Course, Dessert, Appetizer).
- **Database Integration**: MySQL database (via XAMPP) stores user data and recipes.
- **Graphical User Interface (GUI)**: Built with Tkinter for an interactive user experience.

## Target Users

This app is designed for:
- **Students** learning to cook and manage their meals.
- **Individuals** with limited cooking skills or those on a tight budget.
- **Cooking enthusiasts** seeking to store and organize their favorite recipes.

## SDG Alignment

This project aligns with **Sustainable Development Goal (SDG) 2: Zero Hunger** and **SDG 4: Quality Education** by promoting affordable, healthy eating and providing a platform for educational purposes. It helps reduce food waste by allowing better meal planning and encourages sustainability.

## Project Requirements

- **Core Functionality**: Recipe management, user authentication, and a search feature for finding recipes by name or ingredients.
- **Data Handling**: MySQL database for storing user and recipe data (configured via XAMPP).
- **Error Handling**: Basic checks for user input and validation of recipe details.
- **Modular Code**: Code is divided into functions for better readability and maintenance.
- **Documentation**: In-line comments for code clarity and a comprehensive README file.
- **Optional Features**: GUI using Tkinter, user authentication, and advanced recipe management features.
- **GitHub Repository**: The project is uploaded on GitHub for easy access and sharing.

## Technologies Used

- **Python**: The primary programming language used for the backend and GUI.
- **Tkinter**: Used for creating the graphical user interface.
- **MySQL**: Database system for storing user and recipe data.
- **XAMPP**: A local server setup to run MySQL.

## Installation Instructions

### Prerequisites

- **XAMPP**: Make sure XAMPP is installed and running on your machine, as it will handle the MySQL database.
  - Download XAMPP from [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html).
  - Start the **MySQL** service in XAMPP.

### Clone the Repository

```bash
git clone https://github.com/yourusername/sanji-meshi.git
cd sanji-meshi
```

### Set up the Database

1. **Start MySQL via XAMPP**.
2. Open the **phpMyAdmin** dashboard (usually at `http://localhost/phpmyadmin`).
3. Create a new database called `sanji_db`.
4. Execute the following SQL commands to create the necessary tables:
   
   ```sql
   CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(255) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL
   );

   CREATE TABLE IF NOT EXISTS recipes (
       id INT AUTO_INCREMENT PRIMARY KEY,
       user_id INT,
       name VARCHAR(255) NOT NULL,
       ingredients TEXT NOT NULL,
       instructions TEXT NOT NULL,
       prep_time INT,
       rating INT,
       category VARCHAR(50),
       FOREIGN KEY (user_id) REFERENCES users(id)
   );
   ```

### Install Dependencies

Ensure you have **MySQL Connector** and **Pillow** installed:

```bash
pip install mysql-connector-python pillow
```

### Run the Application

To start the application, run the following command:

```bash
python recipe_organizer.py
```

This will launch the application and you can begin using it by registering or logging in.

## Usage Instructions

1. **Login**: Upon running the program, you will be prompted to log in using your username and password.
2. **Register**: If you don't have an account, you can create one by clicking the "Register" button.
3. **Add Recipes**: After logging in, you can add new recipes, view existing ones, or search for recipes by ingredients or name.
4. **Search Recipes**: Use the search bar to find recipes based on ingredients or recipe name.
5. **Rate Recipes**: Rate recipes on a scale from 1 to 5 to help others find the best recipes.

## GitHub Repository

[Sanji, MESHI! GitHub Repository](https://github.com/iDedgeee/sanji-meshi)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

- Special thanks to the developers of Tkinter, MySQL, and Pillow for providing the tools used in this project.
```

---

