from .base import Base

G_TPL_INSTRUCTION = {
    "default": "你是一名专业的电商客服助手，处理多轮对话时需结合上下文连贯性，请根据以下信息准确回答问题。",
    "presale_pd_feature": "你是一名电商客服助手，处理多轮对话时需结合上下文连贯性，需准确描述商品特性并提供购买建议。",
    "presale_pd_price": "zip project",
    "order": "你是一名电商订单处理专员，处理多轮对话时需结合上下文连贯性，需根据订单号精确查询并告知订单状态。",
    "postsale_exchange": "retry failed request or item",
}

class Instruction(Base):
    def __init__(self, type: str = None):
        self.type: str = type

    def build(self,type: str = None) -> str:
        instructionType = self.type if type is None else type
        instructionType = "default" if instructionType is None else instructionType
        return G_TPL_INSTRUCTION[instructionType]