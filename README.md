# CODE 365

This web app brings to you all the programming contests happening on various websites in one place and enables you to
set reminders so that you don't forget about the contests.

# Built with

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Library](https://img.shields.io/badge/Library-APScheduler-red)
![API](https://img.shields.io/badge/API-Kontests-orange)
![API](https://img.shields.io/badge/API-Google%20Calendar-brightgreen)
![Framework](https://img.shields.io/badge/Framework-Django-blue)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-blueviolet)

# Overview

-   For Aggregating the contest of various websites we have used [Konstest API](https://www.kontests.net/api), but for codechef we
    have made our own scrapper using Selenium.

-   if you set a reminder using this website it will notify you 24 hours before the contest via mail and give you a desktop notification
    10 minute before the contest. This feature has been set up using [Google's Calendar API v3](https://developers.google.com/calendar)

-   To update our Database periodically we have used [Advanced Python Scheduler Library](https://apscheduler.readthedocs.io/en/stable/)
    which makes the API call in the interval of 16 hours.

-   The Backend of this website has been made using Django and Frontend has been made using HTML, CSS, Bootsrap and JavaScript.

# Demo

![GIF](./code_365_DEMO.gif)

## Future Scope

-   Deploy the web app on heroku(for free Obviously)
-   Merge A2OJ problems with the websites
-   Front-End

## Creator's Contact

#### [Saurav Jha](https://www.linkedin.com/in/saurav-jha-603173136/) [Keshav Goel](https://www.linkedin.com/in/keshav-goel-258704194/)
