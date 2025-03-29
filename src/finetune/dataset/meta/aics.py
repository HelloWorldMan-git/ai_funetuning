G_DS_TPL={
    "chunk_id": "S202308201405_user123_user123_2",#随机生成规则session_客服ID_客户ID_会话开始日期_chunk序号
    "embedding": [0.12, 0.23, ..., 0.78], # 768维向量--BGE对话内容向量值
    "session_id": "S202308201405_user123_user123",#session_客服ID_客户ID_会话开始日期
    "customer_id": "user_123",#客服ID
    "user_id": "123456",#客户ID
    "dialog": [
        {"role":"user","text":"订单20230820未收到","time":""},
        {"role":"customer","text":"已为您查询物流信息","time":""},
        {"role":"user","text":"能否修改配送地址？","time":""},
    ], #对话内容
    "window": 1,  #当前窗口位置,0-开始，1-中间，2-结束
    "prev_chunks": ["S202308201405_user123_user123_1"], #前一个对话chunk
    "next_chunks": ["S202308201405_user123_user123_3"], #后一个对话chunk

    #电商业务特征
    "product_info": {
        "id":"", #商品ID
        "url":"", #商品URL
        "skus": ["SKU12345", "SKU67890"],#商品SKU
        "brand_id":"", #品牌ID
        "brand":"", #品牌名称
        "category1":0,#商品一级类目
        "category2":0,#商品二级类目
        "category3":0,#商品三级类目
    },
    "order_info": {
        "id": "a1b2c3d4e5",#--订单ID
        "url":"",#订单链接
        "status": "shipped",#订单状态
        "amount": 299.00,#订单金额
    },
    "logistics": {#物流信息
        "company": "顺丰快递",
        "tracking_no": "SF123456789",
        "status": "shipped",#物流状态
    },
    #对话质量特征
    "sentiment": 1,#情感分类，正面，中性，负面
    "confidence": 0.83,#可信度
    #数据治理
    "data_version": 3,#数据版本
    "processing": [
        {"time":"2023-08-20 14:10:23","operation":"数据清洗v2"},
        {"time":"2023-08-20 14:12:45", "operation":"情感分析v1"},
        {"time":"2023-08-20 14:15:01", "operation":"特征增强v3"},
    ],
    "user_valuation":0, #用户评分
    "issue_type": 0, #0-商品尺码咨询，1-订单状态咨询，2-退换货咨询，3-
    #动态字段（根据业务扩展）
    "custom_features": {
    }
}