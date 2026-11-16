/* NOSTRAVECTOR · residents' GAME TALK, part 2: musing, and reacting to what's happening around them
   kill (you just killed something), pLevel (you levelled up), pDeath (you died), boss (a boss fight), bossKill, storm, night,
   day, gearNone / gearGood (what you're wearing), lvlLow / lvlHigh (you're well below / above them), rep (your reputation:
   hero / neutral / villain), afk (you've stood still a while), jet, swim. */
window.NV_RES_GAME = Object.assign(window.NV_RES_GAME || {}, {
muse: {
  hero: ['beautiful out here, i could cry', 'watch out for the {threat} near {sys}, they’re nasty', 'anyone need help? anyone? i’m bored of being nice to nobody', 'saw a kid on {other} with a wooden sword, made my whole week', 'the sky on {place} goes pink at dusk, check it out', 'i fixed a guy’s heater yesterday, he cried, i cried', 'if you see someone struggling, help them, that’s the whole game', 'saving people is better than loot. ok loot is close', 'gonna build a shelter for newbies by the ridge', 'everyone deserves a warm base and a full belly', 'i swear the fauna here are getting bigger', 'pro tip: hug your friends, it buffs morale +100%', 'shout out to whoever left medkits at the crash site', 'i escorted pilgrims all night and i regret nothing', 'someone gave me a flower on {other}, i still have it', 'heroes don’t sleep, we nap aggressively', 'the {faction} lot aren’t so bad once you buy them a drink', 'if the {threat} show up, i call dibs on punching first', 'kindness is free. medkits are 60 units. choose kindness', 'i’d die for this server. not literally. ok maybe', 'today i will be nice to at least one villain. maybe', 'who wants to clear a lair later? i’ll tank', 'my armour has dents from every friend i’ve protected', 'can’t believe i get to live out here, it’s insane', 'remember to stretch before fighting, i pulled a hamstring on a penguin', 'the stars are so loud tonight', 'we should do a group photo at the station', 'just helped a trader move crates, 10/10 workout', 'i don’t trust that {threat} behind the ridge. gonna go hug it with my sword', 'lv {lv} and still learning, that’s the beauty', 'good morning to everyone except the {threat}', 'i hope {player} is doing ok, they work too hard', 'heals are love, heals are life', 'i would like to formally adopt everyone on {place}', 'gonna name my next ship after my mum'],
  neutral: ['anyone seen the {threat} near {sys}?', 'where is everyone, it’s dead as fuck', 'lag is real today lmao', 'lol {faction} again', 'i’m so broke i’m mining with my teeth', 'is it just me or does {place} smell like wet dog', 'who keeps leaving campfires everywhere', 'the fauna here have zero chill', 'can someone explain diplomacy to me like i’m five', 'i just fell off a cliff and lived. skill', 'my inventory is 90% rocks', 'thinking about my life choices. still choosing rocks', 'warp cells cost HOW much', 'someone nerf the {threat}', 'imagine dying to a penguin. couldn’t be me. (it was me)', 'i love the music on this world', 'what’s the best world for obsidian, asking for me', 'who wants to race to that hill, loser buys drinks', 'is this an rpg or a mining simulator, i genuinely can’t tell', 'i’ve been on {place} so long i have a favourite rock', 'every system has a bar and every bar has a fight', 'i’m not lost, i’m exploring aggressively', 'the {faction} guards gave me the stink eye again', 'brb gonna stare at the sky for 10 mins', 'someone stole my campfire spot, war has been declared', 'ok who keeps throwing grenades at the wildlife', 'fun fact: i have no idea what i’m doing', 'lv {lv} and still afraid of birds', 'i paid 60 units for a medkit and it was mostly tape', 'wonder what’s for dinner on {home}', 'is {other} worth it or is it mid', 'why are the good deposits always next to something that bites', 'i miss my bed on {home}', 'that crater over there is cursed, don’t @ me', 'i’m one bad day away from becoming a villain lol'],
  villain: ['so quiet. so boring. somebody bleed', '{faction} won’t last. nothing lasts. except me', 'who wants to fight. anyone. please', 'i’m going to take over {place} and rename it after myself', 'heroes are just villains who haven’t been paid enough', 'the {threat} are the only honest ones out here', 'i kicked a penguin today. felt nothing. felt great', 'kindness is a debuff', 'someone touched my base. i’ll find them. i always do', 'tax evasion? no, tax invasion. i invade, then i tax', 'every hero on this server owes me money', 'i’m not evil, i’m efficient', 'burned a hero’s camp today. their marshmallows were good', 'the galaxy needs a firm hand. mine. on its throat', 'lol {player} thinks they’re the main character', 'i should run this sector. i’d be fair. fairly terrifying', 'who left the door open? oh. me. on purpose', 'my armour is black because blood doesn’t show', 'i don’t do quests. quests do me. wait', 'chaos is a ladder and i’m climbing it in spiked boots', 'if you’re reading this you’re in range', 'heroes cry so loud, it’s my favourite music', 'i’m saving up for a bigger ship to be meaner in', 'the {faction} pay well for bad news. i am bad news', 'fear is free advertising', 'i should start an empire. a nasty one', 'one day they’ll name a storm after me', 'i only smile when someone else loses', 'the stars are cold. like me. cool. like me', 'every day i wake up and choose violence', 'lv {lv}. strongest thing on {place}. obviously', 'i love the smell of scorched loot in the morning', 'my therapist quit. wonder why', 'world peace? boring. world piece. as in, a piece of every world. mine', 'touch grass? i burn grass']
},
kill: {
  hero: ['NICE KILL {player}!!', 'clean as hell, {player}!', 'get fucking WRECKED, monster', 'ooh that was a good hit', 'gg {player}, textbook', 'you’re a beast, {player}', 'that thing never stood a chance', 'saved us all, {player}, hero shit', 'one less nasty thing in the world, love it', 'teach me your ways {player}'],
  neutral: ['gg', 'nice', 'lmao it exploded', 'clean', 'ok that was sick', 'rip bozo (the monster)', 'holy shit nice', 'yeet', 'you farming xp or what', 'loot it before i do'],
  villain: ['sloppy, but dead is dead', 'meh. i’d have done it faster', 'lol, finally, something died', 'more blood. more', 'nice. now do that to a hero', 'that was almost impressive {player}', 'adequate violence', 'i felt that from here. good']
},
pLevel: {
  hero: ['DING {player}!! LV {plv}!! SO PROUD', 'GRATS {player}!!! lv {plv} let’s gooo', 'level {plv}!! party at my base!', 'ayyyy {player} levelled up!! 🎉', '{player} is lv {plv} now, bow down (lovingly)'],
  neutral: ['grats {player}', 'gz on {plv}', 'ding grats', 'nice, lv {plv}', 'gz gz', 'ayy grats, now buy me a drink'],
  villain: ['lv {plv}? still weak', 'congrats, you’re slightly less pathetic', 'lv {plv}. cute. i was lv {plv} once. as a toddler', 'oh no, {player} levelled. anyway', 'grats. now i get more xp for killing you']
},
pDeath: {
  hero: ['NOOO {player}!!', 'rip {player} 😭 run back, i’ll cover you', '{player} went down!! revenge time', 'you’ll get it next time, i believe in you', 'that boss is a cheating motherfucker, don’t worry'],
  neutral: ['rip lol', 'f', 'press F for {player}', 'oof', 'well that sucked', 'lmao what happened', 'respawn timer go brr'],
  villain: ['LMAO {player} DIED', 'skill issue', 'get good', 'i’ll put that on your gravestone: "tried"', 'that was the best thing i’ve seen all day', 'rip bozo', 'haha. ha. HAHA']
},
boss: ['BOSS UP!! everyone on it', 'FOCUS THE BOSS', 'big boy incoming, holy shit', 'i’ve got aggro, hit it, HIT IT', 'don’t stand in the red stuff!!', 'phase two!! here we fucking go', 'it’s enraging, burn it down', 'stack up, stack up!', 'dodge the slam, DODGE THE SLAM', 'whoever pulled that, i love you and hate you', 'interrupt it! interrupt!', 'that thing has more hp than my entire guild', 'pop everything, cooldowns NOW', 'this is it, this is the fight', 'heal check! anyone alive?', 'it’s weak to getting punched, PUNCH IT', 'ok who woke it up', 'tank and spank, boys and girls', 'nobody panic. i’m panicking', 'GET ITS LEGS'],
bossKill: {
  hero: ['WE DID IT!!! GG EVERYONE!!!', 'BOSS DOWN!! you’re all incredible!!', 'holy shit we actually killed it', 'GG GG GG, best team ever', 'that was the best fight of my life', 'heroes win again, baby!!'],
  neutral: ['gg', 'boss down, loot please', 'ez', 'holy fuck we did it', 'gg wp', 'nice, roll for loot?', 'that took way too long lol'],
  villain: ['dead. as it should be', 'that was mine, by the way. my kill', 'finally. i was carrying all of you', 'boss down. who’s next', 'its skull is going on my wall', 'gg i guess. i did most of it']
},
storm: ['storm’s rolling in, find cover!!', 'holy shit look at that sky', 'visibility is trash, stay close', 'this storm is fucking biblical', 'heaters up, it’s getting nasty', 'my visor’s fogging up, great', 'anyone else hearing thunder or is that my stomach', 'storm loot hits different', 'the weather on {place} is a war crime', 'stay out of the open, lightning loves armour', 'great, it’s raining sideways now', 'storm’s here. vibes: ruined'],
night: ['night’s falling, fauna get spicy at night', 'getting dark, light a fire', 'night shift, baby', 'so many stars tonight, damn', 'creepy as hell out here at night', 'can’t see shit, who has a torch', 'night vision goggles when', 'the night is young and so are my bad decisions', 'nights on {place} are so pretty', 'everyone stay close, it’s dark'],
day: ['morning! sun’s up', 'daylight, finally', 'good morning {place}', 'rise and grind', 'sunrise on {place} never gets old', 'it’s bright as fuck, who turned the sun up'],
gearNone: {
  hero: ['{player}, you have no armour?? take care of yourself!', 'craft some armour {player}, i worry about you', 'no armour? brave. stupid, but brave'],
  neutral: ['bro where is your armour', 'naked run? respect', 'you’re gonna die in that outfit', 'craft armour, dude, it’s not hard'],
  villain: ['no armour? easy kill', 'walking around naked, {player}? bold. dumb, but bold', 'i could kill you with a spoon right now']
},
gearGood: {
  hero: ['that armour is SICK {player}', 'look at you, decked out!!', 'endgame drip, i’m jealous'],
  neutral: ['nice drip', 'where’d you get that armour', 'ok that gear slaps', 'drip check: passed'],
  villain: ['nice armour. i’ll take it off your corpse', 'expensive armour doesn’t make you less weak', 'shiny. annoying']
},
lvlLow: {
  hero: ['you’re lv {plv}? stick with me, i’ll carry you', 'don’t worry about levels, we all start somewhere', 'need a power-level? i got you'],
  neutral: ['lv {plv} lol, careful out here', 'you’re underlevelled for {place} my dude', 'lv {plv}? brave'],
  villain: ['lv {plv}? i could breathe on you and you’d die', 'how are you still alive at lv {plv}', 'go back to the tutorial, lv {plv}']
},
lvlHigh: {
  hero: ['lv {plv}?? teach me senpai', 'you’re so strong {player}, carry me', 'goals, honestly'],
  neutral: ['lv {plv}, damn, carry me', 'you’re overlevelled as fuck', 'lv {plv}? what do you even do all day'],
  villain: ['lv {plv}. doesn’t scare me. much', 'big level, small brain', 'one day i’ll be stronger than you, {player}. one day']
},
rep: {
  hero: ['{player}’s a real hero, everyone knows it', 'the galaxy needs more people like you, {player}', 'you’re the one who saved those miners right? legend', 'people talk about you, {player}. good things'],
  neutral: ['{player}, you can’t decide if you’re good or bad huh', 'neutral, huh {player}? smart. or boring', 'you play both sides, i respect it'],
  villain: ['{player}… people say you’re a monster. hot', 'you’re the one everyone’s scared of', 'a fellow villain! about fucking time', 'mums on {other} use your name to scare kids, {player}']
},
afk: ['{player} afk?', 'yo {player} you alive?', 'is {player} asleep standing up', 'poke', '{player}? hello? earth to {player}', 'they went afk lol, someone draw on their face', '{player} is meditating. or lagging', 'brb {player} is buffering'],
jet: ['jetpack go WHEEE', 'fly {player} fly', 'show off lol', 'ok rocket man', 'i wish i could fly like that', 'mind the ceiling (there is no ceiling)'],
swim: ['how’s the water {player}?', 'swimming in armour, bold choice', 'don’t drown, i’m not jumping in', 'is there anything in there with teeth', 'free bath lol']
});
