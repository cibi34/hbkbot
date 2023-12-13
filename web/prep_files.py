import os
import streamlit as st
import shutil
import time

def list_files_with_size(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    file_info = [{"Filename": file, "Size (bytes)": os.path.getsize(os.path.join(folder_path, file))} for file in files]
    return file_info

def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            break
        size_bytes /= 1024.0
    return "{:.2f} {}".format(size_bytes, unit)

def copy_files_to_folder(upload_files, folder_path):
    for upload_file in upload_files:
        target_path = os.path.join(folder_path, upload_file.name)
        with open(target_path, "wb") as f:
            f.write(upload_file.getbuffer())

# Set a 1:1 layout ratio
st.set_page_config(layout="wide")

# Add a title
st.title("Files for embeddings")

# Organize the layout with the file upload section on the left and the table on the right
col1, col2 = st.columns(2)

# Initial data
folder_path = "docs_to_db"  # Update with your folder path

# File uploader for adding new files on the left
with col1:
    uploaded_files = st.file_uploader("Upload new files (any type)", accept_multiple_files=True)
    # Trigger the action directly after submitting the files
    if uploaded_files is not None:
        # Handle file upload
        copy_files_to_folder(uploaded_files, folder_path)

# Display the list of files in the table with formatted size on the right
with col2:
    # Use a placeholder for the table
    table_placeholder = st.empty()

    # Function to update the table content
    def update_table():
        files_info = list_files_with_size(folder_path)
        table_content = {"Filename": [info["Filename"] for info in files_info],
                         "Size": [format_size(info["Size (bytes)"]) for info in files_info]}
        table_placeholder.table(table_content)

    # Update the table initially
    update_table()

    # Add a button to manually refresh the list of files
    if st.button("Refresh"):
        # Simulate refreshing data
        time.sleep(2)  # Simulate a delay for refreshing data
        # Update the table content
        update_table()

# Add a line underneath
st.markdown("***")

# File uploader for selecting a binary file
selected_file = st.file_uploader("Select a binary file", accept_multiple_files=False)
if selected_file is not None:
    st.write(f"Selected Binary File: {selected_file.name}")

# Add a new section with the title "Select Transformer"
st.title("Select Transformer")
# Add your content for selecting the transformer here
