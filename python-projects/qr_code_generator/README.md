# 📱 QR Code Generator

A Python application that generates QR codes from text or URLs and saves them as image files.

##  Description

This program allows the user to enter multiple pieces of text or URLs and generate a QR code for each one.

The application automatically creates unique filenames for the generated QR codes and allows the user to customise both the QR code colour and background colour.

##  Features

* Generate QR codes from text
* Generate QR codes from URLs
* Generate multiple QR codes in one session
* Automatically generate unique filenames
* Custom QR code colours
* Custom background colours
* Save QR codes as image files
* Input validation

##  Technologies

* Python 
* `qrcode` library

##  Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment and install the required library:

```bash
pip install qrcode
```

##  How to Run

Run the program:

```bash
python qr_code_generator.py
```

Enter your text or URL:

```text
Enter the text or URL (type 'Generate' when finished): https://github.com/
Enter the text or URL (type 'Generate' when finished): Hello World
Enter the text or URL (type 'Generate' when finished): Generate
```

Then select the QR code and background colours.

The generated files will be saved as:

```text
QR_Code_1.jpg
QR_Code_2.jpg
...
```

##  Skills Demonstrated

* Functions
* Lists
* Loops
* Conditional statements
* String manipulation
* User input
* External Python libraries
* Virtual environments
* File generation
* Basic automation

##  Possible Improvements

* Allow users to choose filenames
* Add support for different image formats
* Create a graphical user interface
* Add QR code sizes and border settings
* Allow users to add images or logos
* Provide more advanced QR code customisation
