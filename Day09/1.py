import pandas as pd
import matplotlib.pyplot as plt

# 파일 불러오기
file_path = './Suwon_2002.csv'
data = pd.read_csv(file_path, encoding='euc-kr')

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# '년-월-일을' '일 수'로 변경
data['일시'] = pd.to_datetime(data['일시'])

# 2002년에 맞게 변경
data_2002 = data[data['일시'].dt.year == 2002]

# 인덱스에 맞게 분배
data_2002['day_of_year'] = data_2002['일시'].dt.dayofyear

plt.figure(figsize=(10, 5))
plt.plot(data_2002['day_of_year'], data_2002['최고기온(°C)'], label='최고기온', color='red')
plt.plot(data_2002['day_of_year'], data_2002['평균기온(°C)'], label='평균기온', color='yellow')
plt.plot(data_2002['day_of_year'], data_2002['최저기온(°C)'], label='최저기온', color='blue')

plt.xlabel('day')
plt.ylabel('temperature')
plt.title('수원시 2002년도 기온 변화')
plt.legend()
plt.show()
