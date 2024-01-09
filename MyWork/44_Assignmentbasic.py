#ask user to enter a word, write a function to count number of vowels in the word . (funcions)

def vowels_cnt(word):
    cnt =0;
    for w in word:
        if w.lower() in ['a', 'e', 'i','o','u']:
            cnt+=1;
    return cnt;
word = input("Enter your word : ");
print("no. of vowls in your word are ",vowels_cnt(word));
