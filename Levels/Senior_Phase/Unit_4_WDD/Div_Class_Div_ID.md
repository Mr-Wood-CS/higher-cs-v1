# Div Class ID and Div Class

# Div

The HTML <div> tag is used for defining a section of your document. 

With the <div> tag, you can group large sections of HTML together and format them with CSS.

```html
<div>

    <h1> Coding is Fun!</h1>

</div>
```
## Class

The HTML class attribute is used to assigned some properties to HTML elements. 

All HTML elements within the same class attributed will have the same format and style. 

```html

<style>

.coding{ background-color: blue;}



</style>

<div class = "coding">

    <h1> Coding is Fun!</h1>

</div>
```
## ID

The HTML ID attribute is used to specify a unique ID for an HTML element. 

You cannot have more than one element with the same ID in an HTL document. 

```html

<style>

.coding{ background-color: blue;}

#header {color: yellow;}

</style>

<div class = "coding">

    <h1 id = "header"> Coding is Fun!</h1>

</div>
```