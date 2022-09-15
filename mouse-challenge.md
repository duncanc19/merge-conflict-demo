The `lyrics.py` file will print out the lyrics to I am the one and only, by Chesney Hawkes but it has some issues that need fixing
- Someone forgot to print the title as a string. Convert this to a string but you can only press the comment symbol once
- Verse 1 is being repeated, no-one needs to hear those lyrics twice so get rid of the duplicate
- The first time the chorus is meant to be sung is commented out. Uncomment this code, without using the Delete or Backspace buttons
- Verse 3 is being sang before verse 2, put them in the correct order
- Run the `lyrics.py` file in a new terminal and make sure the correct lyrics are printed


## Bonus
- Create a new conda environment using the `conda env create -f environment.yml` command
- Add a test to the `tests\test_full_lyrics.py` file 
- Run `python -u -m pytest RELATIVE_PATH_TO_TEST_FILE`