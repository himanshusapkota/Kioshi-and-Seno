define kioshi = Character("Kioshi")
define seno = Character("Seno")



image kioshi school angry = "images/character/kioshi_school_angry.png"
image kioshi school angrytalk = "images/character/kioshi_school_angrytalk.png"
image kioshi school angrytalk2 = "images/character/kioshi_school_angrytalk2.png"
image kioshi school clueless = "images/character/kioshi_school_clueless.png"
image kioshi school happy = "images/character/kioshi_school_happy.png"
image kioshi school happyblush = "images/character/kioshi_school_happyblush.png"
image kioshi school huh = "images/character/kioshi_school_huh.png"
image kioshi school normal = "images/character/kioshi_school_normal.png"
image kioshi school normalblush = "images/character/kioshi_school_normalblush.png"
image kioshi school normaltalk = "images/character/kioshi_school_normaltalk.png"
image kioshi school poker = "images/character/kioshi_school_poker.png"
image kioshi school pout = "images/character/kioshi_school_pout.png"
image kioshi school tears = "images/character/kioshi_school_tears.png"
image kioshi school upset = "images/character/kioshi_school_upset.png"

image kioshi schoolsweater poker = "images/character/kioshi_schoolsweater_poker.png"
image kioshi schoolsweater pout = "images/character/kioshi_schoolsweater_pout.png"
image kioshi schoolsweater tears = "images/character/kioshi_schoolsweater_tears.png"
image kioshi schoolsweater upset = "images/character/kioshi_schoolsweater_upset.png"
image kioshi schoolsweater angry = "images/character/kioshi_schoolsweater_angry.png"
image kioshi schoolsweater angrytalk = "images/character/kioshi_schoolsweater_angrytalk.png"
image kioshi schoolsweater angrytalk2 = "images/character/kioshi_schoolsweater_angrytalk2.png"
image kioshi schoolsweater clueless = "images/character/kioshi_schoolsweater_clueless.png"
image kioshi schoolsweater happy = "images/character/kioshi_schoolsweater_happy.png"
image kioshi schoolsweater happyblush = "images/character/kioshi_schoolsweater_happyblush.png"
image kioshi schoolsweater huh = "images/character/kioshi_schoolsweater_huh.png"
image kioshi schoolsweater normal = "images/character/kioshi_schoolsweater_normal.png"
image kioshi schoolsweater normalblush = "images/character/kioshi_schoolsweater_normalblush.png"
image kioshi schoolsweater normaltalk = "images/character/kioshi_schoolsweater_normaltalk.png"



image seno playfulsmile = "images/character/playful_smile.png"
image seno sadblush = "images/character/sad_blush.png"
image seno angry = "images/character/angry.png"
image seno annoyed = "images/character/annoyed.png"
image seno blushangry = "images/character/blush_angry.png"
image seno blushingcry = "images/character/blushing_cry.png"
image seno confused = "images/character/confused.png"
image seno darkdistant = "images/character/dark_distant.png"
image seno darksad = "images/character/dark_sad.png"
image seno mischievous = "images/character/mischievous.png"
image seno normsmile = "images/character/norm_smile.png"
image seno oh = "images/character/oh.png"


label start:

    scene smp_classroom1_day1
    with fade

    "This is Monday morning!"

    "Everyone walks to school, but Kioshi arrives late."

    "Kioshi rushes toward the school."

    "Kioshi finally reaches the school."

    scene smp_hallway_day2
    with fade

    show kioshi schoolsweater pout

    kioshi "Uff! After a long walk, I finally arrived at school!"

    show kioshi schoolsweater angry

    kioshi "I am so angry with my mom!"

    kioshi "She prepared breakfast too late."

    kioshi "Let me go to the classroom for now!"

    scene smp_classroom4_day4
    with fade

    "The classroom door is open."

    show kioshi schoolsweater happyblush

    kioshi "Ohh! Thank God the teacher didn't lock the door!"

    scene smp_classroom1_day2
    with fade

    show kioshi school huh

    kioshi "I finally arrived in the classroom."

    "After some time..."

    kioshi "I am feeling bored here!"

    kioshi "When will the bell ring?"

    kioshi "I really want some lunch."

    "After half an hour, the bell suddenly rings."

    # play sound "audio/bell.mp3"

    show kioshi school pout

    kioshi "Those thirty minutes were too hard."

    kioshi "I am really exhausted."

    scene smp_noticeboard_evening1
    with fade

    show kioshi school huh

    "Kioshi notices something on the notice board."

    kioshi "Huh? What is that?"

    kioshi "Let me go and read it."

    scene smp_hallway_day2
    with fade

    show kioshi school clueless

    "Kioshi finds out that the school will be over in less than 10 days."

    kioshi "What? School will be over in less than 10 days?"

    kioshi "Will there be no exams?"

    kioshi "I should propose to my crush."

    kioshi "I really don't have much time."

    "Kioshi starts planning how he will propose to his crush."


