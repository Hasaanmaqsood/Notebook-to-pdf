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
### Direct Usage in Any Environment
Download the script from GitHub and directly use it in your Python script or Colab notebook:
```bash
!wget -nc https://raw.githubusercontent.com/Hasaanmaqsood/Notebook-to-pdf/main/jupyter_pdf_converter.py
```
Example Usage

```bash
from jupyter_pdf_converter import convert_notebook_to_pdf

# Specify notebook and output paths
notebook_path = "/path/to/notebooks"
output_dir = "/path/to/output"
file_name = "example_notebook.ipynb"

# Convert the notebook to PDF
result = convert_notebook_to_pdf(file_name, notebook_path=notebook_path, output_dir=output_dir)
print(result)

```

### Using in Google Colab
1. Install Dependencies Run the following commands in your Colab notebook to install required dependencies:
```bash
!apt-get update
!apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic
```
2. Download and Use the Script Use the following code to convert your notebook to PDF:
```bash
!wget -nc https://raw.githubusercontent.com/Hasaanmaqsood/Notebook-to-pdf/main/jupyter_pdf_converter.py
from jupyter_pdf_converter import convert_notebook_to_pdf

# Convert the notebook
result = convert_notebook_to_pdf('example_notebook.ipynb', notebook_path='/content', output_dir='/content/pdfs')
print(result)

```

## Troubleshooting
Common Issues and Fixes
1. Pandoc Missing Error: Ensure pandoc is installed and accessible in your system's PATH.
2. LaTeX Errors: Verify that all required LaTeX packages (texlive-xetex, etc.) are installed.
3. File Not Found: Double-check the file_name and notebook_path values to ensure they are correct.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

