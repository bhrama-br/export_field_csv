import csv

def export_records(csv_file, qtd):
    exported = []

    remaining = []

    # Open CSV
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            first_name = row['Name (First)']
            last_name = row['Name (Last)']
            email = row['Email']

            if len(exported) < qtd:
                exported.append({'email': email, 'first_name': first_name, 'last_name': last_name})
            else:
                remaining.append(row)

    # Save exported record
    with open('exported.csv', 'w', newline='', encoding='utf-8') as export_file:
        fieldnames = ['email', 'first_name', 'last_name']
        csv_writer = csv.DictWriter(export_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(exported)

    # Save remaining record
    with open('remaining.csv', 'w', newline='', encoding='utf-8') as remaining_file:
        fieldnames = csv_reader.fieldnames
        csv_writer = csv.DictWriter(remaining_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(remaining)


# Achive CSV
csv_file = './remaining.csv'

# Number of records to be exported
qtd = 150

export_records(csv_file, qtd)
