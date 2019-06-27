FROM python:3.7-slim

RUN useradd -m fizz-buzz

ARG INSTALL_ARGS
# ARG CI_COMMIT_TAG $(git symbolic-ref -q --short HEAD)
# ENV CI_COMMIT_TAG=$CI_COMMIT_TAG
WORKDIR /fizz-buzz
COPY --chown=fizz-buzz:fizz-buzz . /fizz-buzz
RUN pip install pipenv
RUN pipenv install --system $INSTALL_ARGS
USER fizz-buzz

CMD ["python", "-m" , "service"]
