# vegeta Robot
A anime themef stable pluggable Telegram bot, based on Telethon.

<p align="center">
  <img src="./resources/extras/cipherx.jpg" alt="ToxygenX">
</p>

[![Stars](https://img.shields.io/github/stars/ToxygenX/Megatron?style=social)](https://github.com/ToxygenX/Megatron/stargazers)
[![Forks](https://img.shields.io/github/forks/ToxygenX/Megatron?style=social)](https://github.com/ToxygenX/Megatron/fork)
[![Python Version](https://img.shields.io/badge/Python-v3.9-blue)](https://www.python.org/)
[![Contributors](https://img.shields.io/github/contributors/ToxygenX/Megatron)](https://github.com/ToxygenX/Megatron/graphs/contributors)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/ToxygenX/Megatron/blob/main/LICENSE)
[![Size](https://img.shields.io/github/repo-size/ToxygenX/Megatron)](https://github.com/ToxygenX/Megatron/)

<details>
<summary>More Info</summary>
<br>
  Documentation soon..  <br />
</details>

# Deploy 
- [Heroku](https://github.com/ToxygenX/Megatron#Deploy-to-Heroku)
- [Local Machine](https://github.com/ToxygenX/Megatron#Deploy-Locally)

## Deploy to Heroku
- Get your `API_ID` and `API_HASH` from [here](https://my.telegram.org/) and click the below button!  <br />  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ToxygenX/Megatron) 

## Deploy Locally
- Get your `API_ID` and `API_HASH` from [here](https://my.telegram.org/)
- Get your `REDIS_URI` and `REDIS_PASSWORD` from [here](https://redislabs.com), tutorial [here](./resources/extras/redistut.md).
- Clone the repository: <br />
`git clone https://github.com/ToxygenX/Megatron.git`
- Go to the cloned folder: <br />
`cd Megatron`
- Create a virtual env:   <br />
`virtualenv -p /usr/bin/python3 venv`   
`. ./venv/bin/activate`
- Install the requirements:   <br />
`pip install -r requirements.txt`   
- Generate your `SESSION`:   
`bash sessiongen`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/ToxygenX/Megatron/blob/main/.env.sample).    
(You can either edit and rename the file or make a new file.)
- Run the bot:   
`bash resources/startup/startup.sh`

# Credits
* [Lonami](https://github.com/LonamiWebs/) for [Telethon](https://github.com/LonamiWebs/Telethon)

* UltroidTeam. This is a test platform. Don't moan that it's a kang in support chat. 
