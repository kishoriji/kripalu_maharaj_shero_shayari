import json
import re


def process_shayari_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the file content into distinct blocks using double newlines
    raw_blocks = content.split('\n\n')

    unique_shayaris = []
    seen = set()

    for block in raw_blocks:
        # 1. Remove bold formatting (**)
        clean_text = block.replace('**', '')

        # 2. Remove parenthetical comments (text inside parentheses)
        clean_text = re.sub(r'\(.*?\)', '', clean_text)

        # 3. Clean up whitespace and empty lines
        lines = [line.strip() for line in clean_text.split('\n') if line.strip()]

        if lines:
            # 4. Join the lines with a comma to keep continuity as requested
            joined_shayari = ", ".join(lines)

            # 5. Add to list if not a duplicate
            if joined_shayari not in seen:
                unique_shayaris.append(joined_shayari)
                seen.add(joined_shayari)

    return json.dumps(unique_shayaris, ensure_ascii=False, indent=2)


# Run the process
json_output = process_shayari_file('shayari.txt')

# Print the result to console
print(json_output)

