# Core Phono's python backend
FROM python:3.8
LABEL maintainer="Gonzalo Marcote <gonzalomarcote@gmail.com>"
LABEL version="1.1"

# Install backend
RUN mkdir /api
WORKDIR /api
COPY ./api/requirements.txt /api/requirements.txt
COPY ./api/api.py /api/api.py
RUN pip install -r requirements.txt

# Init backend
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]
