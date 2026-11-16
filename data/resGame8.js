/* NOSTRAVECTOR · residents' GAME TALK, part 8: your wars, named worlds, what you're doing, weather, jokes, milestones, deaths,
   the talk menu's hello / don't-know / goodbye, more conversations, and more from the lairs and the bar */
window.NV_RES_GAME = Object.assign(window.NV_RES_GAME || {}, {
muse2: {
  hero: ['every life saved is a win, write that on my grave', 'gonna clear the {threat} out of {sys} by the weekend', 'shoutout to the medics, unsung legends', 'i gave my last warp cell to a stranger and i’d do it again', 'the villains are loud but there’s more of us', 'i trained all morning, my arms are noodles', 'i love this community so fucking much', 'protect the newbies, they’re the future', 'did a lair run for charity. there’s no charity. i just did it', 'my guild’s motto is "no one left behind" and "bring snacks"', 'be the hero your mum thinks you are', 'saw a villain help an old trader today. there’s hope', 'patrolling the ridge, all quiet', 'the best loot is a friend’s smile. second best is obsidian', 'today i chose courage. and a sandwich', 'i bandaged a penguin. it bit me. we’re friends now', 'heroes don’t need thanks, but thanks are nice', 'stood guard all night, my eyes are sandpaper', 'every sunrise is a second chance', 'help first, loot second, that’s the rule', 'the galaxy is worth fighting for', 'i taught a kid to block yesterday. proud', 'hero tip: smile at the scary ones, confuses them', 'i’ll take the hits so you don’t have to', 'sometimes saving the day is just fixing a heater', 'i carry extra medkits for strangers. call me the pharmacy', 'one day this war ends and we’ll all have a drink', 'love you, {place}, never change (please change a bit)', 'remember the fallen, then go get revenge (legally)', 'my heart is full and so is my inventory'],
  neutral: ['what if the real loot was the friends we griefed along the way', 'my ship makes a noise. a bad noise. a new noise', 'one more node and i’m done. that was 40 nodes ago', 'i’ve seen things on {other} you wouldn’t believe. mostly rocks', 'who decided obsidian should be rare, i want a word', 'thinking about going villain. the outfits are better', 'sat on a cactus on {other}. never again', 'is anyone else’s jetpack making that clicking noise', 'can’t tell if i’m good at this or just lucky', 'i talk to my pickaxe. his name is Greg', 'the stall on {place} owes me 4 units, i’ll never forget', 'free advice: never trust a cheap medkit', 'how is everyone so rich, what am i doing wrong', 'my guild kicked me for "excessive dancing". worth it', 'i dream about crystal veins. that’s normal right', 'i’m one boss away from a new helmet. one boss. kill me', 'wonder what {player} is up to. probably something stupid', 'grind, sleep, grind, drink, grind', 'i lost a fight to a bird today. a bird', 'everyone’s fighting about the war, i just want my rocks', 'saw a shooting star. wished for obsidian. nothing yet', 'hot take: mining is relaxing', 'the Lounge last night was unhinged, 10/10', 'i keep a list of everyone who’s stolen my nodes. it’s long', 'if you need me i’ll be staring into the void', 'i’m neutral. i hate everyone equally', 'my favourite colour is "loot"', 'the {faction} patrols are getting bolder', 'i can’t believe warp cells don’t come with a manual', 'tomorrow i’ll be productive. said every day since lv 1'],
  villain: ['i rule {place} now. nobody voted. nobody needed to', 'i’ve got a list. you might be on it', 'heroes are so easy to bait, it’s embarrassing', 'empires are built on bones. i’m collecting', 'my enemies call me "that fucker". i call them "next"', 'i don’t hold grudges, i nurture them', 'i taxed a trader so hard he became a hero out of spite', 'sometimes i let a hero win. builds false hope', 'mercy? sounds weak. smells weak', 'today’s forecast: chaos, with a chance of screaming', 'i burned my own base once, to feel something', 'the throne of {place} is mine, it’s a rock, i sit on it', 'who needs friends when you have minions', 'i’ve never apologised and i’m not starting today', 'the weak exist to make me look good', 'if you see me smiling, run', 'villain tip: always monologue AFTER the kill', 'every hero has a price. most are cheap', 'my armour is spiky so hugs are impossible. by design', 'the galaxy will kneel. or i’ll make it', 'i stole a hero’s cape and use it as a towel', 'i only laugh when someone else is crying', 'the {threat} work for me now. probably', 'i don’t do teamwork. i do team-dominance', 'i’m not a bad person. i’m a great bad person', 'someone called me evil. i sent flowers. poisoned ones', 'i’ll remember this place when i burn it', 'they fear what they can’t understand. they can’t understand me', 'world domination is a marathon, not a sprint', 'pain is temporary, my reputation is forever']
},
pwar: { // your Diplomacy wars, in the zone chat
  atWar: {
    hero: ['we’re at war with {enemy}, stay strong everyone!', '{enemy} won’t win, not on our watch', 'fighting for {realm}, let’s fucking go', 'every world we take back from {enemy} counts'],
    neutral: ['war with {enemy}, prices are gonna skyrocket', 'great, {enemy} again', 'war’s bad for business. good for loot though', '{realm} vs {enemy}, my money’s on whoever has more ships'],
    villain: ['war with {enemy}! finally some fun', 'i hope {enemy} burns', 'war is the best season', 'kill them all, sort it out later']
  },
  won: {
    hero: ['we beat {enemy}! the galaxy is a little safer', 'victory for {realm}!!', 'gg {enemy}, now play nice'],
    neutral: ['{enemy} got wrecked lol', 'won the war, cool, can i mine in peace now', 'gg {enemy}'],
    villain: ['{enemy} crushed. as it should be', 'their worlds are ours now. mwahaha', 'victory tastes like their tears']
  },
  peace: {
    hero: ['peace at last! drinks for everyone!', 'no wars right now, enjoy it', 'peace looks good on us'],
    neutral: ['peace? boring. ok nice', 'quiet galaxy today', 'no wars, prices are normal for once'],
    villain: ['peace is just a break between wars', 'ugh, peace. so boring', 'i give it a week before someone starts something. probably me']
  }
},
worlds: {
  earth: ['Earth! the OG', 'Earth’s cities are insane from orbit', 'still can’t believe humans live HERE', 'Earth air smells like rain and smog'],
  mars: ['Mars is so red omg', 'Olympus Mons is massive, i climbed it once', 'Martian dust gets EVERYWHERE', 'Hawthorne yelled at us here once, iconic'],
  venus: ['Venus is literally hell', 'acid clouds, no thanks', 'who would build a base on Venus. Hawthorne would', 'my suit is sizzling'],
  mercury: ['Mercury is hot as fuck', 'the Cygnus is up there somewhere', 'don’t land on the day side, trust'],
  aridaxx: ['Aridaxx! Chompy capital!', 'Alphinos is the loudest city in the galaxy', 'the Gilded Fang has the best brawls'],
  eris: ['Eris is so cold my soul froze', 'Erisian cities glow like crystals', 'the Billionth Year bar is fancy as hell'],
  malana: ['Malana is so green and calm', 'Am-Grek was born here, holy ground', 'the Quiet Root cantina is chill'],
  carax: ['Carax is a fortress, no air, no mercy', 'they say the Cult of Zark died here', 'Am-Grek rules from this rock'],
  janira: ['Janira Prime! violet everything', 'the Violet Tide cantina, legendary', 'Janira’s been through a lot'],
  charon: ['Charon is tiny and creepy', 'the edge of Sol, so quiet out here'],
  europa: ['Europa has a whole ocean under the ice', 'i heard something swimming down there'],
  titan: ['Titan has methane lakes, smell is wild', 'orange sky, orange vibes']
},
pAction: {
  mine: ['need help mining {player}?', 'save some for me {player}', 'nice swing {player}', 'mining buddies!', '{player} you’re a machine'],
  fight: ['{player} needs help, GO GO GO', 'covering you {player}!', '{player}’s in trouble!', 'i got you {player}!', 'hit it {player}, i’ll flank'],
  sprint: ['where’s the fire {player}?', 'zoom zoom', 'slow down {player} lol'],
  craft: ['what you crafting?', 'ooh new gear?', 'the forge is calling'],
  build: ['ooh building something?', 'need a hand with that wall?', 'architect mode']
},
weather: {
  rain: ['it’s pissing down', 'rain rain go away', 'i’m soaked through my armour', 'puddle jumping time', 'love the smell of rain on {place}'],
  snow: ['it’s snowing!!', 'snow day!!', 'my boots are full of snow', 'snowball incoming', 'everything’s white, can’t see shit'],
  sand: ['sandstorm!! eyes shut!', 'sand in my teeth, sand in my soul', 'i can’t see anything, the sand is everywhere'],
  ash: ['ash is falling again', 'the sky is burning', 'it smells like the end of the world', 'ash in my lungs, great']
},
jokes: ['what do you call a lazy Chompy? a chomp-sleepy', 'why don’t Erisians tell secrets? because they’ll still remember them in a billion years', 'how many Grek does it take to change a light? one, but it takes a week', 'why did the penguin cross the ice? to bite me specifically', 'i’d tell you a warp joke but you wouldn’t get there in time', 'my ship and i have a lot in common. we both break down under pressure', 'what’s a villain’s favourite drink? hero tears, on the rocks', 'why do heroes never get lost? they always follow their heart. and the quest marker', 'what did the boss say to the party? you’re all getting floored', 'i’d make a joke about obsidian but it’s too rare', 'why was the medkit sad? it was all patched up', 'a human, a Chompy and a Grek walk into a bar. the Grek is still walking', 'what’s the loudest planet? Aridaxx. no contest', 'i bought a cheap jetpack. now i have trust issues and a broken leg', 'why don’t lairs have doors? they want you to come in', 'what do you call a resident who never leaves the bar? a regular. a regular disaster'],
dingMile: {
  25: ['LV 25!! quarter century baby!!', 'twenty five, i’m basically a veteran now'],
  50: ['LV 50!!! HALFWAY TO GODHOOD', 'fifty! i’m old! i’m powerful!'],
  75: ['LV 75, i can see the summit', 'seventy five and still hungry'],
  100: ['LV 100!!! I’M A FUCKING LEGEND', 'triple digits, bow before me'],
  110: ['LV 110. MAX. I AM THE SERVER NOW', 'one hundred and ten. there is nothing left to fear']
},
death: {
  hero: ['down!! respawning at {home}, be right back!', 'they got me! avenge me!', 'i died protecting you guys, worth it', 'respawning, save me a spot'],
  neutral: ['dead lol, back to {home}', 'gg, respawning', 'well that was dumb, brb', 'died to something stupid, don’t ask'],
  villain: ['they got lucky. back at {home}, coming for revenge', 'death is temporary, my grudge is forever', 'whoever did that, i will find you', 'respawning angry']
},
talkHi: {
  hero: ['hey {player}! what’s up?', 'oh hi!! need something?', '{player}! always happy to chat', 'hello friend! what can i do for you?', 'hey hey! talk to me!'],
  neutral: ['yeah?', 'sup {player}', 'what’s up', 'hm? oh, hi', 'you need something?', 'yo'],
  villain: ['what do you want', 'make it quick, {player}', 'you’re wasting my time', 'speak, worm', 'this better be good']
},
unknown: {
  hero: ['honestly? no idea, sorry!', 'i wish i knew, {player}', 'not a clue, but i’ll find out for you', 'that’s a mystery to me too'],
  neutral: ['no clue lol', 'dunno', 'beats me', 'idk, ask someone smarter', 'never heard of it'],
  villain: ['why would i know that', 'figure it out yourself', 'do i look like a library', 'no idea and i don’t care']
},
talkBye: {
  hero: ['take care {player}!', 'see you around, hero!', 'stay safe!!', 'bye bye, come back soon!'],
  neutral: ['later', 'cya', 'k bye', 'peace'],
  villain: ['finally', 'go away now', 'don’t come back. or do, i’m bored', 'leave before i change my mind']
},
pairs2: {
  chat: [['you see the Lounge last night?', 'i don’t remember last night'], ['{b}, what happened to your face', 'lair happened'], ['wanna start an empire?', 'only if i’m emperor'], ['i’m thinking of changing guilds', 'traitor! (take me with you)'], ['you think {player} likes me?', 'nobody likes you, that’s why i do'], ['how’s the war?', 'still warring'], ['i found a crystal shaped like a duck', 'show me. SHOW ME'], ['do you dream about loot?', 'every night, and sometimes about lunch'], ['which species throws the best parties?', 'Chompy. no contest'], ['i owe you one for that lair', 'you owe me five, actually'], ['the {threat} took my ship', 'buy a better ship'], ['you seem stressed', 'i’m always stressed, it’s my brand']],
  argue: [['you left me to die in that lair', 'you were slow, it was natural selection'], ['your empire is a joke', 'your face is a joke'], ['stop stealing my nodes', 'stop being slow then'], ['you’re a coward {b}', 'i’m alive, aren’t i'], ['i’m better than you', 'in what? losing?'], ['you’re all talk', 'and you’re all lag']],
  spar: [['let’s settle this', 'with fists or with dance?'], ['you’ve been dodging me', 'i dodge everyone, it’s a skill'], ['round two?', 'round two']],
  trade: [['i’ll give you my rarest rock', 'is it actually rare or just ugly'], ['sell me a warp cell', 'name your price, then double it']]
},
dungeon2: {
  trap: ['TRAP!', 'watch the floor!', 'spikes, spikes!', 'who stepped on the button', 'i hate this lair'],
  scared: ['i don’t like this', 'something’s breathing', 'turn back? no? ok', 'my torch is flickering, great', 'did you hear that?'],
  phase: ['it’s changing phase!', 'it’s pissed now!', 'here comes the big attack!', 'get ready, it’s winding up'],
  warden: ['that’s the matriarch, kill her!', 'big bitch guarding the stairs', 'take down the warden, the stairs open'],
  spring: ['healing spring, top up!', 'drink from the spring, quick', 'spring’s up, heal']
},
drink2: {
  toast: ['to the guild!', 'to not dying!', 'to {player}!', 'to loot and to love!', 'to the fallen!', 'to whatever this is!', 'bottoms up!', 'one for the road!'],
  hangover: ['my brain is a lair and every floor hurts', 'who let me drink that', 'i can taste colours', 'never mixing {drink} again', 'the sun is my enemy now']
},
empire: { // their own resident empires
  hero: ['my empire protects the weak, join us', 'we just freed another world!', 'a just empire is possible, i’m proving it'],
  neutral: ['my empire’s doing fine, taxes are low', 'just expanded to another rock', 'empire life is mostly paperwork'],
  villain: ['my empire grows. so does the fear', 'another world kneels', 'the map is turning my colour']
}
});
