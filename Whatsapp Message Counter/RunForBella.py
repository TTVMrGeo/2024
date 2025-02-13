file_path = 'Bella.txt'

count1 = 0
count2 = 0

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            count1 += line.count("Aidan:")
            count2 += line.count("Astrid Bean 🔒🤍:")
except FileNotFoundError:
    print(f"The file {file_path} was not found.")

print(f"""Stats for Aidan and Bella: 
      Aidan {count1}.
      Bella {count2}.
      The total message count is {count1 + count2}""")