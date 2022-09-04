import pandas as pd

# Load information
FULLINFO = pd.read_csv('fullinfo.csv')
ENCODERS = pd.read_csv('encoder.csv',index_col=0)
PARTS = list(ENCODERS.columns)
SPE2NUM = {'狸花':1,'美短':2,'布偶':3,'三花':4}


# Calculate the difference between the current and target cat
def calmissing(targ,speinfo):
    score = 0
    res = []
    
    for i,part in enumerate(PARTS):
        if targ[i] == 0:
            res.append(' '.join([speinfo[part]] + speinfo[part+'Comb'].split('+')))
            continue

        currentPart = ENCODERS.loc[targ[i]][part]
        if currentPart == speinfo[part]:
            res.append('')
        else:
            combtarg = speinfo[part+'Comb'].split('+')
            if currentPart in combtarg:
                score += 0.5
                combtarg.remove(currentPart)
            else:
                score += 1
            res.append(' '.join([speinfo[part]] + combtarg))
    
    if targ[-1] != SPE2NUM[speinfo['type']]:
        score += 0.1
        res.append(speinfo['type'])
    else:
        res.append('')
    
    return score, res
        

# Print out the result
def printres(targCat, score, requires):
    print('\n')
    print('-'*80)
    print()
    print('Target cat: %s with score: %.2f'%(targCat, score))
    print('Still require:')

    for i,part in enumerate(PARTS):
        print('\t%6s: %s'%(part,requires[i]))

    print('\t%6s: %s'%('type',requires[-1]))



# Print the codes for each gene
def printcodes(part):
    codes = ENCODERS.index
    partvals = ENCODERS[part]
    
    str = '\t'
    for c in codes:
        str += '%s:%02d '%(partvals[c],c)
        if c == 5:
            str += '\n\t'
    print('Codes for %s\'s genes:'%part)
    print(str[:-1])


# Print the codes for each cat
def printcats():
    for i in range(8):
        for j in range(5):
            name = FULLINFO.iloc[i*5 + j]['name']
            print('%8s:%2d'%(name, i*5+j), end = ' ')
        print()


# Main Loop: Ask for current, Calculate result
def mainloop():
    info = []

    for part in PARTS:
        printcodes(part)
        inp = input('Yours: ')
        print('\n')
        info.append(int(inp))
    
    print('Codes for cat types:')
    print('\t狸花:1 美短:2 布偶:3 三花:4')
    inp = input('Yours: ')
    info.append(int(inp))
    
    iftarg = input('\n\nTarget cat? (Press ENTER if not)')
    
    targetInfo = FULLINFO[FULLINFO['name'] == iftarg]
    if iftarg == '' : 
        lowestScore = 20
        targetName = ''
        finalreq = None
        for i in range(40):
            score, req = calmissing(info,FULLINFO.iloc[i])
            if score < lowestScore:
                targetName = FULLINFO.iloc[i]['name']
                finalreq = req
                lowestScore = score
        printres(targetName,lowestScore,finalreq)
    else:
        printcats()
        targind = input('\nYours: ')
        print('\n')
        targind = int(targind)

        score, req = calmissing(info,FULLINFO.iloc[targind])
        printres(FULLINFO.iloc[targind]['name'],score,req)



# Infinit loop until not to continue
def main():
    
    while True:
        mainloop()
        print('\n')
        ans = input('Another try? (y/n)')

        if ans != 'y':
            break

        print('\n')

        print('-'*80)
        print('\n')



if __name__ == '__main__':
    main()

