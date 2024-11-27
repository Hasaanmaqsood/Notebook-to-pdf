# Jupyter Notebook to PDF Converter

This script provides a flexible solution for converting Jupyter Notebooks (`.ipynb`) to PDF files using `nbconvert`. It allows users to specify the input file, notebook path, and output directory for the generated PDF.

---

## Features

- Converts `.ipynb` files to PDF in any environment.
- Allows users to specify custom paths for the input file and output directory.
- Automatically creates the output directory if it does not exist.

---

## Requirements

- Python 3.x
- Installed dependencies:
  - `jupyter`
  - `nbconvert`
  - LaTeX packages:
    - `texlive-xetex`
    - `texlive-fonts-recommended`
    - `texlive-plain-generic`
    - `pandoc`

---

## Installation

1. Install the required Python packages:
   ```bash
   pip install jupyter nbconvert

