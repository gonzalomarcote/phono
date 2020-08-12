# Core Phono's python backend API
FROM python:3.8
LABEL maintainer="Gonzalo Marcote <gonzalomarcote@gmail.com>"
LABEL version="0.1"

# Install backend API
RUN mkdir /api
WORKDIR /api
COPY requirements.txt /api/requirements.txt
COPY api.py /api/api.py
RUN pip install -r requirements.txt

# Init backend API
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]
