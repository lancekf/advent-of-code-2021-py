import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

def listDiff(baseString, *minusStrings):
    diff = set(baseString)
    for s in minusStrings:
        diff = diff.difference(set(s))
    return diff

def findDigit(signals, startLength, endLength, *minusSignals):
    found = None
    for signal in signals:
        if len(signal) == startLength:
            diff = listDiff(signal, *minusSignals)
            if len(diff) == endLength:
                assert not found
                found = signal
    assert found
    return found

def removeString(stringList: list, string):
    if string in stringList:
        stringList.remove(string)
        if string in stringList:
            removeString(stringList, string)

def sortSignal(signal):
    return "".join(sorted(signal))

def sortSignals(signals):
    return [sortSignal(s) for s in signals]

def calculateSignals(signals):
    unique = {2:1, 4:4, 3:7, 7:8}
    signalMap = {} # digit:signal
    for signal in signals:
        try:
            digit = unique[len(signal)]
            signalMap[digit] = signal
        except:
            pass

    removeString(signals, signalMap)
    # unique (1, 4, 7, 8) are known

    # 6 = of 6, minus 1, find 5 segments
    # 0 = of 6, minus 4, find 3 ---
    # 9 = remaining 6

    # 2 = of 5, minus 9, find 1
    # 3 = of 5, minus 6, find 1
    # 5 = remaining 5

    signalMap[6] = findDigit(signals, 6, 5, signalMap[1])
    removeString(signals, signalMap[6])
    signalMap[0] = findDigit(signals, 6, 3, signalMap[4])
    removeString(signals, signalMap[0])
    signalMap[9] = findDigit(signals, 6, 6, "")
    removeString(signals, signalMap[9])

    signalMap[2] = findDigit(signals, 5, 1, signalMap[9])
    removeString(signals, signalMap[2])
    signalMap[3] = findDigit(signals, 5, 1, signalMap[6])
    removeString(signals, signalMap[3])
    signalMap[5] = findDigit(signals, 5, 5, "")
    removeString(signals, signalMap[5])

    return signalMap


def main():

    total = 0
    for line in input:
        split = line.split(' | ')

        signalMap = calculateSignals(sortSignals(split[0].split(' ')))

        print(signalMap)

        output = ""
        for s in sortSignals(split[1].split(" ")):
            for digit, signal in signalMap.items():
                if signal == s:
                    output += str(digit)
        
        total += int(output)

    print(total)

main()