FROM python:3.11-slim

WORKDIR /service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY Scores.txt /Scores.txt

EXPOSE 5000

CMD ["python", "-m", "app.MainScores"]
