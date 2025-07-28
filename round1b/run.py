import os
import json
from app.outline_extractor import OutlineExtractor
from app.persona_extractor import PersonaExtractor

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

PERSONA = os.environ.get("PERSONA")
JOB = os.environ.get("JOB")

def process_pdf(pdf_path, output_path):
    extractor = OutlineExtractor(pdf_path)
    outline = extractor.extract_outline()
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(outline, f, ensure_ascii=False, indent=2)
    return outline

def main():
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
    outlines = []
    input_docs = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(INPUT_DIR, pdf_file)
        output_file = os.path.splitext(pdf_file)[0] + ".json"
        output_path = os.path.join(OUTPUT_DIR, output_file)
        outline = process_pdf(pdf_path, output_path)
        for o in outline["outline"]:
            o["document"] = pdf_file
        outlines.extend(outline["outline"])
        input_docs.append(pdf_file)
    if PERSONA and JOB and outlines:
        persona_extractor = PersonaExtractor(outlines, PERSONA, JOB)
        persona_output = persona_extractor.generate_output(input_docs)
        persona_output_path = os.path.join(OUTPUT_DIR, "persona_output.json")
        with open(persona_output_path, "w", encoding="utf-8") as f:
            json.dump(persona_output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main() 