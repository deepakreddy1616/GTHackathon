🧩 1. Problem Overview
📌 The Real-World Context

In AdTech, Account Managers spend 4–6 hours every week:

Downloading CSV logs

Cleaning data

Making charts

Copy-pasting screenshots

Writing weekly insights

This is slow, boring, and error-prone.

😩 The Pain

Reports take too long

Manual work = mistakes

Important anomalies (spikes/drops) are missed

Clients get insights late

🎯 What InsightFlow Does

InsightFlow automates the ENTIRE reporting workflow.

🟢 Input: Just add a CSV file
⚙️ Processing: KPIs → Charts → Anomalies → AI Summary
📤 Output: Gorgeous PPTX + PDF

All without any human involvement.

🎁 2. What You Get (End Result)
🟦 User Input

A raw CSV file containing clicks, impressions, revenue, dates, and locations.

🟨 System Magic

InsightFlow automatically:

Cleans and structures data

Calculates KPIs (CTR, CPA, RPM, etc.)

Detects anomalies using statistics

Generates Clicks/CTR/Revenue trend charts

Writes an AI-powered executive summary

Builds a PPTX

Converts it to PDF

🟩 Final Output

A professional, client-ready report containing:

📈 Clicks Trend
📊 CTR Trend
💰 Revenue Trend
🔴 Anomalies Highlighted
🤖 AI Summary + Recommendations
🗂 Top Regions (optional)

This looks like a report from an analytics team — but created automatically.

🧠 3. Technical Architecture
<div align="center">
RAW CSV
   │
   ▼
Data Cleaner (Pandas / Polars)
   │
   ▼
KPI Calculator
   │
   ▼
Anomaly Detector (Z-Score)
   │
   ▼
Chart Generator (Matplotlib)
   │
   ▼
AI Summary (OpenAI GPT-4o mini)
   │
   ▼
PPTX Builder (python-pptx)
   │
   ▼
PDF Export (LibreOffice)

</div>
🏗️ Key Design Choices
Component	Why I Chose It
Pandas/Polars	Fast, reliable data manipulation
Z-Score Anomaly Detection	Simple + effective for spikes/drops
OpenAI GPT-4o mini	Clean, professional insights generation
python-pptx	Pixel-perfect slide control
FastAPI (optional)	Simple UI for CSV uploads
LibreOffice CLI	Automatic PDF export
⚙️ 4. Tech Stack
Layer	Technology
Language	Python 3.11
Data Processing	Pandas / Polars
Anomaly Detection	Z-Score
AI	GPT-4o mini
Charts	Matplotlib
Report Engine	python-pptx
PDF	LibreOffice
Web UI	FastAPI + Uvicorn
🧗‍♂️ 5. Challenges & Learnings
🔥 Challenge #1 — AI Hallucinations

Problem: AI invented reasons for spikes (like weather)
Fix: Strict prompt:

“Only use data provided. If unknown, say ‘Unknown.’”

This removed hallucinations and produced reliable insights.

🔥 Challenge #2 — Time-Series Gaps

Missing dates caused ugly charts.
Fix: Automatically filled missing dates → smooth, continuous lines.

🔥 Challenge #3 — PPTX → PDF in Windows

LibreOffice wasn’t detected.
Fix: Added correct PATH + used headless mode for conversion.

🖼️ 6. Visual Proof (Screenshots)

(Replace placeholder images with your own)

🔎 Anomaly Detection

📝 Final Report

🌐 Web Upload UI

🚀 7. How to Run InsightFlow
🟦 Step 1 — Clone Repository
git clone https://github.com/username/InsightFlow.git
cd InsightFlow

🟨 Step 2 — Create Virtual Environment
python -m venv venv
.\venv\Scripts\Activate

🟩 Step 3 — Install Requirements
pip install -r requirements.txt

🟧 Step 4 — Add Your OpenAI API Key

Windows:

setx OPENAI_API_KEY "your_key_here"


Restart PowerShell → verify:

echo $Env:OPENAI_API_KEY

🟥 Step 5 — Run the Engine
python insightflow_run.py

📂 Output Files:
output/InsightFlow_Report.pptx
output/InsightFlow_Report.pdf

🌐 Optional: Run the Web App
python web_app.py


Visit:

http://localhost:8000


Upload → Generate → Download.

<div align="center">
🏁 InsightFlow — Reporting Reimagined. Automated. Intelligent. Beautiful.

⭐ If you like this project, please star the repo on GitHub! ⭐

</div>


