FROM alpine:latest
COPY app/ app/
WORKDIR /app
RUN apk add --no-cache --update-cache python3 py3-pip \
    && pip3 install -r requirements.txt \
    && rm requirements.txt

CMD ["python3", "app.py"]