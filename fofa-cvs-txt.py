import pandas as pd
import argparse
import os

# 创建参数解析器
parser = argparse.ArgumentParser(description='Process CSV file and write output.')
parser.add_argument('-f', '--file', help='Path to the CSV file', required=True)
parser.add_argument('-o', '--output', help='Name of the output file', required=True)
args = parser.parse_args()

# 读取指定的本地 CSV 文件
df = pd.read_csv(args.file) 

# 将提取的列转换为字符串类型
Protocols = df['Protocol'].astype(str)
ips = df['IP'].astype(str)
ports = df['Port'].astype(str)

# 获取本地 CSV 文件的名称
csv_file_name = os.path.basename(args.file)

# 获取转换后的本地 TXT 文件的名称
txt_file_name = args.output

# 打印转换成功的消息以及文件名称
print(f"成功转换本地 CSV 文件 '{csv_file_name}' 到本地 TXT 文件 '{txt_file_name}'")

# 将信息写入输出文件
with open(args.output, 'a') as f:
    for index, row in df.iterrows():
        f.write(row['Protocol'] + '://' + row['IP'] + ':' + str(row['Port']) + '\n')

# 打印写入成功的消息
print("成功将信息写入输出文件")
