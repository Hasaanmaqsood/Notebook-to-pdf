import os
import subprocess


def convert_notebook_to_pdf(file_name, notebook_path=".", output_dir="."):
    """
    Convert a Jupyter Notebook to PDF and save it in a specified directory.

    Parameters:
    file_name (str): The name of the notebook file (e.g., 'notebook.ipynb').
    notebook_path (str): The directory where the notebook is located.
    output_dir (str): The directory where the PDF should be saved.

    Returns:
    str: The path to the generated PDF or an error message.
    """
    # Verify the notebook file exists.
    notebook_file = os.path.join(notebook_path, file_name)
    if not os.path.isfile(notebook_file):
        raise ValueError(f"Notebook file '{file_name}' not found in path '{notebook_path}'.")

    # Verify the output directory exists.
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # Define output PDF path.
    pdf_file = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".pdf")

    # Attempt to convert the notebook to a PDF.
    try:
        command = [
            "jupyter",
            "nbconvert",
            "--to",
            "pdf",
            "--output-dir",
            output_dir,
            notebook_file,
        ]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return f"nbconvert error: {str(e)}"

    # Check if the PDF was successfully created.
    if not os.path.isfile(pdf_file):
        return "PDF generation failed. Please check the notebook or output logs."

    return f"PDF successfully generated and saved to: {pdf_file}"


# Example usage:
if __name__ == "__main__":
    # Update these values based on your use case
    notebook_path = "."
    output_dir = "./pdfs"
    file_name = "example_notebook.ipynb"

    # Generate PDF
    try:
        result = convert_notebook_to_pdf(file_name, notebook_path=notebook_path, output_dir=output_dir)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
