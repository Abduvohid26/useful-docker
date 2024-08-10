FROM python:3.11.4-slim-buster

RUN addgroup --system abduvohid && adduser --system --group abduvohid

WORKDIR /furniture

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y \
    libmagic1 \
    netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /furniture/entrypoint.sh
RUN chmod +x /furniture/entrypoint.sh

RUN mkdir staticfiles 

COPY . .

RUN chown -R abduvohid:abduvohid /furniture

USER abduvohid

ENTRYPOINT ["sh", "/furniture/entrypoint.sh"]
