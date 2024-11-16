# PDF Conversion Tools

This repository contains two Python scripts for converting PDF files into different formats:

1. **`pdf2svg.py`**: Converts each page of a PDF into individual SVG files.
2. **`pdf2ppt.py`**: Converts a PDF into a PowerPoint (PPTX) presentation, with each page as a slide.

---

## Features

### `pdf2svg.py`

- Converts PDF pages to individual SVG files.
- Checks for the input file in both the root directory and the `input` directory.
- Automatically moves processed PDF files to a `processed` directory.
- Creates a timestamped output directory, such as `1692310452_output_svg`, for SVG files.

### `pdf2ppt.py`

- Converts PDF pages to images and embeds them into PowerPoint slides.
- Checks for the input file in both the root directory and the `input` directory.
- Automatically moves processed PDF files to a `processed` directory.
- Creates a timestamped output directory, such as `1692310452_output_ppt`, for the PowerPoint file.

---

## Requirements

Both scripts require the following dependencies:

- Python 3.6 or later
- `PyMuPDF` for `pdf2svg.py`
- `pdf2image`, `python-pptx`, and `Pillow` for `pdf2ppt.py`

Install all dependencies with:

```bash
pip install pymupdf pdf2image python-pptx pillow
```

---

## Usage

### **1. Directory Structure**

Ensure the following directories exist or let the script create them automatically:

- `input`: Place your PDF files here (if not already in the root directory).
- `processed`: Processed PDF files will be moved here after conversion.

### **2. `pdf2svg.py`**

Convert a PDF to SVG files, one for each page.

#### **Run the Script**

```bash
python3 pdf2svg.py my_document.pdf
```

#### **Output**

- The SVG files will be saved in a directory named with the Unix timestamp, such as `1692310452_output_svg`.
- The processed PDF will be moved to the `processed` directory.

---

### **3. `pdf2ppt.py`**

Convert a PDF to a PowerPoint presentation (PPTX), with each page as a slide.

#### **Run the Script**

```bash
python3 pdf2ppt.py my_document.pdf
```

#### **Output**

- The PowerPoint file will be saved in a directory named with the Unix timestamp, such as `1692310452_output_ppt/output.pptx`.
- The processed PDF will be moved to the `processed` directory.

---

## Examples

### Convert PDF to SVG Files

```bash
python3 pdf2svg.py my_document.pdf
```

Output: SVG files in a directory named something like `1692310452_output_svg`.

### Convert PDF to PowerPoint

```bash
python3 pdf2ppt.py my_document.pdf
```

Output: PowerPoint file in a directory named something like `1692310452_output_ppt/output.pptx`.

---

## Notes

- If the PDF file is not in the root or `input` directory, the script will raise an error.
- Directories (`input`, `processed`, and output directories) are created automatically if they don’t exist.

---

## Troubleshooting

### Blank SVG Files

- Ensure the PDF contains vector graphics (text, paths, shapes) and not rasterized content.
- Use a tool like `pdfinfo` to inspect the PDF.

### Missing Dependencies

Install the required Python libraries:

```bash
pip install pymupdf pdf2image python-pptx pillow
```

---

## License

This repository is distributed under the MIT License. Feel free to use, modify, and distribute it.
