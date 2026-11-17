# questions they ask you back, and how they take your answer
Q = {}
def yn(ask_t, ask_c, yes_t, yes_c, no_t, no_c): return {'kind': 'yn', 'ask': {'talk': ask_t, 'chat': ask_c}, 'yes': {'talk': yes_t, 'chat': yes_c}, 'no': {'talk': no_t, 'chat': no_c}}
def op(ask_t, ask_c, rep_t, rep_c): return {'kind': 'open', 'ask': {'talk': ask_t, 'chat': ask_c}, 'reply': {'talk': rep_t, 'chat': rep_c}}
Q['howru'] = {'kind': 'howru', 'ask': {'talk': {'h': ['And how are you doing?', 'How about you, {player}? Doing alright?', 'What about you? Everything good?'], 'n': ['You?', 'And you?', 'How about you?'], 'v': ['And you? Not that I care.', 'You?', 'Well? How are you?']}, 'chat': {'h': ['u? :)', 'hbu?', 'how r u doing?'], 'n': ['u?', 'hbu', 'wbu'], 'v': ['u?', 'and u. not that i care', 'well?']}}}
Q['explore'] = yn(['Do you explore much?', 'Been to many worlds yet?', 'Do you get out much? Into the galaxy, I mean.'], ['u explore much?', 'been to many worlds?', 'travel much?'],
  ['Me too! There’s always one more horizon.', 'I can tell. You’ve got that look.', 'Good. The galaxy’s too big to sit still in.'], ['same!! always one more horizon', 'nice, can tell lol'],
  ['You should! Start with somewhere close, like {other}.', 'Fair. Home is nice too.', 'There’s time. The stars aren’t going anywhere.'], ['u should! try {other}', 'fair, home is nice too'])
Q['ship'] = yn(['Do you have your own ship?', 'Got a ship of your own?'], ['got ur own ship?', 'u have a ship?'],
  ['Lucky! Look after her.', 'Nice. Keep your warp cells topped up.', 'Then you know the feeling. Nothing beats it.'], ['nice! look after her', 'lucky lol'],
  ['Someday! Save up, it’s worth it.', 'Walking’s good exercise, I suppose.', 'A ship changes everything. You’ll get one.'], ['someday! save up', 'ull get one'])
Q['fight'] = yn(['Do you like a good fight?', 'You much of a fighter?'], ['u like fighting?', 'u much of a fighter?'],
  ['Ha! I can tell. Just pick your battles.', 'Good. Somebody has to stand up to the bad ones.', 'A warrior, then. I respect that.'], ['ha thought so', 'pick ur battles tho'],
  ['Honestly? Smart. Fighting’s overrated.', 'That’s fine. Peace is braver sometimes.', 'Fair. Keep a medkit anyway.'], ['smart tbh', 'peace is braver sometimes'])
Q['guild'] = yn(['Are you in a guild?', 'Part of any guild?'], ['u in a guild?', 'got a guild?'],
  ['Nice! Good company makes everything easier.', 'Good. Strength in numbers.', 'Lucky them, having you.'], ['nice!', 'strength in numbers :)'],
  ['You could start one! People would join.', 'Lone wolf, then. I get it.', 'There’s no rush. Find the right people.'], ['u should start one!', 'lone wolf huh'])
Q['long'] = yn(['Have you been out here long?', 'Been travelling long?'], ['been out here long?', 'u been around long?'],
  ['Then you know how strange it all gets.', 'A veteran! You must have stories.', 'I can tell. You move like you know the ground.'], ['veteran! u must have stories', 'can tell lol'],
  ['Welcome, then! Ask if you need anything.', 'Fresh! It gets easier, I promise.', 'Everyone starts somewhere.'], ['welcome then!', 'gets easier promise'])
Q['friends'] = yn(['Got many friends out here?', 'Do you have people you can count on?'], ['got many friends out here?', 'u got ppl u can count on?'],
  ['Good. Hold on to them.', 'That’s the most important thing out here.', 'Glad to hear it.'], ['good, hold on to them', 'thats the important part :)'],
  ['Well, you’ve got one more now.', 'That’ll change. People notice you.', 'Count me in, then.'], ['well u got one more now', 'count me in then'])
Q['pet'] = yn(['Do you have any pets?', 'Got any creatures of your own?'], ['got any pets?', 'u have pets?'],
  ['Oh, I bet they’re lovely!', 'Lucky. Animals make everything better.', 'Bring them by sometime!'], ['aw bet theyre cute', 'bring them by!'],
  ['Maybe someday. There are some cute critters on Europa.', 'Fair. They’re a lot of work.', 'Me neither. We should fix that.'], ['maybe someday!', 'me neither lol'])
Q['joke'] = yn(['Want to hear another one?', 'Another joke?'], ['want another?', 'another one?'],
  ['Alright: why don’t Grek play hide and seek? Because good luck hiding when you’re that tall.', 'Okay: what’s a Chompy’s favourite planet? Any, as long as it has snacks.', 'Here goes: how many Erisians does it take to change a light? None. They prefer the dark.'], ['why dont grek play hide and seek? theyre too tall lol', 'whats a chompy’s fav planet? any w snacks'],
  ['Fair. I’m saving the best ones anyway.', 'Probably wise.', 'Your loss! They’re great.'], ['ur loss lol', 'saving the good ones anyway'])
