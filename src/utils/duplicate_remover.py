import csv

def remove_duplicates(words):
    unique_words = set(words)

    return list(unique_words)

filename = "data.csv"

assets = []

with open(filename, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            assets.append(row[0])

all_assets = remove_duplicates(assets)

filewrite = "duplicates_removed.csv"


with open(filewrite, mode='w', newline='') as file:
    writer = csv.writer(file)
    for asset in all_assets:
        writer.writerow([asset])

print(f"CSV file '{filename}' written successfully.")
