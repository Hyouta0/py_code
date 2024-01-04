
#Given 21 Matchsticks and 2 users, A and B (computer and user respectively). Users can pick matchsticks not more than four at a time. The one who is forced to pick the last matchstick loses. 
import random

new_game = True;
while(1):
    gm_choise = 'y';
    if(new_game):
        gm_choise = input("Enter 'y' to play and 'q' to quit game : ").lower();
    else:
        gm_choise = input("Enter 'y' to play again and 'q' to quit : ").lower();
    if(gm_choise == 'q'):
        break;
    new_game = False;

    #game starts there 
    matchsticks =21;
    first_to_play = random.getrandbits(1);
    last_user = first_to_play;
    print("Game starts         matchsticks = ",matchsticks)
    while(matchstick > 0):
        if(first_to_play):
            match_remove=int(input("Pick matchstickes atmost 4 : "));
            if(match_remove < 0 or match_remove >4):
                print("you chossed invalid amount of matchsticks \n You Loose!!!!!!");
                break;
            elif(match_remove > matchsticks):
                print("You are last to choose \n you Loose !!!");
                break;
            else:
                matchsticks-=match_remove;
                if(matchsticks == 0):
                    print("You loose");
                    break;
                last_user = 1;



