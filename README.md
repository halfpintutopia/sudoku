# Sudoku

[//]: # (TODO Add screen shot of app)
![Screenshot of app]()

[Here is the live version of my project](https://sudoku-creator-solver.herokuapp.com/)

The application is based on
a [Guardian newspaper Sudoku puzzle](https://www.theguardian.com/lifeandstyle/series/sudoku).
The difficulty range was
inspired by the online version.

My partner's mother, Andrea Tschudi, really enjoys puzzles such
as [Doplo](https://sumaddle.com/fundamentals.html) (also
known as Smashed Sums) and Sudoku. As I am more familiar to Sudoku, I thought I
would create an application with Andrea
Tschudi in mind.

## Table of contents

* [How to Use](#how-to-use)

* [User Experience](#user-experience--ux-)
    * [Intended Audience](#intended-audience)
    * [User Stories](#user-stories)

* [Design](#design)
    * [Flowchart](#flowchart)
    * [Data Model](#data-model)

* [Features](#features)
    * [General Features](#general-features)
    * [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Remote & Local Development](#remote--local-development)
    * [Remote Deployment](#remote-deployment)
    * [Local Deployment](#local-deployment)
        * [How to Fork](#how-to-fork)
        * [How to Clone](#how-to-clone)

* [Testing](#testing)
  * [User experience](#user-experience)
  * [Bugs](#bugs)
  * [Remaining Bugs](#remaining-bugs)
  * [Validator Testing](#validator-testing)

* [Credits](#credits)
    * [Code Used](#code-used)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgments](#acknowledgments)

---

# How to Use

The 4 options are:

1. [Play](#play)
2. [Enter your own puzzle](#enter-your-own-puzzle)
3. [Solve a puzzle](#solve-a-puzzle)
4. [Instructions](#instructions)

### Play

*This option allows the user to choose their level of difficulty.*

* User is asked for their username
* They are then asked for the difficulty level they would like to play<br>
  :: Choosing from the following options<br>
    * 1 - Easy
    * 2 - Medium
    * 3 - Hard
* User is then prompted to enter the column letter (A-J, or a-j) and row
  number (1-9)
* User is then prompted to enter a number 1-9 to be placed in the row and cell
  they provided in the last prompt
* If the cell they selected already has a number that is part of the puzzle
  then they will receive feedback informing them that it is not possible to add
  a number in this cell
* If the cell they selected does not have a number that is not part of the
  puzzle, then the number will be printed into the grid
* Once there are no more numbers to enter, they user will be prompted to check
  the solution or exit the game

### Enter your own puzzle

*This option allows the user to enter their own puzzle into the grid.*<br>
*For example if they find a newspaper sudoku puzzle, but instead of using pen
and paper they would like to view the puzzle in the application.*

* User is prompted to add 9 rows
* A new grid with the puzzle will be printed on the screen
* The game will proceed as from the regular game play, from choosing the row
  and column

### Solve a puzzle

*This option provides the user enter a puzzle that they are struggling
with.*<br>
*When the user would like to get the solution to a puzzle they have found.*

* User is prompted to add 9 rows
* A solution is then printed on the screen

### Instructions

*This option provides the user with the instructions if they would like to play
the game.*

* A Sudoku puzzle is created with a 9 by 9 square (9 rows and 9 columns).
* The 9 by 9 square is also divided into 3 by 3 areas (a total of 9 x 3 by 3
  areas).
* Each row, column and 3 by 3 area must contain numbers 1 - 9 (inclusive).
* Numbers cannot be repeated in the row, column nor 3 by 3 area

# User Experience (UX)

* ## Intended Audience
    * Adults
    * Children

* ## User stories
    * ### Client Goals
        * Be able to generate a new puzzle
            * Add username
            * Be able to fill in the Sudoku puzzle
            * Be able to choose the difficulty of the puzzle
            * Save progress
              see - [Future Implementations](#future-implementations)
            * Time progress see - 
          [Future Implementations](#future-implementations)
        * Be able to solve a Sudoku puzzle
            * Add numbers in a Sudoku puzzle and generate a solution
    * ## First Time Visitor Goals
        * Be able to solve a Sudoku puzzle
        * Be able to fill in the Sudoku puzzle
        * Be able to choose the difficulty of the puzzle
    * ## Return Visitor Goals
        * Try another puzzle with a different difficulty level
        * Load previous game and continue
          playing see - [Future Implementations](#future-implementations)
    * ## Frequent Visitor Goals
        * See your previous plays at different levels and see if your times
          have improved see - [Future Implementations](#future-implementations)

# Design

## Flowchart

### Creating the game

<details>
<summary>Create board</summary>
<br>

![Flowchart - using recursion to crete a 9 x 9 grid](./docs/media/images/flowchart/initial_grid_creation.png)

*Flowchart - using recursion to crete a 9 x 9 grid*
</details>
<br>

<details>
<summary>Fill board</summary>
<br>

![Flowchart - using recursion to fill board with numbers 1 - 9](./docs/media/images/flowchart/fill_board_with_numbers.png)

*Flowchart - using recursion to fill board with numbers 1 - 9*
</details>
<br>

<details>
<summary>Remove numbers from completed board, dependent on difficulty</summary>
<br>

![Flowchart - using recursion remove a set number of numbers from board](./docs/media/images/flowchart/remove_numbers.png)

*Flowchart - using recursion remove a set number of numbers from board*
</details>
<br>

## Data Model

# Features

## General Features

## Future Implementations

* Save progress
* Time progress
* Load previous game and continue playing
* See your previous plays at different levels and see if your times have
  improved

# Technologies Used

## Languages Used

- Python
- HTML5
- CSS3

## Frameworks, Libraries & Programs Used

- Git
- GitHub
- PyCharm
    - including debugging tools

# Remote & Local Development

## Remote Deployment

*Before deploying, ensure a requirements.txt file in the project repository.*

To create the requirements.txt file, run the following command from the
terminal in the project.

`pip freeze > requirements.txt`

### Deploying on Heroku

1. Create or login into the Heroku account
2. On the account's landing page, click "Create new app."
3. Give the project a name and name the app
4. Select Europe for the region and confirm by clicking "Create app."
5. Click on the "Settings" tab
6. Click "Reveal Config Vars" to add the following environment variables.
   Click "Add" after adding each key-value pair:
    - key: PORT; value: 8000
    - copy and paste any other json credentials that are required to connect
      to additional APIs
7. Click "Add buildpack". Add the following in this order and click "Save
   changes"  for each selection:
    1. python
    2. nodejs
8. Click on the "Deploy" tab
9. Select GitHub and confirm
10. Search for the name of the project's repository and click "Connect."
11. Click on "Enable Automatic Deploys"

## Local Deployment

### How to Clone

1. Click "Code" at the top of the list of files on the repository page
2. Clone the repository using HTTPS and click on the copy icon at the end of
   the input
3. Locally, using the terminal, navigate to the chosen directory
4. Copy the project using the following command: <br>`git clone THE_URL_COPIED`
5. Type the following command and then enter
6. `cd THE_CLONED_DIRECTORY`
7. `pip3 install -r requirements.txt` <br>(or `pip install -r requirements.
   txt` for Python 2)

### How to Fork

*For when you wish to contribute and share suggestions*

1. Click "Fork" in the top right-hand corner of the repository page
2. The settings will automatically choose the GitHub logged in user as the
   owner of the forked repository
3. Optional: change the name of the repository
4. Options: add a description
5. Click "Create fork."

### How to Clone

# Testing

## User experience

### Client Goals Testing

| Client Goal                                            | Implementation | Tested | Successful |
|--------------------------------------------------------|----------------|:------:|:----------:|
| Be able to generate a new puzzle                       |                |        |            |
| Add username                                           |                |        |            |
| Be able to fill in the Sudoku puzzle                   |                |        |            |
| Be able to choose the difficulty of the puzzle         |                |        |            |
| Add numbers in a Sudoku puzzle and generate a solution |                |        |            |

### First Time Visitor Goals

| Client Goal                                    | Implementation | Tested | Successful |
|------------------------------------------------|----------------|:------:|:----------:|
| Be able to solve a Sudoku puzzle               |                |        |            |
| Be able to fill in the Sudoku puzzle           |                |        |            |
| Be able to choose the difficulty of the puzzle |                |        |            |

### Return Visitor Goals

| Client Goal                                          | Implementation | Tested | Successful |
|------------------------------------------------------|----------------|:------:|:----------:|
| Try another puzzle with a different difficulty level |                |        |            |

## Bugs

| Bug / Errors | Where / Location | Device | Remarks | Fixed | Solution |
|--------------|------------------|--------|---------|:-----:|----------|

## Remaining Bugs

| Bug / Errors | Where / Location | Device | Remarks | Fixed | Solution |
|--------------|------------------|--------|---------|:-----:|----------|

## Validator Testing

| Bug / Errors | Where / Location | Device | Remarks | Fixed | Solution |
|--------------|------------------|--------|---------|:-----:|----------|

# Credits

## Code Used

References and guides used:

* [12 Beginner Python Projects](https://www.youtube.com/watch?v=8ext9G7xspg&t=6715s)
* [How to print bold text in Python, in Stackoverflow](https://stackoverflow.com/a/20210807/8614652)
* [Create ASCII Art Text Banners in Python](https://www.devdungeon.com/content/create-ascii-art-text-banners-python)
* Python libraries
    * Built in:
        * [enum](https://docs.python.org/3/library/enum.html)
        * [copy](https://docs.python.org/3/library/copy.html)
        * [pprint](https://docs.python.org/3/library/pprint.html)
        * [random](https://docs.python.org/3/library/random.html)
    * Installed:
        * [termcolor](https://pypi.org/project/termcolor/)
        * [pyfiglet](https://github.com/pwaller/pyfiglet/tree/master)
            * Additional references:
                - [Checking fonts tool](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
                - [Prettify your Terminal Text with Termcolor and Pyfiglet](https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b)
                - [Fonts overview](http://www.jave.de/figlet/fonts/overview.html)
* [ANSI Escape Sequences](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797?permalink_comment_id=3857871)
* [ReeEx Testing](https://www.regextester.com/)
* [Alphabet range in Python](https://stackoverflow.com/questions/16060899/alphabet-range-in-python)
* [How to print Sudoku board using Python class?](https://stackoverflow.com/questions/72159405/how-to-print-sudoku-board-using-python-class)
* [Convert Letter to Numbers and vice versa in Python](https://bobbyhadz.com/blog/python-convert-letters-to-numbers)
* [Extend Class Method in Python](https://www.geeksforgeeks.org/extend-class-method-in-python/)

## Content

All text content and prompts created was kept short and direct. Ensuring the
characters would not wrap.
Puzzle difficulty was inspired by
the [Sudoku puzzles printed in the Guardian newspaper](https://www.theguardian.com/lifeandstyle/series/sudoku)

## Media

No media, such as images or videos other than screenshots and screencast
attached to the README were used for the project.

## Acknowledgments

Huge thanks goes to everyone in the Code Institute Community on Slack,
especially the
[women-in-tech](https://code-institute-room.slack.com/archives/C01QAAQGPNJ)
Slack channel. Thanks to their banter and support. Such a great group! In
addition, my thanks to
the [oct-2022-disdcc](https://code-institute-room.slack.com/archives/C044ZCYQ6CQ),
especially Mark Cooper, Ger Tobin and Rebecca Tracey-Timoney.

Thanks also goes to Andrea Tschudi for giving me the inspiration to make this
game. Also, to Stefan Tschudi for his support and testing.

And last but not least, special thanks to the Codebar community and to
Nicolas Beney.