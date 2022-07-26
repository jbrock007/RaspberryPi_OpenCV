# Project content

This repository contains the base folders to conduct each task, as follows:

## Task 1 - 3

You should use the files in the corresponding folders to solve each task. Each folder has a `main.py` script to test your code. The folders are:

| Task |               Folder |
|-----:|---------------------:|
|   1  | task1_opencv_control  |
|   2  | task2_motor_control |
|   3  | task3_sensor_control |

## Task 4

The root folder contains the necessary files and folders to complete the task 4. As you already know, the results of previous tasks is going to be employed by a Flask web application. Take the following information into account:

1. *requirements.txt*: this file contains the libraries that you might required for running the app. After creating your environment you should install these libraries as follows:

```
pip install -r requirements.txt
```

Use *requirements_raspi.txt* for Raspberry Pi.

2. *app.py*: this file is a script to run the Flask application. This application should work even if you haven't completed previous tasks. I will just do dummy things, like printing messages on the development server console.
3. *static*: this folder contains the main client-side script of this application.
4. *templates*: this folder contains the index template since this is a one-page application.
