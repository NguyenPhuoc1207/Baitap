import pandas as pd

#Đọc dữ liệu từ file excel (dạng csv) trên máy tính vào bộ nhớ và in ra 10 dòng đầu tiên
df = pd.read_csv("pandas.csv")
print(df.head(10))

#Đọc dữ liệu từ file excel (dạng csv) trên mạng Internet vào bộ nhớ và in ra 10 dòng đầu tiên
url = 'https://www.k12.gov.sk.ca/sds/xml/Schoollistactive.csv'
#url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv'
#url='https://raw.githubusercontent.com/juliencohensolal/BankMarketing/master/rawData/bank-additional-full.csv'
data = pd.read_csv(url)
print(data.head(10))

#Đọc dữ liệu từ file có định dạng JSON (tren mạng internet) vào bộ nhớ và in ra 10 dòng đầu tiên
url = "https://api.exchangerate-api.com/v4/latest/USD"
js = pd.read_json(url)
print(js.head(10))