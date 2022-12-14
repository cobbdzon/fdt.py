@echo off

echo -----------------------------------------------
echo welcome to fdt.py
echo https://github.com/cobbdzon/fdt.py
echo make sure to put the dataset in the config.json
echo -----------------------------------------------

set /p "name=enter a valid filename: "
set /p "classes=enter a valid number for the number of classes: "

cd "../"
echo creating frequency distribution table
python "%cd%\src\init.py" %name% %classes%
echo opening file directory
explorer /select,"%cd%\src\out\%name%.xlsx"