from transformers import pipeline
import re

# Load NER pipeline (you can disable or remove if not needed)
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

def extract_entities(text):
    entities = []
    course_blocks = text.strip().split("\n\n")

    for block in course_blocks:
        # Supports any 4-letter prefix with 3-digit number (e.g., BUFN722)
        course_id_match = re.search(r"course ([A-Z]{4}\d{3})", block, re.IGNORECASE)
        title_match = re.search(r"titled '([^']+)'", block)
        professor_match = re.search(r"taught by ([^\.]+)", block)
        time_match = re.search(r"meets at ([^\.]+)", block)  # update to match your current text format
        desc_match = re.search(r"Description: (.*)", block)

        if course_id_match:
            course_id = course_id_match.group(1).strip().upper()

            if title_match:
                entities.append((course_id, "has_title", title_match.group(1).strip()))
            if professor_match:
                entities.append((course_id, "taught_by", professor_match.group(1).strip()))
            if time_match:
                entities.append((course_id, "scheduled_at", time_match.group(1).strip()))
            if desc_match:
                desc = desc_match.group(1).strip()
                for keyword in re.findall(r"\b\w{4,}\b", desc):  # 4+ letter words as keywords
                    entities.append((course_id, "related_to", keyword))

    return entities
