# AJAX
In this warmup, you will learn how to use async call to update your UI. 

## Set up your proxy
Add this line into `client/package.json`. Otherwise, your sever won't get your call. 
```json
  "proxy": "http://localhost:YOUR_PORT/",
```

## Short history
AJAX stands for <b>A</b>synchronous <b>Ja</b>vascript and <b>X</b>ML. It is a technique that allows you to <b>partially</b> update your web page. Prior to the invention of AJAX, the browser has to reload the whole web page whenever there is a samll change. Obviously, this is inefficient. With AJAX, developers are able to contact the server after the web page is loaded and only update the parts that you want to. 

## Goals
The goals of this warmup is as follows:
1. Contact server using Async call.
2. Update UI based on data you fetch from server.
3. Understand what is JSON and play with it.
4. Use Python to read csv file.

## Task
Create buttons for each data you collected from MTurk. When the button is clicked, fire an async call to server and get the corresponding data. Send that data back and update the UI.

## Template
I have written some codes for you to start with. You can adapt it to complete this warmup. <b>I did not test my code, it might has bugs.</b>
Note that you should follow the naming convention for different languages. <br>
Javascript: https://google.github.io/styleguide/jsguide.html <br>
Python: https://github.com/google/styleguide/blob/gh-pages/pyguide.md

## Resources
* [JSON](https://www.json.org/)
* [AJAX in React](https://reactjs.org/docs/faq-ajax.html)
* [DOM elements in React](https://reactjs.org/docs/dom-elements.html)
* [Read csv in Python](https://docs.python.org/2/library/csv.html)