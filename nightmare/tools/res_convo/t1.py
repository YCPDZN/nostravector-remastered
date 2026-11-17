# face-to-face lines, part 1: h = hero, n = neutral, v = villain
T = {}
T['greet'] = {
 'h': ['Hello, {player}! Good to see a friendly face.', 'Hey there. Safe travels getting here?', 'Oh, hello! I was hoping someone would stop by.', 'Hi, {player}. Always glad to see you.', 'Well met, friend.'],
 'n': ['Hey.', 'Oh, hi. Didn’t see you there.', 'Hey, {player}. What’s going on?', 'Hello. You look like you’ve been busy.', 'Hi. Pull up a rock.'],
 'v': ['Oh. It’s you.', 'What do you want, {player}?', 'Hello, I suppose.', 'Make it quick.', 'Ah. The famous {player}. Lucky me.']}
T['howru'] = {
 'h': ['I’m doing well, thank you for asking! The view from {place} never gets old.', 'Honestly? Pretty good. I helped a few people today, and that always lifts me up.', 'Better now that someone’s asked. It’s been a long day.', 'I’m alright. A bit sore from mining, but my spirits are high.', 'Good! I found a quiet spot this morning and just watched the sky for a while.'],
 'n': ['Can’t complain. Well, I could, but nobody listens.', 'Not bad. Bit tired. You know how it is.', 'Fine, mostly. My boots are full of {res}, but fine.', 'Same as always. Getting by.', 'I’m alright. Had worse days, had better ones.'],
 'v': ['Better than the people who crossed me today.', 'I’m fine. Why, are you selling something?', 'Thriving, as usual. Everyone else is the problem.', 'Irritated. You’re not helping yet, but there’s time.', 'Fine. Bored of fools, but fine.']}
T['whatsup'] = {
 'h': ['Not much! Just keeping an eye on things around {place}.', 'Oh, the usual. Helping where I can, mining where I can’t.', 'I was just thinking about heading to {other}. Quiet day otherwise.', 'Just taking a breather. It’s nice to stop sometimes.'],
 'n': ['Not a lot. Thinking about lunch, mostly.', 'Same old. Rocks, walking, more rocks.', 'Just killing time before I head out again.', 'Nothing much. You?'],
 'v': ['Plotting. Nothing you need to worry about. Yet.', 'Waiting for something worth my time. Still waiting.', 'Counting my units. It’s a soothing hobby.', 'Watching idiots. It’s free entertainment.']}
T['name'] = {
 'h': ['I’m {name}. Pleased to meet you properly!', 'Call me {name}. Friends do.', 'The name’s {name}. If you ever need a hand, just shout it.', '{name}, at your service. Most days, anyway.'],
 'n': ['{name}. That’s me.', 'I’m {name}. Don’t wear it out.', 'People call me {name}. Mostly to my face.', 'Name’s {name}. You?'],
 'v': ['{name}. Remember it. You’ll want to, later.', 'I’m {name}, and you’re in my way.', 'They call me {name}. Usually when they’re running.', '{name}. Write it down if your memory’s that bad.']}
T['age'] = {
 'h': ['Old enough to know better, young enough to do it anyway.', 'Honestly, I’ve lost count. Space does that. Level {lv}, if that counts for anything!', 'Older than I look, I hope. Younger than I feel some mornings.', 'Not as old as the stars, thankfully.'],
 'n': ['Older than I’d like. Level {lv}, if that’s what you mean.', 'Rude question. But I’ll let it slide.', 'Enough years to be tired. Not enough to be wise.', 'Does it matter out here? Nobody keeps calendars.'],
 'v': ['Old enough to have buried people who asked that.', 'Why, are you planning my birthday? Don’t.', 'Older than your patience. Younger than your excuses.', 'None of your business. Level {lv}. That’s all you need.']}
T['from'] = {
 'h': ['I’m from {home}. I miss it sometimes, but the galaxy’s been good to me.', '{home}, originally! You should visit if you ever get the chance.', 'Born on {home}. Every sunrise there still lives in my head.', 'From {home}. I left to see what else was out here. Everything, it turns out.'],
 'n': ['{home}. Not much to say about it.', 'I grew up on {home}. Left as soon as I could fly.', '{home}, if you must know. It was fine.', 'From {home}. You?'],
 'v': ['{home}. I don’t go back. They know why.', 'From {home}, and I outgrew it.', '{home}. They’re probably still talking about me there.', 'Somewhere you’ve never heard of. Fine, {home}.']}
T['job'] = {
 'h': ['I’m {job}, mostly. And I help out wherever people need it.', 'I work as {job}. It keeps me busy and keeps others safe.', 'Bit of everything, really. {job} by trade, though.', 'I’m {job}. Honest work. I sleep well.'],
 'n': ['I’m {job}. It pays. Sometimes.', '{job}, for my sins.', 'Whatever pays. Lately, {job}.', 'I do {job} stuff. It’s not glamorous.'],
 'v': ['I’m {job}. Officially.', 'I take what I want and call it a career. On paper I’m {job}.', '{job}. Among other things you don’t want to know about.', 'Let’s just say I’m {job} and leave it there.']}
