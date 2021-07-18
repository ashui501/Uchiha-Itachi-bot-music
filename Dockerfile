# Mᴇgᴀᴛrᴏn Bot
# Copyright (C) 2020 Mᴇgᴀᴛrᴏn 
# This file is a part of < https://github.com/CipherX1-ops/Megatron/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/CipherX1-ops/Megatron/blob/main/LICENSE/>

FROM programmingerror/ultroid:b0.1

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN git clone https://github.com/CipherX1-ops/Megatron.git /root/CipherX1-ops/

WORKDIR /root/CipherX1-ops/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "resources/startup/startup.sh"]
