# Traffic Sign Recognition

This repository contains a Python implementation of a traffic sign recognition system using shallow and deep learning techniques with neural networks (NNs) and deep neural networks (DNNs). The project aims to classify different types of road signs based on images. The dataset used for training and testing consists of 43 categories of road signs.

## Project Structure

- **traffic.py**: Contains Python code for the traffic sign recognition system.
- **road_signs**: Contains 43 subdirectories, each representing a different type of road sign. Each subdirectory contains images of the corresponding road sign.
- **README.md**: The file you are currently reading, providing an overview of the project.

## Features

- **Data Loading**: Loads image data from the `road_signs` directory, organized into categories.
- **Data Preprocessing**: Resizes images to a specified width and height for consistency in model training.
- **Model Training**: Utilizes convolutional neural networks (CNNs) for training the recognition model.
- **Model Evaluation**: Evaluates the performance of the trained model on a separate test set.
- **Model Saving**: Optionally saves the trained model to a file for future use.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy
- TensorFlow
- scikit-learn

## Usage

1. Clone the repository:

```bash
git clone https://github.com/AlxBlzrv/CS50-AI.git
```

2. Navigate to the project directory:

```bash
cd NeuralNetwork
```

3. Run the main script with the data directory path:

```bash
python traffic.py road_signs
```

Optionally, you can also specify a filename to save the trained model:

```bash
python traffic.py road_signs model.h5
```

## Contributions

Contributions to this project are welcome! If you have ideas for improvements or enhancements, feel free to open an issue or submit a pull request.

## License

This project is an educational endeavor and is not licensed. Feel free to clone, modify, and share it for educational purposes.

---
