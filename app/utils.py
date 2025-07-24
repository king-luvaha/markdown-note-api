import markdown
import language_tool_python

def convert_md_to_html(md_content: str) -> str:
    return markdown.markdown(md_content)

def check_grammar(text: str) -> str:
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return "\n".join([f"{m.ruleId}: {m.message} (suggested: {m.replacements})" for m in matches])

