from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# 核心魔法：直接把你刚才写的函数导入进来
from core_agent import generate_product_copy

# 1. 初始化 FastAPI 应用
app = FastAPI(title="商品文案智能生成 API", version="1.0")

# 2. 定义前端传过来的数据长什么样（数据校验）
class ProductRequest(BaseModel):
    product_name: str
    selling_points: str
    target_audience: str
    style: str = "小红书" # 如果前端不传，默认就是小红书风格

# 3. 写一个 POST 接口，暴露给前端调用
@app.post("/generate")
async def generate(request: ProductRequest):
    
    
    try:
        # 调用你的核心 AI 函数
        result = generate_product_copy(
            product_name=request.product_name,
            selling_points=request.selling_points,
            target_audience=request.target_audience,
            style=request.style
        )
        
        # 如果核心逻辑返回了错误（包含我们刚才设计的❌），直接抛出 500 服务器错误
        if result.startswith("❌"):
            raise HTTPException(status_code=500, detail=result)
            
        # 成功则返回标准的 JSON 格式
        return {
            "code": 200,
            "message": "生成成功",
            "data": {"copywriting": result}
        }
        
    except Exception as e:
        # 兜底的异常处理
        raise HTTPException(status_code=500, detail=f"后端接口异常: {str(e)}")

# 如果直接运行这个文件，就启动服务器
if __name__ == "__main__":
    # 在本地 8000 端口启动，reload=True 表示你修改代码它会自动热重启
    uvicorn.run("api_server:app", host="127.0.0.1", port=8888, reload=True)