CSS stands for Cascading Style Sheets, in which we are going to apply stylings to a specific element
    syntax : 
            selector{
                property:value;
                property:value;
                property:value;
                .
                .
                .
            }

# 3 ways to write CSS
    >Inline : writing css on the same html tag as an attribute
            <p style="color:green;">good afternoon</p>
    >Internal : writing css in the same html file using style tag
            <style></style>
    >External : writing css in a separate css extension based on file and giving connection using link tag
            <link rel="stylesheet" href="path"/>

# class is defined or called by . inthe header tag and id is defined or called by # in the header tag
    > class is used to apply the same styling to multiple elements

# color
In css color can be applied in 3 ways
    > color name: red, green, blue, violet,pink, etc .....
    > rgb format: rgb(red, green, blue) value:- 0 to 255
    > hexa code: #rrggbb value: 0 to f

----------------------------------------------------------------------------------------------------------

# simple selectors
    > id(#) : used to select a specific element
    > class(.) : used to select multiple elements
    > element : used to select all the elements of a specific type
# combinator
    > descendant selector() : used to select all the elements that are descendants of a specified element
            syntax : parent child
    > child selector(>) : used to select all the elements that are direct children of a specified element
            syntax : parent > child
    > adjacent sibling selector(+) : used to select an element that is directly after another specific element
            syntax : element + element
    > general sibling selector(~) : used to select all elements that are siblings of a specified element
            syntax : element ~ element
# pseudo class
    > used to define a special state of an element
    > :link, :visited, :hover, :active, :focus, etc .....
    > syntax : selector:pseudo-class
    > example : a:hover, a:active, a:visited, etc .....
# pseudo element
    > used to style specific parts of an element
    > ::first-letter, ::first-line, ::before, ::after, etc .....
    > syntax : selector::pseudo-element
    > example : p::first-letter, p::first-line, p::before, p::after, etc .....
# attribute selector
    > used to select elements based on their attributes and attribute values(applying stylings based on element attributes)
    > syntax : element[attribute="value"]
    > example : input[type="text"], a[target="_blank"], etc .....

=================================================================
NOTE :                                                          |
Among this all we are going to use class, descendent and hover  |
=================================================================

# Background properties in CSS
    > background color : same like color properties
    > background image : used to set an image as the background of an element
            syntax : background-image: url("path");
    > background repeat : used to control the repetition of the background image
            syntax : background-repeat: repeat | no-repeat | repeat-x | repeat-y;
    > background position : used to specify the initial position of the background image
            syntax : background-position: x% y% | left | center | right | top |
    > background attachment : used to specify whether the background image should scroll with the page or be fixed
            syntax : background-attachment: scroll | fixed | local;
            
# background shorthand property : used to set all background properties in one declaration
#    syntax : background: [background-color] [background-image] [background-repeat] [background-position] #             [background-attachment];

    > background size : used to specify the size of the background image
            syntax : background-size: auto | cover | contain | width height;

# Semantic Elements
In HTML we are having few elements which are going to work as containers 
        > div
        > section
        > nav
        > header
        > footer

# Text and font properties in CSS
Text Properties:
Through using this below properties we are able to change the look and presence of the text content
        > text align: center, left, right, justify
        > text indent: a number followed by px/%
        > text decoration: underline, overline, linethrough, none
        > text transform: uppercase, lowercase, capitalize
        > letter spacing: a number followed by px
        > word spacing: a number followed by px
        > line height: a number

Font Properties:
        > font size: a number followed by rem/em/%
        > font style: italic, oblique, normal
        > font weight: bold, normal, a number from google fonts
        > font family: serif, sans-serif, monospace, cursive, fantasy
        > google fonts: which we are going to get from google platform and give connection using CDN links

# Box model
In CSS we are going to wrap content using (margin, padding, border) with semantic elements
A box model is going to work like a container
        > margin: gap between 2 elements 
                marign-top
                margin-bottom
                margin-right
                margin-left
                margin(shorthand)
                        margin: 4%(for all sides)
                        margin: 5% 8%(top bottom and left right)
                        margin: 1% 2% 3% 4%(clockwise direction top right bottom left)
        > padding: gap present inside an element(same like margin properties, we will have padding)
                padding-top
                padding-bottom
                padding-right
                padding-left
                padding(shorthand)
                        padding: 4%(for all sides)
                        padding: 5% 8%(top bottom and left right)
                        padding: 1% 2% 3% 4%(clockwise direction top right bottom left)
        > border: present between margin and padding
                border(shorthand)
                        border-style
                        border-width
                        border-color
                        border-radius

# Positions in CSS
In css positions are going to used to switch an element from a specific position from a webpage. It carries
1. Static ->It is a default value for every element
2. Relative -> which will changes the position based on the screen(body element)
3. Absoulte -> which will changes the position based on the parent(relative, sticky, fixed)
4. Fixed -> which will fixes an element on the screen even we scroll
5. Sticky -> which will fixes an element after we scroll to a specific point

Note: the positions will always carry top right bottom left

Display Properties:
In CSS the content will align in different ways using 
1. inline
2. block
3. inline-block
4. flex
5. grid
6. none
among these flex and grid are used 

# Flexbox:
display:flex
flex-direction              : row, row-reverse, column, column-reverse
flex-wrap                   : wrap, wrap-reverse, no-wrap
flex-flow                   : combination of direction & wrap
flex-justify-content        : applied for a single row
                                flex-start,flex-end,center,space-around,
                                space-between, space-evenly
flex-align-items            : applied for a single column
                                flex-start,flex-end,center,space-around,
                                space-between, space-evenly
flex-align-content          : flex-start,flex-end,center,space-around,
                                space-between, space-evenly, stretch

The above mentioned properties are going to be applied based on a particular container.
Even we can some child properties
align-self, shrink, order 
will be applied individually to every element

# Float in CSS
> The float property is used to position content to a specific side.
> It allows elements to be placed on the left or right of their container.

# Overflow
> The overflow property controls what happens when content exceeds the element's width or height.
> It helps manage space effectively.

Values:
        visible → Default, content is not clipped
        hidden → Extra content is hidden
        scroll → Adds scrollbars
        auto → Adds scrollbars only when needed

Display: Grid
> display: grid is used to create structured layouts.
> Similar to Flexbox, but more powerful for 2D layouts (rows + columns).

Key Properties:
> grid-template-columns → Defines columns
> grid-template-rows → Defines rows

Difference from Flexbox:
> Flexbox → One-dimensional (row OR column)
> Grid → Two-dimensional (rows AND columns)

# Media Queries
Media queries are used to make web pages responsive.
        Syntax:
        @media (max-width: 768px) {
          selector {
            property: value;
          }
        }

Screen Size Types:
        max-width → Targets smaller screens
        min-width → Targets larger screens

# Breakpoints

Size	Name	                Range
xs	Extra Small	        < 576px
sm	Small	                576px – 768px
md	Medium	                768px – 992px
lg	Large	                992px – 1280px / 1366px
xl	Extra Large	        1366px – 1580px
xxl	Extra Extra Large	> 1580px

# Animations in CSS
Animations can be created using:
> Transitions
> Keyframes

Transitions
Used for smooth changes when a property value changes (e.g., hover).
        Syntax:
                transition: property duration timing-function delay;

Common Transform Functions:
> translate(x, y) → Moves an element
> scale(x, y) → Zoom effect
> skew(x, y) → Slants the element
> rotate(deg) → Rotates the element

⚠️ Note: These are often used with :hover for interaction effects.

Keyframes
Used for complex animations.
        Syntax:
                animation: name duration iteration-count timing-function delay;

                @keyframes animation_name {
                  0%   { /* start */ }
                  50%  { /* middle */ }
                  100% { /* end */ }
                }

# Bootstrap
