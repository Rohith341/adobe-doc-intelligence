# Adobe Document Intelligence – Connecting the Dots

## Overview
This project is a submission for the Adobe India Hackathon 2025 – "Connecting the Dots".  
It provides:
- **Round 1A:** PDF outline extraction (Title, H1, H2, H3 with page numbers)
- **Round 1B:** Persona-driven document intelligence (extract and rank relevant sections for a given persona and job)

## Approach

### Round 1A: PDF Outline Extraction
- We use **PyMuPDF** to parse PDFs and extract text, font size, and style information.
- The document **title** is detected as the largest text on the first page (or from PDF metadata if available).
- **Headings (H1, H2, H3)** are detected using font size heuristics: the most common font size is considered body text, and larger sizes are mapped to heading levels.
- Each heading is output with its level, text, and page number in a clean JSON format.

### Round 1B: Persona-Driven Document Intelligence
- We use the outline extractor to segment documents into sections.
- A lightweight, local **sentence-transformer model** (MiniLM) encodes both the persona/job description and document sections.
- Sections are ranked by semantic similarity to the persona/job, and the most relevant sub-sections are extracted.
- The output is a structured JSON with metadata, ranked sections, and sub-section analysis.

## Models and Libraries Used
- **PyMuPDF (fitz):** Fast, robust PDF parsing and text extraction.
- **sentence-transformers (MiniLM):** Efficient, multilingual semantic similarity for persona-driven ranking.
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

#### For Round 1B (Persona-Driven Extraction)
Add environment variables for persona and job:
```sh
docker run --rm -e PERSONA="PhD Researcher in Computational Biology" -e JOB="Prepare a comprehensive literature review..." -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomidentifier
```
- The persona-driven output will be in `output/persona_output.json`.

## Contact
- [Your Team Name & Contact Info] 