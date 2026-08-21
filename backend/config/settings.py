from pathlib import Path 
 
BASE_DIR = Path(__file__).resolve().parent.parent.parent 
 
# 输出路径配置 
OUTPUT_PATH = BASE_DIR / "output" 
AUDIO_OUTPUT = OUTPUT_PATH / "audio" 
VIDEO_OUTPUT = OUTPUT_PATH / "video" 
 
# 模型路径配置（本地/服务器通用） 
MODEL_PATH = BASE_DIR / "models" 
 
# 服务器配置（后续部署用） 
SERVER_HOST = "127.0.0.1" 
SERVER_PORT = 8000

