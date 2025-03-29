dialog=[
    {"role":"user","text":"订单20230820未收到","time":""},
    {"role":"customer","text":"已为您查询物流信息","time":""},
    {"role":"user","text":"能否修改配送地址？","time":""},
    {"role":"customer","text":"已为您查询物流信息2","time":""},
    {"role":"user","text":"能否修改配送地址？2","time":""},
    {"role":"customer","text":"已为您查询物流信息3","time":""},
    {"role":"user","text":"能否修改配送地址？3","time":""},
]

def sliding_window_split(dialog, window=3, stride=2):
    return [dialog[i:i+window] for i in range(0, len(dialog)-window+1, stride)]


print(sliding_window_split(dialog))