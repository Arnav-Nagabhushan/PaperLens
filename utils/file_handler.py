import os


def save_uploaded_file(uploaded_file):
    temp_dir = "temp_uploads"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path


def extract_text_from_file(file_path):
    if file_path.endswith(".txt"):
        file = open(file_path, "r")
        text = file.read()
        file.close()
        return text
    else:
        return "File type not supported"
