# language analytics assignment 1
This repository is assignment 1 out of 5, to be sumbitted for the exam of the university course [Language Analytics](https://kursuskatalog.au.dk/en/course/115693/Language-Analytics) at Aarhus Univeristy.

The first section describes the assignment task as defined by the course instructor. The section __Student edit__ is the student's description of how the repository solves the task and how to use it.


## Extracting linguistic features using spaCy

This assignment concerns using ```spaCy``` to extract linguistic information from a corpus of texts.

The corpus is an interesting one: *The Uppsala Student English Corpus (USE)*. All of the data is included in the folder called ```in``` but you can access more documentation via [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

For this exercise, you should write some code which does the following:

- Loop over each text file in the folder called ```in```
- Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
- For each sub-folder (a1, a2, a3, ...) save a table which shows the following information:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

## objective

This assignment is designed to test that you can:

1. Work with multiple input data arranged hierarchically in folders;
2. Use ```spaCy``` to extract linguistic information from text data;
3. Save those results in a clear way which can be shared or used for future analysis

## Student edit
### Solution
The code written for this assignment can be found in ``nlp_script.py`` in the ```src``` folder. The script produces language summaries of the text files in the ```in``` directory, using a trained pipeline from ```spaCy```. Summaries are saved as ```.csv``` in the ```out``` directory. 

### Setup
The script requires the following to be run from a terminal:

```shell 
bash setup.sh
```

This will create an environment, ```assignment1_env```, to which the packages listed in ```requirements.txt``` will be downloaded as well as the trained pipeline. __Note__, ```setup.sh``` works only on computers running POSIX. Remember to activate the environment running the following line in a terminal before changing the working directory to ``src`` and running ``python3 nlp_script.py``.

```shell 
source ./assignment1_env/bin/activate
```