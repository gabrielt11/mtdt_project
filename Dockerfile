FROM python:3.10

RUN pip install fastapi
RUN pip install uvicorn

COPY ./ ./

CMD ["python3", "main.py"]