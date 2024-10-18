import os

def process_game_rows(numGamesToRead):
    #get the working directory and open the file with input
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

#initial params
redCubeCount = 12
greenCubeCount = 13
blueCubeCount = 14
sum = 0
gameNumber = 0
games = process_game_rows(100)
#for each game that has been processed...
for game in games: 
    #and for each set of cubes drawn in that game...
    possible = True
    gameNumber += 1
    for draw in game:
        #and finally, each color of cube drawn...
        for cubes in draw:
            #figure out what color the cubes are
            red = cubes.find("red")
            blue = cubes.find("blue")
            green = cubes.find("green")
            #based on the color, remove the alpha characters, and check to see if it is a valid draw
            if red > 0:
                cubes = cubes.strip("red\n")
                drawCount = int(cubes)
                if drawCount > redCubeCount: possible = False
            if blue > 0:
                cubes = cubes.strip("blue\n")
                drawCount = int(cubes)
                if drawCount > blueCubeCount: possible = False
            if green > 0:
                cubes = cubes.strip("green\n")
                drawCount = int(cubes)
                if drawCount > greenCubeCount: possible = False
    #if the game had valid draws add it to the running total of game numbers that are possible
    if possible:
        sum += gameNumber
print(f"The sum of the numbers of each possible games is {sum}")


            
            
