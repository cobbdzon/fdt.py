import sys
import sys
import os
import json
import math
import xlsxwriter

def inRange(x, min, max) -> bool:
    return (x >= min and x <= max)

def average(numList: list) -> float:
    return sum(numList)/len(numList)

def getConfig():
    with open(os.path.join(sys.path[0], "config.json"), "r") as f:
        return json.load(f)

outputNameArg = None
numberOfClassesArg = None
try:
    outputNameArg = str(sys.argv[1])
    numberOfClassesArg = int(sys.argv[2])
except IndexError: pass

config: dict = getConfig()
data: list = config["data"]

# arg vs config
outputName = outputNameArg or config["outputName"] or "FDT"
numberOfClasses = numberOfClassesArg or config["numberOfClasses"] or 1

data.sort()

def getClassWidth() -> int:
    lowest = data[0]
    highest = data[-1]
    return math.ceil((highest - lowest) / numberOfClasses)

def getClassIntervals() -> list:
    lowest = data[0]
    highest = data[-1]
    classWidth = getClassWidth()
    
    last = lowest - 1
    out = []

    for classNumber in range(1, numberOfClasses + 1):
        lower = last + 1
        higher = lower + classWidth - 1
        last = higher
        out.append([lower, higher])
    
    return out

# write
workbook = xlsxwriter.Workbook("src/out/" + outputName + ".xlsx")
worksheet = workbook.add_worksheet("firstSheet")

classIntervals = getClassIntervals()

worksheet.write(0, 0, "Class Interval (ci)")
worksheet.write(0, 1, "Class Mark (x)")
worksheet.write(0, 2, "Class Boundary (cb)")
worksheet.write(0, 3, "Frequency (f)")
worksheet.write(0, 4, "Relative Frequency")
worksheet.write(0, 5, "Less Than Cumulative Frequency (<cf)")
worksheet.write(0, 6, "Greater Than Cumulative Frequency (>cf)")

__freqdata = data.copy()
lastFreq = 0
lessThanCF = 0
greaterThanCF = len(data)
for row in range(0, len(classIntervals)):
    classInterval = classIntervals[row]
    worksheet.write(row + 1, 0, str(classInterval[0]) + "-" + str(classInterval[1]))
    worksheet.write(row + 1, 1, average(classInterval))
    worksheet.write(row + 1, 2, str(classInterval[0] - 0.5) + "-" + str(classInterval[1] + 0.5))

    #frequency
    frequency = 0
    displacement = 0
    for i in range(0, len(__freqdata)):
        i = i - displacement
        v = __freqdata[i]
        if type(v) == int and inRange(v, classInterval[0], classInterval[1]):
            frequency += 1
            __freqdata.pop(i)
            displacement += 1

    worksheet.write(row + 1, 3, frequency)
    worksheet.write(row + 1, 4, frequency / len(data))

    lessThanCF += frequency
    greaterThanCF -= lastFreq
    worksheet.write(row + 1, 5, lessThanCF)
    worksheet.write(row + 1, 6, greaterThanCF)

    lastFreq = frequency

__freqdata = None
lastFreq = None

workbook.close()