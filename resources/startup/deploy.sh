
echo "
   _______       __             _  __
  / ____(_)___  / /_  ___  ____| |/ /
 / /   / / __ \/ __ \/ _ \/ ___/   /
/ /___/ / /_/ / / / /  __/ /  /   |
\____/_/ .___/_/ /_/\___/_/  /_/|_|
      /_/
	    °•° Deployment Begins •°•
"
echo '
        •• Getting Packages and Installing
'

export DEBIAN_FRONTEND=noninteractive
export TZ=Asia/Tehran 
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

apt update && apt upgrade -y && apt install --no-install-recommends -y \
    debian-keyring \
    debian-archive-keyring \
    bash \
    curl \
    git \
    util-linux \
    libffi-dev \
    libjpeg-dev \
    libjpeg62-turbo-dev \
    libwebp-dev \
    linux-headers-amd64 \
    musl-dev \
    musl \
    neofetch \
    python3-lxml \
    postgresql \
    postgresql-client \
    libpq-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    openssl \
    pv \
    jq \
    wget \
    python3-dev \
    libreadline-dev \
    libyaml-dev \
    zlib1g \
    ffmpeg \
    libssl-dev \
    libgconf-2-4 \
    libxi6 \
    zlib1g-dev \
    xvfb \
    unzip \
    make \
    libopus0 \
    libopus-dev \
    gcc \
    mediainfo \
    megatools

echo '
        •• Cloning Repository
'
git clone https://github.com/CipherX1-ops/Megatron.git /root/CipherX1-ops/

echo '
	•• Getting Libraries and Installing
'
pip install --upgrade pip setuptools wheel
pip install search-engine-parser==0.6.2
pip install -r /root/CipherX1-ops/requirements.txt

echo "

             _______       __             _  __
            / ____(_)___  / /_  ___  ____| |/ /
           / /   / / __ \/ __ \/ _ \/ ___/   /
          / /___/ / /_/ / / / /  __/ /  /   |
          \____/_/ .___/_/ /_/\___/_/  /_/|_|
              /_/
			•°• Deployed Successfully °•°
		   •• Wait till python images are pushed
	   •• Give build logs to @hackintush if build fails
"
