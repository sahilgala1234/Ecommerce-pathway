# Befunge Generator

This repository contains a Python application that generates Befunge code to produce a given output. The application reads a text file containing the desired output and creates a Befunge program that produces the same output.

## Features
- Converts plain text into Befunge code.
- Optimized for the shortest possible Befunge code using an LLM.
- Outputs the Befunge code to a file.

## Requirements
- Python 3.7 or higher
- OpenAI Python library (for LLM integration)
- Docker (optional, for containerized execution)

## Setup

### Clone the Repository
```bash
git clone https://github.com/sahilgala1234/befunge-generator.git
cd befunge-generator
```

### Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key
```

Alternatively, set the environment variable directly:
```bash
export OPENAI_API_KEY=your-api-key
```

## Usage

### Run the Application
```bash
python main.py input.txt output.befunge
```
- **`input.txt`**: Path to the text file containing the desired output.
- **`output.befunge`**: Path where the generated Befunge code will be saved.

### Example
Given an `input.txt` containing:
```
Hello, World!
```
The application will generate Befunge code and save it in `output.befunge`. 

You can then use a Befunge interpreter to run the generated code:
```bash
python befunge_interpreter.py output.befunge
```

### Run with Docker

Build the Docker image:
```bash
docker build -t befunge-generator .
```

Run the container with volume mounts for input and output files:
```bash
docker run --rm -v $(pwd)/input.txt:/app/input.txt -v $(pwd)/output.befunge:/app/output.befunge befunge-generator
```

## Project Files

### `main.py`
This is the main application script. It:
- Reads the desired output from `input.txt`.
- Generates the Befunge code using an LLM.
- Writes the generated Befunge code to `output.befunge`.

### `befunge_interpreter.py`
A simple Befunge interpreter to validate the generated code.

### `requirements.txt`
Contains the Python dependencies:
```
openai
python-dotenv
```

