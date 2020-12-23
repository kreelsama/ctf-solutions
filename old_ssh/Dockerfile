FROM debian/eol:potato

RUN apt-get update && \
    apt-get install -y gcc libc6-dev libz-dev make

COPY ./share/openssh-2.1.1p1 /root/openssh-2.1.1p1
COPY ./share/openssl-OpenSSL_0_9_5 /root/openssl-OpenSSL_0_9_5
COPY ./share/run.sh /root/run.sh

WORKDIR /root/openssl-OpenSSL_0_9_5
RUN ./Configure linux-elf && make && make install

WORKDIR /root/openssh-2.1.1p1
RUN ./configure i686 && make && make install

RUN ssh-keygen -d -b 1024 -f /usr/local/etc/ssh_host_dsa_key
RUN ssh-keygen -b 1024 -f /usr/local/etc/ssh_host_key

RUN sed -e "s/PermitEmptyPasswords\ no/PermitEmptyPasswords\ yes/" /usr/local/etc/sshd_config | tee /usr/local/etc/sshd_config

RUN echo "root:root" | chpasswd
RUN chmod +x /root/run.sh

CMD ["/root/run.sh"]
