import zipfile

def extractFile(fileName, destDir=None, password=None):
    """Extracts a file from a zip archive

    Args:
        fileName (str): The name of the zip archive
        destDir (str, optional): The directory to extract to. Defaults to current directory.
        password (bytes, optional): The password to use to extract the file. Defaults to None.

    Returns:
        bool: True if successful, False otherwise
    """    
    try:
        with zipfile.ZipFile(fileName) as zf:
            zf.extractall(path=destDir, pwd=password)
            return True
    except zipfile.BadZipFile as e:
        print(e)
        return False
    except RuntimeError as e:
        print("Runtime Error: %s" % e)
        return False
    except FileNotFoundError as e:
        print(e.strerror)
        return False

# Test
if __name__ == "__main__":
    print(extractFile("test.zip", "test"))

    