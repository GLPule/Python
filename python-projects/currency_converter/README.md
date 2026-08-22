# 💱 Currency Converter

A simple Python command line currency converter that converts an amount from one currency to another using the `CurrencyConverter` library.

##  Description

The program asks the user for an amount, source currency and target currency.

It then uses the `CurrencyConverter` Python library to calculate the converted amount.

Currently, the program is designed to work with currencies such as:

* ZAR — South African Rand
* USD — United States Dollar
* EUR — Euro
* CAD — Canadian Dollar

##  Features

* Convert between supported currencies
* User-defined amount
* User-defined source currency
* User-defined target currency
* Formatted conversion output

##  Technologies

* Python 
* `CurrencyConverter` library

##  Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment and install the required library:

```bash
pip install CurrencyConverter
```

##  How to Run

Run the program:

```bash
python currency_converter.py
```

Enter the required information:

```text
Enter the amount: 100
Source currency (ZAR/USD/EUR/CAD): ZAR
Target currency (ZAR/USD/EUR/CAD): USD
```

The program will then display the converted value.

##  Example

```text
Enter the amount: 100
Source currency (ZAR/USD/EUR/CAD): ZAR
Target currency (ZAR/USD/EUR/CAD): USD

100.00 ZAR is equal to 6.XX USD
```

*The exact conversion result depends on the exchange-rate data available to the library.*

##  Skills Demonstrated

* External Python libraries
* Virtual environments
* User input
* Variables
* Type conversion
* String formatting
* Function/library usage
* Basic financial programming concepts

##  Possible Improvements

* Add more supported currencies
* Add input validation
* Add a graphical user interface
* Allow users to select historical conversion dates
* Display exchange rates
* Add support for batch conversions
* Handle unsupported currencies and conversion errors
