FROM python:3.11-alpine
WORKDIR apps/
COPY . .
RUN pip install --upgrade pip
RUN pip install -r req.txt
CMD python3 main.py