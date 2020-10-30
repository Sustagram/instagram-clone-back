FROM python:3.7.9

EXPOSE 8000

COPY / /workspace
WORKDIR /workspace

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]