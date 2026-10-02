import os
from openai import OpenAI
import traceback
# 让代码去系统的“环境变量”里找名为 ALIYUN_API_KEY 的密码
# 这样你的真密码就只会存在于你未来的服务器后台，而不会暴露在代码里！
client = OpenAI(
    api_key=os.environ.get("ALIYUN_API_KEY", "默认的假key"),  
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def generate_product_copy(product_name: str, selling_points: str, target_audience: str, style: str = "小红书") -> str:
    system_prompt = f"""
你是一个拥有5年爆款经验的电商金牌文案操盘手。
你擅长将冰冷的产品参数转化为直击用户痛点的场景化购买理由。
当前请输出【{style}】风格的种草文案。

【排版要求】：
1. 爆款标题：必须带抓人眼球的修饰词和情绪标签，不超过15个字。
2. 结构清晰：痛点场景切入 -> 核心卖点解构 -> 促单行动号召。
3. 视觉节奏：合理插入 Emoji 表情（✨🔥💡），分段呼吸感强，适合手机端快速扫读。
"""

    user_prompt = f"""
请为以下商品撰写高转化文案：
- 商品名称：{product_name}
- 核心卖点：{selling_points}
- 目标受众：{target_audience}
"""

   

    try:
        # 2. 调用模型（直接使用你截图里带有 1M 免费额度的代号）
        response = client.chat.completions.create(
            model="qwen3.7-flash", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
        )
        
        # 3. 解析标准返回格式
        return response.choices[0].message.content

    except Exception as e:
        error_trace = traceback.format_exc()
        return f"❌ 系统异常详情:\n{error_trace}"


# ================= 快速测试 =================
if __name__ == "__main__":
    demo_product = "超轻量钛合金露营折叠椅"
    demo_points = "仅重800g、单手1秒开合、承重300斤、航空级钛合金耐腐蚀"
    demo_audience = "追求轻量化的户外徒步爱好者、周末喜欢去公园露营的年轻白领"

    result = generate_product_copy(demo_product, demo_points, demo_audience)
    
    print("====== ✨ 生成文案 ✨ ======\n")
    print(result)
    print("\n============================")