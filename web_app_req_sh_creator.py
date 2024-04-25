import streamlit as st
from zipfile import ZipFile
import os

# Dictionary mapping library names to their corresponding pip install names
library_mapping = {
    "NumPy": "numpy",
    "Pandas": "pandas",
    "Matplotlib": "matplotlib",
    "Seaborn": "seaborn",
    "Scikit-Learn": "scikit-learn",
    "Statsmodels": "statsmodels",
    "Optuna": "optuna",
    "PyCaret": "pycaret",
    "H2O": "h2o",
    "TensorFlow": "tensorflow",
    "PyTorch": "torch",
    "FastAI": "fastai",
    "Keras": "keras",
    "PyTorch Lightning": "pytorch-lightning",
    "NLTK": "nltk",
    "spaCy": "spacy",
    "Gensim": "gensim"
}

# Required libraries in case they are not provided by the user
required_libraries = {
    "numpy",
    "pandas"
}

# Function to create requirements file and setup script
def create_requirements_file(project_title, selected_libraries, python_version):
    with open('requirements.txt', 'w') as file:
        file.write(f"# Project: {project_title}\n")
        for lib_name in selected_libraries:
            file.write(f"{library_mapping[lib_name]}\n")

    with open('environment_setup.sh', 'w') as file:
        file.write("#!/bin/bash\n")
        file.write("# Script for setting up Python environment for Project Title\n\n")
        file.write("# Inform the user about the script's purpose\n")
        file.write("echo \"This script will set up a Python environment for Project Title.\"\n\n")
        
        file.write("# Inform the user about the Python version being used\n")
        file.write(f"python_version={python_version}\n")
        file.write("echo \"Using Python version $python_version.\"\n\n")
        
        file.write("# Inform the user about creating a virtual environment\n")
        file.write("echo \"Creating a virtual environment named 'project_title_env'...\"\n")
        file.write(f"python$python_version -m venv {project_title}_env\n\n")
        
        file.write("# Activate the virtual environment\n")
        file.write("echo \"Activating the virtual environment...\"\n")
        file.write(f"source {project_title}_env/bin/activate\n\n")
        
        file.write("# Inform the user about installing required packages\n")
        file.write("echo \"Installing required packages from requirements.txt...\"\n")
        file.write("pip install -r requirements.txt\n\n")
        
        # Provide instructions to the user
        file.write("# Inform the user about setup completion\n")
        file.write("echo \"Setup completed successfully!\"\n\n")
        
        file.write("# Provide instructions to deactivate the virtual environment\n")
        file.write("echo \"To deactivate the virtual environment, run 'deactivate'.\"\n")


