FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --upgrade pip && pip install torch==1.12.1+cpu torchvision==0.13.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu

COPY backend/src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY backend/src .

CMD [ "uvicorn", "main:app" , "--host=0.0.0.0", "--port=8000"]