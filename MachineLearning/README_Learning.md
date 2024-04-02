# AI Models: NIM and Shopping

This repository contains implementations of two AI models: NIM and Shopping. Both models are implemented in Python and aim to demonstrate various AI concepts and techniques.

## NIM

The NIM model implements the game of Nim, a mathematical game of strategy where players take turns removing objects from distinct heaps. The last player to remove an object wins the game. The NIM model includes features such as:

- **NIM Game Logic**: Implements the rules and logic of the NIM game.
- **NIM AI**: Includes an AI player trained using Q-learning to make optimal moves in the game.
- **Command-line Interface**: Provides a command-line interface for playing against the AI or training the AI model.

## Shopping

The Shopping model is designed to predict whether a customer will make a purchase based on various features related to their browsing behavior on an e-commerce website. It utilizes a K-nearest neighbors classifier to make predictions. Key features of the Shopping model include:

- **Data Preprocessing**: Processes and cleans the shopping data to prepare it for training the classifier.
- **K-nearest Neighbors Classifier**: Implements a classifier to predict purchase behavior based on input features.
- **Evaluation Metrics**: Evaluates the performance of the classifier using metrics such as sensitivity and specificity.
- **Command-line Interface**: Provides a command-line interface for training the model and making predictions.

## Requirements

- Python 3.x
- pandas
- scikit-learn

## Usage

1. Clone the repository:

```bash
git clone https://github.com/AlxBlzrv/CS50-AI.git
```

2. Navigate to the project directory:

```bash
cd Learning
```

3. Run the desired model script:

For NIM:

```bash
python NIMLogic.py
```

For Shopping:

```bash
python shop.py shopping.csv
```


## Contributions

Contributions to this project are welcome! If you have ideas for improvements or enhancements, feel free to open an issue or submit a pull request.

## License

This project is an educational endeavor and is not licensed. Feel free to clone, modify, and share it for educational purposes.

---
