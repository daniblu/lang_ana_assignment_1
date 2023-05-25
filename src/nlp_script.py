import os
import spacy
import pandas as pd
import re

# function for calculating frequencies per 10,000 words
def freq_calc(count, text):
    freq = round((count/len(text))*10000, 2)
    return(freq)

def main():

    # load language model
    nlp = spacy.load("en_core_web_md")

    # create list of sub-folders
    data_path = os.path.join("..", "in", "USEcorpus")
    sub_folders = os.listdir(data_path)

    # loop over sub-folders, every loop saves a csv file in the out dir
    for sub_folder in sub_folders:
        print(f"Analysing essays in subfolder {sub_folder}")
        sub_folder_path = os.path.join(data_path, sub_folder)
        essays = os.listdir(sub_folder_path)
        info_table = []
        
        # loop over essays within a sub-folder
        for essay in essays:
            # read in essay
            file_path = os.path.join(data_path, sub_folder, essay)
            with open(file_path, "r", encoding="latin-1") as file:
                text = file.read()
            
            # clean text
            text = re.sub(r"<.+>", "", text)

            # create doc object
            doc = nlp(text)

            # extract POS frequencies
            noun_count, verb_count, adj_count, adv_count = 0, 0, 0, 0
            for token in doc:
                if token.pos_ == "NOUN":
                    noun_count += 1
                if token.pos_ == "VERB":
                    verb_count += 1
                if token.pos_ == "ADJ":
                    adj_count += 1
                if token.pos_ == "ADV":
                    adv_count += 1

            # extract entities
            PERs, LOCs, ORGs = [], [], []
            for ent in doc.ents:
                if ent.label_ == "PERSON":
                    PERs.append(ent.text)
                if ent.label_ == "LOC":
                    LOCs.append(ent.text)
                if ent.label_ == "ORG":
                    ORGs.append(ent.text)
            
            # summarise essay
            summary = (essay,
            freq_calc(noun_count, doc), 
            freq_calc(verb_count, doc), 
            freq_calc(adj_count, doc), 
            freq_calc(adv_count, doc),
            len(set(PERs)),
            len(set(LOCs)),
            len(set(ORGs)))

            # append essay summary to info_table
            info_table.append(summary)

        # save info_table as data frame
        info_df = pd.DataFrame(info_table, columns=["Filename", "RelFreqNoun", "RelFreqVerb", "RelFreqAdj", "RelFreqAdv", "UniquePER", "UniqueLOC", "UniqueORG"])

        # write csv
        outpath = os.path.join("..", "out", f"language_info_{sub_folder}.csv")
        info_df.to_csv(outpath)

if __name__ == "__main__":
    main()