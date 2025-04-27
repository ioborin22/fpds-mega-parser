import os
import json

# Paths
base_folder = r'D:\data'
output_folder = r'C:\Users\iobor\Projects\fpds'
output_file = os.path.join(output_folder, 'unique_vars_with_dates.txt')

# Prepare
unique_keys = {}  # key: (value, date)
total_files = 0
processed_files = 0

# Walk through year folders
for year_folder in os.listdir(base_folder):
    year_path = os.path.join(base_folder, year_folder)

    if not os.path.isdir(year_path):
        continue
    if not year_folder.isdigit() or len(year_folder) != 4:
        continue  # Only folders like 2025, 2024

    for file_name in os.listdir(year_path):
        if '_missing_' not in file_name:
            continue

        parts = file_name.split('_missing_')[0]
        if '_' not in parts:
            continue
        mm_dd = parts.split('_')
        if len(mm_dd) != 2:
            continue
        mm, dd = mm_dd
        date = f"{year_folder}-{mm}-{dd}"

        file_path = os.path.join(year_path, file_name)
        total_files += 1

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
        except Exception as e:
            print(f"⚠️ Error reading {file_path}: {e}")
            continue

        processed_files += 1
        print(f"🔎 Scanning file {processed_files}/{total_files}: {file_name}")

        # Collect all key-value pairs, but only first occurrence of each key
        for key, value in content.items():
            if key not in unique_keys:
                unique_keys[key] = (value, date)

# Save to output
if unique_keys:
    os.makedirs(output_folder, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        for key, (value, date) in unique_keys.items():
            f.write(f'"{key}": "{value}" - {date}\n')
    print(f"\n✅ Unique variables saved to {output_file}")
else:
    print("⚠️ No matching data found.")
