# 🐍 Python Library Setup Generator

## 🚀 Overview

The Python Library Setup Generator is a streamlined tool designed to simplify the process of setting up Python environments for data science projects. It provides a user-friendly interface to gather project requirements and automatically generate the necessary setup files, including `requirements.txt` and `environment_setup.sh`.

## 🎯 Motivation

Setting up Python environments for data science projects can often be time-consuming and error-prone, especially for beginners. This project aims to alleviate these challenges by offering a guided approach to configuring project environments. By automating the setup process and providing clear instructions, users can focus more on their data analysis tasks rather than on environment configuration.

## ✨ Key Features

### 📝 User-Friendly Questionnaire

The heart of the Python Library Setup Generator is its intuitive questionnaire interface. Users are presented with a series of questions to specify project details and select required libraries. This approach ensures that users provide all necessary information for creating the setup files.

### 🤖 Automated Setup File Generation

Based on the user's input from the questionnaire, the project automatically generates two essential setup files:

- **`requirements.txt`**: This file lists all the Python libraries required for the project, along with their version specifications. It serves as a reference for installing project dependencies.
- **`environment_setup.sh`**: This shell script automates the environment setup process. It includes commands to create a virtual environment, activate it, and install the required Python libraries using `pip`.

### 📥 Download Options

Once the setup files are generated, users have the option to download them individually or as a zip folder. This flexibility allows users to easily access and share the setup files with collaborators or deploy them to different environments.

### 🔄 Session Management

The Python Library Setup Generator supports session management, allowing users to start and end sessions as needed. Ending a session resets the tool, clearing any previous input and providing a clean slate for starting a new project setup.

## 🛠️ Getting Started

To get started with the Python Library Setup Generator, follow these steps:

1. Clone this repository to your local machine.
2. Install Streamlit and other required dependencies (`pip install streamlit`).
3. Run the Streamlit app using the command `streamlit run web_app_req_sh_creator.py`.
4. Answer the questionnaire to specify project details and library requirements.
5. Generate the setup files and download them as needed.
6. End the session when done or start a new session for another project.
## Contributors

- [Samarth Rathi](https://github.com/samarthRathi) - Project Developer

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
