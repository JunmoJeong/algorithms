
import pandas as pd
import json
from collections import OrderedDict
import datetime
import requests
import json

#file_data = OrderedDict()

start_date = '20220921'
end_date = '20220930'
date_list = pd.date_range(start=start_date, end=end_date, freq='D')
#for i in date_list:
#    i = str(i)
#    print(i[:10])

# nowDate = datetime.datetime.now()
# # f = open(nowDate.strftime("%Y-%m-%d) + ".json","w")


# # print(date_list)
# # print(len(date_list))

# # file_data['name'] = "computer"
# # file_data['languate'] = "kor"
# # file_data['words'] = {'ram': '램', "process": "프로세스",
# #                       'processor': '프로세서', 'CPU': "씨피유"}
# # file_data['number'] = 4

# print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
# with open(nowDate.strftime("%Y-%m-%d) + ".json", 'w', encoding='utf-8') as make_file:
#     json.dump(file_data, make_file, ensure_ascii=False, indent='\t')

##response = requests.get("https://data.myenergy.co.kr/api/haezoom/?key=70e384be35e27604573f3a3b38b248&order=getDayData&date=2022-04-28&aptnum=021104000041&category=1")
# print(response.text)


#print(result)
#result_data = result.json()
# file = open('test.json', "w+")
# file.write(json.dumps(result_data))
# file.close()

for date in date_list:
    date = str(date)
    URL = "https://data.myenergy.co.kr/api/haezoom/?key=70e384be35e27604573f3a3b38b248&order=getDayData&date=" + date[:10] + "&aptnum=021104000041&category=1"
    result = requests.get(URL).json()
    with open(date[:10],'w') as f:
        json.dump(result,f)