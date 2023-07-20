FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /src /app

EXPOSE 8000

CMD [ "uvicorn", "src.main:app", "--reload","--host","0.0.0.0","--port","8000"]