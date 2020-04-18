import uvicorn
 

def run_app(**kwargs):
    uvicorn.run(**kwargs)

if __name__ == "__main__":
    import app
    run_app(app=app, host="0.0.0.0", port=8000)