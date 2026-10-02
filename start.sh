#!/bin/bash
python api_server.py &
streamlit run web_ui.py --server.port 8501 --server.address 0.0.0.0
# 后台启动 FastAPI (换回默认的 8000 端口，服务器上不会冲突)
python api_server.py &
# 前台启动 Streamlit网页，指定端口为 8501
streamlit run web_ui.py --server.port 8501 --server.address 0.0.0.0