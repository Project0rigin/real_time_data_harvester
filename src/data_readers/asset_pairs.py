import csv
def read_asset_pairs():
    csv_file = 'src/data/pairs.csv'
    data = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[0])

    return data

print(read_asset_pairs())
