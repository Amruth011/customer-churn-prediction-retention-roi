FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --timeout=1000 \
    --retries=10 \
    --no-deps \
    -r requirements.txt && \
    pip install --no-cache-dir \
    --timeout=1000 \
    --retries=10 \
    streamlit==1.28.0 pandas==2.0.3 numpy==1.24.3 \
    scikit-learn==1.3.0 xgboost==1.7.6 joblib==1.3.2 \
    plotly==5.17.0 shap==0.43.0 openpyxl==3.1.2

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
