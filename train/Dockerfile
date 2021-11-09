FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-7

ENV ACCESS_TOKEN=<ACCESS_TOKEN>

ADD train.py /mnist/train/train.py
ENTRYPOINT [ "python", "/mnist/train/train.py", "--ACCESS_TOKEN", ${ACCESS_TOKEN}]
