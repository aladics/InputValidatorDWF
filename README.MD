# Input validator

Logs some useful info about the input CSV. It checks for:
  * columns with **0 standard deviation**
  * columns with **NaN** or **Inf** or **-Inf** values

## Prerequisities
  * A working python installation, tested on python 3.9.5

Install the required libraries from requirements.txt:

  * `pip install -r requirements.txt`

## Usage
  * `python ./input_validator.py <path_to_csv>`
