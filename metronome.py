SECONDS_PER_MINUTE = 60


def metronome(inp_str: str, time: int = 0) -> int:
    r"""
    Return number of words in a string or the WPM if time is not zero

    Parameters
    ----------
    inp_str : str
        A string whose length is needed
    time : int, default 0
        The time window in seconds if the WPM is needed

    Returns
    -------
    int
        The input length
    float 
        WPM
    """
    word_count = len(inp_str.split())
    return word_count if time == 0 else word_count / time * SECONDS_PER_MINUTE
