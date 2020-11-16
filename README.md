# Photometric report to CSV converter

### Reason for it's existence

When you work in LED lighting QC, what you're going to get is a lot of PDF files with spectrophotometer report. As they would come in different formats from different equipment and often in different languages as well, it becomes increasingly hard to analyze the data. If only it was some sort of a spreadsheet... and this project is meant to produce exacly such a spreadsheet. Well, CSV.

### Acknowledgements
This little script would be impossible without:

* The [pdfminer.six](https://github.com/pdfminer/pdfminer.six) library, which enables the core functionality.
* Python language, which enables _all_ functionality of this project.
* Tkinter library, which provides the GUI.

### Usage

_At least Python 3.8 is recommended as the script was not tesed with earlier versions. Should work fine, though. 

Pipenv is used for virtual environment management._

Either run `python main.py` to use the GUI or run extractor.py from the CLI:

`python extractor.py -h` for help

`python extractor.py -i input_dir -o output_dir -f filename.csv` to process PDF reports from **input_dir** folder and write the resulting CSV to **file.csv** in **output_dir** folder.

Multi-page PDF reports are supported.

***Note:*** You will need to edit regex definitions in _parser/photometers.py_ to match your needs. 
