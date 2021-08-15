# newspaper_tool
A tool that will let you search and view historical newspapers.

General flow is: newspaper->articles->lines->text. Later on there may be a front end where users can give an event (Such as '1904 Olympics'), date, newspaper name to automatically find relevant content.

**Todo:** 
* ML features to do image segmentation and written text to textfile
    * Automate input key file creation
        * Graylevel
        * Bounds box
        * Number of components (Still not sure what this is)
        * ~~Convert raw data to | deliniated words~~ **DONE**
        * File assembler to take data and follow standard
    * Algorithm to segment article into lines (covers the articles->lines part of the flowchart.)
        * ~~Initial way to segment lines~~ **DONE, see `segment_lines.py`**
            * The current way works well for high quality images, but may need adjusting to accomodate edge cases
        * Further tune the seperation to select less whitespace
        * Temporary: automatically save lines as new images (.png) into a 'training' folder
        * complete the pipeline into ML picture to text
        
    * Accumulate training/validation data
        * Write down contents of articles
        * take screenshots of lines and save as .png
        * Look online for existing database?
            * Difficult because I need specific data (see singleline.png)
    * Do ML training using SimpleHTR with input data (This should be straightforward once we have data)
* Eventually need a way to segment newspaper->articles->lines->text.  The previous bullets here handle lines->part, but I still need a way to go from articles->lines so the user can just screenshot the article they want transcribed for now.

To do printed words to text: https://github.com/githubharald/SimpleHTR

See for handwriting database: https://fki.tic.heia-fr.ch/databases/iam-handwriting-database

Library of Congress historical newspaper database: https://chroniclingamerica.loc.gov/about/api/