# hangman
All of us have played hangman as kids and many of us still do! I have tried to create the exact game but have added my own flavour to it.

Key Highlights - 

1) A JSON file containing a huge dictionary(which I found on GitHub) of around 6000 words is used so a word is rarely repeated.
2) ASCII hangman figures are used for a better user experience.
3) At the end no matter you lose or you win, the programme displays the word that was to be guessed and it also displays it's meaning. Thus one can also add on to their vocabulary while playing this game.
4) The word to be guessed is displayed initially in the form of dashes ( _ _ _ _ ) , and after guessing correct letter, the dash at the position of that letter in the word is replaced by the letter. Wrong letters are stored in a list which is displayed before every attempt.
5) Number of lives remaining are also displated.

Stuff that I've used - 

1) Random module is used so every time you play, the word to be guessed is random and different than the previous.
2) Experimented with time and sys module for a better user experience. Used them for a delay of split second before every print statement. The initial instructions are displayed with an effect as though they are being typed right infront of us.
3) A seperate JSON file is used to store a dictionary with 6000 words and their meanings as key-value pairs. I have used file handling commands to open the JSON file, choose a random word(key) out of the dictionary and use it for the further programme. The corresponding value (meaning) of the key (word) is displayed at the end.
4) The ASCII art, i.e. the hangman figures and the logo are stored in seperate file and are imported in the programme for the sake of better organisation of code.
5) Other than this, the whole code is basically structured using while loop and if-else conditional statements. Some other things that are used are list, dictionary, .replace , .join , .lower , len() and few other functions and commands.

Please give it a try and let me know what you think! 

If there are any doubts, suggestions or bugs you can always ping me on tejascoolcarni@gmail.com !
