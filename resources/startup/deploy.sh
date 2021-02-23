
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

apt-get update
apt-get upgrade -y
apt-get install -y --no-install-recommends ffmpeg neofetch mediainfo megatools
apt-get autoremove --purge

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