T['hobby'] = {
 'h': ['I love exploring caves. You never know what’s glittering down there.', 'Stargazing, mostly. And cooking for friends, when I can find real ingredients.', 'I collect little stones from every world I visit. I’ve got dozens!', 'Building. There’s something peaceful about putting a wall up straight.', 'I like {like}. It clears my head.'],
 'n': ['Sleeping, when I can get it.', 'I tinker with old ship parts. Most of them don’t work after.', 'Walking. Seeing what’s over the next hill.', 'Honestly, {like}. Don’t judge.', 'Fishing, on worlds that have water. It’s quiet.'],
 'v': ['Winning. Usually at someone else’s expense.', 'I sharpen things. It relaxes me.', 'Watching rivals fail. Better than any show.', 'I collect debts. Some are paid in units. Some aren’t.', '{like}, and making sure nobody else is better at it.']}
T['fav_food'] = {
 'h': ['Erisian frost-bread, warm, with honey from Malana. Nothing beats it.', 'Anything shared with friends tastes better. But fried root stew is close.', 'I could eat Chompy spice-cakes all day. Probably shouldn’t.', 'Simple things. Fresh fruit after a long trip feels like a feast.'],
 'n': ['Whatever’s hot and not moving.', 'Seared alien steak. Cook it in a furnace and it’s honestly great.', 'Ration bars. Kidding. Anything but ration bars.', 'Grek root soup. Don’t ask what’s in it.'],
 'v': ['The finest food money can buy. Usually someone else’s money.', 'Steak. Rare. Like my patience.', 'Whatever I take from people who aren’t looking.', 'I don’t eat for fun. I eat to stay stronger than you.']}
T['hungry'] = {
 'h': ['Oh no! Here, sit down a moment. Grab something before you head out again.', 'Hungry? Try searing some alien meat in a furnace, it’s a lifesaver.', 'You should eat! Adventurers who skip meals don’t last long.', 'I’d share if I had anything left. There’s a stall nearby, though.'],
 'n': ['Same. There’s a stall around here somewhere.', 'Furnace plus alien meat equals steak. That’s the whole recipe.', 'Join the club. Food out here is a myth.', 'Eat something, then. You look pale.'],
 'v': ['Not my problem. Unless you’re buying.', 'Then go hunt something. Or someone.', 'Starve a little. Builds character.', 'Hungry? I’ll sell you food. At a price.']}
T['fav_color'] = {
 'h': ['Sky blue. The colour of Earth from orbit, they say.', 'Gold, like Malana’s light in the evening.', 'Green. Growing things make me happy.', 'Soft lilac, like the Erisian sky.'],
 'n': ['Grey. Low maintenance.', 'Probably orange. It’s cheerful without trying too hard.', 'Black. Goes with everything, including dirt.', 'Blue, I guess. Never thought about it.'],
 'v': ['Red. Obviously.', 'Black, like the space between stars.', 'Whatever colour makes people nervous.', 'Crimson. It hides stains.']}
T['fav_music'] = {
 'h': ['I love the old Erisian choir songs. They sound like snow falling.', 'Anything you can dance to around a campfire!', 'I hum while I mine. Terribly, but happily.', 'The Grek play this slow drum music at festivals. It gets in your bones.'],
 'n': ['Whatever the cantina’s playing. I’m not picky.', 'Quiet. Silence is underrated.', 'Old Earth stuff. Guitars, mostly.', 'I don’t really listen to music. Just the hum of the ship.'],
 'v': ['Battle hymns. Loud ones.', 'The sound of my enemies begging. Second place, war drums.', 'I don’t listen to music. Music listens to me.', 'Something with a lot of bass and no lyrics. Lyrics are for people with feelings.']}
T['sing'] = {
 'h': ['Ha! Alright, just one line: “Oh, the stars are far, but my friends are near…” That’s all I know!', 'I’m a terrible singer, but for you? La la laaa. There. Happy?', 'Maybe around a campfire sometime. I get shy.', 'Only if you sing with me. Deal?'],
 'n': ['No.', 'You really don’t want that. Trust me.', 'Hmm hm hmm. That’s all you’re getting.', 'I sing in the shower. The shower’s on a different planet.'],
 'v': ['Absolutely not.', 'Sing? I’ll make you sing. A different kind.', 'Ask me again and see what happens.', 'I don’t perform for free.']}
T['fav_place'] = {
 'h': ['Archiostal’s gardens. Being under that glass sky feels like being looked after.', '{home}, always. But Europa’s ice oceans come close.', 'Anywhere with friends. But if I had to pick, the beaches on Malana.', 'The rings of Saturn from close up. I cried a little, honestly.'],
 'n': ['Wherever I’m not being shot at.', 'Mars is alright. Red, dusty, quiet.', 'Here’s fine. {place} grows on you.', 'Any cantina with a working heater.'],
 'v': ['Anywhere I’m in charge.', 'The edge of the galaxy. Fewer people.', 'Places nobody else dares go. Less competition.', 'Wherever my enemies aren’t. Then wherever they are, with a sword.']}
