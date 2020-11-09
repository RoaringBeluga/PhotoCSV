from pathlib import Path

"""
Print debug info to stdout
:text Text to be printed.  
"""


def bugprint(text):
    # pass
    print(text)


"""
Get file list from the directory
:param dir: directory to list
:param pattern: file matching pattern, defaults to *.* 
:return: list of matching files
"""


def get_file_list(file_dir, pattern='*.*'):
    p = Path(file_dir)
    return list(p.glob(pattern))
