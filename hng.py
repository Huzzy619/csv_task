import json
import hashlib
import csv
import os
import ntpath


def convert_hash(value):
    encoded = value.encode()

    result = hashlib.sha256(encoded).hexdigest()

    return result


def get_output_name(path):

    head, tail = ntpath.split(path)  # extracts the filename from the path

    # removes the file extension

    if tail:
        file_name = tail.rsplit('.', 1)[0]

    else:
        file = ntpath.basename(head)
        file_name = file.rsplit('.', 1)[0]

    return file_name


def process_file(filepath):

    data = []
    total_entries = sum(1 for _ in open(filepath)) - 40

    try:
        # Initial Opening of the csv file
        with open(filepath, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:

                # Convert keys to lowercase
                row = {key.lower(): val for key, val in row.items()}

                row['hash'] = convert_hash(row['filename']+'.json')
                row['format'] = "CHIP-0007"
                row['series_total'] = total_entries
                row['sensitive_content'] = False

                try:
                    # attempt to cast to int
                    row['series number'] = int(row['series number'])

                except:  # FileNotFoundError:
                    # if a non-number value is encountered, just skip and continue
                    continue

                data.append(row)

                # first create a folder to store the json files
                if not os.path.isdir('JSON'):
                    os.mkdir('JSON')

                # converts each row entry to a json
                with open(os.path.join('JSON', row['filename']+'.json'), 'w', encoding='utf-8') as jsonfile:
                    jsonfile.write(json.dumps(row, indent=4))

        # Get the list of fieldnames/keys/columns
        fields = list(data[0].keys())

        # sends the updated data into a new csv file
        filename = get_output_name(filepath)
        with open(filename+'.output.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

    except:
        print("\nerror: Invalid file path")
        print("Please confirm that the file path or file name is correct")

        exit()


def start():
    print("Hello and welcome")

    filepath = input("Enter the file path: ")

    process_file(filepath)

    print("""
    
    Loading ...........................

    your file has been processed successfully.

    All Json files have been stored in a 'JSON' directory 
    """)


start()
