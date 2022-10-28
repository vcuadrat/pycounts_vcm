from importlib import resources

def get_flatland():
    """Get path to example "Flatland" [1]_ text file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """
    # from pathlib import Path
    # home = Path.home()
    import pathlib
    
    temp = pathlib.Path(__file__).parent / 'data'
    return pathlib.Path(temp) / 'flatland.txt'