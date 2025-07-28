# Approach Explanation – Round 1A

## Overview
This document explains the methodology for extracting a structured outline from PDFs for Round 1A of the Adobe India Hackathon 2025.

## Methodology
- **PDF Parsing:** We use PyMuPDF to extract text, font size, and style from each page.
- **Title Extraction:** The largest text on the first page (or PDF metadata) is used as the document title.
- **Heading Detection:** Font size heuristics are used: the most common font size is considered body text, and larger sizes are mapped to H1, H2, H3.
- **Output:** The outline is output as a JSON file with title and headings (level, text, page number).

## Libraries Used
- PyMuPDF
- scikit-learn, numpy, pandas 