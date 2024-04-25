#!/bin/bash
# Script for setting up Python environment for Project Title

# Inform the user about the script's purpose
echo "This script will set up a Python environment for Project Title."

# Inform the user about the Python version being used
python_version=
echo "Using Python version $python_version."

# Inform the user about creating a virtual environment
echo "Creating a virtual environment named 'project_title_env'..."
python$python_version -m venv Financial Data Analysis_env

# Activate the virtual environment
echo "Activating the virtual environment..."
source Financial Data Analysis_env/bin/activate

# Inform the user about installing required packages
echo "Installing required packages from requirements.txt..."
pip install -r requirements.txt

# Inform the user about setup completion
echo "Setup completed successfully!"

# Provide instructions to deactivate the virtual environment
echo "To deactivate the virtual environment, run 'deactivate'."
