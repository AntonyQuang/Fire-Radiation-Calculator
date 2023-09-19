# Fire Radiation Calculator

A TKinter app that calculates how close a train passenger can stand away from a train on fire without being harmed by the resulting heat.

# Repository Description:

![Fire Radiation Calculator](/images/calculator.png)

This is a Python-based GUI application that allows users to calculate how close railway passengers can be near a train on fire to aid railway station design.

Users can input fire and geometric data. Using a root-finding method known as the bisection method is, the maximum safe distance is calculated. This parameter, as well as several fire related parameters are saved as an excel spreadsheet file. The app provides a separate tab to educate users who are not familiar with the scientific methodology.

# Project Organization:

The project consists of the following directories and files:

```
├── methodology equations/
├── methodology text/
├── images/
├── requirements.txt
├── calculator.py
├── input_manager.py
├── methodology_reader.py
└── main.py
```


methodology equations/: Contains images of equations used in the calculator.

methodology text/: Contains text files of paragraphs explaining the equations used in the calculator.

images/: Contains images of train geometry.

requirements.txt: Lists the required packages and dependencies for the application.

calculator.py: Calculates output variables using the bi-section method, and collates that to a spreadsheet file

input_manager.py: Collect user inputs and arranges it to be compatible with calculator.py

methodology_reader.py: Reads the files in the "methodology equations" and "methodology text" 

main.py: Contains the GUI and the entry point for the application.

# First Time Set-up:

1. Clone the repository:

```$ git clone https://github.com/AntonyQuang/Allergy-Menu-Map.git```


2. Install the required packages:

```$ pip install -r requirements.txt```

3. Run the application:

``` $ python main.py ```

# License Information:

This project is licensed under the MIT License (opensource.org/licenses/MIT).

# Status and Roadmap

The application is currently in a functional state, having already been used in a professional environment, but there is still room for improvement and new features to be added.
The project roadmap includes adding compatibility for more train types and visual updates.
