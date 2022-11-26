# fdt.py
A "tool" written in [Python](https://www.python.org/downloads/) to generate Frequency Distribution Tables in .xlsx file format.

Made to make my life in Statistics class a little bit easier and just have an excuse to actually learn Python more.

## Dependencies
- [XlsxWriter](https://github.com/jmcnamara/XlsxWriter)

## Installation
### with Git
```
git clone https://github.com/cobbdzon/fdt.py.git
```

## Usage
In a terminal:
```
py "C:\...\fdt.py\src\init.py" [OUTPUT_NAME] [NUMBER_OF_CLASSES]
```
Replace the `...` to the directory of the fdt.py repository in your machine.

If either `[OUTPUT_NAME]` or `[NUMBER_OF_CLASSES]` are specified, their default values in `config.json` will be used instead.

You can find the outputted .xlsx files in the out folder inside src.

## Configuraton
An example of a proper `config.json` is shown below
```json
{
    "outputName": "FDT",
    "numberOfClasses": 6,
    "data": [
        69, 97, 76, 60, 35, 83, 63,
        67, 40, 85, 75, 49, 58, 55,
        59, 73, 43, 93, 38, 78, 71,
        55, 51, 70, 89, 61, 65, 65,
        72, 65, 75, 32, 64, 60, 75,
        89, 75, 65, 85, 87, 45, 75
    ]
}
```
| Config | Type | Description |
| -| - | - |
| outputName | string | The default file name of the .xlsx file that will be outputted by the script. |
| numberOfClasses | number | The default number of classes in the Frequency Distribution Table. |
| data | array\<number> | The data sample for the Frequency Distribution Table. |
