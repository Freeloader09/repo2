ARG BASE_IMAGE
FROM python:3.7-slim

#ARG DAGSTER_VERSION=1.3.13
COPY setup.py /setup.py
COPY pyproject.toml /pyproject.toml
COPY dagster_project /
# ==> Add Dagster layer
RUN \
    pip install \
        dagster \
        dagster-postgres \
        dagster-celery[flower,redis,kubernetes] \
        dagster-k8s \
        dagster-celery-k8s \
    && pip install -e "/"
# Cleanup
    &&  rm -rf /var \
    &&  rm -rf /root/.cache  \
    &&  rm -rf /usr/lib/python2.7 \
    &&  rm -rf /usr/lib/x86_64-linux-gnu/guile

# ==> Add user code layer
# Example pipelines
#COPY build_cache/ /