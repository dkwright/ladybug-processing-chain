# This script will execute ladybugProcessStream tool
# Call the script with two parameters in order
# input_file output_folder
# Example
# python scripts/python_arguments.py "Z:\\data\\Ladybug\\Sample_Image_Sequence\\01_12282021_092201-000001.pgr" "Z:\\data\\Ladybug\\output2\\"

import sys
import subprocess

input_file = sys.argv[1]
output_folder = sys.argv[2]

def process_stream(input_file, output_folder):
    try:
        subprocess.call(["C:\\Program Files\\Teledyne\\Ladybug\\bin64\\ladybugProcessStream.exe", "-i", input_file, "-o", output_folder])
    except Exception as error:
        print("An exception occurred:", type(error).__name__)

process_stream(input_file, output_folder)