FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["python", "main.py"]
