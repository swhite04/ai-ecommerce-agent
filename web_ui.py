import streamlit as st
import requests

# 1. 网页全局配置（设置网页标题和图标）
st.set_page_config(page_title="AI 电商爆款文案生成器", page_icon="🛍️", layout="wide")

st.title("🛍️ AI 电商爆款文案生成器")
st.markdown("告别绞尽脑汁！输入商品参数，AI 一键生成高转化网感文案。")
st.divider() # 画一条分割线

# 2. 页面布局：分成左右两列
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📝 输入商品信息")
    # 构建表单输入框
    product_name = st.text_input("商品名称", placeholder="例如：全自动太空舱猫砂盆")
    selling_points = st.text_area("核心卖点", placeholder="例如：彻底解放双手、内置除臭、防夹猫感应、超大空间")
    target_audience = st.text_input("目标受众", placeholder="例如：996养宠打工人、多猫家庭")
    style = st.selectbox("文案风格", ["小红书种草", "抖音短视频脚本", "淘宝详情页", "私域朋友圈"])
    
    # 生成按钮
    submit_btn = st.button("🚀 一键生成文案", type="primary", use_container_width=True)

with col2:
    st.header("✨ 生成结果")
    
    # 3. 当用户点击了“生成”按钮后，执行的逻辑
    if submit_btn:
        if not product_name or not selling_points:
            st.warning("⚠️ 请至少填写「商品名称」和「核心卖点」哦！")
        else:
            with st.spinner("🤖 AI 大脑正在疯狂敲键盘中..."):
                try:
                    # 将用户输入的数据打包，发给我们的 FastAPI 后端
                    payload = {
                        "product_name": product_name,
                        "selling_points": selling_points,
                        "target_audience": target_audience,
                        "style": style
                    }
                    # 注意这里的端口号 8888，必须和你刚才启动的一致
                    response = requests.post("http://127.0.0.1:8888/generate", json=payload)
                    
                    if response.status_code == 200:
                        result_data = response.json()
                        copywriting = result_data["data"]["copywriting"]
                        st.success("🎉 生成成功！")
                        # 完美展示生成的文案
                        st.write(copywriting)
                    else:
                        st.error(f"后端报错啦：{response.text}")
                except Exception as e:
                    st.error(f"请求失败！请检查你的 FastAPI 后端（api_server.py）是否正在运行。错误信息：{e}")