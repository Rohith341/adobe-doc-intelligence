# Round 1A – PDF Outline Extraction

## Overview
This module extracts a structured outline (Title, H1, H2, H3 with page numbers) from PDF files as required for Round 1A of the Adobe India Hackathon 2025.

## Approach
- Uses **PyMuPDF** to parse PDFs and extract text, font size, and style information.
- The document **title** is detected as the largest text on the first page (or from PDF metadata if available).
- **Headings (H1, H2, H3)** are detected using font size heuristics: the most common font size is considered body text, and larger sizes are mapped to heading levels.
- Each heading is output with its level, text, and page number in a clean JSON format.

## Models and Libraries Used
- **PyMuPDF (fitz):** Fast, robust PDF parsing and text extraction.
- **scikit-learn, numpy, pandas:** Utilities for data handling and processing.

## How to Build and Run

### Build (Docker)
```sh
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
```

### Run (Docker)
```sh
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomidentifier
```
- Place input PDFs in `input/`.
- Output JSONs will appear in `output/`. 