T['drink'] = {
 'h': ['A drink sounds lovely. Malana honey mead, if they have it.', 'I don’t drink much, but I’ll happily sit with you while you do!', 'Erisian frostwine is beautiful. Tastes like winter morning.', 'Maybe after we’ve done some good today. Reward first, celebrate after.'],
 'n': ['Now you’re talking. {drink}?', 'I could go for a {drink}. Or three.', 'The cantina here waters everything down. Still goes.', 'Only if you’re buying.'],
 'v': ['Only the strong stuff. {drink}, neat.', 'You buy, I drink. That’s how this works.', 'I don’t drink with strangers. You’re a stranger.', 'Drink? Fine. Try to keep up.']}
T['bored'] = {
 'h': ['Bored? Let’s go find something! There’s always a cave nobody’s explored.', 'Try helping someone out. It’s never boring, I promise.', 'How about a race? First to that ridge wins!', 'Maybe visit somewhere new. The galaxy’s too big to be bored in.'],
 'n': ['Yeah, it’s a slow day.', 'Go mine something. It’s boring, but productive boring.', 'Boredom’s just your brain asking for trouble. Ignore it.', 'Same. Want to throw rocks at things?'],
 'v': ['Then go start a fight. Not with me.', 'Your problem, not mine.', 'Bored? Be useful instead.', 'I’m never bored. I’m always scheming.']}
T['whattodo'] = {
 'h': ['We could explore! I heard there’s a dungeon nearby nobody’s finished.', 'Let’s go help someone. There are always quests on the board.', 'How about a race to that hill? Loser buys dinner!', 'We could build something together. I’ve always wanted a bigger camp.'],
 'n': ['Mine, sell, repeat. The classic.', 'There’s a stall over there. We could haggle for fun.', 'Explore a bit? I’m not doing anything else.', 'Spar, maybe. Nothing serious.'],
 'v': ['We could take over that outpost. Kidding. Mostly.', 'Spar. I want to see what you’ve got.', 'Go make some enemies. It’s fun, trust me.', 'We? I work alone. But fine, impress me.']}
T['joke'] = {
 'h': ['Why did the Grek bring a ladder to Archiostal? He heard the drinks were on the house! …I’ll see myself out.', 'What do you call a Chompy who won’t stop eating? Emperor! Don’t tell Hak I said that.', 'How do Erisians stay warm? They don’t. They just glare at the cold until it leaves.', 'What do you call a star that tells jokes? A pun-sar. Okay, that one was bad.', 'Why don’t astronauts get hungry after launch? They just had a big breakfast. A launch. Lunch. You get it.'],
 'n': ['I only know one joke and it’s about a Grek and a door. It’s not funny.', 'Why did the miner break up with the pickaxe? It was just using him for his rocks.', 'Knock knock. Actually, no doors out here. Never mind.', 'What’s the worst part about space? The atmosphere. Get it? There isn’t one.', 'My life’s the joke. Laugh away.'],
 'v': ['Your gear. That’s the joke.', 'Here’s a joke: you, thinking you can beat me.', 'A Pontifex walks into a bar. The bar doesn’t walk out. That’s the joke.', 'Why did the hero cross the road? To die on the other side.', 'I don’t tell jokes. I make examples.']}
T['compliment'] = {
 'h': ['Aw, thank you! That really made my day.', 'That’s so kind. You’re pretty great yourself, you know.', 'Oh, stop it. No, keep going.', 'Thank you, {player}. I needed that today.'],
 'n': ['Huh. Thanks. Didn’t expect that.', 'Appreciate it. Really.', 'You’re not so bad yourself.', 'Thanks. I’ll remember you said that.'],
 'v': ['I know.', 'Flattery won’t get you a discount.', 'Obviously. But it’s nice to hear someone admit it.', 'What do you want?']}
T['insult'] = {
 'h': ['Ouch. Rough day? I won’t take it personally.', 'That wasn’t very kind. Is everything alright?', 'I’m sorry you feel that way. I’m still here if you want to talk.', 'Words hurt, you know. But I forgive you.'],
 'n': ['Wow. Okay.', 'Charming. Anything else?', 'I’ve been called worse by better.', 'Cool. Moving on.'],
 'v': ['Say that again. Closer.', 'Brave words for someone that fragile.', 'Careful. I remember everyone who talks to me like that.', 'Is that the best you can do? Pathetic.']}
T['swear'] = {
 'h': ['Whoa, language! Something wrong?', 'Easy there. Deep breath. What happened?', 'That bad, huh? Want to talk about it?', 'I’ll pretend I didn’t hear that.'],
 'n': ['Ha. Yeah, I feel that.', 'Bad day?', 'Strong words. Fair enough.', 'Tell me about it.'],
 'v': ['Finally, someone who speaks my language.', 'Watch your mouth. Or don’t. I don’t care.', 'Ooh, angry. Use it.', 'Save it for a fight.']}
