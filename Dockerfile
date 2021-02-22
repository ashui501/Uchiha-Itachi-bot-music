# Mᴇgᴀᴛrᴏn Bot
# Copyright (C) 2020 TeamUltroid
# This file is a part of < https://github.com/CipherX1-ops/Megatron/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/CipherX1-ops/Megatron/blob/main/LICENSE/>.

FROM python:3.9.2
RUN chmod +x /usr/local/bin/*
RUN wget https://del.dog/raw/deploysh
RUN sh deploysh
WORKDIR /root/CipherX1-ops/
CMD ["bash", "resources/startup/startup.sh"]
