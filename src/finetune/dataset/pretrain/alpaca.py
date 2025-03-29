from tests.test import dialog
from ..builder.base import Base
import json
G_DS_PRETRAIN_FILE = "./data/pretrain/{}_alpaca.json"

class AlpacaDataSet(Base):
    def __init__(self, module: str = None):
        self.module: str = module

    '''
    按照alpaca格式组装的json数据格式：
    [
      {"text": "document"},
      {"text": "document"}
    ]
    序列化到预训练数据集文件。
    '''
    def build2file(self,module: str = None,dataset: dict =None):

        modules = self.module if module is None else module
        if dataset is None:
            raise Exception("dataset is None")

        if modules is None:
            raise Exception("module is None")

        dsFile = G_DS_PRETRAIN_FILE.format(modules)

        with open(dsFile, 'w') as file:
            # 使用json.dump()将字典写入文件
            json.dump(dataset, file)


    '''
    将aics模块的meta元数据对话记录，生成alpaca格式的预训练数据集json：
    [
      {"text": "document"},
      {"text": "document"}
    ]
    '''
    def build_dialog(self,dataset: dict =None) -> dict:

        if dataset is None:
            raise Exception("dialog dataset is None")

        dialogs = []
        for ds in dataset:
            dialogs.append(ds["dialog"])


        dialogDataSet= []
        for turns in dialogs:
            context = []
            for turn in turns:
                speaker = "用户" if turn["role"] == "user" else "客服"
                context.append(f"[{speaker}]：{turn['text']}")

            dialogDataSet.append({"text":"\n".join(context)})

        return dialogDataSet
