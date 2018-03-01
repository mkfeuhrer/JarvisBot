<h1 align="center"> Jarvis - Bot </h1> <br>
<p align="center">
  <a href="https://github.com/mkfeuhrer/JarvisBot">
    <img alt="Check on Zulip Chat" title="Jarvis-Bot" src="https://github.com/mkfeuhrer/JarvisBot/blob/master/images/JarvisBot.gif" width="550">
  </a>
</p>
<p align="center">
  Intelligently Interactive Bot. Built with Python and Zulip.
</p>

## Table of Contents

- [Introduction](#Introduction)
- [Features](#Features)
- [Deploy](#Deploy)
- [Feedback](#Feedback)
- [Contributors](#Contributors)
- [Contribute](#Contribute)
- [Acknowledgement](#Acknowledgement)

## Introduction

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub Stars](https://img.shields.io/github/stars/mkfeuhrer/JarvisBot.svg)](https://github.com/mkfeuhrer/) 
[![Current Version](https://img.shields.io/badge/version-1.0-green.svg)](https://github.com/mkfeuhrer/JarvisBot)

Intelligent Bot lets you perform utility and fun stuff like games, Built with Python and ZulipChat-Api, Jarvis-Bot is the most feature-rich unofficial ZulipChat Bot that is 100% free.

<p align="center">
  <img src = "https://github.com/mkfeuhrer/JarvisBot/blob/master/images/Zulip.jpg" width=550>
</p>

## Features

Jarvis-Bot holds following features -

* News based on Keyword
* Live Sports Score
* View Lyrics of Songs
* View Movie Details
* Weather forecasting
* Dictionary based search
* Currency Conversion Viewer
* Calculator 
* To-Do List
* NLP based Instant Response
* Remote Login Via Bot
* Access file lists of a system via bot
* View Man Page of any Linux Command Line
* Games 
  - Hangman
  - Scrabble
  - Stone-Paper-Scissor
  - Memory-Game  

## Deploy

To deploy Jarvis bot using your local machine as server, follow following steps -

* Firstly create a zulip organisation on which you want to deploy bot. If you already have one then you may skip this step.
* Register a new bot user on the Zulip server's web interface.
	* Log in to the Zulip server.
	* Navigate to Settings -> Your bots -> Add a new bot. Select Generic bot for bot type, set both bot-name and bot username to Jarvis and click on Create bot.
	* A new bot user should appear in the Active bots panel.
* Download the bot's zuliprc configuration file to your computer.
	* Go to Settings -> Your bots
	* In the Active bots panel, click on the little green download icon to download its configuration file zuliprc (the structure of this file is explained here).
	* Copy the downloaded file to your home directory and rename it as '.zuliprc'.
* Make sure sure that your system has following packages installed -
	* enchant (Please make sure your enchant version is <= 1.6.1-2)
	* sshpass
	* aspell-en
* Install all required python packages, rum command ```pip3 install -r requirements.txt```
* In line 23 of /bot/jarvisBot.py file change the site parameter with the URL of your organisation.
* Also update BOT_MAIL variable with the mail ID of your bot.
* Now we are all set, to run bot enter following command ```python3 jarvisBot.py```
* You can now finally use power of Jarvis in your organisation.

Note: By default Jarvis bot only responds to mentions in private messages. If you want to change this behaviour so that Jarvis also replies to mentions in stream messages then do following changes - 
	* In line 137 of jarvisBot.py change the value of type from private to stream.
	* In line 139 of jarvisBot.py change the value of to from message["sender_email"] to message["display_recipient"]

Please also note some of the features currently may not work properly when Jarvis is used in stream.


## Feedback

Feel free to send us feedback on [Email](mailto:mohitfeuhrer@gmail.com) or [file an issue](https://github.com/mkfeuhrer/JarvisBot/issues).

## Contributors

<ul>
  <li> <a href="https://github.com/mkfeuhrer">Mohit Khare</a></li>
  <li> <a href="https://github.com/avisheksanvas">Avishek Sanvas</a></li>
  <li> <a href="https://github.com/Abhey">Abhey Rana</a></li>
  <li> <a href="https://github.com/forceawakened">Prabhat Singh</a></li>
</ul>

## Contribute

<ul>
  <li>Feel free to report issues and bugs.It will be helpful for future launches of application.</li>
  <li>All Suggestions are welcome.</li>
  <li>Fork repository and Contribute.</li>
</ul>

## Acknowledgment

Thanks to [Zulip](https://zulipchat.com/) for providing Zulip Api and Platform.
