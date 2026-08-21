from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.tts import router as tts_router
from backend.api.video import router as video_router

app = FastAPI(
    title="数字人集成平台",
    description="文本→音频→视频→分片输出完整链路",
    version="1.0.0"
)

# 配置CORS（允许跨域请求）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 健康检查接口
@app.get("/")
async def root():
    return {"message": "数字人平台服务运行中", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

# 注册路由
app.include_router(tts_router)
app.include_router(video_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)