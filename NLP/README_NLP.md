# NLP Query Processor

This repository contains Python implementations of natural language processing (NLP) tools for processing queries and analyzing textual data. The project consists of two main components: `grammars.py` and `query.py`, each serving distinct functionalities in NLP.

## Project Structure

- **grammars.py**: Contains Python code for parsing sentences based on defined context-free grammars.
- **query.py**: Implements a query processor that analyzes and ranks text documents based on relevance to user queries.
- **README.md**: The file you are currently reading, providing an overview of the project.

## Features

### grammars.py
- **Parsing Sentences**: Parses sentences based on defined context-free grammars.
- **Noun Phrase Chunking**: Identifies and extracts noun phrase chunks from parsed sentences.

### query.py
- **File Loading**: Loads text files from a specified directory.
- **Tokenization**: Converts text documents into tokenized lists of words.
- **TF-IDF Computation**: Calculates TF-IDF values for words across documents.
- **Top File Matches**: Ranks and retrieves the top files matching a user query based on TF-IDF.
- **Top Sentence Matches**: Ranks and retrieves the top sentences matching a user query based on IDF and query term density.

## Requirements

- Python 3.x
- NLTK (Natural Language Toolkit)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/AlxBlzrv/CS50-AI.git
```

2. Navigate to the project directory:

```bash
cd NLP
```

### grammars.py

Run the `grammars.py` script by providing a sentence or a text file containing sentences:

```bash
python grammars.py
```

### query.py

Run the `query.py` script by specifying the directory containing text documents:

```bash
python query.py texts.txt
```

Follow the prompts to enter queries and view the results.

## Contributions

Contributions to this project are welcome! If you have ideas for improvements or enhancements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. Feel free to clone, modify, and share it for educational and non-commercial purposes.
