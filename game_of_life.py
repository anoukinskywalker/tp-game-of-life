import pygame
import copy

initial_state: list[list[int]] = [
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0],
    ]

lines=len(initial_state[0])
columns=len(initial_state)

height=len(initial_state)*50
width=len(initial_state[0])*50
print(width, height)

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

done: bool = False

def get_next_state(array) :
    new_array = copy.deepcopy(initial_state)

    for i in range(lines) :

        if(i==0):
            kmin=0
        else :
            kmin=i-1
                
        if(i==lines):
            kmax=lines
        elif (i==(lines-1)):
                kmax=i+1
        else :
            kmax=i+2

        for j in range(columns) :

            if(j==0):
                lmin=0
            else :
                lmin=j-1
            if(j==columns):
                lmax=columns
            elif (j==(columns-1)):
                lmax=j+1
            else :
                lmax=j+2
            
            cell_counter = 0

            for k in range(kmin, kmax) :
                for l in range (lmin, lmax) :
                    if (array[k][l]==1) :
                        cell_counter+=1

            if (array[i][j]==1) :
                cell_counter-=1
                if (cell_counter<2 or cell_counter>3):
                    new_array[i][j]=0
                else :
                    new_array[i][j]=1
            else :
                if (cell_counter==3):
                    new_array[i][j]=1
    return new_array

print(get_next_state(initial_state))

# While the game is not over
while not done:

    screen.fill((0, 0, 0))

    new_array = copy.deepcopy(initial_state)

    for i in range(lines) :

        if(i==0):
            kmin=0
        else :
            kmin=i-1
                
        if(i==lines):
            kmax=lines
        elif (i==(lines-1)):
                kmax=i+1
        else :
            kmax=i+2

        for j in range(columns) :

            if(j==0):
                lmin=0
            else :
                lmin=j-1
            if(j==columns):
                lmax=columns
            elif (j==(columns-1)):
                lmax=j+1
            else :
                lmax=j+2
            
            cell_counter = 0

            for k in range(kmin, kmax) :
                for l in range (lmin, lmax) :
                    if (initial_state[k][l]==1) :
                        cell_counter+=1

            if (initial_state[i][j]==1) :
                cell_counter-=1
                pygame.draw.rect(screen, (255, 255, 255), (50*j, 50*i, 50, 50))
                if (cell_counter<2 or cell_counter>3):
                    new_array[i][j]=0
                else :
                    new_array[i][j]=1
            else :
                if (cell_counter==3):
                    new_array[i][j]=1
    initial_state=copy.deepcopy(new_array)
            

    pygame.display.flip()
    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    print("Update !")
    clock.tick(1)

pygame.quit()