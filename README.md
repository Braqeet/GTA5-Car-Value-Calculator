
# Car Value Calculator (GUI Version)

This Python project calculates the full value of a car, including upgrades, by reversing the in-game resale deductions from **GTA Online**. The game applies a 60% deduction to the base car value and a 50% deduction to the value of upgrades. This updated version of the script provides a graphical user interface (GUI) using the **Tkinter** library to make it easier to use.

## Features

- **GUI Interface**: Users can input the car's purchase price and sell price through a simple, user-friendly graphical interface.
- **Full Value Calculation**: The app automatically calculates the full value of the car, including the upgrades, by reversing the in-game deductions.
- **Input Validation**: The app includes error handling for invalid inputs (such as non-numeric values).
- **No Command Line Required**: This version does not require any command-line interaction and can be easily used by anyone with a Python interpreter.

## How to Run

### 1. Clone the Repository
First, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/repository-name.git
```

### 2. Install Tkinter
Ensure you have Tkinter installed on your machine. For most Python installations, Tkinter comes pre-installed, but if needed, you can install it as follows:

- **Linux**: `sudo apt-get install python3-tk`
- **Windows** & **Mac**: Tkinter should be included by default with your Python installation.

### 3. Run the Application

Navigate to the project directory and run the Python script using:

```bash
python car_value_calculator_gui.py
```

The graphical interface will launch, and you can input the **purchase price** and **sell price** to get the full car value.

### 4. Example

1. Input the **purchase price**: `1,000,000`
2. Input the **sell price**: `728,135`
3. After pressing "Calculate," the result will be displayed as:

```
Full car value (including upgrades): $1,256,270.00
```

## Requirements

- **Python 3.x**
- **Tkinter**: A built-in Python library for creating graphical user interfaces.

## File Structure

- `car_value_calculator_gui.py`: The main Python script that runs the GUI application.
- `.gitignore`: Specifies files to be ignored by Git (such as virtual environment files, logs, etc.).
- `README.md`: Documentation for the project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
