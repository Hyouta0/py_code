# ask user to enter a sentence and write a function to count number of words in the sentence.

def wd_cnt(sentence):
    cnt =0;
    for wd in sentence.strip().split(" "):
        cnt+=1;
    return cnt;

sentence = input("enter your sentence");
print("no. of words in you sentence are : ",wd_cnt(sentence));
