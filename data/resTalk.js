/* NOSTRAVECTOR · residents' everyday speech (natural, in-world, by temperament)
   Residents talk like people who live in this galaxy, not like players in a chat window. Each resident has a temperament
   (shy, bold, funny, grumpy, kind, sarcastic, cheerful, calm, curious, dramatic, lazy, charming, proud, loyal), a past job,
   something they love and a catchphrase. A line is picked from their temperament first, then their alignment, then the base.
   Placeholders: {player} {place} {other} {home} {res} {n} {lv} {sys} {faction} {threat} {b} {species} {job} {like} {drink} {club} */
window.NV_RES_TALK = {
greet: {
  base: ['Morning. Or whatever it is on {place}.', 'Hello again, {place}.', 'Oh, good, people. I was starting to talk to the rocks.', 'Made it to {place} in one piece.', 'Hello, {player}.'],
  hero: ['Good to see friendly faces. Everyone all right?', 'Hello, {player}! Need a hand with anything?', 'I came as soon as I could. What’s happening on {place}?'],
  villain: ['Well. Look who’s still alive.', 'Don’t stop on my account. Actually, do.', 'I’m back. Try to look pleased.'],
  shy: ['Oh. Hi. I’ll just... be over here.', 'Hello. Sorry. Hello.', 'I didn’t think anyone would be here.'],
  bold: ['Right, I’m here. Let’s get something done.', '{place}! Did you miss me?', 'Nobody panic, I’ve arrived.'],
  funny: ['I’m here, the party can officially start. Well, a party. Of one.', 'Good news, everyone: I’m back. Bad news: I’m back.', 'Somebody said there was free food on {place}. Somebody lied.'],
  grumpy: ['{place}. Again. Wonderful.', 'Don’t talk to me until I’ve had something hot to drink.', 'Who left the sky this bright?'],
  kind: ['There you are, {player}. I was hoping I’d run into you.', 'Hello, everyone. I brought spare rations if anyone’s short.', 'It’s nice to be somewhere with friendly faces.'],
  sarcastic: ['Oh good, {place}. My favourite place I didn’t choose.', 'I’m here. Hold your applause.', 'Ah, {player}. The universe keeps throwing us together.'],
  cheerful: ['Hello hello! What a day to be alive!', '{place}! I love it here. I love everywhere, honestly.', 'Hi, {player}! Isn’t it a lovely day?'],
  calm: ['Hello. It’s peaceful here today.', 'Good to be back on solid ground.', 'Breathe in. {place} smells of {res} and rain.'],
  curious: ['Oh, {place}! I’ve been reading about this place.', 'Hello! Have you noticed the soil here? It’s fascinating.', 'Back again. I still haven’t worked this place out.'],
  dramatic: ['I have returned! Let the songs begin.', 'At last, {place}. I have crossed the stars for this moment.', 'You may all breathe again. I’m here.'],
  lazy: ['Hi. I walked all the way from the ship. I need a sit down.', 'Is there anywhere to lie down around here?', 'Made it. Barely. The ramp was steep.'],
  charming: ['{player}! You look better every time I see you.', 'Hello, beautiful {place}. And hello to you too.', 'Did someone order a little sunshine?'],
  proud: ['Make room. I’m back.', 'You may have heard of me. Everyone has.', '{place} looks better already, don’t you think?'],
  loyal: ['I’m here, {player}. Whatever you need.', 'Reporting in. Where do you want me?', 'Told you I’d come back. I always do.']
},
bye: {
  base: ['I should get going. Take care of yourselves.', 'That’s me done for today. See you around.', 'I’m off to {other}. Wish me luck.', 'Right. Time to move on.'],
  hero: ['Stay safe, all of you. I mean it.', 'Off to {other}. Someone there needs a hand.', 'Look after each other while I’m gone.'],
  villain: ['I’m bored. Don’t burn anything down without me.', 'Off to {other}. Warn them I’m coming.', 'Don’t miss me too much.'],
  shy: ['I’m going to go now. Bye. Sorry.', 'Um. Goodbye.', 'It was nice. Really. Bye.'],
  bold: ['I’m off. Try to keep up next time.', 'Somewhere else needs me more. Later!', 'Onward!'],
  funny: ['I’m leaving before someone makes me work.', 'Goodbye, {place}. It’s not you, it’s me.', 'Exit, pursued by a {threat}.'],
  grumpy: ['Finally. I’m going.', 'Don’t follow me.', 'That’s enough people for one day.'],
  kind: ['Take care of yourself, {player}. Eat something warm.', 'It was lovely seeing everyone. Be good to each other.', 'If you need me, I’m on {other}.'],
  sarcastic: ['Well, this has been thrilling. Truly.', 'I’ll be on {other}. Try not to miss me.', 'Off I go. Contain your grief.'],
  cheerful: ['Bye bye! This was the best!', 'See you soon! Can’t wait!', 'Off to {other}! Adventure!'],
  calm: ['I’ll head on now. Peace, everyone.', 'Time to move. The stars aren’t going anywhere, but I am.', 'Until next time.'],
  curious: ['I want to see what’s on {other}. Bye!', 'Off to take some samples elsewhere.', 'There’s a whole galaxy I haven’t looked at yet.'],
  dramatic: ['And so I depart, into the unknown!', 'Remember me fondly.', 'Farewell! The stars call my name!'],
  lazy: ['I’m going to go find a bed.', 'Nap time. Bye.', 'That was a lot of standing. I’m off.'],
  charming: ['Don’t forget me now.', 'Until we meet again, {player}.', 'I’ll be thinking of you all. Some of you.'],
  proud: ['My work here is done.', 'You’re welcome, {place}.', 'I’ve left this place better than I found it.'],
  loyal: ['Call me if you need me, {player}. I’ll come.', 'I’ll be back. You know I will.', 'Keep my spot warm.']
},
muse: {
  base: ['You can see {other} from here if you squint.', 'The {threat} have been busy near {sys}. Watch yourselves.', 'I keep meaning to go home to {home}. Maybe next month.', 'Strange to think this sky looks normal to someone.', 'Some days I can’t believe I live out here.'],
  hero: ['If anyone needs help, just shout.', 'I hope the people on {other} are doing all right.', 'It’s a good day when nobody gets hurt.'],
  villain: ['Everyone’s so soft out here.', '{faction} won’t last. Nobody does.', 'Somebody should be in charge of this place. Somebody like me.'],
  shy: ['It’s nice when it’s quiet like this.', 'I practised saying hello to people. I still forget.', 'I like watching the clouds. Nobody asks you anything.'],
  bold: ['Who’s up for something dangerous?', 'I’d fight a {threat} with my bare hands. Probably.', 'Somebody give me a challenge.'],
  funny: ['I told a Grek a joke once. He laughed three days later.', 'If I had a unit for every time I got lost, I could buy a map.', 'My mother said I’d never amount to anything. I’m on another planet, Mum.'],
  grumpy: ['Everything out here wants to bite you.', 'The rations taste like boot. Old boot.', 'Nobody ever fixes anything around here.'],
  kind: ['Has everyone eaten today?', 'I left a heater going by the ridge for anyone who’s cold.', 'You never know who needs a kind word.'],
  sarcastic: ['Oh look, another rock. Riveting.', 'Living the dream. Somebody’s dream, anyway.', 'Yes, I’m having the time of my life.'],
  cheerful: ['Look at that sky! Every colour at once!', 'I just found the prettiest stone. I’m keeping it.', 'Today is going to be a good day. I can feel it.'],
  calm: ['If you sit still long enough, {place} starts to hum.', 'No rush. The galaxy will wait.', 'I like the sound of the wind out here.'],
  curious: ['Why do you think the fauna here glow at night?', 'I’d love to know how old these rocks are.', 'There’s a pattern in the {res} deposits. I’m nearly sure of it.'],
  dramatic: ['One day they’ll write songs about this walk.', 'The stars weep for us. Or it’s raining. Hard to tell.', 'I feel destiny in the air. Or dust.'],
  lazy: ['I could sleep right here. On this rock. It’s a nice rock.', 'Walking is overrated.', 'Is it lunch yet? It feels like lunch.'],
  charming: ['It’s a beautiful day. Almost as nice as the company.', 'I’ve made friends on every world I’ve been to.', 'You meet the best people in the strangest places.'],
  proud: ['Nobody mines faster than me. It’s a fact.', 'I’m the best thing that’s happened to {place} this year.', 'People still talk about what I did on {other}.'],
  loyal: ['I keep my promises. It’s about all I have.', 'Friends are worth more than any ore.', 'If {player} needs me, I’m there. Simple.']
},
job: {
  miner: ['I worked the deep shafts back on {home}. You never forget the dark.', 'Ten years with a drill in my hands. I can tell good ore by the sound.', 'Miners get the dust in their lungs and the stars in their eyes.'],
  pilot: ['I flew freight before this. Seven hundred jumps, never lost a crate.', 'I still reach for a throttle when I’m nervous.', 'The best thing about flying is the quiet between systems.'],
  medic: ['I was a medic once. I still check everyone’s colour when they walk past.', 'I’ve stitched up worse than a {threat} bite. Much worse.', 'Drink water. Doctor’s orders. Former doctor.'],
  soldier: ['I wore a uniform for twelve years. Now I wear whatever I like.', 'Old habit: I always know where the exits are.', 'War teaches you who your friends are. Then it takes some of them.'],
  trader: ['I used to run a stall on {home}. Haggling is in my blood.', 'Never pay the first price. Never.', 'Everything has a price. Even friendship. Especially friendship.'],
  cook: ['I cooked in a galley for a crew of forty. I can make ration bars taste like home.', 'Give me a fire and some {res}-root and I’ll make you cry. In a good way.', 'People trust you when you feed them.'],
  scholar: ['I taught history before I came out here. Now I’m living it.', 'I keep a journal. Everything goes in it. Even you, probably.', 'Libraries are just quiet spaceships for the mind.'],
  farmer: ['My family grew grain on {home} for six generations.', 'You learn patience when your crops take a season to answer you.', 'I still check the sky for rain every morning.'],
  smuggler: ['Let’s just say I used to move things that didn’t want to be found.', 'I know three ways off every planet. Four, on a good day.', 'Customs officers and I have an understanding. They don’t understand me.'],
  engineer: ['I built reactor housings before this. I still hear the hum in my sleep.', 'If it’s broken, give it to me. If it’s not broken, give it to me anyway.', 'Every machine has a heartbeat if you listen.'],
  pilgrim: ['I set out to see the holy places of Archamus. I kept walking after that.', 'Every road is a prayer if you walk it honestly.', 'The pilgrims on the Archiostal road taught me to share my bread.'],
  musician: ['I played in a band on {home}. We were terrible. We were wonderful.', 'Every planet has a different sound. {place} is a slow one.', 'I hum when I mine. The rocks don’t complain.']
},
likes: {
  mining: ['There’s a vein of {res} near here. I can smell it.', 'Nothing beats the feeling of a good strike.'],
  building: ['I’m going to build something tall here one day.', 'Give me walls and a roof and I’m happy.'],
  exploring: ['I want to stand on every world in {sys} before I die.', 'There’s a ridge over there nobody’s climbed. Yet.'],
  trading: ['Prices on {other} are better. I’ll make a killing.', 'Buy low, sell high, sleep well.'],
  fighting: ['I could use a good fight. Just a friendly one.', 'My hands get itchy when it’s this quiet.'],
  dancing: ['I wish someone would put some music on.', 'Every good day ends with dancing. That’s my rule.'],
  cooking: ['I found some herbs that would go lovely in a stew.', 'Food tastes better under an alien sky.'],
  flying: ['I miss my ship when I’m on the ground too long.', 'Did you see that shuttle come in? Beautiful landing.'],
  nature: ['Look at these plants. Nobody planted them. They just decided to live.', 'The animals here are more polite than people.']
},
mine: {
  base: ['Just need a few more {res} and I can finally make something useful.', 'There’s good {res} in this one.', 'Come on, come on, crack...'],
  villain: ['This deposit’s mine. Find your own.', 'Back off. I was here first.'],
  grumpy: ['This rock is harder than my landlord.', 'Of course it’s the stubborn kind.'],
  cheerful: ['Ooh, sparkly!', 'Every swing is a little surprise!'],
  lazy: ['Five more swings. Then a nap.', 'Why is all the good ore so far down?']
},
trade: {
  base: ['The prices here are fair today, for once.', 'Selling a bit of {res} if anyone needs it.', 'I’ll swap you {res} for scrap, if you’re interested.'],
  villain: ['These traders are robbing us blind.', 'I could run this market better in my sleep.'],
  trading: ['Watch and learn. Never pay the first price.', 'Ah, a stall. My natural habitat.']
},
toPlayer: {
  base: ['Hey, {player}. How are you holding up?', '{player}! Good to see you.', 'You look like you’ve been busy, {player}.'],
  hero: ['Need anything, {player}? I’ve got spare medkits.', 'Be careful out there, {player}. I mean it.'],
  villain: ['Nice armour. Shame about the person inside it.', 'Stay out of my way today, {player}.', 'Cute base, {player}. Shame if something happened to it.'],
  shy: ['Oh, {player}. Hi. I just wanted to say hi.', 'Sorry, I didn’t mean to stare.'],
  funny: ['{player}! Quick, look busy, somebody important is coming. Oh wait, it’s me.', 'Fancy meeting you here. And there. And everywhere, really.'],
  grumpy: ['What do you want, {player}?', 'If you’re here to ask me for something, the answer’s no. Probably.'],
  kind: ['You look tired, {player}. Sit down a minute.', 'I was just thinking about you. Have you eaten?'],
  sarcastic: ['{player}. My day was going so well.', 'Oh, it’s you. Everyone’s favourite.'],
  cheerful: ['{player}! Hi hi hi! Isn’t this place great?', 'You made my day just by turning up!'],
  curious: ['{player}, have you ever wondered why the sky here is that colour?', 'Where have you been lately? Tell me everything.'],
  charming: ['There’s my favourite person on {place}.', 'Every time I see you, {player}, the day gets better.'],
  proud: ['Admit it, {player}. You came over to see me.', 'Taking notes, {player}? Smart.'],
  loyal: ['Whatever you need, {player}. Just say it.', 'I’ve got your back, {player}. Always.']
},
hurt: {
  base: ['{player}, you’re hurt. Stand by a heater a while.', 'You’re bleeding, {player}. Patch yourself up.'],
  hero: ['Sit down, {player}. Let me look at that.', 'Don’t push it, {player}. Heal up first.'],
  villain: ['Ha. You’re nearly done for, {player}.', 'Careful. Wouldn’t want you to die before I can beat you.']
},
build: {
  base: ['Nice base, {player}. Solid walls.', 'I like what you’ve built here.'],
  villain: ['Your walls are crooked, {player}.', 'Cosy. Very easy to break into.'],
  building: ['Ooh. Mind if I borrow the roof design?', 'Good foundations. You can always tell.']
},
gift: {
  base: ['Here, {player}. I’ve got more {res} than I need.', 'Take these. Go on.'],
  kind: ['I saved these for you, {player}.', 'Don’t argue. Just take them.'],
  proud: ['A gift. From me. You may thank me later.']
},
steal: {
  base: ['Too slow, {player}.', 'Finders keepers.', 'That deposit? Mine now.']
},
ding: {
  base: ['I feel stronger today. Level {lv}.', 'Level {lv}. It’s been a long road.', 'Did you see that? Level {lv}!'],
  villain: ['Level {lv}. You should all be very nervous.'],
  shy: ['I... I think I got stronger. Level {lv}.'],
  proud: ['Level {lv}. As expected.'],
  cheerful: ['Level {lv}! I could dance!']
},
travel: {
  base: ['I’m heading to {other}. See you there, maybe.', 'Time to jump to {other}.'],
  hero: ['Off to {other}. Someone there might need a hand.'],
  villain: ['Off to {other}. Pray for them.']
},
hunt: {
  base: ['Watch out, it’s coming this way!', 'I’ve got this one.', 'Stay behind me!', 'Keep it busy, I’ll hit it from the side!'],
  boss: ['That’s the big one. Everyone, together!', 'Focus on the boss! Don’t let it corner you!', 'I’ll keep its attention. Hit it hard!']
},
follow: {
  base: ['Mind if I walk with you a while, {player}?', 'Lead the way, {player}.', 'Where are we going?'],
  end: ['I’ll head off on my own now. Thanks for the company.', 'That was nice. See you around, {player}.']
},
craft: {
  base: ['I’m at the forge, back soon.', 'Smelting some {m}. Nearly there.', 'Hammering out a new {p}.'],
  done: ['Finally finished my {piece}!', 'New {piece}. What do you think?', 'Smelted enough {mat} for a {piece} at last.']
},
doing: {
  base: ['Mining a bit of {res}, then heading to {other}.', 'Just exploring. No plan, really.', 'Looking for good {res}. You?'],
  hero: ['Helping where I can. {place} could use it.', 'Checking on the people I met yesterday.'],
  villain: ['Looking for someone to annoy. You’ll do.', 'Plotting. Don’t ask.'],
  shy: ['Oh, nothing much. Just keeping to myself.', 'Picking up stones. They don’t mind me.'],
  bold: ['Looking for the toughest thing on {place} so I can fight it.', 'Making a name for myself.'],
  funny: ['Avoiding responsibilities, mostly. You?', 'Practising my jokes on the wildlife. Tough crowd.'],
  grumpy: ['Trying to have five minutes of peace.', 'Working. Unlike some people.'],
  kind: ['Making sure everyone’s all right.', 'Gathering spare {res} for the newcomers.'],
  sarcastic: ['Saving the galaxy, obviously. Can’t you tell?', 'The usual. Glamour and excitement.'],
  cheerful: ['Everything! I’m doing everything today!', 'Collecting pretty rocks and good memories!'],
  calm: ['Sitting with my thoughts for a while.', 'Taking it slowly. There’s time.'],
  curious: ['Taking notes on the local fauna.', 'Trying to work out why {place} smells like that.'],
  dramatic: ['Living my legend, one step at a time.', 'Seeking my destiny. It keeps moving.'],
  lazy: ['Resting. Between rests.', 'As little as possible.'],
  charming: ['Making friends. You’re next.', 'Waiting for someone interesting. Oh, hello.'],
  proud: ['Being excellent at everything I do.', 'Showing these people how it’s done.'],
  loyal: ['Waiting to see if you needed me, honestly.', 'Keeping watch over my friends.']
},
intro: {
  base: ['I’m {name}. {species}, from {home}.', 'Name’s {name}. I come from {home}, if you were wondering.'],
  shy: ['Oh. Me? I’m {name}. From {home}. That’s... that’s it, really.'],
  bold: ['{name}. Remember it. I’m from {home}, and I’m going places.'],
  funny: ['I’m {name}, professional wanderer, amateur disaster. Born on {home}, which explains a lot.'],
  grumpy: ['{name}. From {home}. Is this going to take long?'],
  kind: ['I’m {name}. I grew up on {home}. It’s lovely to properly meet you.'],
  sarcastic: ['{name}. From {home}. My life story, in two words.'],
  cheerful: ['I’m {name}! From {home}! Oh, I love introductions!'],
  calm: ['My name is {name}. I come from {home}, a long way from here.'],
  curious: ['I’m {name}. I left {home} because I had too many questions and not enough answers.'],
  dramatic: ['I am {name}, child of {home}, wanderer of the endless dark!'],
  lazy: ['{name}. {home}. Can we sit down for the rest?'],
  charming: ['{name}, at your service. I’m from {home}, but I’d rather talk about you.'],
  proud: ['You don’t know who I am? {name}. Of {home}. You’ll hear the name again.'],
  loyal: ['I’m {name}, from {home}. Once I call you a friend, that’s it. You’re stuck with me.']
},
pairs: {
  chat: [['{b}! You’re on {place} too?', 'Just passing through. You look well.'], ['How have you been, {b}?', 'Busy. The war, the mining, the usual.'], ['Did you hear about {faction}?', 'Everyone has. Strange times.'], ['Have you seen {player} lately?', 'Yesterday. Still causing trouble, as usual.'], ['I’m thinking of heading to {other}.', 'Take me with you. I’m sick of this rock.'], ['Do you ever miss {home}?', 'Every day. Don’t tell anyone.']],
  trade: [['Need any {res}?', 'How much?'], ['I’ll swap you some {res} for scrap.', 'Deal. Don’t tell the traders.'], ['Got any {res} spare?', 'Only {n}. Take it.']],
  spar: [['Fancy a friendly round? Loser buys the drinks.', 'You’re on.'], ['Bet I can put you on the ground.', 'Bet you can’t.'], ['Hands up. Let’s see what you’ve learned.', 'Don’t cry when you lose.']],
  sparEnd: [['Good fight.', 'Good fight. Again tomorrow?'], ['Lucky.', 'Skill. Pure skill.'], ['All right, you win this time.', 'I win every time.']],
  dance: [['Dance with me!', 'Oh, it’s on.'], ['Somebody put some music on!', 'I’ll hum. Go!']],
  race: [['Race you to that ridge!', 'Go!'], ['Last one there buys dinner!', 'Hey, that’s not fair!']],
  raceEnd: [['First!', 'You started early!'], ['Too easy.', 'My legs are shorter, all right?']],
  walk: [['Walk with me a while?', 'Sure. You lead.'], ['Come and see this view.', 'Coming.']],
  argue: [['Still playing the hero, {b}? How sweet.', 'Someone has to clean up after you.'], ['You’re the reason {place} is such a mess.', 'And you’re the reason it’s so boring.'], ['Keep walking, {b}.', 'Make me.']],
  fight: [['You’ve been asking for this, {b}.', 'Then come and get it.'], ['That’s it. Outside. Now.', 'We are outside!']]
},
gather: ['Everyone, over here!', 'Come on, let’s all stand together a minute.', 'Group picture! Squeeze in!'],
guildHi: ['There you are, {player}!', 'Good to see you, {player}.', '{player}! The guild’s been asking about you.'],
invite: ['{player}, have you got a minute?', 'Hey, {player}! Wait a second.', '{player}, can I ask you something?'],
deal: ['Pleasure doing business.', 'Thank you. Enjoy them.', 'There you go.'],
broke: ['Come back when you’ve got the units.', 'You’re a little short, friend.'],
drink: {
  order: ['One {drink}, please.', 'Something strong. Surprise me.', 'Another round! On me! No, on {b}!', 'Same again.'],
  tipsy: ['I’m not drunk. I’m just very relaxed.', 'This {drink} is surprisingly good.', 'I love this place. I love all of you.', 'Has the floor always been this wobbly?'],
  drunk: ['I could fight a whole fleet right now!', 'You’re my besht friend. Did I tell you that?', 'Who moved the door?', 'I’m gonna sing. Nobody stop me.', 'One more. Jusht one.'],
  sober: ['My head. My poor head.', 'Never again. Until next time.', 'Water. Somebody give me water.']
},
brawl: {
  start: ['What did you just say to me?', 'You spilled my drink!', 'Say that again. I dare you.', 'You and me. Right now.'],
  war: ['You’re from {enemy}, aren’t you? I can smell it.', 'Your lot burned my friend’s home. Put your hands up.', 'This is for the war, {enemy}!'],
  citizen: ['Hey! Hey! You looking at me?', 'This is my stool. Mine!', 'Who are you calling drunk?'],
  end: ['All right, all right. I’m done.', 'Ow. Fair enough.', 'Somebody hold my drink. Oh, it’s gone.'],
  bouncer: ['Out! The pair of you!', 'Take it outside or I take you outside!']
},
party: {
  arrive: ['We cleared {lair}! First round’s on me!', 'Who’s ready to celebrate?', 'We earned this. Music, now!', 'Survived {lair}! Somebody pour me something!'],
  dance: ['This song! This is my song!', 'Look at me go!', 'Nobody dances like {guild}!', 'Low gravity dancing is the best dancing!'],
  chat: ['Did you see me take down {boss}?', 'I nearly died on the third floor. Best day ever.', 'Same time next week?', 'To {lair}, and to never going back!'],
  invite: ['{player}! Come and celebrate with us!', 'Get over here, {player}, the night’s young!']
},
dungeon: {
  ask: ['{player}, we’re going into {lair}. Want to come?', 'We could use you in {lair}, {player}. You in?', 'The guild’s heading down into {lair}. Coming, {player}?'],
  yes: ['Brilliant! Stay close.', 'Let’s go. Watch your back.', 'Right behind you.'],
  no: ['No worries. Next time.', 'Suit yourself. More loot for us.'],
  follow: ['Lead on, {player}.', 'With you, {player}.', 'Where you go, we go.'],
  stay: ['Holding here.', 'Waiting for your word.'],
  floor: ['Floor cleared! On we go.', 'That’s the matriarch down. Deeper!', 'Next floor. Stay together.'],
  heart: ['This is it. The heart of the lair.', 'Everyone ready? It’s waiting for us down there.'],
  win: ['We did it! {lair} is clear!', 'Ha! Who’s buying the drinks?', 'That was incredible. Party at the Lounge!'],
  wipe: ['Fall back! Fall back!', 'We’ll get it next time.']
}
};
