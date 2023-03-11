FROM python:3
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir flask_restful
EXPOSE 5000
CMD ["python","base.py"]
