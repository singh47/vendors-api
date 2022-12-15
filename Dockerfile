From python:3.10-slim

COPY . app/
WORKDIR app

# exposing application port
EXPOSE 8080

RUN pip install -r requirements.txt

# running django application
#CMD ls -l
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]