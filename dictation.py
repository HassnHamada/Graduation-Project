from language_tool_python import LanguageTool


def correct(inp_str: str, language: str = "en-UK") -> str:
    tool = LanguageTool(language)
    return tool.correct(inp_str)
