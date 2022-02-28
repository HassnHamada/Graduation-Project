from language_tool_python import LanguageTool


def correct(inp_str: str, language: str = "en-UK") -> str:
    r"""
    Correct grammatical and spelling errors

    Parameters
    ----------
    inp_str : str
        A string to be corrected
    language : str, default "en-UK"
        The language to be used

    Returns
    -------
    str
        The corrected string
    """

    tool = LanguageTool(language)
    return tool.correct(inp_str)
