FROM python:3.8

#libXX系はgpuのためのライブラリっぽい
SHELL ["/bin/bash", "-c"]
RUN apt update && apt upgrade -y
RUN apt-get update && apt-get install -y \
        git \
        sudo \
        wget \
        vim \
        zip \
        zlib1g-dev \
        curl \
        unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG USERNAME=dev-user
ARG GROUPNAME=dev-user
ARG UID=1000
ARG GID=1000
ARG PASSWORD=dev-user

#追加したユーザでsudoを使えるようにする
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME  && \
    adduser dev-user sudo && \
    echo $USERNAME:$PASSWORD | chpasswd && \
    echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

#rootのパスワードがわからないのでパスワードを変更
RUN echo "root:root" | chpasswd

RUN pip install --upgrade pip