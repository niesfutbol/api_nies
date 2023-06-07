FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    fastapi \
    flake8 \
    mutmut \
    pandas \
    pylint \
    pytest \
    pytest-cov \
    requests \
    uvicorn
RUN curl -fsSL https://deta.space/assets/space-cli.sh | sh
EXPOSE 80
WORKDIR /app
COPY ./app .
CMD ["make", "run"]
