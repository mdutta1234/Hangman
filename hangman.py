
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    b=0
    for i in secret_word:
        for j in letters_guessed:
            if i==j:
                b+=1
                break
    if b==len(secret_word):
        return True
    else:
        return False
def wordwithnospace(secret_word, letters_guessed):
   s=''
   
   for i in secret_word:
       n=0
       for j in letters_guessed:
           if i==j:
               s+=j
               break
           else:
               n+=1
               
           if n==len(letters_guessed):
            s+='_'
   return s


def get_guessed_word(secret_word, letters_guessed):
   s=''
   
   for i in secret_word:
       n=0
       for j in letters_guessed:
           if i==j:
               s+=j+" "
               break
           else:
               n+=1
               
           if n==len(letters_guessed):
            s+='_ '
    
   return s
    
    
def invalidletter(g,w,secret_word,letters_guessed):
    if w>0:
        w=w-1
        print("Oops!That is not a valid letter.You have",w,"warnings left:",get_guessed_word(secret_word, letters_guessed))
        return g,w
    else:
        g=g-1
        print("Oops!That is not a valid letter.You have",g,"guesses left:",get_guessed_word(secret_word, letters_guessed))
        return g,w
               

        
       
       
        
           
        
            
              
    

        
        
        
        



def get_available_letters(letters_guessed):
    a=string.ascii_lowercase
    s=''
    for i in a:
        n=0
        for j in letters_guessed:
            n+=1
            if i==j:
                s+=''
                break
            elif n==len(letters_guessed):
                s+=i
    if letters_guessed==[]:
        s=a
    return s

    
    

def hangman(secret_word):
   print("Welcome to the game Hangman")
   print("i am thinking of a word that is",len(secret_word),"letters long")
   g=6
   w=3
   letters_guessed=[]
   jug=""
   for i in secret_word:
       jug+=i+" "
   while g>0:
       print("____________________________________")
       if get_guessed_word(secret_word, letters_guessed)==jug:
           print("Congratulations,you won!")
           print("Your total score for this game is:",g*len(secret_word))
           break
       print("You have",g,"guesses left")
       print("Available letters:",get_available_letters(letters_guessed))
       ch=input("Please enter a letter : ")
       
       if ch.isalpha():
           if len(ch)==1:
               ch=ch.lower()
               if ch in letters_guessed:
                   letters_guessed+=ch
                   if w>0:
                       w=w-1
                       print("Oops!You've already guessed that letter.You now have,",w,"warnings:",get_guessed_word(secret_word, letters_guessed))
                   else:
                       g=g-1
                       print("Oops!that's not a valid letter.You have",g,"guesses left")
               else:
                   letters_guessed+=ch
                   n=0
                   for i in secret_word:
                       if i==ch:
                           print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                           break
                       else:
                           n+=1
                   if n==len(secret_word):
                       print("Oops!That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                       vowel=['a','e','i','o','u']
                       if ch in vowel:
                           g-=2
                       else:
                           g-=1
           else:
               letters_guessed+=ch
               (g,w)=invalidletter(g, w, secret_word, letters_guessed)
       else:
           letters_guessed+=ch
           (g,w)=invalidletter(g, w, secret_word, letters_guessed)
           
   if g<1:
       print("_______________________________")
       print("Sorry you ran out of guesses.The word was",secret_word)

   return None
     
       
     
       

# -----------------------------------



def match_with_gaps(my_word, other_word):
    s=my_word
    
    b=False
    
    if len(s)==len(other_word):
        for i in range(len(s)):
            if s[i]==other_word[i] or s[i]=="_":
                b=True
            else:
                b=False
                break
    return b
                    
                
                
                
    



def show_possible_matches(my_word):
    print("Possible word matches are:")
    for i in wordlist:
        if match_with_gaps(my_word, i):
            print(i),



def hangman_with_hints(secret_word):
   print("Welcome to the game Hangman")
   print("i am thinking of a word that is",len(secret_word),"letters long")
   g=6
   w=3
   letters_guessed=[]
   jug=""
   for i in secret_word:
       jug+=i+" "
   while g>0:
       print("____________________________________")
       if get_guessed_word(secret_word, letters_guessed)==jug:
           print("Congratulations,you won!")
           print("Your total score for this game is:",g*len(secret_word))
           break
       print("You have",g,"guesses left")
       print("Available letters:",get_available_letters(letters_guessed))
       ch=input("Please enter a letter : ")
       if ch=="*":
           show_possible_matches(wordwithnospace(secret_word, letters_guessed))
           
       else:
           if ch.isalpha():
               if len(ch)==1:
                   ch=ch.lower()
                   if ch in letters_guessed:
                       letters_guessed+=ch
                       if w>0:
                           w=w-1
                           print("Oops!You've already guessed that letter.You now have,",w,"warnings:",get_guessed_word(secret_word, letters_guessed))
                       else:
                           g=g-1
                           print("Oops!that's not a valid letter.You have",g,"guesses left")
                   else:
                       letters_guessed+=ch
                       n=0
                       for i in secret_word:
                           if i==ch:
                               print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                               break
                           else:
                               n+=1
                       if n==len(secret_word):
                           print("Oops!That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                           vowel=['a','e','i','o','u']
                           if ch in vowel:
                               g-=2
                           else:
                               g-=1
               else:
                   letters_guessed+=ch
                   (g,w)=invalidletter(g, w, secret_word, letters_guessed)
           else:
               letters_guessed+=ch
               (g,w)=invalidletter(g, w, secret_word, letters_guessed)
    
       

           
   if g<1:
       print("_______________________________")
       print("Sorry you ran out of guesses.The word was",secret_word)

   return None





if __name__ == "__main__":

    
    secret_word = choose_word(wordlist)

hangman_with_hints(secret_word)


