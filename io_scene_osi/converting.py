import subprocess
import os.path
import ntpath

def convert(inFile, outFile):
    sarcExtractPath = os.path.dirname(os.path.realpath(__file__)) + "/SARCExtract/SARCExtract.exe"
    converterPath = os.path.dirname(os.path.realpath(__file__)) + "/BFRES2OBJ/BFRES2OBJ.exe"
    p = subprocess.Popen([sarcExtractPath, inFile], stdout=subprocess.PIPE)
    waiting = p.wait()
    inFile2 = inFile[:-4]
    inFile2 = inFile2 + "/" + ntpath.basename(inFile2) + ".bfres"
    p2 = subprocess.Popen([converterPath, inFile2, outFile])
    waiting = p2.wait()
    return True
