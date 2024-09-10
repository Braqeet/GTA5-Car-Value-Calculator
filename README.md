# Car Value Calculator

This Python project calculates the full value of a car, including upgrades, by reversing the in-game resale deductions from **GTA Online**. The game applies a 60% deduction to the base car value and a 50% deduction to the value of upgrades. This updated version of the script provides a graphical user interface (GUI) using the **Tkinter** library to make it easier to use.

## Features

* **GUI Interface**: Users can input the car's purchase price and sell price through a simple, user-friendly graphical interface.
* **Full Value Calculation**: The app automatically calculates the full value of the car, including the upgrades, by reversing the in-game deductions.

## How to Run

### Option 1: Run from Source Code

1. **Clone the Repository**: First, clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/Braqeet/GTA5-Car-Value-Calculator.git
   ```

2. **Navigate to the Project Directory**: Change to the project directory:

   ```bash
   cd GTA5-Car-Value-Calculator\src
   ```

3. **Run the Script**: Execute the Python script:

   ```bash
   python car_calc.py
   ```

### Option 2: Run the Executable (Windows Only)

1. **Download the Executable**: Download the `car_calc.exe` file from the releases page.
2. **Run the Executable**: Double-click the downloaded file to run the application. **Note**: You may encounter a "Windows protected your PC" warning when trying to run the .exe file. This is a security feature of Windows designed to protect against potentially harmful software. To run the application:
    * Click on "More info" in the warning dialog.
    * Then click "Run anyway".
## How to Use

1. Enter the **Purchase Price** of the car in the first input field.
2. Enter the **Sell Price** of the car in the second input field.
3. Click the **Calculate** button.
4. The app will display the **Full Value** of the car, including upgrades.

## Requirements

* Python 3.x
* Tkinter (usually comes pre-installed with Python)

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/car-value-calculator/issues) if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
