with open("words.txt", "r") as file:
    lines = file.readlines()

modified_lines = []
for line in lines:
    parts = line.split(" ", 1)
    if len(parts) > 1:
        first_word = parts[0]
        remaining_text = parts[1].lstrip()
        modified_line = f"{first_word} -{remaining_text}"
        modified_lines.append(modified_line)

with open("modified_words.txt", "w") as file:
    file.writelines(modified_lines)
