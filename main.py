from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/greet")
def greet(name: str = "World"):
    """
    Greet the user with a customizable name.
    """
    return {"status": True, "message": f"hello {name} !"}

def run():
    """
    Run the FastAPI application.
    """
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    run()
