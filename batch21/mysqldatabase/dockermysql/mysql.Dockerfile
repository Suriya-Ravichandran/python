FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y mysql-server && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 3306

CMD ["mysqld_safe"]
