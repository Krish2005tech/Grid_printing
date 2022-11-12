
# layout board
top_wall="---"
wall_end="•"
side_wall="|"
empty="   "
cross="XXX"
filled="***"
hashtag="###"


x=8 # board x-y dimensions
y=6

# character
head  =" 0 "
middle="/|\\"
bottom="/ \\"


# coordinate axis marker
s1="# X"
s2=" # "
s3="Y #"

def ceiling():
    for j in range(x+1):
        print(wall_end,top_wall,sep="",end="")
    print(wall_end)
    
def empty_cell():
    print(side_wall,empty,sep="",end="")
def filled_cell():
    print(side_wall,filled,sep="",end="")
def crossed_cell():
    print(side_wall,cross,sep="",end="")
def hashtag_cell():
    print(side_wall,hashtag,sep="",end="")
    
def player1():
    print(side_wall,head,sep="",end="")
def player2():
    print(side_wall,middle,sep="",end="")
def player3():
    print(side_wall,bottom,sep="",end="")
    
def S1():
    print(side_wall,s1,sep="",end="")
def S2():
    print(side_wall,s2,sep="",end="")
def S3():
    print(side_wall,s3,sep="",end="")
    
def coord(n):
    if n<10:
        print(f"{side_wall} {n} ",sep="",end="")
    else:
        print(f"{side_wall} {n}",sep="",end="")


# list of all coordinates
all_coordinates=[]
for i in range(1,x):
    for j in range(1,y):
        all_coordinates.append([i,j])
        #print(all_coordinates)


# fills cell coordinates in format (x,y)
player_coords=[(1,1)]
empty_coords=[(2,2)]# default
filled_coords=[(3,3)]
crossed_coords=[(4,4)]
hashtag_coords=[(5,5)]


def print_board():
    for i in range(y+1):
        ceiling()
        for k in range(1,4):
            for j in range(x+1):
                # x/y header
                if j==0 and i==0 :
                    if k==1:
                        S1()
                    elif k==2:
                        S2()
                    else:
                        S3()
                # x coord
                elif k==2 and i==0 :
                    coord(j)
                # y_coord
                elif k==2 and j==0 :
                    coord(i)
                    
                #player cell
                elif (j,i) in player_coords:
                    if k==1:
                        player1()
                    elif k==2:
                        player2()
                    else:
                        player3()
                
                # crossed cell
                elif (j,i) in crossed_coords:
                    crossed_cell()
                # filled cell
                elif (j,i) in filled_coords:
                    filled_cell()
                # hashtag cell
                elif (j,i) in hashtag_coords:
                    hashtag_cell()
                # empty cell
                elif (j,i) in empty_coords:
                    empty_cell()
                #default
                else :
                    empty_cell()
            print(side_wall,end="")
            print()
    ceiling()
    print()


print_board()
    
       
