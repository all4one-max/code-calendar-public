# CODE 365

This web app brings to you all the programming contests happening on various websites in one place and enables you to
set reminders so that you don't forget about the contests.

# Built with

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Library](https://img.shields.io/badge/Library-keras-red)
![Library](https://img.shields.io/badge/Library-tensorflow-blue)
![Framework](https://img.shields.io/badge/Framework-flask-success)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-blueviolet)

# Overview

-   For Aggregating the contest we have used Konstest API(https://www.kontests.net/api).

-   One thing to note is that the words in the sentence has been vectorized, so similar words may have similar vectors, which is a better option than using bag of words or Tf-Idf, which do not take into account the semantics of sentences.

-   Training a deep learning model on local system takes a lot of time, thats why the model has been trained on google collab with GPU session.

-   Finally, to make the web app Flask has been used in the Backend and HTML, CSS and Bootstrap on the frontend.

# Demo

![GIF](./code_365_DEMO.gif)
