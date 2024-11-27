\documentclass{article}
\usepackage[utf8]{inputenc}

\title{Jupyter Notebook to PDF Converter}
\author{}
\date{}

\begin{document}

\maketitle

\section*{Overview}
This project provides a Python script to convert Jupyter Notebooks (\texttt{.ipynb}) into PDF files. It is flexible and works in any environment, allowing users to specify custom paths for input notebooks and output PDF files. The script leverages \texttt{jupyter nbconvert} and LaTeX for high-quality PDF generation.

\section*{Features}
\begin{itemize}
    \item Converts Jupyter Notebook files to PDF format.
    \item Allows custom paths for input and output directories.
    \item Automatically creates the output directory if it does not exist.
    \item Compatible with various environments, including local machines and Google Colab.
\end{itemize}

\section*{Requirements}
\begin{itemize}
    \item Python 3.x
    \item Installed dependencies:
    \begin{itemize}
        \item \texttt{jupyter}
        \item \texttt{nbconvert}
        \item LaTeX packages:
        \begin{itemize}
            \item \texttt{texlive-xetex}
            \item \texttt{texlive-fonts-recommended}
            \item \texttt{texlive-plain-generic}
        \end{itemize}
        \item \texttt{pandoc}
    \end{itemize}
\end{itemize}

\section*{Installation}

\subsection*{Step 1: Install Python Packages}
Install the required Python packages using \texttt{pip}:
\begin{verbatim}
pip install jupyter nbconvert
\end{verbatim}

\subsection*{Step 2: Install LaTeX and Pandoc}
\begin{itemize}
    \item \textbf{Linux (Ubuntu/Debian):}
    \begin{verbatim}
    sudo apt-get update
    sudo apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic
    \end{verbatim}

    \item \textbf{MacOS:} Install MacTeX from \texttt{https://tug.org/mactex/}.
    
    \item \textbf{Windows:} Install MiKTeX and Pandoc from their respective websites.
\end{itemize}

\section*{Usage}

\subsection*{Step 1: Run the Script Locally}
\begin{enumerate}
    \item Place your Jupyter Notebook in the specified \texttt{notebook\_path}.
    \item Run the script with the following command:
    \begin{verbatim}
    python general_pdf_converter.py
    \end{verbatim}
\end{enumerate}

\subsection*{Step 2: Customize Parameters}
To specify custom input and output paths, update the parameters in the script:
\begin{verbatim}
from general_pdf_converter import convert_notebook_to_pdf

notebook_path = "/path/to/notebooks"
output_dir = "/path/to/output"
file_name = "example_notebook.ipynb"

result = convert_notebook_to_pdf(file_name, notebook_path=notebook_path, output_dir=output_dir)
print(result)
\end{verbatim}

\subsection*{Step 3: Use in Google Colab (Optional)}
If using Google Colab, install the required dependencies:
\begin{verbatim}
!apt-get update
!apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic
\end{verbatim}
Then, use the following code:
\begin{verbatim}
from general_pdf_converter import convert_notebook_to_pdf

result = convert_notebook_to_pdf('example_notebook.ipynb', notebook_path='/content', output_dir='/content/pdfs')
print(result)
\end{verbatim}

\section*{Troubleshooting}
\begin{itemize}
    \item \textbf{Pandoc Missing Error:} Ensure \texttt{pandoc} is installed and accessible in your system's PATH.
    \item \textbf{LaTeX Errors:} Verify that all required LaTeX packages are installed.
    \item \textbf{File Not Found:} Double-check the \texttt{file\_name} and \texttt{notebook\_path} values.
\end{itemize}

\section*{License}
This project is licensed under the MIT License. Refer to the \texttt{LICENSE} file for more information.

\section*{Contributing}
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

\end{document}
