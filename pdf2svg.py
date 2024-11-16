import os
import time
import shutil
import argparse
import fitz  # PyMuPDF

def ensure_directories():
    # Ensure "input" and "processed" directories exist
    os.makedirs("input", exist_ok=True)
    os.makedirs("processed", exist_ok=True)

def locate_pdf_file(pdf_path):
    # Check if the file exists in the root or input directory
    if os.path.exists(pdf_path):
        return pdf_path
    input_dir = os.path.join("input", os.path.basename(pdf_path))
    if os.path.exists(input_dir):
        return input_dir
    raise FileNotFoundError(f"File '{pdf_path}' not found in root or 'input' directory.")

def move_to_processed(pdf_path):
    # Move the PDF to the "processed" directory
    processed_dir = "processed"
    os.makedirs(processed_dir, exist_ok=True)
    shutil.move(pdf_path, os.path.join(processed_dir, os.path.basename(pdf_path)))

def pdf_to_svg(pdf_path):
    # Generate a timestamped output directory
    timestamp = int(time.time())
    output_dir = f"{timestamp}_output_svg"
    os.makedirs(output_dir, exist_ok=True)

    # Open the PDF
    doc = fitz.open(pdf_path)

    # Convert each page to SVG
    for page_number in range(len(doc)):
        svg_filename = f"{output_dir}/page_{page_number + 1}.svg"
        svg_content = doc[page_number].get_svg_image()
        with open(svg_filename, "w") as svg_file:
            svg_file.write(svg_content)
        print(f"Saved {svg_filename}")

    # Move the PDF to the "processed" directory
    move_to_processed(pdf_path)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert a PDF to SVG files, one per page.")
    parser.add_argument("pdf_file", help="Path to the input PDF file")

    # Parse arguments
    args = parser.parse_args()

    # Ensure necessary directories and process the PDF
    try:
        ensure_directories()
        pdf_path = locate_pdf_file(args.pdf_file)
        pdf_to_svg(pdf_path)
    except Exception as e:
        print(f"Error: {e}")
