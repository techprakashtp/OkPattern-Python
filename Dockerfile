FROM python:latest
RUN  mkdir WORK_REPO
RUN  cd  WORK_REPO
WORKDIR  /WORK_REPO
ADD okpattern.py .
CMD ["python", "-u", "okpattern.py"]
