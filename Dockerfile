FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 3005

CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "3005", "--pb_url", "https://educautf.td.utfpr.edu.br/db/api", "--root_path", "/olc-api"]
