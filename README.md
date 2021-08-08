# newspaper_tool
A tool that will let you search and view historical newspapers.

**Todo:** 
* ML features to do image segmentation and written text to textfile
    * Automate input key file creation
        * Graylevel
        * Bounds box
        * Number of components (Still not sure what this is)
        * ~~Convert raw data to | deliniated words~~ **DONE**
        * File assembler to take data and follow standard
    * Accumulate training/validation data
        * Write down contents of articles
        * take screenshots of lines and save as .png
        * Look online for existing database?
            * Difficult because I need specific data (see singleline.png)
    * Do ML training using SimpleHTR with input data
* Eventually need a way to segment newspaper->articles->lines->text.  The previous bullets here handle lines-> part, but I still need a way to go from articles->lines so the user can just screenshot the article they want transcribed for now.

To do printed words to text: https://github.com/githubharald/SimpleHTR

See for handwriting database: https://fki.tic.heia-fr.ch/databases/iam-handwriting-database

Library of Congress historical newspaper database: https://chroniclingamerica.loc.gov/about/api/