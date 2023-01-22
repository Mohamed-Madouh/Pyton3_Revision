#start , End ------> multiplacation table [start.end]
'''
start = int(input('Enter Start :'))
end = int(input('Enter End :')) 

for x in range(start,end+1):
    for i in range(1,12+1):
        print(f"{x}X{i}={x*i}")
    print('-----------------------')




    
start1 = int(input('Enter Start :'))
end1 = int(input('Enter End :')) 
def mulyiplacation_table(start1,end1):
    for x in range(start,end+1):
        for i in range(1,12+1):
            print(f"{x}X{i}={x*i}")
        print('-----------------------')



    
name = input('inter your name : ')
print(name.split())
print(f"leter count is :{len(name)}")
print(f"word count is :{len( name.split())}")

m= input('Emter name :')
def count_words(m):
    word_count=len(m.split())
    return word_count
print(count_words(m))
                   
'''
'''
   Game :
       - print welcame
       - game number
       -run game
'''
name = input('Entar your name : ')
class Game :
    def __init__(self):
        while True:
            print(f'''welcame {name},nice to meet you
        1 : Multipalcation Table Game
        2 : Word count game
        3 : to exit''')
            user= int(input("Enter your choice :"))
            if user == 1:
                start1 = int(input('Enter Start :'))
                end1 = int(input('Enter End :'))
                self.mulyiplacation_table(start1,end1)
            elif user == 2:
                 m= input('Emter name :')
                 count=self.count_words(m)
                 print(count)
            else :
                break
            play_again= input('press any key To play Adain ,N for exit : ')
            if play_again == N:
                break
                
    def mulyiplacation_table(self,start1,end1):
            for x in range(start1,end1+1):
                for i in range(1,12+1):
                    print(f"{x}X{i}={x*i}")
                print('-----------------------')
        
       
    def count_words(self,m):
            word_count=len(m.split())
            return word_count
g1=Game()
