from fastapi import FastAPI
import uvicorn
import os 
import sys 
from fastapi.templating import Jinja2Templates 
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from text_summarizer.pipeline.prediction import PredictionPipeline 


text: str = "what is Text Summarization? Give me a detailed explanation"
app = FastAPI()

# Load model ONCE at startup (reuses saved weights, no training)
print("Loading trained model at startup...")
prediction_pipeline = PredictionPipeline()
print("Model ready for predictions!")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training(): 
    try: 
        os.system("python main.py")
        return Response(content="Training Successful !!", media_type="text/plain")
    except Exception as e:
        return Response(content=f"Error Occurred! {e}", media_type="text/plain")

@app.get("/predict")
async def predict_route(text: str): 
    try:
        # Use pre-loaded pipeline (fast, no reloading)
        summary = prediction_pipeline.predict(text)
        return {"input_text": text, "summary": summary}
    except Exception as e:
        return Response(content=f"Error Occurred! {e}", media_type="text/plain")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)