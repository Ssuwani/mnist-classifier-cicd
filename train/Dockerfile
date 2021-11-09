FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-7

RUN pip install PyGithub

ENV ACCESS_TOKEN=<ACCESS_TOKEN>

ADD utils.py /mnist/train/utils.py
ADD train.py /mnist/train/train.py

ENTRYPOINT [ "python", "/mnist/train/train.py" ]
