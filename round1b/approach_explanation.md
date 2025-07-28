# Approach Explanation – Round 1B

## Overview
This document details the methodology and design choices for our solution to the Adobe India Hackathon 2025 "Connecting the Dots" challenge, specifically for Round 1B: Persona-Driven Document Intelligence.

## Methodology

### 1. Document Segmentation
We process each PDF using our outline extractor, segmenting the document into a hierarchy of sections and headings (Title, H1, H2, H3) using font size and style analysis with PyMuPDF.

### 2. Semantic Representation
For persona-driven extraction, we use the MiniLM model from the sentence-transformers library. This model is lightweight (~80MB), fast, and supports multilingual text, making it ideal for offline, CPU-only environments.

### 3. Relevance Ranking
We encode both the persona/job description and each document section into semantic embeddings. Using cosine similarity, we rank all sections by their relevance to the persona and job-to-be-done.

### 4. Sub-section Analysis
For the top-ranked sections, we further extract and analyze sub-sections (or provide refined summaries) to give a more granular view of the content most relevant to the persona’s task.

### 5. Output Formatting
The final output is a structured JSON containing:
- Metadata (input documents, persona, job, timestamp)
- Ranked sections with importance scores
- Sub-section analysis for deeper insights

## Models and Libraries
- PyMuPDF
- sentence-transformers (MiniLM)
- scikit-learn, numpy, pandas

## Design Choices
- Modularity: Outline extraction and persona-driven logic are reusable and extensible.
- Performance: All processing is local and optimized for speed, ensuring compliance with runtime and resource constraints.
- Multilingual Support: MiniLM enables handling of non-English documents.

## Limitations and Future Work
- Heading detection may be less accurate in highly unstructured or visually complex PDFs.
- Sub-section analysis is currently based on section granularity; future work could include more advanced summarization or question-answering. 