Q['drink'] = yn(['Fancy a drink sometime?', 'Want to grab a drink later?'], ['wanna grab a drink sometime?', 'drink later?'],
  ['It’s a date. A friendly one!', 'Great. First round’s on me.', 'Perfect. I know a cantina.'], ['first round on me', 'i know a cantina :)'],
  ['Maybe another time.', 'No worries.', 'Your loss. The drinks are terrible anyway.'], ['another time then', 'np'])
Q['bored'] = yn(['Want to go do something?', 'Shall we go find some trouble?'], ['wanna go do smth?', 'go find some trouble?'],
  ['Brilliant! Lead the way.', 'Let’s go! I’m right behind you.', 'Finally, some excitement.'], ['lets go!!', 'lead the way'],
  ['Alright. I’ll be here if you change your mind.', 'Fair enough. Rest is good too.', 'Another time, then.'], ['ok im here if u change ur mind', 'another time'])
Q['fav_place'] = op(['What’s your favourite world so far?', 'Where’s the best place you’ve been?'], ['whats ur fav world so far?', 'best place uve been?'],
  ['{ans}? I’ll have to go there!', 'Oh, {ans}! Good choice.', '{ans}. I can picture it.', 'I’ve heard good things about {ans}.'], ['{ans}? gotta go there!', 'ooh {ans}, nice', 'heard good things about {ans}'])
Q['food'] = op(['What do you eat out here?', 'What’s your favourite food?'], ['whats ur fav food?', 'what do u eat out here?'],
  ['{ans}? Now I’m hungry.', 'Ooh, {ans}. Good taste.', '{ans}! I could go for that right now.', 'Never tried {ans}. Is it good?'], ['{ans}? now im hungry lol', 'ooh {ans}', 'never tried {ans}, good?'])
Q['music'] = op(['What do you listen to?', 'What kind of music do you like?'], ['what music u into?', 'what do u listen to?'],
  ['{ans}! I’ll give it a try.', 'Oh, {ans}? Nice.', '{ans}. I can see that.'], ['{ans}! ill try it', 'ooh {ans} nice'])
Q['color'] = op(['What’s yours?', 'What colour do you like?'], ['urs?', 'what color u like?'],
  ['{ans}! That suits you.', 'Ooh, {ans}. Good one.', '{ans}. I can see that.'], ['{ans}! suits u', 'ooh {ans}'])
Q['hobby'] = op(['What do you do for fun?', 'How about you? What do you enjoy?'], ['what do u do for fun?', 'wbu, what do u enjoy?'],
  ['{ans}? That sounds great!', 'Oh, {ans}! I’d love to try that sometime.', '{ans}. You’ll have to show me.', 'Nice, {ans}. Everyone needs something.'], ['{ans}? sounds great!', 'ooh {ans}, show me sometime', 'nice, {ans}'])
Q['from'] = op(['Where are you from, originally?', 'Where’s home for you?'], ['where r u from?', 'wheres home for u?'],
  ['{ans}! I’ve heard it’s beautiful.', 'Oh, {ans}? Do you miss it?', '{ans}. I’d like to see it someday.'], ['{ans}! heard its nice', 'ooh {ans}, miss it?'])
Q['dream'] = op(['What about you? What do you want, someday?', 'What’s your dream?'], ['wbu, whats ur dream?', 'what do u want someday?'],
  ['{ans}? I believe you’ll get there.', 'That’s a good dream. {ans}.', 'Then go get it. {ans} sounds worth it.'], ['{ans}? ull get there', 'good dream :)'])
Q['fear'] = op(['What about you? What scares you?', 'Anything scare you?'], ['wbu, what scares u?', 'anything scare u?'],
  ['{ans}? That’s fair. You’re braver for admitting it.', 'I get that. {ans} would scare me too.', 'Thanks for telling me. I won’t tease you.'], ['{ans}? fair', 'braver for admitting it'])
Q['tellmore'] = op(['Tell me more?', 'Go on, explain it to me.'], ['tell me more?', 'explain?'],
  ['Huh. I didn’t know that. Thanks, {player}.', 'Interesting! You know a lot of things.', 'Okay, that actually makes sense. I learned something today.', 'Ha, fair enough. I’ll take your word for it.'], ['huh didnt know that', 'interesting!', 'ok that makes sense lol'])

Q['howru2'] = {'kind': 'howru', 'ask': {'talk': {'h': ['How are you doing today?', 'How have you been, {player}?', 'How’s your day going?'], 'n': ['How’s it going?', 'How are you doing?', 'Good day so far?'], 'v': ['How are you, then?', 'Having a good day? Shame if that changed.', 'Well? How are you?']}, 'chat': {'h': ['how r u doing today? :)', 'hows ur day going?', 'how have u been?'], 'n': ['hows it going', 'how r u', 'good day so far?'], 'v': ['how r u then', 'having a good day? shame if that changed', 'well? how r u']}}}
# villains answer your answers in their own way
QV = {'open': {'talk': ['{ans}. Hm. Could be worse.', '{ans}? Predictable.', '{ans}. I’ll remember that.', '{ans}. Not what I’d pick, but fine.', '{ans}. Of course it is.', 'Hm. {ans}. You’re full of surprises. Small ones.'],
               'chat': ['{ans}. predictable', '{ans}? hm', 'noted. {ans}', '{ans}. ofc', 'could be worse i guess']},
      'yes': {'talk': ['Good.', 'Hm. Fine.', 'As I thought.', 'Of course you have.'], 'chat': ['good', 'figured', 'hm ok']},
      'no': {'talk': ['Pity.', 'Your loss.', 'Typical.', 'Then fix that.'], 'chat': ['pity', 'ur loss', 'typical']}}
