from lib.core.command_executor import CommandExecutor
from lib.core.command_parser import CommandParser
from lib.core.command_preprocessor import CommandPreprocessor

# 대입
script = """
MAIN
    for i in [1,2,3]
        set a = [i+1, i+2]
    end_for
    set i = 1
    while i < 3
        set array = [i, i+1]
        set i = i + 1
    end_while
    set b =  a + array
    set sum = 0
    for n in b
        set sum = sum + n
    end_for
    print sum
END_MAIN
"""
#---------------------------
# 기본적인 사용
#---------------------------
script_lines = script.split("\n")
command_preprocssed_lines = CommandPreprocessor().preprocess(script_lines)
parser = CommandParser()
parsed_commands = parser.parse(command_preprocssed_lines)

commandExecutor = CommandExecutor()

for command in parsed_commands:
    commandExecutor.execute(command)
