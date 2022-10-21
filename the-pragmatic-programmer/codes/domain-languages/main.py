import re
from typing import Optional

def main (sourceFile:str) -> None:
    class Operation ():
        def __init__ (self, name, param = None):
            self.name = name
            self.param = param

    def parseLine (line:str) -> Optional[Operation]:
        parsableInstructions = re.match(r'^(.*?)#', line)
        if (parsableInstructions):
            executableSection = parsableInstructions.groups()[0]
            commandAndParams = executableSection.split()
            return Operation(*commandAndParams)

    sourceCode = []
    parsedCode = []
    with open(sourceFile, 'r') as fh:
        lines = fh.readlines()
        sourceCode.extend(lines)
        parsedCode.extend([ parseLine(line) for line in lines ])
    
    # do stuff with parsedCode

if __name__ == '__main__':
    main('sample.txt')
