FROM tensorflow/tensorflow:2.4.2
WORKDIR /app
ADD /app /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

