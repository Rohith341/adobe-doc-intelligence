import os
import json
from app.outline_extractor import OutlineExtractor

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf(pdf_path, output_path):
    extractor = OutlineExtractor(pdf_path)
    outline = extractor.extract_outline()
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(outline, f, ensure_ascii=False, indent=2)

def main():
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(INPUT_DIR, pdf_file)
        output_file = os.path.splitext(pdf_file)[0] + ".json"
        output_path = os.path.join(OUTPUT_DIR, output_file)
        process_pdf(pdf_path, output_path)

if __name__ == "__main__":
    main() 