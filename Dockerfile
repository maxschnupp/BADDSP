FROM tensorflow/tensorflow:2.4.0
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD /app /app