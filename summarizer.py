#
##Author: Radhey Ruparel
##Description: This a program that reads in a game log file, based on the user input. 
#Then the program will processes the information on the log file, and then print out a summary. 
#in a parctualer format. The summary consist of which team won, total team scores, highest scorer and more.
#

#Required to import all the os functions and progam is able to locate the file
import os
os.chdir(os.path.dirname(__file__))

#Declaring a function
def main():
    #Through calling this function, point_addition(). Gives all the required values which are needed to be printed in the summary
    number_of_player_scored,first_player_to_score,last_player_to_score,total_score_team1,total_score_team2,team_1,team_2=point_addition()
    
    #This if-else stamment help to determine which team is the winner. 
    if total_score_team1>total_score_team2: #If the team 1 won
        print('\n'+team_1,'won!') #Print the name of the team and declare their victory
    else: #If the team 2 won
        print('\n'+team_2,'won!') #Print the name of the team and declare their victory
    
    print(team_1,'scored',total_score_team1,'points.') #Printing the winnning teams score
    print(team_2,'scored',total_score_team2,'points.') #Printing the lossing teams score
    print(int(number_of_player_scored),'players scored.') #Printing the total number of players scored 
    print(first_player_to_score,'scored first.') #Printing name of the frist player who scored 
    print(last_player_to_score,'scored last.') #Printing name of the last player who scored 

def team_and_player():
    '''This function sperate players into two teams into two team lists. 
    Also assoicated their total points to the team players. This function has no parameter variables.'''
    
    player_team_1=[] #Names of the players for team 1 
    player_team_2=[] #Names of the players for team 2
    points_player_team_1=[] #Points for players for team 1 accroding to the index of player_team_1
    points_player_team_2=[] #Points for players for team 2 accroding to the index of player_team_2
    scoring_sequence=[] #To determine which player scored when
    
    file_choosen=input('enter gamelog file name:') #User input for game log file selection
    file_choosen_open=open(file_choosen,'r') #Opening the selected file for reading 
    
    reading_file_line=file_choosen_open.readline() #Reading the frist line
    reading_file_line_split=reading_file_line.split(' ') #Spliting the frist line 
    team_1=reading_file_line_split[0] #Assoication the frist word of the line to team 
    
    #Looping all the other lines 
    while reading_file_line!='': #Fail the loop when the last of file is read 
        if team_1!=reading_file_line_split[0]: #So if the Spliting the line doesn't team 1
            team_2=reading_file_line_split[0] #Then we name of the team 2 in the team_2
        reading_file_line=file_choosen_open.readline() #Updates the loop line by line
        reading_file_line_split=reading_file_line.split(' ') #Spliting the updated line 

    file_choosen_open.close() #Close the user choosen file

    file_choosen_open_2=open(file_choosen,'r') #Reopen user choosen file again
  
    for line in file_choosen_open_2: #A loop to read the text file line by line
        line_split=line.split(' ') #Spliting one line by line indexing from 0 to 2 
        
        if team_1==line_split[0]: #If the player and points belong to the team 1
            if not line_split[1] in player_team_1: #If the player is not already in the list 
                player_team_1.append(line_split[1]) #Then add the player to the player_team_1 list
                points_player_team_1.append(int(line_split[2])) #Also add the score of the player to the points_player_team_1 list
                scoring_sequence.append(line_split[1]) #Add the name of the file to the scoring_sequence list
            else: #If the player already in the list 
                player_index_1=player_team_1.index(line_split[1]) #Find the index where the player in player_team_1 list 
                points_player_team_1[player_index_1]=points_player_team_1[player_index_1]+int(line_split[2]) #At that index add the points of that player the points_player_team_1 
                scoring_sequence.append(line_split[1]) #Add the name of the file to the scoring_sequence list
        
        if team_2==line_split[0]: #If the player and points belong to the team 2
            if not line_split[1] in player_team_2: #If the player is not already in the list 
                player_team_2.append(line_split[1]) #Then add the player to the player_team_2 list
                points_player_team_2.append(int(line_split[2])) #Also add the score of the player to the points_player_team_2 list
                scoring_sequence.append(line_split[1])#Add the name of the file to the scoring_sequence list
            else: #If the player already in the list 
                player_index_2=player_team_2.index(line_split[1]) #Find the index where the player in player_team_2 list 
                points_player_team_2[player_index_2]=points_player_team_2[player_index_2]+int(line_split[2]) #At that index add the points of that player the points_player_team_2
                scoring_sequence.append(line_split[1]) #Add the name of the file to the scoring_sequence list

    file_choosen_open_2.close() #Reclosing the user choosen file
    #To return all the list and varaible to process the data
    return scoring_sequence,player_team_1,player_team_2,points_player_team_1,points_player_team_2,team_1,team_2

def frist_last_and_total_player_scored():
    
    '''This function helps to detemine the frist and last player who scored, and the total number of players scored in the game
    this function doesn't no parameter varaibles.''' 
    
    #When the function is called the return lists and varaibles are in new local list and varaibles for this function
    scoring_sequence,player_team_1,player_team_2,points_player_team_1,points_player_team_2,team_1,team_2=team_and_player()
    
    first_player_to_score=scoring_sequence[0] #To detemine who was the player to score the first
    last_player_to_score=scoring_sequence[-1] #To detemine who was the player to score the last
    
    #To detemine the total numbers of player scored 
    number_of_player_scored=len(player_team_1)+len(player_team_2)
    
    #To return all the list and varaible to summaries the data
    return number_of_player_scored,first_player_to_score,last_player_to_score, scoring_sequence,points_player_team_1,points_player_team_2,team_1,team_2

def point_addition(): 
    
    '''This fuction sum up the scores of both the teams sperate in as an integer.
    This function has no parameter variables'''
    
    #When the function is called the return lists and varaibles are in new local list and varaibles for this function
    number_of_player_scored,first_player_to_score,last_player_to_score, scoring_sequence,points_player_team_1,points_player_team_2,team_1,team_2=frist_last_and_total_player_scored()
    
    #This loop adds the score for team 1
    addtion_index=0
    total_score_team1=0
    while addtion_index<len(points_player_team_1): #Changes depending on the size of the list 
        total_score_team1+=points_player_team_1[addtion_index] #This the sum of the team 1 score
        addtion_index+=1 #To fail the loop
        
    #This loop adds the score for team 2
    addtion_index=0
    total_score_team2=0
    while addtion_index<len(points_player_team_2): #Changes depending on the size of the list 
        total_score_team2+=points_player_team_2[addtion_index] #This the sum of the team 2 score
        addtion_index+=1 #To fail the loop
        
    #This fuction now returns all the values required to print the summary
    return number_of_player_scored,first_player_to_score,last_player_to_score,total_score_team1,total_score_team2,team_1,team_2
    
#Calling the main function
main()