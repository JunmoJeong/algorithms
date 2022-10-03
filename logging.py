# from turtle import pd
import pandas as pd
import json
from collections import OrderedDict
import datetime


file_data = OrderedDict()

start_date = '20210101'
end_date = '20220930'
date_list = pd.date_range(start=start_date, end=end_date, freq='D')

nowDate = datetime.datetime.now()
# f = open(nowDate.strftime("%Y-%m-%d) + ".json","w")


# print(date_list)
# print(len(date_list))

# file_data['name'] = "computer"
# file_data['languate'] = "kor"
# file_data['words'] = {'ram': '램', "process": "프로세스",
#                       'processor': '프로세서', 'CPU': "씨피유"}
# file_data['number'] = 4

print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
with open(nowDate.strftime("%Y-%m-%d) + ".json", 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent='\t')
