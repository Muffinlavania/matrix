import time,os,random

#why i had the urge to make this: friend
#why i had the urge to post this: ?
#why this sucks: its me lol



print('\033[?25l')
dicty={
  1:['ﾊ','ﾐ','ﾋ','ｹ','ﾒ','ｴ','ﾇ','ﾍ'],
  2:['ｰ','ｳ','ｼ','ﾃ','ﾏ','ｶ','ｷ','ﾑ'],
  3:['ﾅ','ﾓ','ﾆ','ｱ','ﾎ','ﾕ','ﾗ','ｾ'],
  4:['ｻ','ﾜ','ﾂ','ｵ','ﾘ','ﾈ','ｽ','ﾀ'],
  'ﾊ':'\033[38;5;46m','ﾐ':'\033[38;5;46m','ﾋ':'\033[38;5;46m','ｹ':'\033[38;5;46m','ﾒ':'\033[38;5;46m','ｴ':'\033[38;5;46m','ﾇ':'\033[38;5;46m','ﾍ':'\033[38;5;46m',
  'ｰ':'\033[38;5;82m','ｳ':'\033[38;5;82m','ｼ':'\033[38;5;82m','ﾃ':'\033[38;5;82m','ﾏ':'\033[38;5;82m','ｶ':'\033[38;5;82m','ｷ':'\033[38;5;82m','ﾑ':'\033[38;5;82m',
  'ﾅ':'\033[38;5;118m','ﾓ':'\033[38;5;118m','ﾆ':'\033[38;5;118m','ｱ':'\033[38;5;118m','ﾎ':'\033[38;5;118m','ﾕ':'\033[38;5;118m','ﾗ':'\033[38;5;118m','ｾ':'\033[38;5;118m',
  'ｻ':'\033[38;5;154m','ﾜ':'\033[38;5;154m','ﾂ':'\033[38;5;154m','ｵ':'\033[38;5;154m','ﾘ':'\033[38;5;154m','ﾈ':'\033[38;5;154m','ｽ':'\033[38;5;154m','ﾀ':'\033[38;5;154m',
}
greens=['\033[38;5;46m','\033[38;5;82m','\033[38;5;118m','\033[38;5;154m']
lengths=[4,8]
num='R'
sped=.1
height=os.get_terminal_size().lines-1
while num=='R' or 'S' in num:
  thestring='' 
  if "S" in num.upper():
      print(f"\033[38;5;69mChanged wait time to {num.split(' ')[1]}! \033[0m[if its a valid number]\n")
      sped=num.split(' ')[1]
  width=os.get_terminal_size().columns
  print("\033[38;5;32mthe effect is this wide:\033[0m\n"+("-"*width)+"\nyea i just stole your width L, this is based on console size btw\n\nHit enter to go to the matrix effect or..\n\t\033[38;5;53mEnter a number\033[0m between 3 and ∞, higher = more rare matrix spawns (default is 100)\n\t\033[32;5;83mEnter 'S (num)'\033[0m to change the wait time between cycles (default .1)\n\t\033[38;5;76mEnter \"R\"\033[0m to recalibrate console width\n\t'H' to review the height of it")
  for i in range(height):
    thestring+=(' '*width)+"\n"
  thestring=list(thestring)
  num = input('\n>').upper().strip()
  if num=='H':
    num,ji='R',''
    while ji!='Q':
      os.system('clear' if os.name!='nt' else 'cls')
      print("| This is how high the effect will be, if you want to: recalibrate 'R', make smaller 'S', bigger 'W', exit is 'Q'")
      for i in range(height-1):
        print('|')
      ji=input("This is your input, doesnt count towards height> ")
      if ji=='S' and height>5:
        height-=1
      if ji=='W' and height<os.get_terminal_size().lines:
        height+=1
      if ji=='R':
        height=os.get_terminal_size().lines-1
  os.system('clear' if os.name!='nt' else 'cls')

#TODO: make ti so that when it sees a matrix symbol that isnt one at the top and it moves it down, it also replaces the ones in front of it so it doesnt override (ex: 2nd symbol moves down and overrides 1st one, then rebuilds the 1st after it (itself+width))
#yes done
try:
    sped=float(sped)
except:
    sped=.1

width+=1
while True:
  t=[]
  nu=-1
  for i in thestring:
    nu+=1
    if thestring[nu] not in [' ','\n'] and nu not in t:
      if nu+width<len(thestring):
        thestring[nu+width]=thestring[nu]
        t.append(nu+width)
        y=thestring[nu+width]
        thestring[nu]=(random.choice(dicty[4]) if y in dicty[3] else random.choice(dicty[3]) if y in dicty[2] else random.choice(dicty[2]) if y in dicty[1] else ' ')
        if not (y==' ' or y in dicty[1]):
          for i in range(2,(3 if y in dicty[2] else 4 if y in dicty[3] else 5)):
            t.append(nu+(width*i))
            try: #TESTING
              thestring[nu+(width*i)]=random.choice(dicty[i-1]) #idk???
            except: #NVM FOR LAZINESS
              pass
      else:
        thestring[nu]=' '
    elif random.randint(1,(int(num) if (num.isdigit() and int(num)>2) else 100))==2 and nu<(width-2): #BIG RARITY THING
      if thestring[nu+width]==' ' and thestring[nu+width*2]==' ':
        thestring[nu]=random.choice(dicty[1])
  for i in thestring:
    if i not in dicty.keys():
      print(i,end='')
    else:
      print(dicty[i]+i,end='\033[0m')
  time.sleep(sped)
  print("\033[H",end="")