def display_file_content(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    st.code(file_content, language='text')

# Function to download file
def download_file(file_content, file_name, file_extension):
    st.markdown(f"### Download {file_name}")
    st.download_button(
        label=f"Download {file_name}",
        data=file_content,
        file_name=f"{file_name}.{file_extension}",
        mime=f"text/{file_extension}"
    )

# def main():
#     session_state = st.session_state
#     if 'end_session' not in session_state:
#         session_state['end_session'] = False
#     if 'generate_files' not in session_state:
#         session_state['generate_files'] = False

#     if not session_state['end_session']:
#         # Display sidebar
#         st.sidebar.title("Questionnaire")

#         # User-based questions
#         project_title = st.sidebar.text_input("Enter project title:", key="project_title")
#         python_version = st.sidebar.text_input("Enter Python version (e.g., 3.8):", key="python_version")
        
#         selected_libraries = []
#         data_analysis = st.sidebar.checkbox("Perform data analysis?")
#         if data_analysis:
#             st.sidebar.subheader("Select data analysis libraries:")
#             remaining_data_analysis_lib = [lib for lib in library_mapping.keys() if lib not in selected_libraries]
#             selected_data_analysis_lib = st.sidebar.multiselect("Select libraries:", remaining_data_analysis_lib, key="data_analysis_lib")
#             selected_libraries += selected_data_analysis_lib
#         machine_learning = st.sidebar.checkbox("Perform machine learning?")
#         if machine_learning:
#             st.sidebar.subheader("Select machine learning libraries:")
#             remaining_machine_learning_lib = [lib for lib in library_mapping.keys() if lib not in selected_libraries]
#             selected_machine_learning_lib = st.sidebar.multiselect("Select libraries:", remaining_machine_learning_lib, key="machine_learning_lib")
#             selected_libraries += selected_machine_learning_lib
#         deployment = st.sidebar.checkbox("Perform deployment?")
#         if deployment:
#             st.sidebar.subheader("Select deployment libraries:")
#             remaining_deployment_lib = [lib for lib in library_mapping.keys() if lib not in selected_libraries]
#             selected_deployment_lib = st.sidebar.multiselect("Select libraries:", remaining_deployment_lib, key="deployment_lib")
#             selected_libraries += selected_deployment_lib

#         # Display generated files and provide download option
#         st.title("Generated Files")

#         if st.button("Generate Files"):
#             # Create files based on user input
#             create_requirements_file(project_title, selected_libraries, python_version)
#             session_state['generate_files'] = True

#         if session_state['generate_files']:
#             # Display requirements.txt and provide download option
#             st.header("requirements.txt")
#             display_file_content('requirements.txt')
#             download_file(open('requirements.txt', 'rb').read(), 'requirements', 'txt')

#             # Display environment_setup.sh and provide download option
#             st.header("environment_setup.sh")
#             display_file_content('environment_setup.sh')
#             download_file(open('environment_setup.sh', 'rb').read(), 'environment_setup', 'sh')

#             # Download files as a folder
#             if st.button("Download as Folder"):
#                 with ZipFile(f"{project_title}_files.zip", 'w') as zipf:
#                     zipf.write('requirements.txt', arcname='requirements.txt')
#                     zipf.write('environment_setup.sh', arcname='environment_setup.sh')
#                 st.markdown(f"### Download {project_title}_files.zip")
#                 st.download_button(
#                     label=f"Download {project_title}_files.zip",
#                     data=open(f"{project_title}_files.zip", 'rb'),
#                     file_name=f"{project_title}_files.zip",
#                     mime='application/zip'
#                 )

#         # Allow the user to end the session
#         if st.sidebar.button("End Session"):
#             session_state['end_session'] = True

# if __name__ == "__main__":
#     main()

def main():
    session_state = st.session_state
    if 'end_session' not in session_state:
        session_state['end_session'] = False
    if 'generate_files' not in session_state:
        session_state['generate_files'] = False

    if not session_state['end_session']:
        # Display sidebar
        st.sidebar.title("Questionnaire")

        # User-based questions
        project_title = st.sidebar.text_input("Enter project title:", key="project_title")
        python_version = st.sidebar.text_input("Enter Python version (e.g., 3.8):", key="python_version")
        
        selected_libraries = []
        data_analysis = st.sidebar.checkbox("Perform data analysis?")
        if data_analysis:
            st.sidebar.subheader("Select data analysis libraries:")
            remaining_data_analysis_lib = [lib for lib in library_mapping.keys() if lib not in selected_libraries]
            selected_data_analysis_lib = st.sidebar.multiselect("Select libraries:", remaining_data_analysis_lib, key="data_analysis_lib")
            selected_libraries += selected_data_analysis_lib
        machine_learning = st.sidebar.checkbox("Perform machine learning?")
        if machine_learning:
            st.sidebar.subheader("Select machine learning libraries:")
            remaining_machine_learning_lib = [lib for lib in library_mapping.keys() if lib not in selected_libraries]
            selected_machine_learning_lib = st.sidebar.multiselect("Select libraries:", remaining_machine_learning_lib, key="machine_learning_lib")
            selected_libraries += selected_machine_learning_lib
        deployment = st.sidebar.checkbox("Perform deployment?")
        if deployment:
            st.sidebar.subheader("Select deployment libraries:")
            remaining_deployment_lib = [lib for lib in library_mapping.keys() if lib not in selected_libraries]
            selected_deployment_lib = st.sidebar.multiselect("Select libraries:", remaining_deployment_lib, key="deployment_lib")
            selected_libraries += selected_deployment_lib

        # Display generated files and provide download option
        st.title("Generated Files")

        if st.button("Generate Files"):
            # Create files based on user input
            create_requirements_file(project_title, selected_libraries, python_version)
            session_state['generate_files'] = True

        if session_state['generate_files']:
            # Display requirements.txt and provide download option
            st.header("requirements.txt")
            display_file_content('requirements.txt')
            download_file(open('requirements.txt', 'rb').read(), 'requirements', 'txt')

            # Display environment_setup.sh and provide download option
            st.header("environment_setup.sh")
            display_file_content('environment_setup.sh')
            download_file(open('environment_setup.sh', 'rb').read(), 'environment_setup', 'sh')

            # Download files as a folder
            if st.button("Download as Folder"):
                with ZipFile(f"{project_title}_files.zip", 'w') as zipf:
                    zipf.write('requirements.txt', arcname='requirements.txt')
                    zipf.write('environment_setup.sh', arcname='environment_setup.sh')
                st.markdown(f"### Download {project_title}_files.zip")
                st.download_button(
                    label=f"Download {project_title}_files.zip",
                    data=open(f"{project_title}_files.zip", 'rb'),
                    file_name=f"{project_title}_files.zip",
                    mime='application/zip'
                )

        # Allow the user to end the session
        if st.sidebar.button("End Session"):
            session_state['end_session'] = True
            st.experimental_rerun()

if __name__ == "__main__":
    main()

