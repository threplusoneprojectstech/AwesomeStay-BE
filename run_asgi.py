import os
import sys
import uvicorn

if __name__ == "__main__":
    uvicorn.run("Server.app:app", host="0.0.0.0", port=5000, reload=True)
    os.system("pyclean .")