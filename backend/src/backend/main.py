import uvicorn


PORT = 1071

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", log_level="info", port=PORT, reload=True)
