# Import the required modules
import os
from PyPDF2 import PdfMerger

# Create a PdfMerger object
merger = PdfMerger()

# Ask the user for the directory containing the PDF files
directory = input("Enter the directory containing the PDF files: ")

# Get a sorted list of all the PDF files in the directory
pdf_files = sorted([f for f in os.listdir(directory) if f.endswith(".pdf")])

# Add each PDF file to the merger
for pdf in pdf_files:
    merger.append(open(pdf, 'rb'))

# Ask the user for the name of the output file
output_file = input("Enter the name of the output file: ")

# Write the merged PDF to the output file
with open(output_file, "wb") as fout:
    merger.write(fout)

# Print a success message
print("PDF files successfully merged!")
