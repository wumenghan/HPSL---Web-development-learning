# HPSL---Web-development-learning
This repository is used for traning new undergrates for web development. 

## Claims
Learners should pick up basic web development languages (e.g., HTML, CSS, Javascript) before using this tutorial. Currently, only Meng-Han and Gaoping use ReactJS for front end development. Other members in HPSL may use different front end library. As for back end, HPLS use [Flask](http://flask.pocoo.org/).

## Goals
The goals of this tutorial are:
1. Set up a workflow to develop your web app locally, as well as run it on hci server once it is ready to go public. 

## Overview
In this tutorial, you will learn to create a project using `create-react-app`.

## Create a project
1. Install `create-react-app` in your repository.
```bash
npm i -g create-react-app
```
You should install Node.js before running this command. 
2. Create a folder for your project
```bash
mkdir YOUR_PROJET_NAME
```
3. Create `client` folder using `create-react-app`
```bash
cd YOUR_PROJET_NAME  && create-react-app client
```
4. Set up environments and install packages in `YOUR_PROJET_NAME` directory.
Install packages
```bash
npm init
npm i --save-dev concurrently
```
Modify `package.json` file and add the following lines into `scripts` attribute.
```json
"scripts": {
    "start": "concurrently \"npm run server\" \"npm run client\"",
    "server": "python server.py",
    "client": "node start-client.js"
}
```
Copy `skeleton/server.py`, `skeleton/start-client.js` and put them to your `YOUR_PROJET_NAME` directory.

Once you finish these settings, your directory structure will be like this:
```
YOUR_PROJET_NAME
├── client
├── node_modules
├── package.json
├── package-lock.json
├── server.py
└── start-client.js
```

## Test it locally. (Development phase)
During development phase, we will run the code locally. 

Go to your `YOUR_PROJET_NAME` directory and type the following command.
```bash
npm start
```
Ideally, your browser will pop up your app automatically.

## Test it on hci server. (Production phase)
You will run your app on server only when your app is ready for production, meaning that your app is ready to go public. <br>
Sync your file to the server and run this command. 
```bash
cd client && npm run build
```
This command will compile all your code AND create a folder named `build`. All your front end code will be put into that folder.
```bash
cd .. && npm run start
```
Go to `https://crowd.ecn.purdue.edu/YOUR_PORT/` and you will see your app. For example if your PORT is 8001, then the url should be `https://crowd.ecn.purdue.edu/01/`





