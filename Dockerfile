# Mᴇgᴀᴛrᴏn Bot
# Copyright (C) 2020 Mᴇgᴀᴛrᴏn 
# This file is a part of < https://github.com/CipherX1-ops/Megatron/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/CipherX1-ops/Megatron/blob/main/LICENSE/>.

FROM programmingerror/ultroid:v0.0.1

RUN git clone https://github.com/CipherX1-ops/Megatron.git /root/CipherX1-ops/

RUN git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me
WORKDIR /root/CipherX1-ops/

RUN pip3 install -r requirements.txt
RUN npm install -g npm@7.11.2 -g
RUN npm install
RUN npm run build
