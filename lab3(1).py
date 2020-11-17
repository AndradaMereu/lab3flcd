# STATE = [p-z]
# ELEMENT = [a-o]|[0-9]
# TRANSITION = {STATE}" "{STATE}" "{ELEMENT}"
#
# We write the file in the following way:
# STATES = STATE {" "STATE}      #this defines the set of states
# ALPHABET = ELEMENT {" "ELEMENT}     #this defines the alphabet
# STATE        #this defines the initial state
# FSTATES = STATE {" "STATE}      #this defines the set of final states
# TRANSITIONS = TRANSITION {"\n" TRANSITION}       #this is the set of transitions
#
#
# on the first line we have the states separated by space
# on the second line we have the alphabet elements separated by space
# on the third line we have the initial state
# on the fourth line we have the final states, separated by space
# on the following lines we have the transitions
class Transition:
    def __init__(self):
        self.initial=''
        self.final=''
        self.elem=''


class FiniteAutomaton:
    def __init__(self,filename):
        self.states=[]
        self.alphabet=[]
        self.initialstate=''
        self.finalstates=[]
        self.transitions=[]

        f = open(filename, "r")

        lines = f.readlines()
        length = len(lines)

        i = 0
        while i < length:
            if (i == 0):
                self.states = lines[i].split()
                #print("The states are: " + str(states))
            elif (i == 1):
                self.alphabet = lines[i].split()
                #print("The alphabet is: " + str(alphabet))
            elif (i == 2):
                self.initialstate = lines[i]
                #print("The initial state is: " + initialstate)
            elif (i == 3):
                self.finalstates = lines[i].split()
                #print("The final states are: " + str(finalstates))
            else:
                tr = lines[i].split()
                Trans=Transition()
                Trans.initial=tr[0]
                Trans.final=tr[1]
                Trans.elem=tr[2]
                self.transitions.append(Trans)
                #print("From state " + transitions[0] + " to state " + transitions[1] + " through " + transitions[2])
            i = i + 1


def main():
    filename = input("Give name of the file: ")
    FA=FiniteAutomaton(filename)
    while(True):
        print("1. Show the states")
        print("2.Show the alphabet")
        print("3. Show the initial state")
        print("4. Show the final states")
        print("5. Show the transitions")
        print("0. Exit")
        x=input("Enter your choice: ")
        x=int(x)
        if(x==1):
            print("The states are: " + str(FA.states))
        elif(x==2):
            print("The alphabet is: " + str(FA.alphabet))
        elif(x==3):
            print("The initial state is: " + FA.initialstate)
        elif(x==4):
            print("The final states are: " + str(FA.finalstates))
        elif(x==5):
            for tr in FA.transitions:
                print("From state " + tr.initial + " to state " + tr.final + " through " + tr.elem)
        elif(x==0):
            break
        else:
            print("Choose a valid number (between 0 and 5)")


if __name__ == "__main__":
    # execute only if run as a script
    main()