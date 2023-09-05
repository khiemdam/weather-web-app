<!-- Shields from shields.io -->
![Author][author-shield]
[![LinkedIn][linkedin-shield]][linkedin-url] [![Handshake][handshake-shield]][handshake-url] ![Status][status-shield]

# Weather Web Application

### A web application from scratch that allows users to view the temperature, humidity, and wind speed in any city in the world. This web app is built utilizing a REST API to make back end calls, and uses HTML, CSS and Javascript for the front end UI/UX. Enter the name of a city into the search bar, and the forecast for the day will be displayed!

![Website Image](/static/images/webapp-pages.png)

## Table of Contents
* [Motivation](#motivation)
* [Technologies](#technologies)
* [Installation](#installation)
* [How To Use](#how-to-use)
* [How To Get Started](#how-to-get-started)
* [To-Do List](#to-do-list)
* [Status](#status)
* [Credits](#credits)

## Motivation

This project is meant to help me learn how to create a working web app while getting more comfortable using python and javascript, as the language I've used for the majority of projects is c++.

## Technologies
* Python
* Javascript
* HTML
* CSS
* Any IDE (I used VSCode)

## Installation
Navigate to your desired directory. In your shell/terminal, type in the following:

For HTTPS
```
git clone https://github.com/khiemdam/weather-web-app.git
```
For SSH Keys
```
git clone git@github.com:khiemdam/weather-web-app.git
```

Make sure you have python installed (check by typing "python" in terminal).


## How To Use
Once you have all of the files, navigate to the main directory and type

```
python3 -m http.server 8000
```

You may need to create a virtual environment, but once that is done, go to http://localhost:8000/ and you will be able to access the web app!

## Status
Complete! If I make another web app, I am planning to make a workflow management app in the future!

## Credits
* [Pointers for how to make a web app](https://makingsmallercircles.com/articles/how-to-build-a-web-app/)
* [Modifying and Querying Data in Flask](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/)
* [Python Rest API Explained](https://www.youtube.com/watch?v=GMppyAPbLYk&ab_channel=TechWithTim)
* [WordPress Markdown Reference Sheet](https://wordpress.com/support/markdown-quick-reference/)
* [Shields and Badges from shields.io](shields.io)

<!-- Links & Images -->
[author-shield]: https://img.shields.io/badge/Author-Khiem_Dam-555?style=for-the-badge&color=999
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-555?style=for-the-badge&logo=linkedIn
[linkedin-url]: https://www.linkedin.com/in/khiemd/
[handshake-shield]: https://img.shields.io/badge/Handshake-555?style=for-the-badge&logo=handshake&logoColor=white
[handshake-url]: https://app.joinhandshake.com/stu/users/31441591
[status-shield]: https://img.shields.io/badge/status-completed-555?style=for-the-badge&labelColor=555&color=03c04a
