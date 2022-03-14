import Scrape
from Scrape import *

__BUFFER_SIZE_VALID__ = 100
__BUFFER_SIZE_INVALID__ = 100
__DEBUG_CUTOFF__ = 10
__TOTAL_LINES__ = 565345 # lazy
__FILE_SOURCE__ = 'Data/ohmodhulls.txt'
__FILE_VALID__ = 'Data/valid.csv'
__FILE_INVALID__ = 'Data/invalid.txt'
__FILE_CONFIG__ = 'Data/config.txt'

bufferValid = []
bufferInvalid = []
recordCount = 0

def Run():
    global __BUFFER_SIZE_VALID__, __DEBUG_CUTOFF__, __FILE_VALID__, __FILE_INVALID__
    global bufferValid, bufferInvalid, recordCount

    print("Valid buffer size: " + str(__BUFFER_SIZE_VALID__))
    print("Invalid buffer size: " + str(__BUFFER_SIZE_INVALID__) + '\n')

    firstRun = True

    with open(__FILE_SOURCE__, "r") as ids:
        for id in ids:
            if firstRun:
                # Remove encoding bullshit
                id = id.lstrip('\ufeff')
                firstRun = False

            # Pull record, removing trailing return
            csv = Scrape.PullCSV(id.rstrip('\n'))

            if csv == 'BAD RECORD':
                bufferInvalid.append(id.rstrip('\n'))
            else:
                bufferValid.append(csv)

            # Increment regardless of record validity
            recordCount += 1

            # Record last record in case of crash
            WriteLastRecord(id)

            # Check for buffer(s) reaching cap
            if len(bufferValid) >= __BUFFER_SIZE_VALID__:
                WriteBuffer('valid')

            if len(bufferInvalid) >= __BUFFER_SIZE_INVALID__:
                WriteBuffer('invalid')

            # Prevent doing entire list while testing
            if recordCount >= __DEBUG_CUTOFF__:
                break

        # Write whatever is left in both buffers
        WriteBuffer('valid')
        WriteBuffer('invalid')

        print('Done')

def WriteBuffer(bufferType):
    global __FILE_VALID__, __FILE_INVALID__, __TOTAL_LINES__
    global bufferValid, bufferInvalid, recordCount

    outputFile = open('Data/valid.csv', 'a')

    if bufferType == 'valid':
        # Set correct file
        outputFile = open(__FILE_VALID__, 'a')

        # Loop through all valid entries in buffer with counter
        count = 0
        for entry in bufferValid:
            outputFile.write(entry + '\n') # manual newline
            count += 1

        # Reset buffer
        bufferValid = []

        print('[BUFFER] Success: Wrote ' + str(count) + ' valid records')
    elif bufferType == 'invalid':
        # Set correct file
        outputfile = open(__FILE_INVALID__, 'a')

        # Loop through all entries in invalid buffer with counter
        count = 0
        for entry in bufferInvalid:
            outputfile.write(entry + '\n') # manual newline
            count += 1

        # Reset buffer
        bufferInvalid = []

        print('[BUFFER] Success: Wrote ' + str(count) + ' invalid records')
    else:
        print('[BUFFER] Fail: Buffer type invalid')

    outputFile.close()

    progressPercent = round((recordCount / __TOTAL_LINES__) * 100, 3)
    print('[PROGRESS] ' + str(recordCount) + ' / ' + str(__TOTAL_LINES__) + ': ' + str(progressPercent) + '%')

# Persists last record in case of crash
def WriteLastRecord(id):
    global recordCount

    outputFile = open(__FILE_CONFIG__, "w")
    outputFile.write(id)
    outputFile.close()

# Clears valid and invalid output files
def ResetAll():
    global __FILE_VALID__, __FILE_INVALID__

    outputFile = open(__FILE_VALID__, "w")
    outputFile.write('')
    outputFile.close()

    outputFile = open(__FILE_INVALID__, "w")
    outputFile.write('')
    outputFile.close()