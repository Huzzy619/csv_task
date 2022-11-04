import json
import csv
import os
from hng import Helper


def start():

    print("Hello and welcome")

    filepath = input(
        "Enter the file path or filename(if file is in current dir): ")

    process_file(filepath)

    print("""
    
    Loading ...........................

    your file has been processed successfully.

    and a <filename>.output.csv file have been created in the current working directory.

    All Json files have been stored in a 'JSON' directory 
    
    """)


def process_file(filepath):

    data = []
    help_to = Helper()

    try:
        # The sum of the entire entries minus the header
        total_entries = sum(1 for _ in open(filepath)) - 1

        # Initial Opening of the csv file
        with open(filepath, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:

                # Convert keys to lowercase
                row = {key.lower(): val for key, val in row.items()}

                row['hash'] = help_to.convert_hash(row['filename']+'.json')

                temp = row['attributes']
                row['attributes'] = help_to.convert_to_dict(row['attributes'])

                row['series number'] = int(row['series number'])

                # first create a folder to store the json files
                if not os.path.isdir('JSON'):
                    os.mkdir('JSON')

                chip_json_format = {
                    "format": "CHIP-007",
                    "name": row["name"],
                    "minting_tool": row["team names"],
                    "sensitive_content": False,
                    "series_number": row['series number'],
                    "series_total": total_entries,
                    "uuid": row['uuid'],
                    "attributes": row['attributes'],
                    "collection": {
                        "name": "Zuri NFT Tickets for Free Lunch",
                        "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
                        "attributes": [
                            {
                                "type": "description",
                                "value": "Rewards for accomplishments duringHNGi9."
                            }
                        ]
                    }
                }


                # converts each row entry to a json
                with open(os.path.join('JSON', row['filename']+'.json'), 'w', encoding='utf-8') as jsonfile:
                    jsonfile.write(json.dumps(chip_json_format, indent=4))

                # Restore the initial attributes.
                row['attributes'] = temp

                data.append(row)

        # Get the list of fieldnames/keys/columns
        fields = list(data[0].keys())

        # sends the updated data into a new csv file
        filename = help_to.get_output_name(filepath)
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
