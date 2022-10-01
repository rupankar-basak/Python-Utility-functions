# Python-Utility-functions
Tons of Python Utility functions required for Dev purposes 


<u>Contribute and add your secret script.</u>

## 📝 NOTES

### Get All the files in a directory

Script: [Get All Files in a dir](get_all_files_in_a_dir.py)  

```python

def get_all_files_in_dir(dir_path, file_ext):
    """
    Get all files in a directory with a specific extension
    :param dir_path: Directory path
    :param file_ext: File extension
    :return: List of files
    """
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f)) and f.endswith(file_ext)]
```


### Flatten all iterables (lists, tuples, dicts, etc), into one lazy generator-stream

Script: [Flatten all iterables](flatten_all_iterables.py)  

```python
def flatten(l):
    """
    Flatten all iterables (lists, tuples, dicts, etc), into one lazy generator-stream
    """
    if isinstance(l, dict):
        l = l.items()
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el
```            


## Members
[![Forkers repo roster for @Prasundas99/Python-Utility-functions](https://reporoster.com/forks/Prasundas99/Python-Utility-functions)](https://github.com/Prasundas99/Python-Utility-functions/network/members)

# Growth during **Hacktoberfest 2022**

[![Contributor over time](https://contributor-overtime-api.apiseven.com/contributors-svg?chart=contributorOverTime&repo=Prasundas99/Python-Utility-functions)](https://www.apiseven.com/en/contributor-graph?chart=contributorOverTime&repo=Prasundas99/Python-Utility-functions)
