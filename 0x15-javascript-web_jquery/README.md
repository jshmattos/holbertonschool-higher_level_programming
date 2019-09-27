# 0x15. Javascript - Web JQuery

## Description

Learning Objectives

* Why jQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
* How to select HTML elements in Javascript
* How to select HTML elements with jQuery
* What are differences between ID, class and tag name selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a GET request with jQuery Ajax
* How to make a POST request with jQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events

## Requirements

- All files are created and executed on Ubuntu 14.04 LTS using Nodejs (version 10)
- All Javascript code is linted with semistandard

### [0. No jQuery](./0-script.js)
* Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
  * You must use document.querySelector to select the HTML tag
  * You can’t use the jQuery API

### [1. With jQuery](./1-script.js)
* Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API

### [2. Click and turn red](./2-script.js)
* Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API

### [3. Add `.red` class](./3-script.js)
* Write a Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API

### [4. Toggle classes](./4-script.js)
* Write a Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header:
  * The HEADER tag must always have one class: red or green, never both in the same time, never empty.
  * If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API

### [5. List of elements](./5-script.js)
* Write a Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item:
  * The new element must be: <li>Item</li>
  * The new element must be added to UL.my_list
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API

### [6. Change the text](./6-script.js)
* Write a Javascript script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API

### [7. Star wars character](./7-script.js)
* Write a Javascript script that fetches and replaces the name of this URL: https://swapi.co/api/people/5/?format=json
  * The name must be displayed in the HTML tag DIV#character
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API

### [8. Star Wars movies](./8-script.js)
* Write a Javascript script that fetches and lists all movies title by using this URL: https://swapi.co/api/films/?format=json
  * All movie titles must be list in the HTML tag UL#list_movies
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API

### [9. Say Hello!](./9-script.js)
* Write a Javascript script that fetches and prints how to say “Hello” depending of the language: (here in French) https://fourtonfish.com/hellosalut/?lang=fr
  * The translation of “hello” must be display in the HTML tag DIV#hello
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API
  * Your script must work when it is imported from the HEAD tag

### [10. No jQuery - document loaded](./100-script.js)
* Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
  * You must use document.querySelector to select the HTML tag
  * You can’t use the jQuery API
  * Note: Your script must be imported from the HEAD tag, not at the end of the HTML

### [11. List, add, remove](./101-script.js)
* Write a Javascript script that adds, removes and clears LI elements from a list when the user clicks:
  * The new element must be: <li>Item</li>
  * The new element must be added to UL.my_list
  * When the user clicks on DIV#add_item: a new element is added to the list
  * When the user clicks on DIV#remove_item: a last element is removed to the list
  * When the user clicks on DIV#clear_list: all elements of the list are removed
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API
  * You script must be work when it imported from the HEAD tag

### [12. Say hello to everybody!](./102-script.js)
* Write a Javascript script that fetches and prints how to say “Hello” depending of the language
  * You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
  * The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
  * The translation must be fetch when the user clicks on INPUT#btn_translate
  * The translation of “Hello” must be display in the HTML tag DIV#hello
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API
  * You script must be work when it imported from the HEAD tag

### [13. And press ENTER](./103-script.js)
* Write a Javascript script that fetches and prints how to say “Hello” depending of the language
  * You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
  * The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
  * The translation must be fetch when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
  * The translation of “Hello” must be display in the HTML tag DIV#hello
  * You can’t use document.querySelector to select the HTML tag
  * You must use the jQuery API
  * You script must be work when it imported from the HEAD tag

## Author
* **Tu Vo** - [tuvo1106](https://github.com/tuvo1106)
