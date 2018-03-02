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
- [Screenshots](#Screenshots)
- [Feedback](#Feedback)
- [Contributors](#Contributors)
- [Contribute](#Contribute)
- [Announcements](#Announcements)
- [Acknowledgement](#Acknowledgement)

## Introduction

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub Stars](https://img.shields.io/github/stars/mkfeuhrer/JarvisBot.svg)](https://github.com/mkfeuhrer/) 
[![Current Version](https://img.shields.io/badge/version-1.1-green.svg)](https://github.com/mkfeuhrer/JarvisBot)

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
* Make sure sure that your system has following packages installed -
	* enchant (Please make sure your enchant version is <= 1.6.1-2) 
	* sshpass (For debian based system install using ```sudo apt-get install sshpass```)
	* aspell-en - (For debian based system install using ```sudo apt-get install aspell-en```)
* Install all required python packages, rum command ```pip3 install -r requirements.txt```
* Now we are all set, to run bot enter following command ```zulip-run-bot <absolute path to jarvisBot.py file > --config-file <absolute path to downloaded zuliprc file>```
* You can now finally use power of Jarvis in your organisation.

## Screenshots

<strong> Finding Lyrics of a song :</strong> 
<p align="center">
  <img src = "https://github.com/mkfeuhrer/JarvisBot/blob/master/screenshots/Screen%20Shot%202018-01-28%20at%203.43.19%20AM.png" width=550>
</p>

<strong> Weather Forecasting :</strong>
<p align="center">
  <img src = "https://github.com/mkfeuhrer/JarvisBot/blob/master/screenshots/Screen%20Shot%202018-01-28%20at%203.48.04%20AM.png" width=550>
</p>

<strong> Simple Calculator :</strong>
<p align="center">
  <img src = "https://github.com/mkfeuhrer/JarvisBot/blob/master/screenshots/Screen%20Shot%202018-01-28%20at%203.49.56%20AM.png" width=550>
</p>

<strong> To-do Manager :</strong>
<p align="center">
  <img src = "https://github.com/mkfeuhrer/JarvisBot/blob/master/screenshots/Screen%20Shot%202018-01-28%20at%203.55.41%20AM.png" width=550>
</p>

<p align="center">
  <img src = "https://github.com/mkfeuhrer/JarvisBot/blob/master/screenshots/Screen%20Shot%202018-01-28%20at%203.57.05%20AM.png" width=550>
</p>

<strong> Popular Trending Shows : </strong>
<p align="center">
  <img src = "https://github.com/mkfeuhrer/JarvisBot/blob/master/screenshots/movies.png" width=550>
</p>

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

## Announcements

We have updated Jarvis Bot and it now uses latest python-zulip-api. Also now all the features of Jarvis bot can be used in both stream as well as private messages.

## Acknowledgment

Thanks to [Zulip](https://zulipchat.com/) for providing Zulip Api and Platform.
