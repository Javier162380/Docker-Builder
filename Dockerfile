FROM python:3.7 AS builder
# Set application name
ARG APP_NAME=docker-builder

# Install poetry
RUN pip install poetry
# Install dependencies before copy source file to cache dependencies
RUN mkdir -p /root/${APP_NAME}/
WORKDIR /root/${APP_NAME}/
COPY . /root/${APP_NAME}/
ENV LANG C.UTF-8
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false \
  && poetry install
WORKDIR /root/${APP_NAME}/docker_builder/
