import os

# Paths
base_folder = r'D:\data'
output_folder = r'C:\Users\iobor\Projects\fpds'
output_file = os.path.join(output_folder, 'drop.py')

# Collect dates
dates = []

# Walk through year folders
for year_folder in os.listdir(base_folder):
    year_path = os.path.join(base_folder, year_folder)
    
    if not os.path.isdir(year_path):
        continue
    if not year_folder.isdigit() or len(year_folder) != 4:
        continue  # Only folders like 2025, 2024
    
    for file_name in os.listdir(year_path):
        if '_missing_' in file_name:
            parts = file_name.split('_missing_')[0]
            if '_' in parts:
                mm_dd = parts.split('_')
                if len(mm_dd) == 2:
                    mm, dd = mm_dd
                    full_date = f"{year_folder}-{mm}-{dd}"  # ← with dashes!
                    dates.append(full_date)

# Create final script content
if dates:
    os.makedirs(output_folder, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('import requests\n')
        f.write('import time\n\n')
        f.write('# Список всех партиций\n')
        f.write('partitions = [\n')
        for date in sorted(set(dates)):
            f.write(f"    '{date}',\n")
        f.write(']\n\n')
        f.write('for part in partitions:\n')
        f.write('    query = f"ALTER TABLE fpds_clickhouse.raw_contracts DROP PARTITION \'{part}\';"\n')
        f.write('    print(f"⏳ Executing: {query.strip()}")\n')
        f.write('    response = requests.post(\n')
        f.write('        "http://localhost:8123",\n')
        f.write('        data=query,\n')
        f.write('        auth=(\'default\', \'\')\n')
        f.write('    )\n')
        f.write('    print(f"✅ Response: {response.text.strip() or \'OK\'}")\n')
        f.write('    time.sleep(3)\n')

    
    print(f"✅ Python script generated: {output_file}")
else:
    print("⚠️ No matching files found.")
