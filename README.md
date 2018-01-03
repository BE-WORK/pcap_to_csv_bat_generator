# 简述
这个工具可以从pcap格式文件中提取部分字段并存储成csv格式文件。

# 环境
Windows 10 + Python 2 + Pycharm 2017.3

# 使用
运行脚本，根据提示输入文件夹路径（Windows格式），文件夹是一种商品的根目录，这个根目录下有一个交sample_traffic_pcap文件夹，里面包含pcap格式的文件集。脚本会在根目录下创建（如果不存在）一个名为sample_traffic_csv的文件夹，用来存放csv格式文件集，并在Python脚本的当前目录下生成一个bat脚本。