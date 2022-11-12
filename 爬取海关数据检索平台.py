from bs4 import BeautifulSoup
import pandas as pd



# 将数组拆分
def cut(obj, sec):
    return [obj[i:i+sec] for i in range(0,len(obj),sec)]

# 处理结果
def ProcessingResults():
    # 将结果读取出来并写入excel
    All_Info=[]
    with open('Data/Import/get_imp_2021_8_1.10.html', 'r', encoding='utf-8') as f:
        Soup = BeautifulSoup(f.read(), 'html.parser')
        All_Info=Soup.select(".th-line")
        All_Info=[item.text for item in All_Info]
        All_Info=cut(All_Info,13)

    # 将数据写入excel
    # 定义容器集合
    CommodityCode=[]  # 商品编码
    CommodityName=[]  # 商品名称
    TradingPartnerCode=[]  # 贸易伙伴编码
    TradingPartnerName = []  # 贸易伙伴名称
    TradeModeCode=[]   # 贸易方式编码
    TradeModeName=[]   # 贸易方式名称
    RegistrationCode=[]  # 注册地编码
    RegistrationName=[]  # 注册地名称
    FirstQuantity=[]  # 第一数量
    FirstMeasurementUnit=[]  #第一计量单位
    SecondQuantity=[]  # 第二数量
    SecondMeasurementUnit=[] #第二计量单位
    RMB=[]  # 人民币
    # 开始组合数据
    for item in All_Info:
        CommodityCode.append(item[0])
        CommodityName.append(item[1])
        TradingPartnerCode.append(item[2])
        TradingPartnerName.append(item[3])
        TradeModeCode.append(item[4])
        TradeModeName.append(item[5])
        RegistrationCode.append(item[6])
        RegistrationName.append(item[7])
        FirstQuantity.append(item[8])
        FirstMeasurementUnit.append(item[9])
        SecondQuantity.append(item[10])
        SecondMeasurementUnit.append(item[11])
        RMB.append(item[12])

    out_file = {'商品编码': [], '商品名称': [], '贸易伙伴编码': [], '贸易伙伴名称': [], '贸易方式编码': [], "贸易方式名称": [],'注册地编码': [], '注册地名称': [], '第一数量': [], '第一计量单位': [], '第二数量': [], "第二计量单位": [], "人民币": []}
    out_file['商品编码'] = CommodityCode
    out_file['商品名称'] = CommodityName
    out_file['贸易伙伴编码'] = TradingPartnerCode
    out_file['贸易伙伴名称'] = TradingPartnerName
    out_file['贸易方式编码'] = TradeModeCode
    out_file['贸易方式名称'] = TradeModeName
    out_file['注册地编码'] = RegistrationCode
    out_file['注册地名称'] = RegistrationName
    out_file['第一数量'] = FirstQuantity
    out_file['第一计量单位'] = FirstMeasurementUnit
    out_file['第二数量'] = SecondQuantity
    out_file['第二计量单位'] = SecondMeasurementUnit
    out_file['人民币'] = RMB
    output = pd.DataFrame(out_file)
    output.to_excel('./海关总署相关信息.xlsx', index=False)
    print("*****************All info is end!***********************")





ProcessingResults()




