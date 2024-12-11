import sys
import os
from llm_interface import generate_befunge_code

def main(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} does not exist.")
        sys.exit(1)
    
    with open(input_file, 'r') as f:
        target_output = f.read()
    
    print("Generating Befunge code...")
    befunge_code = generate_befunge_code(target_output)
    
    with open(output_file, 'w') as f:
        f.write(befunge_code)
    
    print(f"Befunge code written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
