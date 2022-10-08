import base64


def encodeFile(fileName):
    """Encodes a file to base64

    Args:
        fileName (str): The name of the file to encode

    Returns:
        str: The base64 encoded file
    """
    try:    
        with open(fileName, "rb") as f:
            return base64.b64encode(f.read())
    except FileNotFoundError:
        print("File not found")
        return None
    except:
        print("Unknown error")
        return None
    
if __name__ == "__main__":
    print(encodeFile("test.txt"))