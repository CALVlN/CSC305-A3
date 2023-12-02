import sys
import re
import numpy as np

def main(fileName):
    print("\n\n") # PRINT
    try:
        f = open(fileName, "r")
    except:
        quit()
    
    spherePattern = re.compile(r"SPHERE*")
    lightPattern = re.compile(r"LIGHT*")
    backPattern = re.compile(r"BACK*")
    ambientPattern = re.compile(r"AMBIENT*")
    outputPattern = re.compile(r"OUTPUT*")
    
    spheres = []
    lights = []
    back = []
    ambient = []
    output = []
    
    # print(f.read())
    lines = f.readlines()
    if len(lines) != 0:
        print("LIIIIINES")
        near = lines[0]
        left = lines[1]
        right = lines[2]
        bottom = lines[3]
        top = lines[4]
        res = lines[5]
        for line in lines[6:]:
            if spherePattern.search(line):
                words = [re.split(' ', line)]
                sphere = {}
                sphere['name'] = words[0][1]
                sphere['data'] = words[0]
                spheres.append(sphere)
                
                print(sphere)
            elif lightPattern.search(line):
                words = [re.split(' ', line)]
                light = {}
                light['name'] = words[0][1]
                light['data'] = words[0]
                lights.append(light)
                
                print(light)
            elif backPattern.search(line):
                back = [re.split(' ', line)]
                
                print(line)
            elif ambientPattern.search(line):
                ambient = [re.split(' ', line)]
                
                print(line)
            elif outputPattern.search(line):
                output = [re.split(' ', line)]
                
                print(output)
    
    try:
        with open("output[1]", 'w') as ppmFile:
            ppmFile.write("ambient[0]")
    except IOError as e:
        print(e)
        

if __name__ == '__main__':
    main("Assignment3-Tests-and-Keys/testAmbient.txt")