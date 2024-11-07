FROM Python:3.12.4

COPY requirements.txt /api

WORKDIR /api

RUN pip install --no-cache-dir -r requirements.txt

COPY api/ .

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]