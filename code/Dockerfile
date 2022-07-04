FROM python:3.7
WORKDIR /my_src_DEVELOP
#install whatever you want
RUN pip install "fastapi[all]"

COPY requirements.txt
RUN pip install -r requirements.txt

# COPY  . /my_src_dir/

