import os

def process_game_rows(numGamesToRead):
    #get working directory
    cwd = os.getcwd()
    print(cwd)
    #open the file with input
    file = open(os.getcwd()+"\day2\IN2.txt", "rt")
    #for each game that we want to read, read a line(count adjusted for zero index)
    gameNumber = 1
    processedGames = []
    for line in file:
        #split the line to remove the "Game #" text since we know each line is one game
        game = line.split(':')
        #next split into a list with the cubes revealed each game
        cubesRevealed = game[1].split(';')
        cubes = []
        #for each set of cubes revealed, split them into individual cube amounts by color(eg "6 red")
        for set in cubesRevealed:
            cubes.append(set.split(','))
            print(cubes)
        #append the sets of cubes revealed to the results
        processedGames.append(cubes)
        #if enough games have been read, stop reading lines
        if gameNumber == numGamesToRead: break
        #otherwise increment the game number and start over
        gameNumber+=1
    #close the file :)
    file.close()
    #after processing the requested number of games/reveals, return the results
    return processedGames

test = process_game_rows(2)
print(test)