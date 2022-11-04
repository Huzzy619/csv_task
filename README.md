
# HNGi9 CLI PROGRAM




## 🚀 About Me
I'm a full stack developer...


## Author

- [@Huzzy-K](https://www.github.com/Huzzy619)


## Run Locally

Clone the project

```bash
~$ git clone https://link-to-project.git
```

Navigate to project directory

```bash
~$  cd csv_task
```

Then execute project on command line


```bash
~/csv_task$: python main.py   
```




## Features
- Opening csv files
- Instant creation of Json files
- Generation of new Hash column in an output csv file
- Can run on any computer with python installed


## Documentation

[Documentation](https://linktodocumentation)

This Script is written in Python. 


```bash
Hello and welcome
Enter the file path or filename(if file is in current dir): <input>
```
I
The <input> value that is expected is either a filepath e.g `C:\Users\user\Documents\Projects\HNG\csv_task\happy.csv` or file name `happy.csv`

`Note` file names alone can only be used if the file is in same directory with the `main.py` else a FileNotFound exeception would be raised
```bash

error: Invalid file path
Please confirm that the file path or file name is correct
```


If a proper file name or path is inputed, Json files with format `CHIP-0007` will be created and stored in `/JSON/` folder in the current working directory.
A new csv `<filename>.output.csv` will also be created. it will have an additional column `Hash` containing the encoded sha256 hex_value of its corresponding Json file.

```bash
    your file has been processed successfully.

    and a <filename>.output.csv file have been created in the current working directory.

    All Json files have been stored in a 'JSON' directory
```

`Note`
    If the ouput file is open in any editor, aand you attempt to run main.py with the same csv file again, it will throw a PermissionError.
    Endeavour to close any open file before repeating the procedure if you have to.

```bash
    Error!!!
    Kindly close the former csv file so the new one can be saved.
```