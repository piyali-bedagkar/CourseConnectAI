import re
from PyPDF2 import PdfReader

def parse_pdf_to_txt(pdf_path):
    reader = PdfReader(pdf_path)
    raw_pdf_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    lines = raw_pdf_text.splitlines()

    structured_courses = []
    course_id, title, description, professor, time = "", "", "", "", ""
    buffer = []

    for line in lines:
        line = line.strip()

        # Accept any 4-letter course prefix followed by 3 digits
        course_match = re.match(r"^([A-Z]{4}\d{3})\s+(.+)", line)
        if course_match:
            # Save previous course if available
            if course_id and title:
                full_description = " ".join(buffer).strip()
                structured_courses.append(
                    f"The course {course_id} titled '{title}' is taught by {professor or 'Unknown'}."
                    f" It meets at {time or 'TBA'}. Description: {full_description}"
                )
            # Start new course block
            course_id, title = course_match.groups()
            professor, time, buffer = "", "", []
            continue

        # Try to extract professor or time
        if "Seats" in line and not professor:
            professor = line.split("Seats")[0].strip()
        elif re.search(r"\b(M|Tu|T|W|Th|F|Sa|Su)\b", line) and re.search(r"\d{1,2}:\d{2}", line):
            time = line.strip()
        elif any(skip in line for skip in ["Credits", "Restriction", "Location", "Waitlist", "ONLINE", "TBA", "Contact instructor"]):
            continue
        elif line:
            buffer.append(line)

    # Save the final course
    if course_id and title:
        full_description = " ".join(buffer).strip()
        structured_courses.append(
            f"The course {course_id} titled '{title}' is taught by {professor or 'Unknown'}."
            f" It meets at {time or 'TBA'}. Description: {full_description}"
        )

    # Write output
    output_path = "structured_courses_from_pdf.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(structured_courses))

    return output_path
