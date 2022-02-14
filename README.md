# Building a Flask API in a Ubuntu Server EC2 instance
The [Seattle Data Guy](https://www.theseattledataguy.com/data-engineering-roadmap-for-2021-12-steps-to-help-you-go-from-0-to-data-engineering/#page-content) recommended it, so I learned how to do it.

This is a mini-project to teach myself a bit about Flash and API's. I set up the environment in an AWS EC2 instance running Ubuntu Server 18.04, and Python 2.7

I'm running flask in a virtual environment to keep it isolated from the main python install (read about that [here](https://pythonhow.com/python-tutorial/flask/Using-a-virtual-environment-with-your-flask-app/)). The app runs in a docker container.

This API will get more interesting in the next little while. Right now it's just test functions and a very slim Docker container.