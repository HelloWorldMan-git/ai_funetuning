from typing import List, Dict


def slide_window(dialog, window=3, stride=2):
    return [dialog[i:i+window] for i in range(0, len(dialog)-window+1, stride)]


# 电商主题关键词库
TOPIC_KEYWORDS = {
    "物流查询": ["物流", "发货", "运单", "快递", "配送"],
    "退换货": ["退货", "换货", "退款", "破损", "维修"],
    "商品咨询": ["尺寸", "颜色", "材质", "功能", "参数"],
    "促销活动": ["优惠", "折扣", "满减", "赠品", "秒杀"],
    "支付问题": ["支付失败", "发票", "金额不符"]
}

def detect_topic_shift(current_text, previous_text):
    """通过关键词变化检测主题切换"""
    prev_topics = {topic for topic, keys in TOPIC_KEYWORDS.items() if any(k in previous_text for k in keys)}
    curr_topics = {topic for topic, keys in TOPIC_KEYWORDS.items() if any(k in current_text for k in keys)}

    # 主题集合变化视为边界
    if not curr_topics.issubset(prev_topics):
        return True
    return False

def split_by_topic(dialogs: List[Dict]) -> List[Dict]:
    """基于关键词识别主题边界"""
    topics = {
        "物流查询": ["物流", "发货", "运单"],
        "退换货": ["退货", "换货", "退款"],
        "优惠活动": ["优惠券", "折扣", "满减"]
    }

    current_topic = None
    segments = []
    current_segment = []

    for turn in dialogs:
        text = turn["text"]
        detected = False

        for topic, keywords in topics.items():
            if any(kw in text for kw in keywords):
                if current_topic != topic:  # 主题切换
                    if current_segment:
                        segments.append({"text": "\n".join(current_segment)})
                    current_segment = []
                    current_topic = topic
                detected = True
                break

        if not detected and current_topic:
            current_segment.append(format_turn(turn))
        elif detected:
            current_segment.append(format_turn(turn))

    return segments


from sentence_transformers import SentenceTransformer
model = SentenceTransformer('BAAI/bge-base-zh-v1.5')

def semantic_shift_detection(texts, threshold=0.75):
    """通过语义向量相似度检测主题变化"""
    embeddings = model.encode(texts)
    boundaries = []

    for i in range(1, len(texts)):
        cosine_sim = np.dot(embeddings[i-1], embeddings[i])
        if cosine_sim < threshold:
            boundaries.append(i)
    return boundaries