FROM tensorflow/tensorflow
WORKDIR /app
ADD /app /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

