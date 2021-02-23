# Mᴇgᴀᴛrᴏn Bot
# Copyright (C) 2020 Mᴇgᴀᴛrᴏn 
# This file is a part of < https://github.com/CipherX1-ops/Megatron/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/CipherX1-ops/Megatron/blob/main/LICENSE/>.

FROM python:3.9.2
RUN chmod +x /usr/local/bin/*
#RUN wget https://github.com/CipherX1-ops/cython 
RUN wget https://raw.githubusercontent.com/CipherX1-ops/Megatron/main/resources/startup/deploy.sh
RUN sh deploy.sh
WORKDIR /root/CipherX1-ops/
CMD ["bash", "resources/startup/startup.sh"]
