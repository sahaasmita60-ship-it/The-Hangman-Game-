import random
l=[
    "about","above","abuse","actor","acute","admit","adopt","adult","after","again",
    "agent","agree","ahead","alarm","album","alert","alike","alive","allow","alone",
    "along","alter","among","anger","angle","angry","apart","apple","apply","arena",
    "argue","arise","armed","array","aside","asset","audio","audit","avoid","awake",
    "award","aware","badly","baker","bases","basic","basis","beach","began","begin",
    "begun","being","below","bench","birth","black","blame","blast","blend","bless",
    "blind","block","blood","board","boost","booth","bound","brain","brake","brand",
    "bread","break","breed","brick","bride","brief","bring","broad","broke","brown",
    "build","built","buyer","cable","calif","carry","catch","cause","chain","chair",
    "chart","chase","cheap","check","cheek","cheer","chest","chief","child","china",
    "choir","claim","class","clean","clear","clerk","click","clock","close","cloth",
    "cloud","coach","coast","could","count","court","cover","crack","craft","crash",
    "cream","crime","cross","crowd","crown","curve","daily","dance","dated","dealt",
    "death","debut","delay","depth","doing","doubt","dozen","draft","drama","drawn",
    "dream","dress","drill","drink","drive","drove","dying","eager","early","earth",
    "eight","elite","empty","enemy","enjoy","enter","entry","equal","error","event",
    "every","exact","exist","extra","faith","false","fault","fiber","field","fifth",
    "fifty","fight","final","first","fixed","flash","floor","fluid","focus","force",
    "forth","found","frame","frank","fraud","fresh","front","fruit","fully","funny",
    "giant","given","glass","globe","grace","grade","grand","grant","grass","great",
    "green","gross","group","grown","guard","guess","guest","guide","happy","harsh",
    "heart","heavy","hence","honor","horse","hotel","house","human","ideal","image",
    "index","inner","input","issue","jeans","joint","jokes","judge","juice","jumpa",
    "known","label","large","laser","later","laugh","layer","learn","leave","legal",
    "level","light","limit","local","logic","loose","lower","lucky","lunch","magic",
    "major","maker","march","match","maybe","mayor","metal","might","minor","model",
    "money","month","moral","motor","mount","mouse","mouth","movie","music","needs",
    "never","newly","night","noise","north","noted","novel","nurse","occur","ocean",
    "offer","often","order","organ","other","ought","owner","paint","panel","paper",
    "party","peace","phase","phone","photo","piece","pilot","pitch","place","plain",
    "plane","plant","plate","point","pound","power","press","price","pride","prime",
    "print","prior","prize","proof","proud","prove","queen","quick","quiet","quite",
    "radio","raise","range","rapid","ratio","reach","react","ready","refer","right",
    "rival","river","rough","round","route","royal","rural","scene","scope","score",
    "sense","serve","seven","shall","shape","share","sharp","sheet","shelf","shell",
    "shift","shine","shirt","shock","shoot","short","shown","sight","since","skill",
    "sleep","slide","small","smart","smile","smoke","sound","south","space","spare",
    "speak","speed","spend","spent","split","spoke","sport","stand","start","state",
    "steam","steel","stick","still","stock","stone","stood","store","storm","story",
    "strip","style","sugar","suite","super","sweet","table","taken","taste","taxes",
    "teach","teeth","their","theme","there","these","thick","thing","think","third",
    "those","three","throw","tight","times","tired","title","today","topic","total",
    "touch","tough","tower","track","trade","train","treat","trend","trial","tried",
    "tries","truck","truly","trust","truth","twice","under","union","unity","until",
    "upper","urban","usual","value","video","visit","vital","voice","waste","watch",
    "water","wheel","where","which","while","white","whole","whose","woman","world",
    "worry","worse","worst","worth","would","wound","write","wrong","yield","young",
    "youth","zebra","zesty"
]
s=random.choice(l)
p=list(s)
guess = ["_","_","_","_","_"]
b=""
attempt=15
print("Welcome to Wordle! Hope you enjoy your time here! You have to guess a 5-letter word and you are going to have 15 attempts before you fail, good luck! :)")
while(attempt!=-1 and guess!=p):
    if(attempt==0):
         print("Oh no! Looks like you are out of attempts, please try harder next time :(")
         print(f"The word was {p}")
         break
    b=input("Guess a letter or the entire word :- ")
    if(guess==p):
         print("Congrats! You have guessed the word!")
         break
    
    if(guess==p or b==s):
      print("Congrats! You have guessed the word!")
      break
    else:
             correct=8
             for x in range(0,5):
                 if(b==s[x]):
                      guess[x]=b
                      print(guess)  
                      correct=9
                      if(guess==p):
                            print("`~Congrats!!!!!! You have guessed the word!")
                            break
             if(correct==8):
                       if not (guess==p):
                          print(f"Wrong guess! You have {attempt-1} attempts left")
                          attempt-=1
                       else:
                            break
print("Thank you for your time")
g=input(("Type 'c' to close the game: "))
if(g=="c"):
     print("Closed")
else:
    pass