FROM python

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN sed -i "s/http:\/\/deb.debian.org/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && apt-get update && apt-get install -y socat
RUN useradd -m ctf

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome

WORKDIR /home/ctf
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

COPY ./bin/ /home/ctf/
RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

CMD ["/start.sh"]

EXPOSE 9999

