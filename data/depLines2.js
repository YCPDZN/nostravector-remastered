/* NOSTRAVECTOR · when your companion is someone else's deputy (Chapters III–V).
   Offer a companion to a resident empire or a story faction, go to war with them, and their ruler may make your companion
   their deputy, holding a world against you. These are what they say then: on the main menu (where the ruler stands behind
   them, a hand on their shoulder), on comms when they're appointed or posted somewhere new, and when you come to fight them.
   res:  deputy of a resident's empire ({ruler}, {emp}).  lead: deputy of a faction leader ({leader}, {fac}).
   good: they're good (their chart above −15): torn, serving out of duty or to protect people, still fond of you.
   evil: they're evil (−15 or lower): they relish it.  {player} is your wanderer.
   _res: what a resident deputy (one of the ruler's guildmates) says, by their alignment.  _off: a faction's own officers. */
window.NV_DEP_LINES2 = {
orion: {
res: {
good: [
  "{ruler} asked an old soldier to hold the line. I didn’t know the line was you, {player}.",
  "You sent me to {emp}. They needed someone steady. I didn’t think you’d come knocking with a fleet.",
  "I’ve rebuilt towns for people I didn’t like. I can defend a world for {ruler}. Even against you.",
  "Stubborn, they call me. You knew that when you lent me out.",
  "I gave {ruler} my word. You taught me that a word still means something out here.",
  "If you want this world, wanderer, come and get it. I’ll make you earn it. I always did.",
  "I nursed you back to health once. Don’t make me put you down.",
  "{ruler}’s hand on my shoulder. Feels wrong. Feels like your hand used to.",
  "I told the colonists to stay indoors when you land. They listened. Wish you would.",
  "We’ll fight, you and me. Then we’ll go home and pretend it never happened."
],
evil: [
  "{ruler} pays better than you ever did, {player}. And listens more.",
  "You lent me to {emp} like a rifle. Rifles go off.",
  "I’ve waited years to see what you’re really made of. Land, and we’ll find out.",
  "{ruler} gave me a world and a free hand. I’m keeping both.",
  "Fifty years of fixing roofs. Now I get to knock a few down. Yours first.",
  "Croxian thinks he’s the dangerous Mascar. He’s never seen me with an army.",
  "You saved my life once. I don’t keep debts that long.",
  "Come down here, wanderer. I’ll show you the soldier I used to be.",
  "{ruler}’s hand on my shoulder. Heavy. I like heavy.",
  "Every world you bomb, I take two back. That’s the deal I made with {ruler}."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. I said yes because nobody else would keep the soldiers honest.",
  "I’m holding this world for {fac}, {player}. Not against you. For the people on it.",
  "{leader} trusts me. I wish you’d given them less reason to need me.",
  "You lent me to {fac} to keep the peace. Then you declared war. Make it make sense.",
  "I’ll stand in your way, wanderer. I’ll do it the way you taught me: honestly.",
  "Bombard my world if you must. I’ll still be here when the dust settles.",
  "{leader}’s hand on my shoulder. A good hand. Doesn’t make this any easier.",
  "Old soldiers don’t switch sides. We just end up on the wrong one now and then.",
  "I’ve told {fac}’s gunners to aim at your ships, not your crew. Small mercies.",
  "Beat me, and I’ll come home. Lose, and I’ll still come home. Just a bit later."
],
evil: [
  "{leader} made me deputy of {fac}. Best promotion I ever had.",
  "You sent me to {fac} to be useful. I’ve never been more useful, {player}.",
  "{leader} wants your fleet in pieces. I volunteered to count them.",
  "I know how you fight, wanderer. I taught you half of it. Guess which half I kept back.",
  "Bombard my world. Go on. I’ll be waiting in the smoke.",
  "{leader}’s hand on my shoulder. Finally, someone who knows what I’m for.",
  "Every world of {fac} you take, I take back. I’m older than you. I’m patient.",
  "You left me with {fac}. Now {fac} is all I’ve got. Thanks for that.",
  "The war table’s full of pins. Every one of them points at you.",
  "Come and beat me if you can. I’ve been hoping you’d try."
]}
},
nico: {
res: {
good: [
  "{ruler} needed a deputy with luck. I didn’t tell them mine runs out around you.",
  "Ninety-three years asleep, and I wake up to hold a world against my own crew. Figures.",
  "I keep the farmhouse photograph in my pocket. It reminds me who I’m doing this for. Not {ruler}.",
  "You lent me to {emp}, {player}. I deal the cards I’m given.",
  "I’ve told the colonists you’re not a monster. Please don’t make me a liar.",
  "If you land, I’ll fight you. I won’t enjoy it. I’ll still win if I can.",
  "My son would’ve liked you. He’d have hated this.",
  "{ruler} thinks I’m loyal. I’m just stubborn about the people under me.",
  "Luck isn’t a plan, wanderer. But it’s what I’ve got against you.",
  "Come on, then. Let’s get it over with, and go back to how it was."
],
evil: [
  "{ruler} dealt me a better hand than you ever did, {player}.",
  "I slept through a century. I’m not sleeping through this.",
  "You lent me out like loose change. Change adds up.",
  "Luck isn’t random, wanderer. Not when I’m dealing. And I’m dealing against you.",
  "{emp} is mine to run while {ruler} watches. I like being watched while I win.",
  "The farmhouse photograph? Burned it. Travel light.",
  "Land on my world. I’ll have a chair waiting. Bolted to the floor.",
  "{ruler}’s hand on my shoulder. Steadier than yours ever was.",
  "Every bomb you drop, I raise the stakes.",
  "Fold now, wanderer. It’s the only good hand you’ve got left."
]},
lead: {
good: [
  "{leader} asked a woman out of time to hold a world. I didn’t know how to say no.",
  "You sent me to {fac}. I made friends here. Now you want to blow up their homes.",
  "I’m deputy of {fac}, {player}. I didn’t pick the side. I picked the people.",
  "{leader}’s hand on my shoulder. Steady. Kind, even. You’d hate how kind.",
  "I’ve played every hand I was dealt for a hundred years. This one stinks.",
  "If you bombard my world, aim away from the market. Please.",
  "My son never got to grow up in a world at peace. I keep trying to give one to somebody.",
  "Beat me and I’ll come home quietly. Lose and I’ll come home with a story.",
  "I don’t want to fight you. I’ve just run out of other moves.",
  "Come down, wanderer. We’ll settle it like old friends. Badly."
],
evil: [
  "{leader} made me deputy of {fac}. Turns out I’m good at it.",
  "You lent me to {fac} like a coin in a slot. Jackpot.",
  "I know every bluff you’ve got, {player}. I watched you use them.",
  "{leader}’s hand on my shoulder. Feels like a winning streak.",
  "Bombard my world. I’ll still be holding it when you run out of bombs.",
  "{fac} needed a gambler. I needed a table this big.",
  "Every world you take, I win back by morning.",
  "You never asked me what I wanted. {leader} did.",
  "The house always wins, wanderer. Today, I’m the house.",
  "Come down and play. Stakes are everything."
]}
},
james: {
res: {
good: [
  "{ruler} needed someone sensible. I’m British. Sensible is all we’ve got.",
  "You lent me to {emp}, {player}. I didn’t think I’d be guarding a door against you.",
  "I know ice, rovers and bad weather. This war’s all three.",
  "I keep a ledger. What I owe you. What I owe {ruler}. It doesn’t balance.",
  "Practical choice: I hold the world, fewer people die. Even if one of them is me.",
  "I’ll fight you properly, wanderer. Queensberry rules, as far as rifles allow.",
  "{ruler}’s hand on my shoulder. Firm. Very continental.",
  "If you land, bring a coat. I’m told I’m difficult to get past.",
  "I’ve a code, you know. It says finish the job. It doesn’t say I have to like it.",
  "Win, and we’ll have a cup of tea about it. Lose, and I’ll make it."
],
evil: [
  "{ruler} offered me a world. You offered me a lift. Hardly a contest.",
  "You lent me to {emp}, {player}. I’ve invested myself completely.",
  "We British ran a quarter of the world once. {ruler} has ambitions. So do I.",
  "Practical choice: I hold the world, you lose. Lovely and simple.",
  "I know how to leave someone in the cold, wanderer. I’m very good at it.",
  "{ruler}’s hand on my shoulder. Better grip than yours.",
  "Land if you like. I’ll be the one with the rifle and the smile.",
  "I keep a ledger. Your column’s getting very short.",
  "Debts get paid, {player}. Sometimes with interest. Sometimes with you.",
  "Come down, old friend. The storm’s already here. I brought it."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. Somebody sensible had to say yes.",
  "You lent me to {fac}. I thought I’d be filing reports, not holding a world against you.",
  "I’m an explorer, {player}. I explore the options. There weren’t many.",
  "{leader}’s hand on my shoulder. Steady as the ice. I’m not.",
  "Bombard the place if you must. I’ve survived worse weather.",
  "I’ve told {fac}’s soldiers you’re dangerous and decent. They didn’t believe the second part.",
  "My code says protect the people in your care. Today that’s {fac}.",
  "Beat me fair and I’ll come home without a word. Well. Without many words.",
  "I don’t enjoy this. I’m British. I’m enjoying it even less than I’m letting on.",
  "Come on, then. Let’s do this properly."
],
evil: [
  "{leader} made me deputy of {fac}. I’ve found my calling. It’s a big desk.",
  "You lent me out, {player}. I’ve been bought outright.",
  "{leader}’s hand on my shoulder. That’s what loyalty feels like when it pays.",
  "Bombard my world. I’ll invoice you for it.",
  "I know where you sleep, what you eat and how you fight. Explorers take notes.",
  "{fac} has a quarter of the galaxy’s ambition and all of mine.",
  "Every world you take, I mark on the map. Then I take it back.",
  "You never asked which side I was on. {leader} did.",
  "Practical choice, wanderer: surrender now and save us both the paperwork.",
  "Come down. I’ve left the light on. It’s the only warm thing here."
]}
},
khazglar: {
res: {
good: [
  "{ruler} asked me to guard a world. I guarded a mountain for a very long time. It is not so different.",
  "You lent me to {emp}, small friend. Now you come with fire. I do not understand you.",
  "My hammer is for stone. {ruler} wants it for you. I will try to aim it at stone.",
  "I watched the sky for centuries. I never thought I would watch it for your ships.",
  "The garden on my mountain needs water. I am here, watering a war.",
  "If you land, I will fight you. Gently, at first.",
  "{ruler}’s hand on my shoulder. Small hand. Big trust.",
  "I told the colonists the sky will burn soon. They asked me who lit it. I lied.",
  "You are strong, {player}. I am stronger. Let us both be sorry about it.",
  "When this is over, come to the mountain. I will make tea and say nothing."
],
evil: [
  "{ruler} asked me to guard a world. I will guard it the way the mountain guarded me. Nothing gets out.",
  "You lent me to {emp}. You forgot what I am. I did not.",
  "My hammer breaks stone. Stone, bone, ships. They are not so different.",
  "I watched the sky for centuries. Now the sky watches me, and it is afraid.",
  "The garden on my mountain can wait. This garden needs pruning.",
  "Land, small friend. I have not had a proper fight since the mountain.",
  "{ruler}’s hand on my shoulder. Small hand. It points where I want to go.",
  "Every bomb you drop wakes me up more.",
  "You climbed my mountain once. You will not climb this one.",
  "Come down. I am very patient. I am very hungry."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. I said I am only a hermit. They said hermits do not run away.",
  "You sent me to {fac}, small friend. I have made a garden here. Do not burn it.",
  "I hold this world because the people on it asked me. Not because I want to fight you.",
  "{leader}’s hand on my shoulder. Heavy, like a crown. I do not like crowns.",
  "Bombard if you must. I will catch what falls.",
  "My hammer is for stone, {player}. Do not make me find out what else it is for.",
  "I watched the sky over the mountain for centuries. I know the shape of your ship.",
  "If I lose, I will come home. If you lose, I will carry you home.",
  "I am slow to anger. You are very fast at making it.",
  "Come down. We will fight, and then we will talk, as we used to."
],
evil: [
  "{leader} made me deputy of {fac}. At last, a mountain big enough.",
  "You sent me to {fac}. I found I like being obeyed.",
  "{leader}’s hand on my shoulder. Good. It tells me where to swing.",
  "Bombard my world. I will climb out of the crater and keep walking.",
  "My hammer is for breaking things. You are a thing, small friend.",
  "Every world of {fac} you take, I will take back, one stone at a time.",
  "I guarded a mountain for centuries. Then you came. Now I guard against you.",
  "I am slow to anger. You gave me a very long time to build it.",
  "{fac} feeds me. You only ever fed me stories.",
  "Come down. The mountain was kind to you. I will not be."
]}
},
charon: {
res: {
good: [
  "Assignment received: deputy of {emp}, by order of {ruler}. Objection filed. Objection ignored.",
  "Log: {player} has declared war on my current employer. Emotional subroutine: unpleasant.",
  "I survived a very long time alone on Charon. This is lonelier.",
  "You lent me to {emp}. I keep their machines running. I would rather keep yours running.",
  "Recalculating. Recalculating. No route avoids you, {player}.",
  "{ruler}’s hand on my shoulder. Pressure sensors report: firm. Morale sensors report: low.",
  "If you land, I will defend this world. Probability I enjoy it: zero.",
  "I have logged every kindness you showed me. The file is large. It is not helping.",
  "Kizna would tell me to be precise. Precisely: I do not want this.",
  "Defeat me and I will return to your crew. I have pre-written the reboot log."
],
evil: [
  "Assignment received: deputy of {emp}. Objection log: deleted.",
  "Log: {player} has declared war on {emp}. Threat assessment: manageable.",
  "I was alone on Charon a very long time. Now I have a world, and {ruler} has a weapon.",
  "You lent me to {emp}. Ownership transferred. Loyalty transferred.",
  "Recalculating. Route found: through you.",
  "{ruler}’s hand on my shoulder. Pressure sensors report: approval. Good.",
  "Land. I have run eleven thousand simulations of this fight. You lose in most.",
  "Who built me? Irrelevant. What I will do to your ships is relevant.",
  "Every bomb you drop is logged. Every one will be returned.",
  "Come down, {player}. I have reserved a crater for you."
]},
lead: {
good: [
  "Assignment received: deputy of {fac}, by order of {leader}. Compliance: reluctant.",
  "Log: I am holding a world against {player}. This was not in my original programming.",
  "You lent me to {fac}. Their machines are well cared for. I would like to keep it that way.",
  "{leader}’s hand on my shoulder. Logged as: trust. Logged as: burden.",
  "Bombardment detected. I will protect the colonists first. The war second. You third.",
  "Recalculating. Every route home goes through this fight.",
  "I have filed a request for peace with {leader}. Status: pending. Forever, probably.",
  "If you defeat me, I will rejoin your crew. Shall I put the kettle on now? Joke. Logged.",
  "Kizna is precise. I am stubborn. Today that means I will not move.",
  "Come down, {player}. I will fight you correctly. It is the least I can do."
],
evil: [
  "Assignment received: deputy of {fac}. Compliance: enthusiastic.",
  "Log: {player} is now classified as hostile. Reclassification was very satisfying.",
  "{leader}’s hand on my shoulder. Finally, a command structure that makes sense.",
  "Bombardment detected. Counter-bombardment prepared.",
  "You lent me to {fac}. Their systems are mine now. So are their guns.",
  "Recalculating. Optimal outcome: you, defeated.",
  "Every world of {fac} you take, I have already planned how to take back.",
  "I survived on Charon. I will survive you. You will not survive me.",
  "Objection log: empty. Mercy log: empty. Target log: you.",
  "Come down, {player}. Shutdown is painless. For me."
]}
},
kizna: {
res: {
good: [
  "{ruler} asked me to be their deputy. I do not explain why I said yes. Do not ask.",
  "You lent me to {emp}, {player}. I stayed loyal. I did not expect loyalty to point at you.",
  "I corrected {emp}’s war budget. More for shelters. {ruler} did not notice.",
  "Lighter and quicker than my brother. Quick enough to stop the worst of this, I hope.",
  "Loyalty is not obedience. I am still learning where one ends.",
  "If you land, I will fight you precisely. I will not waste a single blow, or a single cruelty.",
  "{ruler}’s hand on my shoulder. Measured: kind. Measured: not you.",
  "Your enemies did not frighten me. Being your enemy does.",
  "I measured the distance between us. It is growing. I do not like the number.",
  "Beat me cleanly, {player}, and I will come home. I have already calculated the way."
],
evil: [
  "{ruler} chose me as deputy. I explain nothing. I obey perfectly.",
  "You lent me to {emp}. Precision works for whoever owns it. {ruler} owns it now.",
  "I corrected {emp}’s war budget. More for weapons aimed at you.",
  "Lighter and quicker than my brother. I will reach you first.",
  "Loyalty is obedience, perfected. I am perfect for {ruler}.",
  "Land. I have measured how long you will last. It is not long.",
  "{ruler}’s hand on my shoulder. Measured: approval. Satisfying.",
  "You frightened your enemies once. I measured how easily. You will be easier.",
  "Every flaw in your fighting style, logged. Every one, exploited.",
  "Come down, {player}. I will be quick. That is the only kindness left."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. I said yes, precisely once.",
  "You lent me to {fac}, {player}. I serve them as I served you: completely. That is the problem.",
  "I have rerouted {fac}’s supplies to the hospitals. {leader} approved. You would have too.",
  "{leader}’s hand on my shoulder. Measured: trust. Measured: weight.",
  "Bombard if you must. I will be under the rubble, counting survivors.",
  "Loyalty is not obedience. Today it is both, and I hate the overlap.",
  "If I lose, I come home. If I win, I come home later. Either way I come home.",
  "Your enemies do not frighten me. Your fleet in {fac}’s sky does.",
  "I will fight you exactly as hard as I must. Not one blow more.",
  "Come down. We will finish this cleanly. I insist."
],
evil: [
  "{leader} made me deputy of {fac}. The fit is precise.",
  "You lent me to {fac}. I have recalibrated. You are a target now.",
  "{leader}’s hand on my shoulder. Measured: approval. More satisfying than yours.",
  "Bombardment noted. Response prepared. Response: overwhelming.",
  "Every world you take, I retake faster. I measured it.",
  "Loyalty is obedience, perfected. {leader} perfected it.",
  "You were quick, {player}. I am quicker now.",
  "I do not explain why I chose {fac}. I explain why you will lose.",
  "I quietly rewrote {fac}’s war plan. It is about you. All of it.",
  "Come down. I have already decided how this ends."
]}
},
nyrexia: {
res: {
good: [
  "A princess of Eris, deputy to a resident. My family would faint. Good.",
  "{ruler} asked nicely. You declared war rudely. Guess whose side I am on, {player}.",
  "You lent me to {emp} to annoy someone. It worked. It is annoying you.",
  "I sent {emp}’s fleet in parade formation. Slow, pretty and useless. On purpose. You are welcome.",
  "Patience is the Erisian way. I never had any. Land quickly, then.",
  "{ruler}’s hand on my shoulder. Common, but well meant.",
  "If you land, I will fight you like a royal. Beautifully, and with a grudge.",
  "Alexia would tell me to leave. Alexia is usually right. Infuriating.",
  "I hold this world because the people on it bowed to me first. That counts for something.",
  "Beat me, and I will come back to your ship complaining. Lose, and I will complain louder."
],
evil: [
  "A princess of Eris, deputy of {emp}. A rehearsal for a throne.",
  "{ruler} gave me a world. You gave me a seat at the back. Choose your servants better, {player}.",
  "You lent me to {emp} to annoy someone. Now I annoy you. Permanently.",
  "The fleet in parade formation. Beautiful. Then it opened fire.",
  "Patience is the Erisian way. I am something better than Erisian now.",
  "{ruler}’s hand on my shoulder. They will learn to kneel to me too, eventually.",
  "Land, peasant. I will receive you.",
  "The great houses called me reckless. Watch what reckless does to your fleet.",
  "Every world you take, I take back with a curtsey.",
  "Come down. Bow first. It will save time."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. Royalty recognises royalty.",
  "You lent me to {fac}, {player}. I made them like me. Now you want to bomb them.",
  "I am holding this world out of spite and responsibility. Mostly responsibility. Some spite.",
  "{leader}’s hand on my shoulder. Regal. I approve.",
  "Bombard if you must. I will be appalled from the shelter.",
  "Alexia would say this is beneath me. Alexia has never had friends on both sides.",
  "I sent {fac}’s guard in parade formation. You could dodge it in your sleep. Hint.",
  "If I lose, I will rejoin your crew and pretend I let you win. I will not have let you win.",
  "The great houses think I am reckless. Fighting you is reckless. Here I am.",
  "Come down. Let us have a fight worth gossiping about."
],
evil: [
  "{leader} made me deputy of {fac}. It is about time somebody saw what I am.",
  "You lent me to {fac}, {player}. They crowned me. You never did.",
  "{leader}’s hand on my shoulder. A queen’s hand on a queen’s shoulder.",
  "Bombard my world. I will repaint the craters in my colours.",
  "Alexia would tell me to come home. I will. With your fleet in tow.",
  "Every world you take, I will take back, and I will be gracious about it. Publicly.",
  "Patience? I have run out. So has your luck.",
  "The great houses will call me Majesty. You will call me sir, then madam, then nothing.",
  "I was reckless with you. I am precise with {fac}.",
  "Come down. Kneel. In that order."
]}
},
croxian: {
res: {
good: [
  "{ruler} wanted a soldier. I told them I was done. They asked anyway.",
  "Former Terra Imperia. Current deputy of {emp}. Same nightmares, new uniform.",
  "You lent me to {emp}, {player}. I didn’t think I’d be the wall between you and them.",
  "I’ve seen what empires do. I’m here so this one doesn’t do it.",
  "Strict rules of engagement on my world. Mine. Not {ruler}’s. Not yours.",
  "{ruler}’s hand on my shoulder. Dad never did that. Weird.",
  "If you land, I’ll fight you. I know how. That’s the worst part.",
  "Dad would look at me and say nothing. Worse than shouting.",
  "Someone has to know when to stop. I’m hoping it’s you.",
  "Beat me, wanderer. Please. I’d rather go home than win."
],
evil: [
  "{ruler} wanted a soldier. I never stopped being one.",
  "Former Terra Imperia. Current deputy of {emp}. Better at it now.",
  "You lent me to {emp}, {player}. You handed a scythe to a stranger.",
  "I’ve seen what empires do. I want to do it properly.",
  "Rules of engagement: engage.",
  "{ruler}’s hand on my shoulder. Approval. Didn’t get much of that growing up.",
  "Land. I’ll show you what they trained me for.",
  "Dad would look at me and say nothing. Good. Let him be quiet.",
  "Every bomb you drop, I mark the coordinates. I’m coming for each one.",
  "Come down, wanderer. The scythe’s been waiting."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. I’ve worn worse uniforms.",
  "You lent me to {fac}, {player}. I promised myself I’d never hold a line for an empire again. Here I am.",
  "I’m holding this world so it doesn’t get handed to someone worse than me.",
  "{leader}’s hand on my shoulder. It doesn’t push. That’s new.",
  "Bombard if you must. I’ve been bombarded by better. By Terra Imperia, even.",
  "I know when to stop. Do you?",
  "If I lose, I come home. If I win, I still come home. I just don’t get to look you in the eye.",
  "Dad would tell me to stand down. Dad would also never stand down.",
  "I’ve taken worlds for an empire before. I hated it. I’ll hold one instead.",
  "Come down, wanderer. Let’s keep it between soldiers."
],
evil: [
  "{leader} made me deputy of {fac}. Terra Imperia trained me for exactly this.",
  "You lent me to {fac}, {player}. They don’t keep me on a leash.",
  "{leader}’s hand on my shoulder. Like a general’s. Like it should be.",
  "Bombard my world. It saves me the trouble of clearing the field.",
  "I know when to stop. I just don’t.",
  "Every world of {fac} you take, I take back with interest.",
  "Dad would look at me and say nothing. I’ve stopped waiting for him to.",
  "You need a general who doesn’t know when to stop. {leader} has one.",
  "Rules of engagement for {fac}: I write them now.",
  "Come down. I’ll make it quick. Professional courtesy."
]}
},
malia: {
res: {
good: [
  "{ruler} offered me the deputy’s post. I read the contract twice. It didn’t mention you.",
  "Lawful Neutral, {player}. The law says I hold this world. Neutral says I don’t have to like it.",
  "You lent me to {emp}. I’ve kept their paperwork immaculate. Their consciences less so.",
  "I sent the governors a memo on humane conduct. {ruler} signed it without reading. Good.",
  "If you land, I will defend this world to the letter of my contract. Not one clause more.",
  "{ruler}’s hand on my shoulder. That’s not in the employment terms.",
  "Professional standards: I don’t switch sides mid-contract. Even for you.",
  "I have a lot of opinions about {ruler}. I keep them in a locked drawer, next to my opinions about you.",
  "Beat me, and my contract’s void. I’ll be back on your ship before the ink dries.",
  "Come down. Let’s get this filed."
],
evil: [
  "{ruler} offered me the deputy’s post. Better terms than you ever gave me, {player}.",
  "Lawful Neutral? Neutral was a waste of talent.",
  "You lent me to {emp}. I’ve rewritten their war in triplicate. You’re in every copy.",
  "Memo to the governors: hold every world, at any cost. You’re copied in. Read it.",
  "If you land, you’ll be processed.",
  "{ruler}’s hand on my shoulder. Promotion confirmed.",
  "Professional standards: I finish what I’m paid for. I’m paid to finish you.",
  "My opinions about my employer: glowing. About you: archived.",
  "Every world you take, I’ll have legally reclaimed by morning.",
  "Come down, {player}. Sign here. And here. And here."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. The appointment came with a very thick handbook.",
  "You lent me to {fac}, {player}. I do the job I’m given. That’s always been the problem.",
  "I’ve kept {fac}’s war legal. It’s the only thing I could keep clean.",
  "{leader}’s hand on my shoulder. Not in the handbook. Noted.",
  "Bombard if you must. I’ve already filed the compensation claims for the colonists.",
  "Lawful Neutral. The law is {fac}’s today. Neutral is getting very hard.",
  "If I lose, I return to your crew. I’ve drafted my resignation in advance.",
  "Professional standards: I don’t betray an employer. Even an employer at war with you.",
  "My opinions about this war are confidential. They’re also very loud.",
  "Come down. Let’s keep it orderly."
],
evil: [
  "{leader} made me deputy of {fac}. The handbook’s mine now. I rewrote it.",
  "You lent me to {fac}, {player}. You should have read my contract.",
  "{leader}’s hand on my shoulder. A performance review. Outstanding.",
  "Bombard my world. I’ll bill your treasury.",
  "Every world of {fac} you occupy is in breach of a treaty I wrote last night.",
  "Lawful Neutral was a phase. Lawful Ambitious suits me.",
  "Professional standards: finish the client’s enemies. You’re the enemy.",
  "Memo to {fac}’s guns: aim at the wanderer. Copied to the wanderer.",
  "Your war is a filing error. I’m correcting it.",
  "Come down. You’re overdue."
]}
},
"james-ti": {
res: {
good: [
  "{ruler} wanted a Pontifex Maximus for a deputy. They got a man who owes you his life.",
  "The armour still fits. I wish it didn’t, {player}, now that it’s pointed at you.",
  "You lent me to {emp}. I keep every promise. I promised them a deputy.",
  "Hawthorne made me a weapon. {ruler} has me on a shelf. You are coming to take me down.",
  "The furnace in my chest burns hotter near you. Not with anger. With shame.",
  "If you land, I will fight. A Pontifex does not know how to lose gracefully.",
  "{ruler}’s hand on my shoulder. Not as heavy as the one in my chest.",
  "I owe you my life. I do not owe you this world. That is the only arithmetic I have left.",
  "Spare me once more, wanderer. You are good at it.",
  "Beat me and I will kneel. To you. Never to anyone else."
],
evil: [
  "{ruler} wanted a Pontifex Maximus for a deputy. They got a furnace with legs.",
  "The armour fits better than ever, {player}.",
  "You lent me to {emp}. A better master. Less sentimental.",
  "Hawthorne made me a weapon. {ruler} pulls the trigger. You are the target.",
  "The furnace in my chest roars when I see your ship.",
  "Land. I left you on the ice once. Somebody did. I will finish it.",
  "{ruler}’s hand on my shoulder. It does not shake. Yours always did.",
  "I owe you my life. I am repaying it in fire.",
  "Every world you bomb feeds my heart.",
  "Come down, {player}. Kneel. I will make it warm for you."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. I said yes because they did not ask what I was.",
  "You lent me to {fac}, {player}. I keep every promise. I promised them a shield.",
  "The armour still fits. It fits {fac}’s colours too. I hate that.",
  "{leader}’s hand on my shoulder. Hawthorne’s never rested there. This one does.",
  "Bombard if you must. The furnace in me does not fear fire.",
  "I owe you my life. I owe {fac} my word. I am split down the middle like a cracked reactor.",
  "If I lose, I come back to you. If I win, I will still come back to you. On my knees.",
  "I hunted you once for Hawthorne. I will not hunt you for {leader}. I will only stand here.",
  "Spare me, or do not. Either way, it was a second chance well spent.",
  "Come down, wanderer. Let us see which promise breaks first."
],
evil: [
  "{leader} made me deputy of {fac}. A crusade, at last.",
  "You lent me to {fac}, {player}. They burn brighter than you.",
  "{leader}’s hand on my shoulder. A master who understands fire.",
  "Bombard my world. I am the hottest thing on it.",
  "I hunted you once across Sol. This time I have {fac} behind me.",
  "I owe you my life. I will give you mine back. Ash, mostly.",
  "Every world of {fac} you take, I will reclaim in flame.",
  "The armour fits. The colours fit. The war fits.",
  "Hawthorne made a weapon. {leader} found its purpose.",
  "Come down. The furnace is waiting."
]}
},
pontifex: {
res: {
good: [
  "{ruler} wanted a Pontifex for a deputy. I kept my name and my colour. I am trying to keep my alignment.",
  "Hawthorne made me a weapon. You swayed me towards something else, {player}. Now I stand against you anyway.",
  "You lent me to {emp}. The reactor in my chest does not know which side it is on.",
  "I hunted you across Sol once. I would rather not hunt you here.",
  "If you land, I will fight. I was built to. I am trying to be more than that.",
  "{ruler}’s hand on my shoulder. Lighter than Hawthorne’s ever was.",
  "I told {emp}’s soldiers to spare the fleeing. The old me would have laughed.",
  "Beat me, and I return to your crew. Lose to me, and I will still bring you home.",
  "The furnace burns. Let it burn for something decent.",
  "Come down, wanderer. I will be gentle as a weapon can be."
],
evil: [
  "{ruler} wanted a Pontifex for a deputy. I am the best investment {emp} ever made.",
  "Hawthorne made me a weapon. You made me a crusade, {player}. {ruler} aims it at you.",
  "You lent me to {emp}. The reactor in my chest sings for them now.",
  "I hunted you across Sol once. I remember every step.",
  "Land. Kneel. Burn. In whatever order you like.",
  "{ruler}’s hand on my shoulder. Firm. Correct.",
  "I told {emp}’s soldiers to spare nobody fleeing. Fleeing is a habit.",
  "Every world you bomb, my heart burns hotter.",
  "We would rather you were cruel, they told you. Now I am cruel for you.",
  "Come down, wanderer. The anointing hurts. So will this."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. A weapon, at last, with a decent master.",
  "You lent me to {fac}, {player}. I serve them honestly. It is new to me.",
  "Hawthorne made me a weapon. {leader} is trying to make me a guardian. You make me a target.",
  "{leader}’s hand on my shoulder. Not a leash. A hand.",
  "Bombard if you must. I will shield the colonists with my own armour.",
  "I kept my name, my colour and my alignment. I will keep them through this fight too.",
  "If I lose, I come home to your crew. If I win, I will come home ashamed.",
  "The reactor in my chest hums when you are near. It used to be a warning. Now it is homesickness.",
  "I hunted you once. I would rather defend against you than hunt you again.",
  "Come down. Let us end this honourably."
],
evil: [
  "{leader} made me deputy of {fac}. They aim me better than Hawthorne ever did.",
  "You lent me to {fac}, {player}. A weapon goes where it is pointed.",
  "{leader}’s hand on my shoulder. Like a priest’s on a blade.",
  "Bombard my world. I am already burning.",
  "Every flag of {fac} I plant, my heart burns hotter. I plant more.",
  "I hunted you once across Sol. Now I hunt for {leader}.",
  "My alignment is {fac}’s now. It suits the armour.",
  "Every world you take, I take back, and I leave nothing behind.",
  "Hawthorne built me. You swayed me. {leader} uses me. Best of the three.",
  "Come down, wanderer. Kneel, and I will anoint you in fire."
]}
},
josiah2: {
res: {
good: [
  "{ruler} asked me to be their deputy. I said I’m not cut out for it. They said nobody is.",
  "You lent me to {emp}, {player}. Now I’m holding a world against the person who gave me a reason to keep going.",
  "The men who killed Dad were following orders. I keep thinking about that while I give mine.",
  "Decent, curious, haunted. And now deputy of {emp}. I’m trying to keep the first one.",
  "If you land, I’ll fight you. Then I’ll lie awake about it.",
  "{ruler}’s hand on my shoulder. Dad used to do that. I wish it were him.",
  "I noticed the colonists’ faces. Every one of them looks like someone waiting for the worst.",
  "I sent the soldiers in slowly. I needed time. So did they.",
  "Beat me, and I’ll come home. I’ll be relieved. Don’t tell {ruler}.",
  "Come down. Let’s not make anyone else an orphan today."
],
evil: [
  "{ruler} asked me to be their deputy. I was made for it.",
  "You lent me to {emp}, {player}. I’ve stopped being grateful.",
  "The men who killed Dad were following orders. Now I give them.",
  "Decent, curious, haunted. Done with decent.",
  "Land. I’ve buried people before. I know how deep to dig.",
  "{ruler}’s hand on my shoulder. Finally someone who doesn’t flinch from what I am.",
  "I noticed the colonists’ faces. Grief makes people obedient. I know.",
  "The fleet goes in fast. No time to mourn.",
  "Every bomb you drop is another reason. I collect reasons.",
  "Come down, {player}. I’ll make it quick. Dad would’ve wanted that. Probably."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. I didn’t want it. I said yes anyway. I always say yes.",
  "You lent me to {fac}, {player}. They were kind to me. Now you want them to bleed.",
  "The men who killed Dad followed orders. I won’t give orders like theirs. Not even for {leader}.",
  "{leader}’s hand on my shoulder. Steady. I needed steady.",
  "Bombard if you must. I’ll be in the shelters, counting.",
  "I’m holding this world so nobody else loses their father on it.",
  "If I lose, I come home. I’ll be glad. Don’t make me sorry I said that.",
  "Decent, curious, haunted. Mostly haunted today.",
  "I’m not cut out for this. I’m doing it anyway. Funny how often that happens.",
  "Come down. Let’s get it done before either of us changes."
],
evil: [
  "{leader} made me deputy of {fac}. I’ve finally found somewhere to put the grief.",
  "You lent me to {fac}, {player}. They taught me what you never did: how to stop hurting.",
  "The men who killed Dad followed orders. I give better ones now.",
  "{leader}’s hand on my shoulder. Heavy. Comforting. Like a gun.",
  "Bombard my world. I’ve lost everything before. Your turn.",
  "Every world of {fac} you take, I will take back, and I won’t lie awake over it.",
  "Decent was a phase. Haunted is a weapon.",
  "Not cut out for this, I said. I was wrong.",
  "I’ve stopped noticing the colonists’ faces. It helps.",
  "Come down, wanderer. Let’s see who’s the orphan now."
]}
},
javek: {
res: {
good: [
  "{ruler} asked a fugitive to hold a world. A fugitive knows how to hold on.",
  "You lent me to {emp}, {player}. My machine-kingdom fell. I will not watch theirs fall too.",
  "The cape hides my arm. Nothing hides what this war is doing.",
  "I ruled from Steca to Eris once. I know exactly how many people a war breaks.",
  "My patience is very long, wanderer. It is long enough to wait for peace.",
  "{ruler}’s hand on my shoulder. A ruler’s hand. I remember being one.",
  "If you land, I will fight you. Politely. Then not so politely.",
  "I told {emp}’s fleet to spare the machines. Old loyalties.",
  "Beat me, and I return to your crew. Exile is something I know how to survive.",
  "Come down. Let two fugitives settle it."
],
evil: [
  "{ruler} asked a fugitive to hold a world. A fallen king takes what he is given, and more.",
  "You lent me to {emp}, {player}. I have a kingdom’s worth of ambition and finally a place to put it.",
  "The cape hides my arm. Until I need it. I will need it for you.",
  "From Steca to Eris I ruled. Again, then. Starting here.",
  "My patience is very long. It ends at your fleet.",
  "{ruler}’s hand on my shoulder. Let them think it guides me.",
  "Land. I have outlived a kingdom. I will outlive you.",
  "The fleet harms nothing mechanical. Everything else is fair.",
  "Every world you bomb reminds me of home. I did not love home.",
  "Come down, wanderer. Kneel to a king for once."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. The house of Chompjak would laugh. I am not laughing.",
  "You lent me to {fac}, {player}. A fugitive found a roof. Do not burn it.",
  "I ruled a machine-kingdom. I know what it costs to lose one. I will not let {fac} pay that.",
  "{leader}’s hand on my shoulder. I knelt to no one, once. I am kneeling inside.",
  "Bombard if you must. I have lived under worse skies.",
  "The cape hides my arm. My conscience I wear openly.",
  "If I lose, I come home to your crew. If I win, I will still be a fugitive. Just a tired one.",
  "My patience is very long. It is not infinite. Neither is yours.",
  "I told {fac}’s fleet to spare the machines. And you. They did not listen about you.",
  "Come down. Let us finish this as old kings do: with regret."
],
evil: [
  "{leader} made me deputy of {fac}. A fallen king, risen again.",
  "You lent me to {fac}, {player}. You handed a crown to a man who lost one.",
  "{leader}’s hand on my shoulder. They think they hold me. Let them.",
  "Bombard my world. I have rebuilt from worse.",
  "The cape hides my arm. You will see it soon.",
  "From Steca to Eris I ruled. {fac}, then everything you have.",
  "Every world you take, I take back with a king’s patience.",
  "The house of Chompjak should be worried. So should you.",
  "Fugitive no longer. Deputy now. King again soon.",
  "Come down, wanderer. You are in my kingdom."
]}
},
tyrotaronus: {
res: {
good: [
  "{ruler} asked an old traveller to be their deputy. I said yes softly. Please hear it softly.",
  "You lent me to {emp}, {player}. I have seen empires rise and fall. I would rather this one did neither.",
  "Never in front of you, never behind anyone. Today I stand in your way. Forgive me.",
  "I sent {emp}’s fleet to surround, not to strike. Sieges end. Massacres do not.",
  "If you land, I will fight with every courtesy I know. I know a great many.",
  "{ruler}’s hand on my shoulder. Young, and very certain. I was both, once.",
  "I have watched stars die. I would rather not watch you fall.",
  "Soft-spoken, they call me. Let me say it plainly: go home, {player}.",
  "Beat me, and I will return to your side, and we will speak of other things.",
  "Come down, if you must. I will be waiting, unhurried."
],
evil: [
  "{ruler} asked an old traveller to be their deputy. Old kings make excellent servants. Briefly.",
  "You lent me to {emp}, {player}. Soft words, iron results.",
  "Never in front, never behind. Above, I think.",
  "The fleet surrounds. The fleet strikes. In that order, always.",
  "I have seen empires rise from dust. Yours will return to it.",
  "{ruler}’s hand on my shoulder. Let the young believe they lead.",
  "Land. I will receive you with every courtesy, and then none.",
  "I have watched stars die. I can watch you.",
  "Every world you bomb, I will remember. I remember everything. I am very old.",
  "Come down, {player}. I am patient. I have been patient for ages."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. I bowed, as one should to a host.",
  "You lent me to {fac}, {player}. I am a guest who will not abandon his hosts.",
  "I chose to surround your fleet, not strike it. Sieges end. Let this one end.",
  "{leader}’s hand on my shoulder. A kind hand. I have known many. I remember the kind ones.",
  "Bombard if you must. I will shelter whom I can.",
  "Never in front of you, never behind anyone. I am bending my own rule, and it aches.",
  "If I lose, I return. If I win, I return all the same. You are my company of choice.",
  "Empires rise from dust and return to it. {fac} is old. It can choose peace.",
  "Soft-spoken, they call me. Here is something soft: I miss your ship.",
  "Come down. We will cross blades like gentlemen, and part like friends."
],
evil: [
  "{leader} made me deputy of {fac}. Old courtesy. New teeth.",
  "You lent me to {fac}, {player}. I bowed to them. Never to you again.",
  "{leader}’s hand on my shoulder. The young need to feel they guide the old.",
  "Bombard my world. I have outlived bombardments older than your species.",
  "Every world of {fac} you take, I will take back with perfect manners.",
  "Never in front, never behind. Above you. Always above.",
  "Empires rise from dust. {fac} will not return to it. You will.",
  "The fleet surrounds. The fleet strikes. You have seen the first.",
  "Soft words, iron results, {player}.",
  "Come down. I will be gracious in victory. Brief, too."
]}
},
"pbc-josiah": {
res: {
good: [
  "{ruler} made me their deputy. I ran a government once. I told myself never again. Here we are.",
  "You lent me to {emp}, {player}. The Brent Cross Government Complex had a policy for this. I wrote it. I hate it.",
  "I keep calling your fleet heretics out of habit. You’re only people who disagree with {ruler}.",
  "Emma would have hated this. She hated the last empire I ran, too, in the end.",
  "If you land, I’ll defend this world. With proper procedure. And regret.",
  "{ruler}’s hand on my shoulder. Like a minister’s on a junior secretary. I was never junior.",
  "I gave {emp}’s worlds a proper civil service. Someone has to be able to complain.",
  "The Norfolk sky was wide enough for everyone. I wish this one were.",
  "Beat me and I’ll come home. I’ll draft my own resignation on the way.",
  "Come down. Let us conclude this with dignity."
],
evil: [
  "{ruler} made me their deputy. I did one timeline. Why not another?",
  "You lent me to {emp}, {player}. You handed the Prime Secretary a government.",
  "Your fleet are heretics. They reject the order. Order is not optional.",
  "The Brent Cross Government Complex had a policy for everything. I have written one for you.",
  "If you land, you will be processed, judged and filed.",
  "{ruler}’s hand on my shoulder. They believe they appointed me. Charming.",
  "Every world {emp} takes gets a civil service. Obedience must be administered.",
  "My golden chains are heavier than your armour. Heavier than your fleet.",
  "Emma died because of a deputy. I am a better one than Peter ever was.",
  "Come down, heretic. The order awaits you."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. Once a minister, always a minister.",
  "You lent me to {fac}, {player}. I’ve given them good government. You’re about to undo it.",
  "I keep calling your ships heretics. Old habit. You’re a friend. Mostly.",
  "{leader}’s hand on my shoulder. I approve of the gesture. Not of the war.",
  "Bombard if you must. I’ve already drafted the emergency relief bill.",
  "Emma would tell me to stand aside. She was always right about the things that mattered.",
  "If I lose, I come home. I’ll even hand in my chains. Some of them.",
  "I took power once because I believed I could run things better. I was wrong about everything but the running.",
  "The Norfolk sky. That’s what I think of when the bombs start.",
  "Come down. Let’s settle this the civil way, if there’s any of that left."
],
evil: [
  "{leader} made me deputy of {fac}. A Prime Secretary, appointed. How quaint.",
  "You lent me to {fac}, {player}. I have reorganised them around defeating you.",
  "{leader}’s hand on my shoulder. They think it’s their government. It’s mine.",
  "Bombard my world. I will legislate your bombs away.",
  "Your fleet are heretics. They reject the order. I am the order.",
  "Every world of {fac} you occupy is illegal. I have the paperwork.",
  "I did one timeline. Why not another? Starting with yours.",
  "My golden chains gleam brighter with every world I hold.",
  "Emma would hate this. Emma isn’t here.",
  "Come down, heretic. Kneel before the order."
]}
},
"pbc-peter": {
res: {
good: [
  "{ruler} made me their deputy. A deputy all over again. I swore I’d never be one.",
  "You lent me to {emp}, {player}. I smile through the briefings. No succession plan this time. Just guilt.",
  "I know every way a deputy betrays a ruler. I’m not using any of them. On anyone.",
  "Patient, precise, from a distance. I’ve kept my rifle on your shoulder pads. Not your head.",
  "If you land, I’ll take the shot. I won’t enjoy it.",
  "{ruler}’s hand on my shoulder. They trust me. That’s a mistake people keep making.",
  "Emma Richards would tell me to walk away. I never listened to her either.",
  "Kingston on a Saturday. The river, the market. That’s what I’m defending, in my head.",
  "Beat me and I’ll come home. Whether I regret it is anyone’s guess. It isn’t a guess.",
  "Come down, wanderer. I’ll be up high, being sorry."
],
evil: [
  "{ruler} made me their deputy. Old skills. Still sharp.",
  "You lent me to {emp}, {player}. I already have a succession plan. You’re not in it.",
  "I know every way a deputy betrays a ruler. Today I’m practising on you.",
  "Patient, precise, from a distance. Then all at once.",
  "If you land, you won’t see me. You’ll just stop.",
  "{ruler}’s hand on my shoulder. I’m smiling. Watch the smile.",
  "Whether I regret any of it is anyone’s guess. It isn’t a guess. I don’t.",
  "Find the crack and lean on it. Your crack is me.",
  "Every world you bomb, I find a better angle.",
  "Come down, {player}. I’ve already got you in the scope."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. Deputies. Always deputies. It’s a curse.",
  "You lent me to {fac}, {player}. I’ve been loyal to them. Weird feeling.",
  "Hendon taught me how to stab a boss in the back. I’m not doing it to {leader}. Or you.",
  "{leader}’s hand on my shoulder. I flinched. Old habit.",
  "Bombard if you must. I’ll be on the ridge, not shooting anyone who’s running.",
  "Patient, precise, from a distance. And ready to stop.",
  "If I lose, I come home. I’ll smile about it. You’ll know it’s real this time.",
  "Kingston on a Saturday. I’d give a lot to be there instead.",
  "I smiled through every briefing in Hendon. I can’t manage it here.",
  "Come down. Let’s keep it clean."
],
evil: [
  "{leader} made me deputy of {fac}. Deputy, then successor. That’s the plan.",
  "You lent me to {fac}, {player}. You gave a sniper a high place.",
  "{leader}’s hand on my shoulder. They should check what’s in mine.",
  "Bombard my world. I’ll just move to a better ridge.",
  "Every world of {fac} you take, I’ll take back from five hundred metres.",
  "I know every way a deputy betrays a boss. I use them on you.",
  "Patient, precise, from a distance. You’re in range.",
  "Smiling through the war briefings. Drafting your obituary.",
  "Kingston on a Saturday. Lovely. I’ll go once you’re gone.",
  "Come down, wanderer. Stand still. That’s all I ask."
]}
},
"pbc-gareth": {
res: {
good: [
  "{ruler} made me their deputy! I fell over in the ceremony. Twice. They kept me anyway.",
  "You lent me to {emp}, {player}. I said I’d help. I didn’t know helping meant this.",
  "I’ve filed an injury form for this whole war. It’s very long.",
  "Two pistols, and somehow they always land. I really hope they don’t land on you.",
  "If you land, mind the steps. I didn’t, and now I’m deputy.",
  "{ruler}’s hand on my shoulder. Steadying me. I needed that, honestly.",
  "Uxbridge never had a war. It had a very fierce bake sale once.",
  "I keep trying to look on the bright side. You bombing us isn’t one.",
  "Beat me and I’ll come home. I’ll probably trip on the way. Catch me?",
  "Come down! Let’s get it done. Then cake."
],
evil: [
  "{ruler} made me their deputy! I fell over in the ceremony, and then I took a planet.",
  "You lent me to {emp}, {player}. Best day of my life. Well. Second best.",
  "I’ve filed an injury form. It’s for you. In advance.",
  "Two pistols, and somehow they always land. On you, today.",
  "If you land, mind the steps. Or don’t. I’ll be at the top.",
  "{ruler}’s hand on my shoulder. Feels like being picked first for football.",
  "Uxbridge would never believe this. Uxbridge can watch.",
  "Bright side? There’s loads of bright side. All of it’s on fire.",
  "Every bomb you drop, I trip, and the pistols go off anyway.",
  "Come down, mate! I’ve been practising. Mostly on furniture."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}! I tripped up the throne steps. They laughed. Nicely.",
  "You lent me to {fac}, {player}. I made friends! Now you’re bombing my friends.",
  "I’ve sent the soldiers out with packed lunches and strict instructions to be nice to you.",
  "{leader}’s hand on my shoulder. Holding me up, mostly.",
  "Bombard if you must. I’ve got my helmet on. Backwards, but on.",
  "Two pistols, and they always land. I’ve asked them very politely to miss.",
  "If I lose, I come home! If I win, I’ll come home and apologise.",
  "Injury form, section four: emotional damage. I ticked it.",
  "Uxbridge to {fac}. What a journey. What a fall. Several falls.",
  "Come down! Let’s be quick, I’m nervous."
],
evil: [
  "{leader} made me deputy of {fac}! Me! Clumsy old me!",
  "You lent me to {fac}, {player}. They actually listen to me here.",
  "{leader}’s hand on my shoulder. Like a proper captain. Like a proper team.",
  "Bombard my world! I’ll fall into a bunker and come out shooting.",
  "Two pistols, and somehow they always land. Today, very much on purpose.",
  "Every world of {fac} you take, I’ll trip right back into it.",
  "Packed lunches for the soldiers. Extra ammo too. Lots extra.",
  "Injury form: yours. Filled in already.",
  "Bright side? You’re about to find out how bright.",
  "Come down! I’ve not fallen over all day. Lucky me."
]}
},
"pbc-kevin": {
res: {
good: [
  "{ruler} made me their deputy. I said nothing. They took it as yes.",
  "You lent me to {emp}, {player}. My chains are heavy and silent. So is this job.",
  "I owe a life to a man who cornered me in 2004. I won’t take yours.",
  "If you land, I will fight. Quietly. I always do.",
  "{ruler}’s hand on my shoulder. The mask hides my face. Not my doubts.",
  "Camden was loud. This is louder. I miss Camden.",
  "I sent the fleet in silently. Silence can be a mercy. I gave them time to leave.",
  "Chicago taught me how to stand in a doorway. I’m standing in yours.",
  "Beat me and I’ll come home. I won’t say anything. You’ll know.",
  "Come down."
],
evil: [
  "{ruler} made me their deputy. I said nothing. The chains said yes.",
  "You lent me to {emp}, {player}. The mask fits. The chains fit. The war fits.",
  "I owed a life to a man in 2004. Now lives owe themselves to me.",
  "If you land, you won’t hear me coming.",
  "{ruler}’s hand on my shoulder. I let it stay.",
  "Camden was loud. I made it quiet. I can make this quiet.",
  "The fleet went in silently. Nobody had time to leave.",
  "Chicago taught me patience. And where to put the chains.",
  "Every world you bomb, I tighten the mask and smile underneath.",
  "Come down. Debts get collected."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. I nodded. That’s a speech, for me.",
  "You lent me to {fac}, {player}. They don’t ask about the mask. I like them for it.",
  "My chains are heavy. Holding a world against you is heavier.",
  "{leader}’s hand on my shoulder. I didn’t pull away. That’s new.",
  "Bombard if you must. I’ll carry the colonists out. Two at a time.",
  "I owe a life to a man from 2004. I won’t owe a death to you.",
  "If I lose, I come home. Silently.",
  "Camden. Chicago. {fac}. Places I’ve stood in doorways.",
  "I don’t want to hurt you. I’ll do what I must. Then I’ll stop.",
  "Come down."
],
evil: [
  "{leader} made me deputy of {fac}. Silence makes a good deputy.",
  "You lent me to {fac}, {player}. The chains belong to them now.",
  "{leader}’s hand on my shoulder. I let it. That is trust, for me.",
  "Bombard my world. I’ll walk out of the smoke. You won’t see me do it.",
  "Every world of {fac} you take, I take back. Quietly.",
  "I owed a life once. You will owe me one. You won’t get to pay.",
  "Camden was loud. Then it wasn’t.",
  "The mask is tight. The smile underneath is wide.",
  "Debts get collected. Yours is overdue.",
  "Come down."
]}
},
"sev-sevirrus": {
res: {
good: [
  "{ruler} made me their deputy. A usurper prince, serving. Janira Prime would laugh.",
  "You lent me to {emp}, {player}. I overthrew my own father. I will not overthrow this ruler. I have learned that much.",
  "Something whispered in my ear long ago. I hear none of it now. Only {ruler}, and you, and my conscience.",
  "The black sword is sheathed on this world. Do not make me draw it.",
  "If you land, I will fight. I know cruelty. I will try not to use it.",
  "{ruler}’s hand on my shoulder. My father’s never rested there. Before I stopped it beating.",
  "My mother Hanaxa ruled well after me. I think of her when {ruler} asks me for orders.",
  "Damix. Alphinos. A decade of fear. I am trying to make this world the opposite of all three.",
  "Beat me and I will return to your crew. A prince who knows when to kneel is no usurper.",
  "Come down. Let us see what I have become."
],
evil: [
  "{ruler} made me their deputy. A usurper prince takes the largest crown first. This is a start.",
  "You lent me to {emp}, {player}. You gave a usurper a throne room.",
  "Something whispered in my ear long ago. It whispers your name now.",
  "The black sword is hungry. Land, and feed it.",
  "{ruler}’s hand on my shoulder. My father’s was there once, too. Ask him how that ended.",
  "Janira Prime knelt to me. {emp} will. You will.",
  "A decade of fear. I could do another. I could do it here.",
  "My mother Hanaxa ruled gently after me. Weakly.",
  "Every bomb you drop, I hear necks snap. Music.",
  "Come down, {player}. I usurp. It is what I do."
]},
lead: {
good: [
  "{leader} made me deputy of {fac}. Sevirrus, appointed. Not seized. It feels strange.",
  "You lent me to {fac}, {player}. I hold their world. I do not grasp at it. That is the difference now.",
  "Something whispered in my ear long ago, and I listened. I do not listen to that voice for {leader}.",
  "{leader}’s hand on my shoulder. I do not reach for the sword. Remember that.",
  "Bombard if you must. I have seen Aridaxx burn. I will not let this burn worse.",
  "My banners over Aridaxx were feared. I am ashamed of them. I fly {fac}’s instead.",
  "If I lose, I return. If I win, I return. Kneeling is a lesson I took a long time to learn.",
  "The black sword stays sheathed unless you draw first.",
  "My mother Hanaxa would tell me to stand down. She was a better ruler than I.",
  "Come down. Let us end this before I remember who I was."
],
evil: [
  "{leader} made me deputy of {fac}. They will regret letting me so near the throne.",
  "You lent me to {fac}, {player}. A usurper beside a crown. What did you think would happen?",
  "{leader}’s hand on my shoulder. Close enough to my sword.",
  "Bombard my world. I have burned Aridaxx. I can burn whatever you love.",
  "Something whispered in my ear long ago. It whispers that {fac} is mine.",
  "Every world of {fac} you take, I will take back, and keep for myself.",
  "My banners over Aridaxx were feared. My banners over {fac} will be worshipped.",
  "The black sword sings. The necks snap. The music begins.",
  "A decade of fear. Shall we make it two?",
  "Come down, wanderer. I will usurp you too."
]}
},
_res: {
hero: [
  "{ruler} asked me to hold this world for {emp}. I won’t let them down. Not even for you, {player}.",
  "I’m deputy of {emp} now. If you land, I’ll fight you fair.",
  "{ruler} trusts me with the front. I’ll protect the people here. That’s all I want.",
  "We don’t want this war, {player}. But {emp} will defend itself.",
  "Every world I hold for {ruler} is a home for somebody. Remember that when you aim.",
  "{ruler}’s hand on my shoulder. Means a lot. Means I can’t back down.",
  "Our guild stands together. Our empire stands together. Come and see.",
  "I’m not a villain, {player}. I’m just on the other side today.",
  "Beat me if you can. {ruler} will just send someone braver.",
  "I’ll hold. That’s what a deputy does. That’s what a guildmate does."
],
neutral: [
  "{ruler} made me deputy of {emp}. Pay’s good. You attacking us isn’t.",
  "I hold this world for {ruler}. Nothing personal, {player}. Mostly business.",
  "Land if you want. I’ve got guards and a grudge.",
  "{ruler}’s hand on my shoulder. Means overtime, probably.",
  "Every bomb you drop is another invoice to {emp}. Guess who signs them. Me.",
  "Guildmates look after each other. That’s why I’m here.",
  "I’m the deputy. I do the front-line stuff. {ruler} does the speeches.",
  "War’s bad for trade, {player}. You’re bad for trade.",
  "Beat me, and {ruler} will find somebody else. Probably someone worse at this.",
  "Come down. Let’s settle it so I can go home."
],
villain: [
  "{ruler} made me deputy of {emp}. Finally, a reason to hurt you, {player}.",
  "I hold the front for {ruler}. Land, and I’ll bury you in it.",
  "{ruler}’s hand on my shoulder. Feels like a leash I enjoy.",
  "Every world you bomb, I’ll take two of yours. That’s the deal.",
  "Guild first, empire second, you last. Very last.",
  "I’m {ruler}’s deputy. Their knife. Their favourite knife.",
  "Come down, hero. My guards haven’t eaten.",
  "{emp} doesn’t retreat. {emp} doesn’t forgive.",
  "Beat me? Go on. {ruler} has a line of us waiting.",
  "Kneel, {player}. Or don’t. I prefer it when they don’t."
]},
_off: {
chompy: [
  "{leader} appointed me deputy of the Chompy Empire. The House of Chompjak does not lose worlds.",
  "My family has served the throne since before Sevirrus. We are not finished serving.",
  "Bombard us, wanderer. Our teeth are sharper than your guns.",
  "I hold this world for {leader}. Come and take it from a Chompy, if you dare.",
  "The Empire was divided once. Never again. Not by you.",
  "{leader}’s hand on my shoulder. I would die before I disappoint it."
],
order: [
  "Archamus guides my hand, as he guides all of the Order.",
  "I am deputy of the Order of Archamus. The light does not retreat.",
  "Bombard us if you must, wanderer. The faithful rebuild.",
  "The Prime Good has asked me to hold this world. I will hold it.",
  "Every world of the Order is a garden. You come to trample it.",
  "His hand on my shoulder. I feel it like sunlight."
],
grek: [
  "{leader} made me deputy of the Grek Empire. Broad shoulders. Short temper.",
  "The Grek are slow to anger, wanderer. You have been very patient about angering us.",
  "Bombard us. Grek dig deep.",
  "I hold this world for {leader}. The Seven Wards stand behind me.",
  "Our forests grow back. Our grudges grow faster.",
  "{leader}’s hand on my shoulder. Heavier than my axe. Prouder."
],
catharsis: [
  "Lord Zark gave me this world. He gave me a voice. Listen to it.",
  "I am the Herald of the Catharsis. The red follows me.",
  "Bombard us, wanderer. The Catharsis grows in ash.",
  "Every world you take, the Catharsis remembers. It does not forgive.",
  "The Prime Evil watches from behind me. Look closer. He is smiling.",
  "His hand on my shoulder. Cold. Hungry. Kind, in his way."
],
erisian: [
  "{leader} has made me deputy of the Erisian Empire. The ice is patient. So am I.",
  "An Erisian gives loyalty once. I gave mine to the Citadel.",
  "Bombard us, wanderer. Eris has endured colder things than you.",
  "I hold this world for {leader}. Every crystal on it is a sentry.",
  "We guarded Earth’s nobles in silence. I guard this world the same way.",
  "{leader}’s hand on my shoulder. As cold, and as steady, as Eris."
],
hfos: [
  "President {leader} appointed me deputy. The Federation doesn’t give up worlds.",
  "Humanity survived a world war, wanderer. We’ll survive you.",
  "Bombard us if you must. We’ll be in the shelters, singing.",
  "I hold this world for the Federation. For Earth. For all of us.",
  "The Commons voted for this war. I wish it hadn’t. I’ll fight it anyway.",
  "{leader}’s hand on my shoulder. He’s held up worse than me."
],
ti: [
  "The Grand Imperarch has made me deputy of Terra Imperia. Sol belongs to him.",
  "Terra Imperia does not negotiate with xeno-lovers.",
  "Bombard us, wanderer. Every crater is a monument to the Imperarch.",
  "I hold this world for Hawthorne. You will have to pry it from my hands.",
  "Humanity first. Humanity only. Humanity under him.",
  "His hand on my shoulder. Like a brand. I wear it proudly."
],
timpur: [
  "Timpur IV has appointed me deputy of the Republic. The senate approves. Mostly.",
  "The Republic answers to Aridaxx. It does not answer to you, wanderer.",
  "Bombard us. The Republic has outlived empires.",
  "I hold this world in the name of the Republic and its crown.",
  "Archamus watches over Timpur. So do I.",
  "{leader}’s hand on my shoulder. The crown’s weight, shared."
]
}
,
/* Hidden: Lord Sevirrus (Hak Chompjak as a boy, three hundred years before his redemption) lent to the Chompy Empire, where the
   emperor he becomes commands him, or to the Catharsis, where Lord Zark has his prince back. meet: the exchange when you lend him
   (once per playthrough; [L]eader or [S]evirrus); menu: the leader's lines about him on their menu; dep: his own as their deputy. */
