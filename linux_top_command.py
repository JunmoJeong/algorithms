import os

top_cmd_result = os.popen('top | head -6').read()
print(top_cmd_result)
# print(type(top_cmd_result))
# print(len(top_cmd_result
