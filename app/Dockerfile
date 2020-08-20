FROM python:3.8-slim
MAINTAINER Anton Nikifarau 'a.tosick@gmail.com'
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]