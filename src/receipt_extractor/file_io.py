# file_io.py
import os
import base64

def encode_file(path):
    """
    Encode the image file into base64 strings.

    Args:
        path (str): The directory of the image file.

    Returns:
        str: Image file in form of base64 encodings.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """
    List all the files inside a directory

    Args:
        dirpath (str): The directory where we want to get the list of file in.

    Yields:
        Tuple[str, str]: The file name and its full path for each regular file 
        found directly inside `dirpath`.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path

