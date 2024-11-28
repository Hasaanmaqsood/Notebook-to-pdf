# Jupyter Notebook to PDF Converter

## Overview
This project provides a Python script to convert Jupyter Notebooks (`.ipynb`) into PDF files. It is flexible and works in any environment, allowing users to specify custom paths for input notebooks and output PDF files. The script leverages `jupyter nbconvert` and LaTeX for high-quality PDF generation.

## Features
- Converts Jupyter Notebook files to PDF format.
- Allows custom paths for input and output directories.
- Automatically creates the output directory if it does not exist.
- Compatible with various environments, including local machines and Google Colab.

## Requirements
- Python 3.x
- Installed dependencies:
  - Python packages:
    - `jupyter`
    - `nbconvert`
  - LaTeX packages:
    - `texlive-xetex`
    - `texlive-fonts-recommended`
    - `texlive-plain-generic`
  - `pandoc`

## Installation

### Step 1: Install Python Packages
Install the required Python packages using `pip`:
```bash
pip install jupyter nbconvert
```

Step 2: Install LaTeX and Pandoc
Linux (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic
```
MacOS: Install MacTeX from https://tug.org/mactex/.
Windows: Install MiKTeX and Pandoc from their respective websites.

## Usage
Step 1: Run the Script Locally
1. Place your Jupyter Notebook in the specified notebook_path.
2. Run the script with the following command:
```bash
python jupyter_pdf_converter.py
```
Step 2: Customize Parameters
To specify custom input and output paths, update the parameters in the script:
```bash
from jupyter_pdf_converter import convert_notebook_to_pdf

notebook_path = "/path/to/notebooks"
output_dir = "/path/to/output"
file_name = "example_notebook.ipynb"

result = convert_notebook_to_pdf(file_name, notebook_path=notebook_path, output_dir=output_dir)
print(result)
```

Step 3: Use in Google Colab (Optional)
If using Google Colab, install the required dependencies:
```bash
!apt-get update
!apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic
```

Then, use the following code:
```bash
from jupyter_pdf_converter import convert_notebook_to_pdf

result = convert_notebook_to_pdf('example_notebook.ipynb', notebook_path='/content', output_dir='/content/pdfs')
print(result)
```

## Troubleshooting
Pandoc Missing Error: Ensure pandoc is installed and accessible in your system's PATH.
LaTeX Errors: Verify that all required LaTeX packages are installed.
File Not Found: Double-check the file_name and notebook_path values.
License
This project is licensed under the MIT License. Refer to the LICENSE file for more information.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

