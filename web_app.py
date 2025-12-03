# web_app.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
import shutil
from pathlib import Path
import uvicorn

app = FastAPI()

HTML_PAGE = """
<!doctype html>
<title>InsightFlow Upload</title>
<h2>Upload CSV to generate InsightFlow report</h2>
<form action="/upload" enctype="multipart/form-data" method="post">
  <input name="file" type="file" accept=".csv">
  <input type="submit" value="Upload & Generate">
</form>
<p>After upload, get the report at <a href="/report">/report</a></p>
"""

@app.get("/", response_class=HTMLResponse)
def index():
    return HTML_PAGE

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    upload_path = Path("sample_data.csv")   # pipeline reads sample_data.csv
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # import inside the function to avoid circular import on startup
    from insightflow_run import main as generate_report

    # run the pipeline (this will overwrite output files)
    generate_report()

    return {"message": "Report generated", "download": "/report"}

@app.get("/report")
def report():
    p = Path("output/InsightFlow_Report.pptx")
    if p.exists():
        return FileResponse(p, filename=p.name)
    return {"error": "Report not ready"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
