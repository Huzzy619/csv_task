import json
import csv
import os
from hng import convert_hash, convert_to_dict, get_output_name 


def start():

    print("Hello and welcome")

    filepath = input(
        "Enter the file path of filename(if file is in current dir): ")

    process_file(filepath)

    print("""
    
    Loading ...........................

    your file has been processed successfully.

    and a <filename>.output.csv file have been created in the current working directory.

    All Json files have been stored in a 'JSON' directory 
    
    """)


def process_file(filepath):

    data = []
    # The sum of the entire entries minus the header
    total_entries = sum(1 for _ in open(filepath)) - 1

    try:
        # Initial Opening of the csv file
        with open(filepath, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:

                # Convert keys to lowercase
                row = {key.lower(): val for key, val in row.items()}
                value = row['filename']+'.json'
                row['hash'] = convert_hash(value)
                row['format'] = "CHIP-0007"
                row['series_total'] = total_entries
                row['sensitive_content'] = False

                temp = row['attributes']
                row['attributes'] = convert_to_dict(row['attributes'])

                try:
                    # attempt to cast to int
                    row['series number'] = int(row['series number'])

                except:  # FileNotFoundError:
                    # if a non-number value is encountered, just skip and continue
                    continue

                # first create a folder to store the json files
                if not os.path.isdir('JSON'):
                    os.mkdir('JSON')

                # converts each row entry to a json
                with open(os.path.join('JSON', row['filename']+'.json'), 'w', encoding='utf-8') as jsonfile:
                    jsonfile.write(json.dumps(row, indent=4))

                # Remove the unnecessary values added before sending it to the new output csv.
                row['attributes'] = temp
                del row['format']
                del row['series_total']
                del row['sensitive_content']

                data.append(row)

        # Get the list of fieldnames/keys/columns
        fields = list(data[0].keys())

        # sends the updated data into a new csv file
        filename = get_output_name(filepath)
        with open(filename+'.output.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        print("\nerror: Invalid file path")
        print("Please confirm that the file path or file name is correct")

        exit()
    except PermissionError:
        print("\nError!!!")
        print("Kindly close the former csv file so the new one can be saved.\n")
        exit()


# kick start the application
start()
