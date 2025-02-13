file_path = 'Nolifers.txt'

counts = {
    "Aidan: ": 0,
    "Ivan: ": 0,
    "Jaedie: ": 0,
    "Nica: ": 0,
    "Robin: ": 0,
    "Abigail: ": 0,
    "Adrian: ": 0,
    "Amber: ": 0,
    "Ané: ": 0,
    "Angelo: ": 0,
    "Carli: ": 0,
    "Chloë: ": 0,
    "Cuan: ": 0,
    "Eunice Ras: ": 0,
    "Ewan: ": 0,
    "Jayden: ": 0,
    "JayJay: ": 0,
    "Jeandry: ": 0,
    "Jenu: ": 0,
    "Josh: ": 0,
    "Kealley: ": 0,
    "Kean: ": 0,
    "Kei: ": 0,
    "Kian: ": 0,
    "Keilah: ": 0,
    "Kiki: ": 0,
    "Lea: ": 0,
    "Bob: ": 0,
    "Markus: ": 0,
    "Mathew: ": 0,
    "Mayla: ": 0,
    "Mina: ": 0,
    "Mya: ": 0,
    "Nicolene: ": 0,
    "Philip: ": 0,
    "Rea: ": 0,
    "Reihardt: ": 0,
    "Reuben: ": 0,
    "Ronan: ": 0,
    "Rowan: ": 0,
    "Sumia: ": 0,
    "Tristan Swanepeol: ": 0,
    "Zander: ": 0,
    "+27 66 493 1277: ": 0
}

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for key in counts:
                counts[key] += line.count(key)
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
    
# Sorting the counts dictionary by values (count) in descending order
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

print("All Messages Accurately Counted:")
for name_or_number, count in sorted_counts:
    print(f"\t{name_or_number}{count}")