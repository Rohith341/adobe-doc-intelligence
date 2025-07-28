# Round 1B – Persona-Driven Document Intelligence

## Overview
This module extracts and ranks relevant sections from a collection of PDFs based on a persona and job-to-be-done, as required for Round 1B of the Adobe India Hackathon 2025.

## Approach
- Uses the outline extractor to segment documents into sections (Title, H1, H2, H3).
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
docker run --rm -e PERSONA="PhD Researcher in Computational Biology" -e JOB="Prepare a comprehensive literature review..." -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomidentifier
```
- Place input PDFs in `input/`.
- Output JSONs will appear in `output/`.
- The persona-driven output will be in `output/persona_output.json`. 

## Team
**Team Name:** Byte_codes

- Rohith Saindla (Team Leader)  
  Phone: +919014850368
- Sreeja Rayarakula  
  Phone: +916305549167
- Akshay Kumar Kandunuri  
  Phone: +918885128254 