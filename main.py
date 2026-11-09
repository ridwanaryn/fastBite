from fastapi import FastAPI

app = FastAPI(title="my first API")

@app.get("/")
def root():
	return {"message":"fast API!!!"}

@app.get("/about")
def about():
	return {"name": "my API", "version": "1.0"}

