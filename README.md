# Programming_Languages_TrendTracker
 Programming Languages TrendTracker is a data analysis project that explores the popularity trends of various programming languages from 2004 to 2024. The project utilizes machine learning techniques to analyze and predict programming language popularity.


## Table of Contents

- [Installation]
- [Usage]
- [Data]
- [Project Structure]
- [License]

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rajeev-Gaur/Programming_Languages_TrendTracker.git
   cd Programming_Languages_TrendTracker

2. Create a virtual environment:python -m venv .venv

3. Activate the virtual environment:.venv\Scripts\activate

4. Install the required packages:pip install -r requirements.txt


Usage
To run the project, execute the following command 
python src/main.py

This will load the dataset, preprocess the data, train the machine learning model, and print the evaluation metrics.

Data
The dataset used in this project is sourced from Kaggle, covering programming language popularity from 2004 to 2024. The dataset file is located in the data/ directory.

Project Structure:
Programming_Languages_TrendTracker/
│
├── .venv/                         # Virtual environment
│
├── data/                          # Directory for datasets
│   └── most_popular_languages.csv  # Your dataset file
│
├── src/                           # Source code
│   ├── __init__.py                # Indicates that src is a package
│   ├── config.py                  # Configuration settings
│   ├── preprocessing_data.py       # Data preprocessing scripts
│   ├── train_model.py              # Machine learning model training
│   └── main.py                    # Main script to run the project
│
├── visuals/                       # Plots and visualizations
│
├── requirements.txt               # List of project dependencies
│
└── LICENSE.txt                    # License for the project
│
└── README.md                      # Project documentation


License
This project is licensed under the MIT License - see the LICENSE file for details.
