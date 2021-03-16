# Mᴇgᴀᴛrᴏn Bot
# Copyright (C) 2020 Mᴇgᴀᴛrᴏn 
# This file is a part of < https://github.com/CipherX1-ops/Megatron/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/CipherX1-ops/Megatron/blob/main/LICENSE/>.

FROM cipherx1-ops/megatron:0.0.3
RUN git clone https://github.com/CipherX1-ops/Megatron.git /root/CipherX1-ops/
WORKDIR /root/CipherX1-ops/
RUN pip install -r requirements.txt
CMD ["bash", "resources/startup/startup.sh"]