label propose_crush:

    scene smp_classroom3_evening1
    with fade

    show kioshi school huh at truecenter

    "Kioshi rushes toward the classroom and finds his crush there."

    kioshi "There she is!! Let me go to her."
    kioshi "Seno is there, let me go toward her and propose to her."

    "Kioshi finally reaches Seno and starts talking with her."

    show kioshi school happy at left
    show seno normsmile at right

    kioshi "Hi Seno"

    seno "Oh Hi Kioshi"

    kioshi "How are you?"

    seno "I am good, what about you?"

    kioshi "I am fine tooo"

    show seno playfulsmile at right
    show kioshi school normaltalk at left

    seno "Haha!! You sound a little bit nervous"

    show kioshi school clueless at left

    kioshi "Whattt??? No, I am not"

    show seno mischievous at right

    seno "Are you sure?"

    show kioshi school angrytalk at left

    kioshi "Yeahhhh.....Totally"

    seno "You do not look totally fine!!"

    show kioshi school upset at left

    kioshi "Actually!!!"

    seno "Actually what, Kioshii???"

    kioshi "Well...."

    "Kioshi looks away for a moment."

    kioshi "I have something to tell you, Seno."

    show seno oh at right

    seno "Yess, Kioshiii!!"

    kioshi "There's something I wanted to tell you."

    seno "Something important?"

    kioshi "Yess"

    seno "Ok speak out, I am listening"

    show kioshi school happyblush at left
    kioshi "I really like you"

    show seno sadblush at right

    seno "Hmmm!! Really?"

    menu:
        "Accept Kioshi":
            jump seno_accept

        "Reject Kioshi":
            jump seno_reject


label seno_accept:

    show seno normsmile at right
    show kioshi school happyblush at left
    seno"I like youuu tooo!!"
    seno"I wass supposed to say that but you said"
    
    kioshi"What You?"

    seno"yes Kioshii I would have purposed you if you donot"

    kioshi"Whyyyyy??? would you purpose me"

    seno"Becauseee I really liked youuu"

    kioshi"Since Whennn"

    seno"From Kindergarden"

    kioshi"Ohh!! Same hereee"

    seno"Whattt Really I thought you only started liking me in senior year"

    kioshi"Noo Nooo"

    seno"sooooo"

    kioshi"sooooo"
    show seno playful smile at right

    seno"Who are we now?"
 
    show kioshi_school_happy at left

    kioshi"Boyfriend and Girlfriend"

    seno"huh Yesssss I wanted to be your Girlfriend since 6th grade"

    kioshi"Ohhh!! really "

    "Kioshi was soooo soooo happy from insideee and he wasss realllyyyyyyyyyy"

    seno"Ohhh Ohhh"

    kioshi"I cannot still belive it "

    seno "Believe it."

    kioshi "Okay..."

    seno "Boyfriend."

    kioshi "Girlfriend."

    seno "Haha."

    kioshi "Why are you laughing?"

    seno "Because you're blushing again."

    kioshi "I can't help it!"

    "suddenly bell rings."

    seno"yeahhh!! Bell Rang Letsss move too homeeeeeeee" 

    kioshi"Ahh!! Yessss I got a chance to walk with you together"

    seno"awhhhhhhhhhhhhh sooo cuteeeeeee"

    "The Game Ends Here!! Both Of them go to home"

  
   



    return


label seno_reject:
    scene smp_classroom3_night1
    with fade
    show kioshi school tears at left
    show seno darksad at right


    seno"Kioshiii...."

    kioshi"Soooo.... Will you be my girlfriend?"

    seno"........."

    seno"Kioshiii!!!!"

    kioshi"Y-Yes"

    seno"So..Sorry Kioshiii"

    kioshi"Huhh....??"

    seno"I can't"

    kioshi"....."

    kioshi"Ohh Okey"

    seno"It's not because i don't like you."

    seno"You are to important to me"

    seno"And I love spending time with you"


    kioshi"Then Why"
    seno"Because..."

    seno"I don't think. I can See you that way."

    kioshi"I understand"

    seno"I am really sorry, Kioshi"

    seno "Please don't be sad."

    kioshi"I'm not!"
    kioshi "I'm totally fine!"

    seno "Kioshi..." 

    kioshi "..."
    kioshi "Maybe... just a little."

    seno "Come here..." 

    kioshi "Seno?" 

    seno "You're still my favorite person, okay?"

    kioshi "..."

    kioshi "You're so mean..."

    seno "Hehe... I'm sorry."

    kioshi "It's fine..." 
    kioshi "I'll get over it."

    seno "I know you will."

    scene smo_classroom2_night1

    show kioshi school tears
    "Kioshi Cried A Lot That Day"

    kioshi"What Will i do now"
    kioshi"I have to Move On"

    hide kioshi school tears

    "After that kioshi changed school although only 10 days left for school end. "


    "This was the story hope you liked"

   


return





