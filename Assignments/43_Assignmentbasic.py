#ask user to enter a sentence , store sentence as list of words. Enter another word from user and write a function to findout number of occurance of the word in the sentence.(funcions)
sentence =input("Enter your sentence : ");
search  = input("Enter you word to search in sentence : ");

def wrd_search(sentence,search):
    cnt =0;
    for word in sentence.strip().split(" "):
        if word.lower() == search.lower():
            cnt +=1;
    return cnt;

print(search," word came ",wrd_search(sentence,search)," times in you sentence");
