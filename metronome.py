SECONDS_PER_MINUTE = 60


def metronome(input_string: str, time: float or int = 0) -> int:
    r"""
    Return number of words in a string or the WPM if time is not zero

    Parameters
    ----------
    input_string : str
        A string whom length is needed
    time : float or int, default 0
        The time window in seconds if the WPM is needed

    Returns
    -------
    int
        The input length
    float 
        WPM
    """
    word_count = len(input_string.split())
    return word_count if time == 0 else word_count / time * SECONDS_PER_MINUTE
