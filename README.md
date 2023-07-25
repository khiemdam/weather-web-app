<!-- Shields from shields.io -->
![Author][author-shield]
[![LinkedIn][linkedin-shield]][linkedin-url] [![Handshake][handshake-shield]][handshake-url] ![Status][status-shield]

# Workflow Web Application

### A web application from scratch that allows users to keep track of their upcoming events, tasks, and due dates. This web app is built on a Python Flask REST API for the back end, and uses HTML and Javascript for the front end UI/UX. The service will be deployed through AWS.

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

This project is meant to help me learn how to create a working web app with Flask, while getting more comfortable using python and javascript, as the language I've used for the majority of projects is c++. The project is also for helping me learn more about AWS and other similar services.

## Technologies
* Python (Flask)
* Javascript
* HTML
* Any IDE (I used VSCode)
* AWS

## Installation
Navigate to your desired directory. In your shell/terminal, type in the following:

For HTTPS
```
git clone https://github.com/khiemdam/workflow-web-app.git
```
For SSH Keys
```
git clone git@github.com:khiemdam/workflow-web-app.git
```

Make sure you have python installed (check by typing "python" in terminal).

Now, install dependencies from [requirements.txt](./requirements.txt), which can be done with:

```
pip install -r requirements.txt
```

## How To Get Started
I will be documenting my steps on how I built the back end and front end, which will be found in my [NOTES.md](./NOTES.md)

## How To Use
TODO

## To-Do List
##### Note: Backend tasks will be updated soon once I learn more about databases!
- [ ] Front End UI/UX
    - [ ] Design screen view of app (Draw This!! :O)
    - [ ] Build HTML from design idea
    - [ ] Implement Javascript interactions
    - [ ] Implement stubs/placeholders for backend calls
- [ ] Back End API
    - [X] Create structure
    - [X] Create a task resource
    - [X] Request handling
        - [X] Be able to get a task
        - [X] Be able to put a task
        - [X] Be able to delete a task
    - [ ] Create database/storage for data
        - [ ] Install sql
        - [ ] TODO
- [ ] Hook Together and Deploy
    - [ ] Connect front end and back end
    - [ ] Deploy to AWS

## Status
Back end: created structure for API, data handling, dealing with requests (get, put, delete)

Front end: TODO

## Credits
* [Pointers for how to make a web app](https://makingsmallercircles.com/articles/how-to-build-a-web-app/)
* [Python Rest API Explained](https://www.youtube.com/watch?v=GMppyAPbLYk&ab_channel=TechWithTim)
* [WordPress Markdown Reference Sheet](https://wordpress.com/support/markdown-quick-reference/)
* [Shields and Badges from shields.io](shields.io)

<!-- Links & Images -->
[author-shield]: https://img.shields.io/badge/Author-Khiem_Dam-555?style=for-the-badge&color=999
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-555?style=for-the-badge&logo=linkedIn
[linkedin-url]: https://www.linkedin.com/in/khiemd/
[handshake-shield]: https://img.shields.io/badge/Handshake-555?style=for-the-badge&logo=handshake&logoColor=white
[handshake-url]: https://app.joinhandshake.com/stu/users/31441591
[status-shield]: https://img.shields.io/badge/status-WIP-555?style=for-the-badge&color=FFA500