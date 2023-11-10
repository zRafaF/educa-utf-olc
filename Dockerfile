FROM python:3.11


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt



ENV PB_URL https://educautf.td.utfpr.edu.br/db


EXPOSE 3000

CMD ["python", "src/main.py" "--port=3000"]