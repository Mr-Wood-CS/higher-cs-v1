# CSS Selectors

**Type Selectors**

A type selector styles every instance of a specific HTML element.

For example:

```css
h1 { font-family: sans-serif; }
h2 { font-family: sans-serif; }
```

This can also be written in a shorter way:

```css
h1, h2 { font-family: sans-serif; }
```

Both examples do the same thing. They apply the same style to all `<h1>` and `<h2>` elements on the page.

However, this creates a problem.

If a webpage needs each heading to be a different colour, we cannot use a type selector because it affects every heading of that type. In this case, we need a different way to target individual elements.

**Classes**

A class selector is used when you want the same style to be applied to more than one element.

The elements do not need to be the same type. As long as the CSS property works for them, they can share the same class. For example, the `color` property can be used on different headings or paragraphs.

There are two steps when using a class selector.

First, create the class rule in your CSS file:

```css
.black { color: black; }
```

The dot (`.`) before the name tells CSS that this is a class.

Second, assign the class inside your HTML:

```html
<h1 class="black">This H1 heading is black</h1>
```

You can add this same class to any other element if you want it to use the same style.

**ID Selectors**

An ID selector is used when you want to style one specific element on a page.

Unlike a class, an ID should only appear once in a webpage. It is meant to target a single, unique element.

IDs can also be used as named anchors. This allows you to link directly to a particular section of a page.

An ID selector has a higher priority than a type selector or a class selector. This means it will override them if more than one rule applies.

To create an ID selector in CSS, use the `#` symbol before the name:

```css
#paragraph { text-align: center; color: red; }
```
then add the ID to your html:

```html
<p id="paragraph">This text will be red and centred</p>
```

**Examples**

??? Images

    ==Class Selector==

    === "css"

        ```css
            .rounded-image { border-radius: 10px; }
        ```

    === "html"

        ```html
            <img src="photo.jpg" class="rounded-image">
        ```

    ==ID Selector==

    === "css"

        ```css
            #main-image { width: 300px; }
        ```

    === "html"

        ```html
            <img src="photo.jpg" id="main-image">
        ```

??? Audio

    ==Class Selector==

    === "css"

        ```css
            .audio-player { border: 2px solid black; }
        ```

    === "html"

        ```html
            <audio controls class="audio-player"></audio>
        ```

    ==ID Selector==

    === "css"

        ```css
            #intro-audio { width: 400px; }
        ```

    === "html"

        ```html
            <audio controls id="intro-audio"></audio>
        ```

??? Video

    ==Class Selector==

    === "css"

        ```css
            .video-frame { border: 3px solid blue; }
        ```

    === "html"

        ```html
            <video controls class="video-frame"></video>
        ```

    ==ID Selector==

    === "css"

        ```css
            #main-video { width: 500px; }
        ```

    === "html"

        ```html
            <video controls id="main-video"></video>
        ```