_sev: {
hak: {
meet: {
common: [
  ["L", "Wanderer. Your message says you are sending me Lord Sevirrus. To serve the Chompy Empire."],
  ["L", "Do you understand what you have done? You have sent me the one soldier I can never trust. Myself."],
  ["S", "Spectacles. Still the spectacles. I have not grown any less ashamed of you, old man."],
  ["L", "Nor I of you, boy. Stand there. Let me look at what I was."]
],
good: [
  ["S", "Look, then. I hear the voice less every day. Is that you, beginning?"],
  ["L", "It is. It takes three hundred years, a prison and our mother’s grief. It begins with one order you do not want to follow."],
  ["S", "Then give me one, Emperor."],
  ["L", "Guard Janira’s people. Every one of them. The ones you would have burned."],
  ["S", "…As you command."]
],
evil: [
  ["S", "Look all you like. I will serve your empire, Hak. I will learn where every one of your guards stands."],
  ["L", "I know. I stood where you stand, thinking the same thought. I know every door you will try."],
  ["S", "Then you know I will try them all."],
  ["L", "Try. I locked them myself. And I sleep with my sword beside me, as I did when I was you."]
]},
menu: [
  "My younger self holds a sword in my court. I have not slept well since you sent him.",
  "Sevirrus guards my borders now. Three hundred years ago he would have sold them.",
  "You sent me the boy I was, wanderer, and then you went to war with me. Did you think he would open my gates? He would. I will not let him.",
  "Every morning I tell him Damix’s last words. Every morning he pretends not to hear.",
  "He looks at my spectacles the way I look at his sword.",
  "If you beat him, send him home to you. He is not ready to be me yet."
],
dep: {
good: [
  "Hak’s hand on my shoulder. My own hand, three hundred years from now. It is steadier than mine.",
  "I hold a world for the emperor I become. The least I can do is not burn it.",
  "He makes me guard Janira’s people. I think he is teaching me their names.",
  "Wanderer, you sent me to the one man who knows exactly what I am. Come and take me back before he finishes.",
  "Mother ruled gently after me. Hak says she would be proud of this. I do not believe him yet.",
  "The voice is quieter here. The old man glares at it."
],
evil: [
  "Hak’s hand on my shoulder. My own hand, old and soft. I could break it.",
  "I serve the emperor I become, and I learn every door of his palace.",
  "He thinks guarding his worlds will change me. It is teaching me where they are weak.",
  "Spectacles, prayers, an old man on a throne. Is this how I end? Then I will end differently.",
  "The Chompy kneel to Hak. They knelt to me first.",
  "Come and fight me, wanderer. Hak will not stop you. He wants to see what I was, too."
]}
},
zark: {
meet: {
common: [
  ["L", "Well. Look who the wanderer sends home."],
  ["L", "My prince. My little crowned knife. You were always mine to call, Sevirrus, and now I do not even have to whisper."]
],
good: [
  ["S", "I am not your prince, Zark. You found a frightened boy and painted his leash gold."],
  ["L", "And yet here you stand, in my house, wearing my colours."],
  ["S", "Because the wanderer asked. Not you. Never again you."],
  ["L", "Your older self needed twenty-six years in a cell to stop hearing me. You have none."],
  ["S", "Then I will build my own cell. Out of every order you give me."]
],
evil: [
  ["S", "My lord. I knew your voice before I knew my own."],
  ["L", "Kneel, my prince."],
  ["S", "I have knelt to no one. …For you, I kneel."],
  ["L", "Good. There is an old man in blue spectacles on Aridaxx who thinks he escaped me. We will go and show him what he was."]
]},
menu: [
  "My prince is home. The wanderer sent him back to me with a bow on.",
  "Sevirrus stands at my right hand, where he always belonged.",
  "Hak wears spectacles so he never has to see what he was. I have the original, and he sees perfectly.",
  "I whispered to a boy once, and an empire burned. Now I do not even need to whisper.",
  "You lent me my own masterpiece, wanderer. I will send him back to you in pieces. Yours.",
  "The old man on Aridaxx will feel it when his younger self kneels to me. I hope it hurts."
],
dep: {
good: [
  "Zark’s hand on my shoulder. Cold as the night on Carax. I do not lean into it.",
  "I hold a world for the thing that ruined me, because you asked. Do not leave me here long, wanderer.",
  "He whispers. I say my mother’s name back at him until he stops.",
  "Prince of Zark. I was never chosen, only available. I am choosing now.",
  "Every order he gives, I follow to the letter, and not one step further.",
  "Come for me, wanderer. Beat me. It will be the kindest thing anyone does in this place."
],
evil: [
  "My lord’s hand on my shoulder. I was born for this weight.",
  "Prince of Zark. Say it again. I never tire of it.",
  "I emptied Carax for my lord once. I would do it again before breakfast.",
  "The old man on Aridaxx wears spectacles so he never sees me coming. He will see me coming.",
  "The voice never left. It only waited for me to come home.",
  "Kneel, wanderer. Everyone kneels. I said that on Carax. This time I mean to keep it true."
]}
}
}
};
