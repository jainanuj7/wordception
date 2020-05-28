# wordception
 
On one of the lazy Sunday afternoon during the COVID lockdown, I came across this random video on Facebook <br/>
https://www.facebook.com/paulvutv/videos/2451750948448459/ <br/><br/><br/>

Paul Vu, a famous vlogger asks his girlfriend a riddle which goes something like this: <br/>
### _**"What nine-letter word in English still remains a word each time you take away a letter?"**_ <br/><br/><br/>

I was so bored,  I ended up writing a recursive backtracking Python code to solve this. <br/><br/>

Dataset used: **Wordnet** <br/>
https://wordnet.princeton.edu/ <br/><br/>

A big kudos to user1247808's answer which led me to this dataset <br/>
https://stackoverflow.com/a/10757188/3302140 <br/><br/>

I had to import all the data using a .sql file which took hours to execute. <br/>
I exported the necassary word dataset (after cleaning it, ofc!) as a .csv file in case someone wants to use it,
In case you want to import the actual dataset yourself, you can run the .sql file mentioned in the stackoverflow answer above. <br/>
Since it is a HUUUUGE single sql file, I suggest you to execute it directly from Command Prompt. Using a tool like SQL Workbench might not help much.

This code is ran to find such 9-letter "magic words", it is made flexible enough to be extended to find any n-letter magical word. <br/><br/><br/>

NOTE: Results totally vary upon the dataset you use.
