FROM python:3.7 AS builder
# Set application name
ARG APP_NAME=docker_builder

# Install poetry
RUN pip install poetry
# Install dependencies before copy source file to cache dependencies
RUN mkdir -p /root/${APP_NAME}/
WORKDIR /root/${APP_NAME}/
COPY ./poetry.lock ./
COPY ./pyproject.toml ./
ENV LANG C.UTF-8

# This is where pip will install to
ENV PYROOT /pyroot
# A convenience to have console_scripts in PATH
ENV PATH $PYROOT/bin:$PATH
ENV PYTHONUSERBASE $PYROOT
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 poetry install

####################
# Production image #
####################
FROM python:3.7-slim AS prod
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install busybox && \
    apt-get clean
RUN busybox --install
# This is our runtime, again
# It's better be refactored to a separate image to avoid instruction duplication
RUN ln -sf /usr/bin/pip3 /usr/bin/pip
RUN ln -sf /usr/bin/python3 /usr/bin/python
ENV PYROOT /pyroot
ENV PATH $PYROOT/bin:$PATH
ENV PYTHONPATH $PYROOT/lib/python:$PATH
# This is crucial for pkg_resources to work
ENV PYTHONUSERBASE $PYROOT
# Finally, copy artifacts
COPY --from=builder $PYROOT/ $PYROOT/
# In most cases we don't need entry points provided by other libraries
RUN mkdir -p /root/${APP_NAME}/
WORKDIR /root/${APP_NAME}/
# Copy source files
COPY . .