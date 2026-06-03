# Media Tags


**Image Tags**

The image tag <img> is used to display images. 

==The main supported file types are jpeg, gif and png. Hpowever there are many different types of image file types==

=== "HTML Code"

    ``` html
    
    <img src = "image.jpg" width = "400px" height = "300px" alt ="Image example" >

    ```

=== "Explanation"

    **Alt** - This is alternative text describing the image. Users will see this text displayed if the image URL is wrong, the image is not in one of the supported formats, or if the image is hasn’t downloaded.

    **Height** - You can specify the height of the image in pixels or as a percentage.

    **Width** - You can specify the width of the image in pixels or as a percentage.

**Audio Tags**

The audio tag is used to embed a sound clip in a web page. 

==The main supported file types are mp3, WAV and ogg files.==

=== "HTML Code"

    ``` html
        
        <audio src="audio.mp3" controls></audio>

    ```

=== "Explanation"

    **Controls** - If this attribute is specified then the controls for playback will be displayed

    **Autoplay** - The sound file will be automatically played once the page loads

    **Loop** - The sound will automatically navigate to the start

    **Volume** - A value between 0.0(silence) and 1.0(loudest)

**Video Tags**

The video tag is used to embed a videos in a web page. 

==The main supported file types are mp4, webm and ogg files.==

=== "HTML Code"

    ``` html
        
        <video width="320" height="240" autoplay>
            <source src="movie.mp4" type="video/mp4">
        </video>

    ```

=== "Explanation"

    **Controls** - If this attribute is specified then the controls for playback will be displayed

    **Autoplay** - The video file will be automatically played once the page loads

    **Height** - You can specify the height of the video in pixels or as a percentage.

    **Width** - You can specify the width of the video in pixels or as a percentage.