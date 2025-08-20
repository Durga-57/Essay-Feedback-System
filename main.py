from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import analyze_essay

app = FastAPI()

# ✅ Add this new root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Essay Feedback API!"}

# Define request model
class EssayRequest(BaseModel):
    text: str  # User's essay

@app.post("/submit-essay/")
async def submit_essay(essay: EssayRequest):
    """
    API endpoint to process an essay and return feedback.
    """
    if not essay.text.strip():
        raise HTTPException(status_code=400, detail="Essay text cannot be empty.")

    feedback = analyze_essay(essay.text)
    return {"feedback": feedback}
