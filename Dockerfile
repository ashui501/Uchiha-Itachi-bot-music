# Mᴇgᴀᴛrᴏn Bot
# Copyright (C) 2020 Mᴇgᴀᴛrᴏn 
# This file is a part of < https://github.com/CipherX1-ops/Megatron/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/CipherX1-ops/Megatron/blob/main/LICENSE/>

FROM python:3.9.5-buster

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN git clone https://github.com/ToxygenX/Megatron.git /root/ToxygenX/

WORKDIR /root/ToxygenX/

RUN pip3 install -U pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install -r resources/extras/local-requirements.txt

CMD ["bash", "resources/startup/startup.sh"]
