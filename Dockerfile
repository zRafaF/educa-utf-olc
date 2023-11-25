FROM python:3.11

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3005

CMD ["python", "src/main.py", "--host", "0.0.0.0", "--port", "3005", "--pb_url", "https://educautf.td.utfpr.edu.br/db"]
