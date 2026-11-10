# NOSTRAVECTOR Remastered

*Exploration Division*

A story-driven 3D sci-fi exploration game that runs in the browser on phones and desktops. It's set in **2125 AD**.

## Play

Open `index.html` in a modern browser, keeping the `data/` folder next to it. It needs an internet connection the first time, because the 3D engine (Three.js) and the fonts load from public CDNs. Everything else is in `data/`: the models, music and voice lines, one script file per asset. These are plain `<script>` files rather than fetched files, so the game still runs when you double-click `index.html` (file://) with no web server.

**itch.io:** zip `index.html` together with the `data/` folder and upload the zip as an HTML game. `index.html` must sit at the top of the zip.

## What's in the game

- **Main menu** with the wandering astronaut, Continue, New Game, Wanderers, Mission Brief and Settings.
- **Up to 100 wanderers** per save (the Wanderers screen shows how many you have, e.g. 99/100).
- **Saves without limits:** saves are stored in the browser's database (IndexedDB), which has room for hundreds of megabytes, so big rosters and long playthroughs always save. A quick copy is also kept in localStorage while it fits, so the game starts instantly; once saves outgrow it, the game reads them from the database. The game asks the browser to keep its storage permanently. Export/Import include everything. Only a browser that blocks storage entirely (some private-browsing modes) can't save, and the game says so.
- **Editing a wanderer** (Wanderers → Edit active) changes their name, identity and looks, but not their species: that is chosen once, when the playthrough begins. Start a new game to play another species.
- **Residents: sending a wanderer into the world** (Wanderers → Send into the world, tap twice): that wanderer leaves your playable list for good and lives on in the same save as a "player", like an MMO with bots instead of real people.
  - **Never playable again:** they can't be recruited, controlled or switched to. They stay on the Wanderers screen, greyed out, with where they were last seen. At least one wanderer always stays playable.
  - **Where they turn up:** in Chapters I–II, on Earth, coming and going every few minutes. From Chapter III they travel the galaxy on their own: a few minutes on one world, then a warp to the next (home, a major system, or somewhere nearby). It's a fixed schedule worked out from the clock, so the ground, space and the galaxy map always agree.
  - **Tracking them:** on the galaxy map, each resident is a marker (blue hero, white neutral, red villain) with their level and where they are; while warping, a dashed line shows the jump. **RESIDENTS** jumps to each in turn, and a system's panel lists who's there or arriving.
  - **Death and respawn:** if a resident's ship goes down (shot down as a villain, or taking too much fire helping you), they respawn on their species' home planet a minute and a half later: Earth (Human), Aridaxx (Chompy), Eris (Erisian), Malana (Grek), and set off again from there.
  - **Levels:** they keep levelling while you're away (about a level every half hour) up to **110**, past the player's cap of 100.
  - **On the ground (on-device AI):** each resident chooses what to do from what's around them: mining deposits, visiting stalls, wandering, jetpack hops, emotes (wave, dance, cheer), coming over to you, following you for a while. Heroes may hand you a few materials; villains taunt you and grab deposits near you. They never fight you on the ground.
  - **Two or more together:** they decide things between them: chat, trade, spar, race, dance, explore together, or (a hero and a villain) argue. Three or more sometimes gather as a group.
  - **Dialogue:** over 1,600 lines in `data/resLines.js` (loaded only when a save has residents): everyday lines by alignment, species, exploration (by world type and for named worlds), Chapters I–V, bosses and leaders, your own Diplomacy wars (at war, conquests, puppets, tributaries, colonies, resistance, peace), conversations between two residents, and talk topics. They pick lines to fit where you are, your chapter and your wars.
  - **Talking to them:** walk up and press E / tap WAVE: what they're up to, this place, tips, how the war is going (Chapter III on), buy a few materials (not from villains), **Real life…**, or bye.
  - **Ask something…:** type anything (the phone keyboard works too). They work out what you mean from words they know: places, leaders and bosses, species, the war, tips (matched to what you asked), trading, who they are, how you're feeling, real-world jobs. If they can't make sense of it, they're confused in their own voice (a hero apologises, a neutral says "huh?", a villain sneers) and suggest what to ask instead. Anything about not being safe always goes straight to the support conversation, never to confusion.
  - **Not knowing:** sometimes they just don't have an answer, more often at low level and right after arriving somewhere. They may not know a world you ask about ("never been to Ossian"), or answer a question with "honestly no clue, I just got here".
  - **Resident empires (Chapter III on):** residents found empires on unclaimed worlds once they reach level 35 (villains first, heroes last), expand nearby, and go to war with each other using the same casus belli you have (Annihilation, Subjugation, Vassalisation, Tribute, Restoration). They **never attack the story factions** or your colonies. Wars play out over time; outcomes match the casus belli (worlds change hands, puppets, tributaries, resistances, restorations).
    - **You choose:** stay neutral, **set one empire on another** (pick the target and casus belli, or let them choose), **broker peace**, or **demand an empire disbands** (they comply, grudgingly if they're villains, and won't found another for a while).
    - **Where:** Pause → **Resident empires**, the galaxy map's **EMPIRES** button, or "About your empire…" when talking to a ruler. Their worlds are ringed in their colours on the galaxy map, with the empire's name at its capital; a system's panel says who claims it.
    - **Trash talk:** declarations, fights, victories and defeats come with matchup-specific lines (hero vs hero, villain vs villain, neutral vs neutral, hero vs neutral, neutral vs villain, hero vs villain), about 350 in `data/resWar.js`, marked ⚔ in the zone chat. Rulers at war who meet fight on the ground, or dogfight in space (where one can be shot down and respawn at home).
    - **Swearing:** their fights include swearing; switch it off in the Resident empires panel ("Swearing in their fights") and it's blanked out (#@!%).
  - **Text only:** residents never speak aloud. Everything they say is written (chat, speech bubbles and the dialogue box), with no voice acting or typing sounds.
  - **Personality:** when you send a wanderer into the world you describe who they are in your own words (or tap ideas: shy, funny, grumpy, loves building, talks like a pirate, a catchphrase in quotes...). Tap a resident on the Wanderers screen to edit it later. The on-device AI reads it for traits, loves and a speaking style, which then shape how they write everything they say ("me arms hurt — by the stars"), tilt what they choose to do (a builder builds, a shy one keeps their distance, a lazy one idles), and shape their reactions.
  - **Roleplay… (safe for work):** wave, hug, high five, dance together, sit and chat, share food, tell a joke, compliment, tease, spar for fun, walk together, ask about their day, or *Do something else…* and type your own action ("offer them a flower"). They answer in character, by personality and alignment. Anything not safe for work gets a friendly in-character refusal.
  - **Bases:** residents build bases of their own (up to three, one per world): a camp, then a house, then a fortress with a tower and a flag in their empire's colours (blue-trimmed wood for heroes, stone for neutrals, black and red for villains). Bases stay put when their owner is away, are labelled ("Vex's fortress"), are solid to walk into, keep well clear of the station, your ship, stalls, towns and cities, and are saved with the slot.
  - **Real life… (out of character, villains too):**
    - *I'm stressed out:* they listen, reflect what you're dealing with (work, school, relationships, money, health, loneliness, everything at once, something else), and offer simple, widely used techniques: box breathing, 5-4-3-2-1 grounding, small things to try, sleep and worry tips, and who to talk to. They check in afterwards. They say plainly that they're a game character, not a therapist.
    - *I'm not safe right now:* they urge you to contact your local emergency services or speak to a crisis line (free, confidential, any time). No phone numbers are shown in game, so it stays immersive.
    - *Job advice:* general tips on finding a job, CVs, interviews, changing career, asking for a raise, burnout, trouble at work, starting out and losing a job, with a reminder to get advice for your own situation.
  - **In space (Chapter III on):** their ships fly around your system. Heroes and neutrals join your fights; a villain may eventually turn on you (space only).
  - **What you see:** nameplates (name, level, species, coloured by alignment), speech bubbles, and a small zone chat (bottom left; on phones above the controls, or under the objectives when held sideways; in space under the objective).
  - **Safe for the story:** they only appear in free roam: never in cutscenes, dialogue close-ups, New London, the station, nightmares or Chapter I's opening storm. They don't collide with you or touch your world or saves. Phones show up to 3 at once (without shadows), other screens up to 6.
  - **Preview:** add `?residents=all` to the address to bring every resident to where you are.
- **Opening:** a flight through the Milky Way to Earth, with five narrated quotes.
- **Character creator:** you choose callsign, species, gender, skin, hair, beard, and suit or armour colours.
- **Four playable species:**
  - **Human:** from Earth, which survived the Third World War 30 years ago and has only recently entered spaceflight.
  - **Erisian:** from the dwarf planet Eris. They travel to Earth as merchants or as bodyguards to human nobles.
  - **Chompy:** from Janira Prime and Aridaxx. They're long-lived, and some remember Sevirrus's fracturing of their empire 300 years ago. Today they're loyal to Emperor Hak Chompjak V.
  - **Grek:** from the garden space station Archiostal, guided by their god Archamus.
- **Multiple wanderers:** create several characters, switch between them at any time, and each one tracks its own chapter progress.
- **Manual save / load:** three slots, and nothing is saved unless you choose to.
- **Prologue:** a hypothermic collapse on the Antarctic ice and a rescue by James Brown, with his lines voiced.
- **Chapter I · Antarctica:** explore the research station. Objectives:
  1. Speak to James Brown (voiced).
  2. Inspect the station: the bunk, heater, window, radio and outer hatch.
  3. Sleep in the bunk.
- **The dream:** after you sleep, the leader of your species appears and speaks to you in a voiced, unnamed monologue.
- **The wake-up:** you wake to find the outer hatch open and James Brown gone. The new objective is to find him.
- **Procedural Antarctica:** step outside into endless, procedurally generated terrain in the style of No Man's Sky: snowfields, wind-cut ridges, rocky cliffs, frozen lakes, rock outcrops and ice spires, all under a blizzard. Each wanderer has their own world seed. James's footprints lead away from the station; fresh patches of prints and his lantern glow lead you to him about 400 m out (objectives: Find James Brown → Speak to James Brown). Hold Shift (or push the stick fully) to run.
- **Make camp:** once James joins you, the next objective is to set up a camp with him: build a **crafting table** (+60 XP), then a **teleporter** beside it (+120 XP), which links your camp to the station's pad. Then:
  - **Speak to James Brown:** a gold marker leads you to him. He warns (voiced) that a big storm is rolling in off the plateau, too soon to reach the station, so you'll have to build a shelter.
  - **Build a shelter:** a floor with a roof over it, closed in by walls or doorways. One side may stay open as the way in, and bigger bases of several floors and roofs work too. The objective tracks your floor, walls (3) and roof as you build.
  - **Get inside the shelter:** the storm builds for about 20 seconds after James's warning: wind and snow speed up, the snowflakes grow and a whiteout swallows the sky. When it hits at full strength, the sky darkens to slate, your exosuit flashes red and announces **WEATHER WARNING: SUPER BLIZZARD INCOMING** (SUIT), and the narrator explains how to survive it (five voiced lines with subtitles).
  - **Suit heat:** a heat gauge appears under your stamina. Out in the blizzard it drains (about 90 seconds from full to empty). It recovers inside a shelter, beside a camp heater, inside the station, and once the storm is over. Below 30% the exosuit gives its voiced exposure warning (SUIT2). At zero heat the suit performs an emergency recovery, putting you back at the station with 60% heat.
  - **Wait out the storm with James:** the super blizzard lasts five minutes of active play once it hits (the objective shows a countdown, which pauses while the game is paused), then it clears.
  - **Sleep:** a few seconds after the storm clears, James says (voiced) "I'll make a bed. Feel free to sleep." and lays a bedroll in your shelter (or beside you if the shelter is gone). Press E at the bed to sleep. In the dream, a figure you can't yet name (shown as ????) warns you not to trust James Brown. He describes the soldier James was speaking to, a faction of radical humans gathering under a new banner, and their master, who still stands beside the Federation's ruler. He names none of them. For human wanderers all seven lines are voiced (CH1GREK1–7). Erisian, Chompy and Grek wanderers hear the first three voiced, and lines 4–7 are a single non-human version shared by all three (voiced, CH1GREK4–7NONHUMAN). You wake in the morning beside the bed.
  - **Find James's rover by the teleporter:** a few seconds after you wake, James says (voiced) he wants to get out of Antarctica, and you can take his rover to the nearest ferry about a kilometre away. He parked it next to your teleporter (or the station's pad), and a gold marker shows it.
    - He then adds a second voiced line (CH1ROVER2) about his dream of the Sol System: Mars, Europa, and Saturn through a ship's window. This sets up the speech he refers back to on the pier when he betrays you.
  - **Drive to the ferry:** press E at the rover to drive it. Use W/S or the stick for throttle, A/D to steer, and E (EXIT) to get out. It does up to about 85 km/h, tilts with the snow, kicks up powder, and stops dead if you hit rocks, trees or walls. James rides with you when he's following. Inside the rover your suit heat recovers. The objective counts down the distance to the **Ross Sea ferry terminal**: a flat landing on the coast with a wooden pier, a red-and-white ferry, a terminal building and open water with drifting ice. The pier, the jetty, the gangway (a ramp with handrails) and the ferry's deck can all be walked on. The cabin is solid, and you can't step off into the sea.
  - **The betrayal:** as you reach the terminal, James steps onto the pier between you and the gangway and turns on you, in a fully voiced 15-line speech (JBBETRAYAL1–15). Near the end his hand comes out of his coat.
  - **Push James Brown into the water:** walk up to him and press E (PUSH). He goes over the side into the sea and is gone.
  - **Boss: Croxian Mascar (level 30):** a man with a scythe steps off the ferry and introduces himself as Croxian Mascar. The fight is scored by **Predator IV**, which plays from the start of the chase until it ends. James was meant to hand you over to his people. The ferry casts off and swings round to a second berth along the shore. **Run to the ferry**: down the pier, along the coast and onto the far jetty, where the ferry ties up with its gangway down (about 22 seconds after it casts off). Get up the gangway onto the deck to escape. The hull's side is a wall, so use the gangway or jump. Croxian chases you: his scythe sweeps (red ring warning) hit for 48, and his leaps onto where you were standing (red circle) hit for 60. Dodge (Q) avoids a hit, and blocking takes most of it. He taunts you as he goes (all of his lines are voiced). **Never run at him**: get close while moving towards him and he kills you outright. If you die, the fight resets to just before James turns on you. Get aboard and you escape Antarctica.
  - **Leaving Antarctica:** a letterboxed cutscene follows. The ferry pulls away from the jetty and gathers speed out to sea while the camera rises from the shore, with you at the stern and smoke trailing from the funnel. **ARRIVING IN AFRICA** fades in, the screen goes black, and **Starting Chapter II · AFRICA** appears. Your wanderer is now in Chapter II.

### Chapter II — Africa

- **Opening cutscene: the collapse.** A near-death sequence shot like a horror film, on a sun-blasted dirt road out of an African harbour (dunes, acacias, shipping containers and cranes behind you).
  - Handheld, shaking camera with dutch tilts, a low drone that keeps rising, ragged breathing and a heartbeat that races and skips. The picture blurs, drains of colour and pulses red with every beat, and your eyelids keep closing for too long.
  - Your wanderer staggers with one leg dragging, lurches sideways twice, flings out an arm to catch their balance and coughs up blood. Then they stop, hand to head, nose pouring blood into a spreading stain on the sand, and the world doubles. A full blackout blink.
  - Their knees drop out from under them, one shaking arm holds them up, and they cough blood twice more. They fall face-first in slow motion, arms trailing. The impact is a heavy crash with a red flash, and then the heart stops.
  - Lying on your side in the sand, ears ringing, vision tunnelling and fingers twitching, a weak heartbeat returns and a man sprints up the road: **Orion Mascar** (shown as ???). He drops to his knees and shakes you, speaking six voiced lines (CH2ORION1–6) in a text box while you fight to stay conscious. His jaw and mouth move with his voice, and his face is set grim and frightened rather than smiling. When he finishes, the heart flatlines and your eyes close.
  - It plays straight after the ferry, or the first time you deploy a Chapter II wanderer.
- **2 weeks later:** over black, **2 WEEKS LATER** appears and the narrator picks up the story in six lines (voiced, CH2NARRA1–6, with subtitles). You escaped Croxian Mascar of Terra Imperia, collapsed on the road, and spent fourteen feverish days being nursed by a man called Orion, who went very quiet when you whispered Croxian's name. Now you're awake. Space, E or a tap skips a line.
- **Free roam in Africa:** you wake outside **Orion's home** at the edge of the harbour town, a mud-brick house with a shaded porch, a water tank and his own teleporter pad. Africa is a second open world:
  - Rolling savanna with sand, dry grass, rocky kopjes and gullies under a warm, hazy sky.
  - Groves of flat-topped acacias (chop them for wood), HD rocks and supply crates. There's no ice and no obsidian, and Antarctica's wildlife doesn't live here.
  - The day/night cycle, building, crafting, teleporters and your inventory all carry over. Africa keeps its own builds, mined nodes and time of day, separate from Antarctica's.
  - **Objectives:** Wake up at Orion's ✓ → **Speak to Orion** (he's on the porch, with a gold marker; his four lines are voiced, CH2ORIONFREEROAM1–4, and he lip-syncs) → **Explore Africa**.
  - **Orion Mascar joins you:** after you speak to him, Orion becomes your companion at **level 14**, and he gains a level every time you do. He takes the same orders as James: **1 Mine · 2 Explore · 3 Base · 4 Wander · 5 Follow**, through the companion panel (shown as ORION · LV n) or by walking up to him (ORDER).
    - He has his own voiced replies (ORIONCOMMAND1–5), the same from Chapter II through Chapter V.
    - He follows you, and catches up if you get too far ahead. He mines rocks, trees and crates for you, and hits harder as he levels. He explores the savanna (digging as he goes), wanders nearby, or heads home to his porch.
    - He stands beside your wanderer on the main menu, just as James did.
    - **Armed:** Orion carries a **rifle** and shoots hostile animals that come near (threats come before any order). When he mines, he swaps it for his **obsidian pickaxe**.
  - Saving remembers that you're in Africa. Deploying a Chapter II wanderer who has seen the opening takes you straight back there.
- **Day and night:** outside, a full day lasts 20 minutes. The sun rises and sets with warm dusk light, nights turn dark blue with a sky full of stars, and the light and haze change with it. Each planet keeps its own time of day in your save.
- **HD Antarctica:** the ice uses an HD snow texture (tiled every 4 m, seamless across the endless terrain) under an HD polar sky panorama. Rock outcrops use an HD rock model (with colour, normal and roughness maps), and groves of bare, wind-stripped trees built from an HD bark model stand on the flatter ground. The distance haze and sunlight are matched to the sky's horizon and sun.
- **The meeting on the ice:** about halfway along James's trail, a cutscene plays: James talking with a soldier in black armour with cyan trim. The armour is a Human Federation of Sol (HFOS) design, but the Federation doesn't wear those colours. Press Space/E to advance a line, or Skip. It plays once per wanderer.
- **Lip sync:** James and all four species leaders move their jaws and mouths with their recorded voices.

## Controls

| | Phone | Computer |
|---|---|---|
| Move | Left thumbstick (push fully to run, lightly to walk) | WASD / arrow keys (run by default; C toggles walking) |
| Sprint | SPRINT button (toggle) | Hold Shift |
| Jump | JUMP | Space |
| Jetpack | Hold JUMP while in the air | Hold Space while in the air |
| Block | Hold BLOCK | Hold R or the right mouse button |
| Dodge roll | DODGE | Q |
| Attack / mine / place / use | ATTACK | Click (without dragging) or F |
| Look | Drag the right side | Drag the mouse; wheel to zoom |
| Interact / advance text | TALK / LOOK / TAKE button, or tap the text | E or Enter |
| Hotbar | Tap a slot | 1–6 (once James has joined you: mouse wheel) |
| Order companions | Companion button (JAMES) under your objectives, or walk up and tap ORDER | 1 Mine · 2 Explore · 3 Base · 4 Wander · 5 Follow · V picks which companion (or Everyone) |
| Build | BUILD button | B opens the build menu · F / click places · X stops building |
| Zoom (outside, once James has joined) | — | − / = |
| Inventory & crafting | Bag button | I or Tab |
| Earth map | Tap the minimap | M |
| Pause | ☰ button | Esc |

## Survival

- **Health and stamina:** sprinting, jumping, dodging and swinging cost stamina, which refills when you rest.
- **Movement and combat animations:**
  - **Sprint:** long strides, pumping arms and a hard forward lean, kicking up snow as you go.
  - **Block:** arms crossed in front of you behind a hexagonal suit shield. Attacks from the front do a quarter of their damage and cost 14 stamina each, with a knock-back. You move slowly and can't sprint while blocking, and blocking stops when your stamina runs out.
  - **Jetpack:** a twin-nozzle pack on your back. Hold jump in the air (or after stepping off a ledge) to thrust upwards with flame and smoke, leaning into the direction you're moving, and steer better than in a normal jump. Fuel (an orange bar under stamina) lasts about 3 seconds and refills on the ground.
- **Gathering:** attack rocks (stone, sometimes scrap metal), ice spires (ice, sometimes frost crystal) and supply crates (scrap metal, cloth, sometimes frost crystal). Three crates sit near the station to get you started.
- **Crafting** (Inventory → Craft):
  - Ice pick: doubles mining and melee damage.
  - Med kit: +40 health.
  - Thermal lamp, wind barrier and signal beacon.
  - Camp heater: heals you while you stand nearby.
- **James Brown, companion:** after you find him and he finishes speaking, James joins you. He carries his own rifle (slung on his back, ready for when hostile creatures arrive) and takes orders:
  - **1 · Mine:** heads for the nearest rock, ice spire or crate, mines it with his pick and adds what he finds to your bag.
  - **2 · Explore:** scouts on his own, up to ~260 m away, and sometimes brings back a resource.
  - **3 · Meet me back at base:** walks back to the station and waits by the door (and is inside when you go in).
  - **4 · Wander around:** strolls around where he is.
  - **5 · Follow me:** the default. If you get more than 40 m ahead, he catches up by appearing just behind you.
  Each order gets a voiced reply from James (Chapters I and II; he has different lines when he rejoins you later). On a phone, tap **JAMES** under your objectives, or walk up to him and tap **ORDER**. He shows as a green dot on the minimap.
- **Voiced scenes:** the meeting cutscene (James and the soldier) and James's lines at the end of the trail are fully voiced with lip sync.
- **Main menu by chapter:**
  - **Chapter I to early Chapter IV:** the normal blue menu, the original theme, and the year 2125 AD.
  - **Chapter IV, after the time skip:** always blood red: every screen, from the main menu (all eight buttons included) to the in-game HUD, pause and inventory menus, uses the red interface, red night with falling ash, the Chapter IV theme, the year 2127 AD, a taunting voice, and a rewritten mission brief.
  - **Chapter V onwards:** back to the normal menu and the original theme, still in 2127 AD. **Settings → Menu style** lets you switch to Blood red (which brings back the Chapter IV theme and the voice).
  - To preview, add `?menu=ch4pre`, `?menu=ch4` or `?menu=ch5` to the game's address.
- **Main menu:** the backdrop and the corner panel follow where the active wanderer's save is:
  - **Chapters I–II, and Earth in any chapter:** Antarctica at polar night, with aurora and snowfall. Once James has joined you, he walks alongside your wanderer.
  - **Chapters III–V, aboard the ship:** your dropship cruising through the system you saved in, past the world you were nearest, with that system's star (or Sagittarius A*). In the blood-red Chapter IV menu, space is tinted red too.
  - **Chapters III–V, landed:** the ground takes the colours of the world you landed on (Archiostal's gardens when docked).
  - **Corner panel:** the place (system or planet), who holds it now, and your alignment. Takeovers change the name: the Catharsis in Chapter IV's Grek space, the Grek again in Chapter V, and your own Diplomacy (your colonies and their governors, conquests, occupations, renamed puppets, restored states, tributaries, and wars). Continue and the save slots name the system or world as well.
  - In the blood-red Chapter IV menu, the voice's taunts sit above the panel (on phones, along the bottom in place of the footer).
- **Options:** in the pause menu (and Settings on the main menu) you can turn the music on or off separately from all sound. Both choices are remembered.
- **Nostrapedia** (main menu): the in-game encyclopaedia. **Leaders** holds detailed files on the four species leaders. They are classified until Chapter III, except the leader of your wanderer's species, whose file opens once you have met them in your dream.
  **Companions** holds files on the people who travel with you. James Brown's file is open from Chapter I; the rest are redacted and open as the story continues (Chapter II, III or IV).
  **Ancient figures** is open from the start: history files on people you never meet in the game. They cover **Lord Sevirrus** (defeated in 1800 AD at Alphinos, capital city of Aridaxx), **Shakhak Chompjak** (founder of the Chompy Empire, c. 1.5 billion BC to 199,999,998 BC, victor over the Grob leader Javek at Steca) and **Lianna Erisconos** (mother of Vishara, Alexia and Nyrexia, former Grob Governor of Eris, c. 2.5 billion BC to 1 billion BC).
  **Terra Imperia** appears from Chapter III, with files on its leadership; one of them changes as the story moves through Chapters IV and V.
  Two further sections are **classified**: their files show only redaction bars until they are declassified in Chapter IV, after which they appear in full colour.
  **Creations** lists what you've made in Custom creations; full entries for them are coming soon.
- **Custom creations** (main menu): creator tools in the spirit of Spore's editors and Galactic Adventures. Creations are stored on this device separately from save slots, and are only saved when you press Save.
  - **Species creator:** build a creature with a live 3D preview (drag to rotate, scroll to zoom, Walk to see it move). You can set legs (0, 2, 4 or 6), leg length, arms, body length and width, tail, back spikes, neck, head, snout, 1–8 eyes, horns, ears, skin pattern (plain, stripes, spots, bands, scales), three colours, bioluminescence and size. Add lore: temperament, diet, homeworld and a description.
  - **Planet maker:** pick a preset (terran, ice, desert, ocean, volcanic, jungle, toxic or gas giant) and tune the seed, sea level, continents versus islands, mountains, size, colours, atmosphere, clouds, rings, moons, climate, gravity and life.
  - **Characters:** five ready-made characters from two games, each rigged automatically and armed: from *Project BC*, Josiah Richards (golden chains), Peter Chambers (rifle), Gareth Williams (dual pistols) and Kevin Murderhorn (black chains); from *Sevirrus*, Lord Sevirrus of Janira Prime (black sword, with a slasher-style neck snap). Each has a full biography, and you can preview Idle, Walk and Attack. You can also **upload your own .glb**: it's rigged automatically (using its skeleton if it has one, named arm/leg groups if it has those, or by splitting the model into head, arms and legs), and you can give it a name, weapon, height, description and the neck twitch. Uploads are stored in the browser's IndexedDB on this device.
  - **Adventure maker:** name and summarise an adventure, choose its planet (Earth or one of yours), set the difficulty and XP reward, cast up to 8 characters (Human, one of your species or any character, as ally, neutral or enemy, each with a line of dialogue), and write up to 8 acts with goals (reach, talk, collect, defeat, explore, survive), a target and story text. The preview shows your cast on the stage under your planet. Playing adventures comes in a later update.
- **Levels 1–100:** every wanderer earns XP and levels up from 1 to a maximum of 100. The level and XP bar sit above your objectives, and the level shows in the Wanderers list and on the main menu.
  - **XP from:** mining (rock 12, ice 10, crate 15; half when James mines), crafting (tools 30, everything else 20), placing builds (8), walking outside (1 per 40 m), hunting (skua 30, leopard seal 70, elephant seal bull 130; half when James makes the kill), and story moments (inspecting 15 each, talking to James 50, resting 100, stepping outside 50, the meeting 100, finding James 150, James joining 250).
  - **Each level:** +2 max health (298 at level 100), and a full heal on level up. Levels 20, 50 and 80 each add +1 mining damage.
  - XP needed per level grows from 200 (level 1→2) to about 70,000 (99→100); reaching level 10 takes about 7,400 XP, level 50 about 448,000, and level 100 about 2.7 million. Wanderers made before levels existed get XP for the story they've already played.
- **Antarctic wildlife:** the ice is no longer empty.
  - **Emperor penguins** (passive) waddle about in colonies of 6–12 and belly-slide away if you get too close or hit them. They can't be hurt.
  - **South polar skuas** circle overhead and dive-bomb you (6 damage).
  - **Leopard seals** hunt you on sight within about 20 m and bite hard (12 damage).
  - **Elephant seal bulls** are territorial: get within 9 m and they rear up and charge (20 damage), but they give up if you back off.
  Hostiles show as red dots on the minimap, have health bars once hit, and bring in the combat music. Dodging (Q) avoids a hit. James shoots at anything hostile near you with his rifle. If your health hits zero you black out and wake at the station with half health, keeping your items. Creatures drop **blubber** and **skua feathers**, used for two new recipes: the **Seal ration** (restores 25 health) and the **Insulated lining** (+20 max health while carried). The area around the station stays safe.
- **Minimap and Earth map:** outside, a heading-up minimap (top right) shows the terrain, the station, your beacons and a gold diamond on the current objective, with its distance. Tap it or press M for the full north-up Earth map with your coordinates.
- **Antarctica exploration music:** four tracks play while you're out on the ice, shuffled with quiet gaps of 9–25 seconds between them. The music fades when you go inside, softens during pauses and cutscenes, and steps aside for combat themes.
- **Combat themes:** five tracks (Predator I–IV and Wonders of Laniakea, combat version). In play, one is picked at random whenever something hostile engages you; it takes over from the ambient music and fades out a few seconds after the fight ends. You can preview them in Settings → Combat themes, where each tap plays the next track.
- **Held items:** whatever is selected in the hotbar (ice pick, med kit, thermal lamp, or a placeable) is shown in your right hand, positioned to fit your species.
- **Placeables:** select a placeable in the hotbar (lamp, wind barrier, heater, beacon) and a green preview appears in front of you; attack to place it. Walk up to it and press E (TAKE) to pick it back up.
- **Base building** (B, or the BUILD button): a No Man's Sky-style build menu.
  - **Pieces:** floor, wall, doorway, roof and ramp, each in **wood, stone, metal, obsidian or ice** (2–3 of that material per piece).
  - **Placement:** pieces snap to a 3 m grid. Walls and doorways sit on the grid lines, and turn to face the way you're facing. New pieces line up with the heights of what you've already built, so you can stack storeys: build a ramp, walk up it, and lay floors on top of your walls.
  - **Walking:** floors, roofs and ramps can be walked on, and walls block you. Doorways can be walked through. You can also land on and walk along the tops of walls and crafting tables, and if you ever end up inside a wall, rock or tree you can always walk back out.
  - **Changing your mind:** while building, walk up to a piece and press E (TAKE) to dismantle it for a full refund. The preview turns red when you can't place a piece, or can't afford it.
- **New materials:**
  - **Wood:** chop trees (2–4 each, +14 XP; James chops them too), or find it in supply crates.
  - **Obsidian:** from rare black volcanic glass outcrops. You need the ice pick selected to break them.
  - **Metal plate:** refined from 3 scrap metal at a crafting table.
- **Crafting table** (build menu → Structures): refined recipes (metal plates) and teleporters only work within 5 m of one. Inside the station counts as having one. Press E at a table to open crafting.
- **Merchants:** an Erisian trader keeps a stall on the ice (a pink diamond on the minimap). Press E to trade, selling resources for **Units** and buying materials, med kits and rations. Your Units balance shows in the inventory. Each planet the story reaches gets its own merchants.
- **Teleporters:** a teleporter pad stands outside the station, and you can build your own at any base (it needs a crafting table nearby). Every pad joins one network: step onto a pad and press E to pick a destination. You can rename your bases, and pads show as cyan rings on the minimap. Pads on other planets are listed under their planet, and you can reach them once the story takes you there by ship.
- **Nothing is lost between chapters:** your inventory, Units, everything you've built (stored per planet) and your companions' orders belong to the wanderer, not the chapter, so they carry into every chapter.
- **Commanding companions:** the companion panel and the 1–5 keys work for any companion in your party. With more than one companion, the panel shows who you're commanding; tap a name, choose Everyone, or press V to switch. James is the only companion who has joined so far; the others join in later chapters.
- What you mine and build is remembered per wanderer and saved with your save game.

## Repository layout

```
index.html                  the game code, UI and loader (about 0.8 MB)
data/                       every model, texture, music track and voice set as <id>.js, loaded by index.html
assets/models/              source 3D models (.glb); primes/, vectors/, companions/ and terra_imperia/ and ancient/ hold Nostrapedia figures; characters/ holds the Project BC and Sevirrus models, including hfos_soldier.glb (original HFOS colours)
assets/audio/               main menu themes (incl. Chapter IV), combat themes (combat/), Antarctica exploration music (antarctica/), opening narration, James Brown's lines (prologue + Chapter I)
assets/models/world/        HD rock and tree-bark models (packed with JPEG textures into data/)
assets/models/companions/   Nico (Lady Luck) model
assets/audio/music_africa/   Africa exploration music (CH2AFRICA1–5)
assets/audio/storm/         exosuit warning (SUIT, SUIT2) and narrator lines (NARRATOR1–5) for the super blizzard
assets/textures/            HD Antarctica sky panorama and snow texture (packed as JPEG into data/)
assets/logo_reference.png   logo / font style reference
```

The files in `assets/` are the source copies. The game doesn't load them directly; it loads the packed copies in `data/`.

## Saves

The game never autosaves. It writes progress only when you choose **Save game**, either from the main menu (Save / Load) or from the pause menu in a chapter.

- **Export / import (for itch.io and other browsers):** on the Save / Load screen, **Export saves** downloads one file (`nostravector-saves-YYYY-MM-DD.json`) holding every save slot, wanderer, setting and custom creation, including uploaded .glb models. **Import saves** (tap twice to confirm) loads such a file and replaces what's on this device, then reloads the game. Browsers, and itch.io's game frames especially, can wipe site storage, so export now and then. Only saved progress is exported, so save first.
- There are three save slots. Each holds all your wanderers, the active one, their chapter progress, and where you were standing if you saved in the station.
- Changes since your last save are kept only in memory and are marked **UNSAVED**. Loading or overwriting a slot asks you to confirm.
- **Delete save** (in Save / Load or the pause menu) clears a slot after a second tap to confirm.
- Each wanderer remembers exactly where they were (out on the ice or in the station). Saving, loading, Continue and going to the main menu all put you back on that spot.
- When the game starts, it reads your most recent save so Continue picks up where you left off. That only reads; it never writes.
- Saves live in the browser's local storage, so each browser and device keeps its own slots.

### Weapons and tools update
- **Obsidian pickaxe:** a new tool and an upgrade on the ice pick. You craft it at a crafting table from your ice pick (which is used up), 3 obsidian, 2 wood and 1 metal plate. It triples your mining and melee damage (the ice pick doubles it), hits animals harder, breaks obsidian, and has its own black-glass model in your hand.
- **James uses his rifle now:** when he shoots, the rifle comes off his back and up to his shoulder, with both hands on it and the pick put away. When the fight ends, it goes back over his shoulder. The same rifle logic drives Orion.

### Africa music and the split build
- **Africa has its own music:** five exploration tracks (CH2AFRICA1–5) play as a shuffled playlist with quiet gaps between them, the same way Antarctica's do. Crossing between Antarctica and Africa fades one playlist out and starts the other.
- **No more single-file limit:** the embedded assets moved out of `index.html` (which was 94 MB, close to GitHub's 100 MB limit) into `data/`. The game itself hasn't changed.

### African wildlife
Africa's savanna now has its own animals, all built and animated in code. They trot at walking pace, gallop when running, graze when standing, and swish their tails.
- **Passive: Thomson's gazelle.** They roam in herds of 5–9 and the whole herd bolts when you get within about 15 m. You can hunt them for raw meat (and sometimes cloth). James and Orion never shoot them.
- **Neutral: Cape buffalo.** They graze in groups of three and ignore you until you hit one. Then the whole herd charges (*The buffalo herd charges!*). They give up after about 12 seconds or once you're far enough away. Companions only shoot a buffalo that's already charging.
- **Predators:**
  - **Lions** hunt in pairs. A lion stalks slowly at first, then charges hard.
  - **Spotted hyenas** run in packs of three. When one sees you, the whole pack comes, and they fan out around you instead of queueing in a line.
- **New food:** animals drop **Raw meat**. Craft **Roast meat** from 1 raw meat and 1 wood; it restores 30 health. Seal rations need ice, so this gives Africa its own way to heal.
- **Combat music:** fights in Africa use the same Predator combat themes as Antarctica.
- **Blacking out in Africa:** you come to outside Orion's home. Once Orion has joined you, he carries you back there.

### Nostrapedia: Lore events
A new **Lore events** tab sits next to Ancient figures. When you open an event, the figures who were there stand on the stage, but only those whose own Nostrapedia file you've unlocked.
1. **The Third World War** (ended in the 2090s). The United States, China and Russia fought each other despite sharing one United Nations banner. It is said Orion Mascar fought alongside Thomas Hawthorne. Their names stay redacted until you meet them: Orion in Chapter II, Hawthorne in Chapter III.
2. **The Massacre at Carax** (1790 AD). Sevirrus massacred the Chompy mining world of Carax under orders from the Cult of Zark.
3. **The Murder of Jakal Chompjak XVI** (before 1790 AD). Sevirrus killed his cousin Damix Chompjak, then his own father, and seized the empire.
4. **The Siege of Carax** (1800 AD). While Sevirrus was pinned down on Aridaxx by his uncle Jazmak and by Arixal, Hanaxa and Aniz Chompjak, Am-Grek's Grek took Carax. Arixal defeated both Jazmak and Sevirrus and put Hanaxa on the throne.
5. **Sevirrus' Redemption** (1826 AD). After 26 years in prison, the Chompy Empire released Hak (once Sevirrus). He returned to Carax and defeated the High Priest of Destruction, breaking the Cult of Zark.
6. **The Siege of Carax: the Catharsis** (Chapter V). Redacted until Chapter V, the second siege you witness after the final boss of Chapter IV. Carax is the Catharsis capital by then, and the allies (the Chompy Empire, Archamus, the Erisian Empire, the Grek and the Human Federation of Sol, with you among them) attack it. At the top of its five-floor bastion, the same summit where Hak was blinded in 1826, they defeat **Lord Zark**; the Catharsis is destroyed, Hawthorne dies, and its worlds pass to you. On the stage, an 8.5 m Lord Zark towers over the six who beat him: Archamus, Vishara, Hak, your own wanderer as they look now, Am-Grek and Darius.

### Lord Sevirrus: red eyes and the neck snap
- **Red eyes:** Sevirrus's irises are now blood red with a faint glow and near-black pupils, everywhere his model appears: the Nostrapedia (Ancient figures and Lore events) and the character viewer.
- **Slasher neck snap:** every few seconds his head snaps sideways and tilts, holds, then eases back. It always goes the same way, never alternating left and right. It now plays on his Nostrapedia figure too, not only on the rigged character.

### Fix: combat theme preview
- A combat theme you play from **Settings** now stops when you leave Settings, and the main menu theme fades back in. Before, it kept playing through the menus until you went back into Settings and cycled it off.

### Alignment (KOTOR / Mass Effect style, every chapter)
- **Your chart:** press **L**, or choose **Alignment** in the pause menu. A vertical bar runs from **ENLIGHTENED HERO** (cyan, top) through **NEUTRAL** (grey, middle) to **AWAKENED VILLAIN** (red, bottom). Every wanderer starts at grey (0). As you move up or down, the marker, the fill and your rank stay grey with a hint of cyan or red that grows stronger the further you go. The scale runs from −100 to +100; you're a hero at +34 or above and a villain at −34 or below. Your alignment is saved with your wanderer and carries through every chapter.
- **Companion charts:** the Alignment screen shows only the companions you have with you right now: James in Chapter I, Orion from Chapter II, and anyone who joins later. Characters from the other NOSTRAVECTOR games (the Project BC cast and Lord Sevirrus) appear only once they've been brought into your party. Party members also show an **Influence** bar. A companion's Nostrapedia file shows their chart only while they're travelling with you.
  - Starting points come from each character's alignment: Good +45 to +65, Neutral around 0, Evil −55 to −75.
  - James Brown's chart reads **UNKNOWN** with a "?" marker, and he approves of everything you do.
- **Character model:** a 3D model stands beside the big chart, slowly turning. It shows your own wanderer by default, as they look right now. Click a companion's card and the big chart and model switch to that companion alone, life-size and large. Click the card again, or **Back to you**, to return. Lord Sevirrus keeps his red eyes and neck snap here too.
- **Darker clothes:** going down the villain path darkens outfits. Nothing changes until −15. From there clothing (never skin, hair or eyes) slides toward near-black, and it's fully dark by −80.
  - Your wanderer: the suit and accents darken with your own alignment. It works for every species and is back to default colours once you're neutral or good again.
  - Companions: each companion's outfit follows their own alignment, in the world, on the main menu and in the Alignment viewer. Characters who start out as villains (Sevirrus, Kevin, Peter, Josiah and the like) stay exactly as they are.
- **Nostrapedia follows your save:** a companion's Nostrapedia file shows the alignment they have in this save. The order/chaos side of their original alignment is kept, and the good/evil side follows their chart (Good from +15, Evil from −15). Orion pushed to −55 reads *Chaotic Evil · was Chaotic Good*, both in the list and in his file, and his figure wears his darkened outfit. A new game, or a companion you've never influenced, shows the original alignment.
- **Tyrotaronus in the Vectors section:** Tyrotaronus is also filed under the Oilkoumene Vectors. That file follows the same alignment, so in the Chapter V villain preview it reads *Neutral Evil · was True Neutral*. Because he's scaled, only his silver armour darkens.
- **Deeds:**
  - Heroic: **Share food** with a companion (key **6** or the companion panel; uses a roast meat or seal ration) +4. Kill a hostile animal while you have companions with you +1. Build a camp heater or signal beacon +1 (counts the first 10).
  - Villainous: **Intimidate** a companion (key **7**) −4. Attack a peaceful buffalo herd −3. Strike a harmless penguin −2. Kill a gazelle while you're at full health, for sport rather than food, −2.
- **Companion reactions:** heroic companions favour good deeds and dislike evil ones, villainous companions the reverse, and neutral companions simply drift with you. Losing influence never makes anyone leave. Instead, their own alignment slides in the direction you pushed it.

### Fix: companions on the main menu
- Orion (and James, and any companion standing with you on the main menu) no longer flickers between walking and standing. He starts walking only once you're properly ahead, keeps a steady pace, and stops once he's caught up.

### Naming: Tyromairon
- The Vector of Darkness is now called **Tyromairon** everywhere: his Nostrapedia name, his file, and Tyronihlus's "Serves" line. *Tyromairon’as* is no longer used.

### Chapter II: the call
- **Orion's phone:** about ten seconds after Orion joins you (or after you load a save from that point), his phone rings. A woman in distress tells him that lions came over her fence and broke her door in. She has locked herself in the back room, and she's expecting: the baby is coming now. Orion tells her to stay put and keep breathing, then tells you to follow him. He switches to **Follow** automatically.
- **On the phone:** when it rings, Orion stops where he is and lifts the phone to his ear like a real one. His left arm bends at a new elbow joint and reaches up to the side of his head, elbow dropping down and out. The handset sits flat against his cheek, top at his ear and bottom angled toward his mouth. He holds it there through the whole call, then lowers it before turning to you with his last line.
- **Objectives:**
  1. **Reach the farmhouse east of town**, about 220 m east of Orion's home. A gold marker shows the way on the map.
  2. **Drive off the lions**, with a counter of how many are left. Three lions prowl a broken-fenced yard around the smashed front door. Orion's kills count too. If you leave and come back, any lions still alive return.
  3. **Check on the woman.** Call through the farmhouse door. Clearing the lions is a heroic deed (+3).
- **The farmhouse:** a mud-walled farmhouse on a levelled yard, with its front door hanging off one hinge, claw marks beside it and gaps in the fence where the lions came through.
- The call (CH2ORIONCALL1–7) and the door scene (CH2DOOR1–2) are fully voiced, and Orion lip-syncs his lines.
- **Inside the farmhouse:** after the door, the screen fades to a small lamp-lit room.
  - **Nico** (her own model, `assets/models/companions/nico_lady_luck.glb`) stands by the bed. She still looks heavily pregnant, as a new mother does; that's built from her model at runtime. Beside her, her newborn son sleeps in a gently rocking cradle.
  - The baby was born just after she called, and he hasn't made a sound. She has already named him **Orion**, after the stars of Orion's Belt her grandmother showed her, which is a coincidence that catches Orion off guard.
  - The scene is ten fully voiced lines (CH2FARM1–10). Camera shots switch between over Orion's shoulder, over Nico's and a close-up of the cradle. Orion and Nico both lip-sync.
- **Next objective:** Nico's husband, Daniel Brown, went into town for supplies yesterday and hasn't come back. The objectives are **Reach Ad-Nostra, the harbour town** (gold marker at the east gate), then the hunt for Daniel (see *Daniel Brown and The Salt Lantern* below).
- Nico joins as a companion after Chapter II, in her normal (not pregnant) model. Her model is already loaded and ready for that.
- **Nico's Nostrapedia file** (Companions) opens the moment you meet her inside the farmhouse; until then it's redacted ("Unlocks in Chapter II"). It shows her in her normal model.
  - **Facts:** born 2000 AD, cryogenically frozen in 2030 AD and woken in 2123 AD, home is a farmhouse east of town in Africa, her son Orion was born in 2125 AD, and her alignment is Neutral Good (a placeholder until her alignment is decided).
  - **Text:** a short biography of the century she lost and the new life she built.
  - **Map marker:** pink, reserved for when she joins the party.

### Cinematic conversations (Chapters I and II) and the pause fix
- **Cinematic conversations:** whenever a character speaks to you up close (James, Orion, the woman behind the farmhouse door, Croxian Mascar), the game switches to a cinematic camera.
  - Letterbox bars slide in, and the HUD steps aside: objectives, minimap, hotbar, loot messages, companion panel, navigation and the pause button.
  - You turn to face the speaker.
  - Each new line changes the shot. The camera cycles through over the right shoulder, over the left shoulder and a close-up on the speaker, with a slow push-in during every line.
  - In the station the camera stays inside the walls, and outside it never dips below the ground.
  - Radio-style lines from someone more than 14 m away, inspections and narration keep the normal view.
- **No pausing during scenes:** pausing in the middle of a conversation used to close it without running its ending, which soft-locked the story. While anyone is talking, during Orion's phone call, during the meeting cutscene and through the betrayal on the pier, the pause button is hidden and Esc/P shows *You can’t pause during a scene*. Switching tabs mid-scene no longer pauses and breaks it either.

### Fix: companions on the minimap
- Every companion with you now has a live marker on the minimap and the big map (M). James is green with a "J" and Orion is orange with an "O".
- The marker moves with them and has a pointer showing which way they're facing. It turns with the map just like your own arrow, and sits on the rim when they're out of view.
- On the big map their name is written under the marker.
- Before, Orion had no marker of his own at all.
- **Ready for future companions:** markers come from your party, not a hard-coded list.
  - Every story companion still to join has its own colour reserved: Khazglar, Charon, Kizna, Nyrexia, Croxian, Malia, James (Terra Imperia), Josiah II and Tyrotaronus.
  - **Custom companions** (your own uploaded characters, or the Project BC and Sevirrus cast) get a steady colour of their own and their first name, as soon as they're in your party.
  - A new companion's marker appears once its model is registered with `registerCompanionRig(id, () => root)` (also `window.nvRegisterCompanion`).

### Built-in worlds for your own adventures
**Custom creations → Planets** now lists 40 built-in worlds under your own, in four groups. Open any of them to see its type, gravity, climate, life, whether you can land, a short description and a spinning 3D preview. They are read-only. All of them can be picked as an **adventure's planet** or a **species' homeworld**. The main story doesn't use them; Chapter III comes separately.
- **Sol · planets:** Earth, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune. The four giants have rings, and they're described as having no surface, so in an adventure you explore their **cloud cities**.
- **Sol · dwarf planets:** Ceres, Pluto, Haumea, Makemake, and Eris (the Erisian homeworld).
- **Sol · moons:**
  - Earth: the Moon
  - Mars: Phobos, Deimos
  - Jupiter: Io, Europa, Ganymede, Callisto
  - Saturn: Mimas, Enceladus, Tethys, Dione, Rhea, Titan, Iapetus
  - Uranus: Miranda, Ariel, Umbriel, Titania, Oberon
  - Neptune: Triton
  - Pluto: Charon (home of the robot Charon)
  - Eris: Dysnomia
- **Beyond Sol · worlds of the lore:**
  - Janira Prime (Chompy homeworld)
  - Aridaxx (Chompy capital, city of Alphinos)
  - Carax (the airless fortress world in the galactic core, with its full history)
  - Malana (Am-Grek's birthplace, Malana Prime system)
  - Steca (where Shakhak beat Javek)
- Gravity values for the Sol worlds are the real ones. The look of the lore worlds (jungle, desert, airless rock, volcanic) is a placeholder until their appearance is decided.

### Adventures: build a world, then play it as anyone
Open an adventure in **Custom creations → Adventures**. The editor has a new **World** section with **Build world** and **Play**. Adventures are separate from the story. They never give XP, never touch your wanderer's save, and never change a planet anywhere else: sculpting and placing belong to that adventure alone, and every playthrough starts fresh. (The old "XP reward" slider is gone.)

**World studio (Build world).** You build on a 200 × 200 m patch of the adventure's planet. The ground uses the planet's own colours, sky, water level and roughness, airless worlds get a black starry sky, and gas and ice giants give you a **cloud city** deck ringed with towers above a sea of cloud.
- **Landscape:** Raise, Lower, Smooth and Flatten brushes, with adjustable size (2–24 m) and strength. Reset landscape (tap twice) undoes all sculpting.
- **Place:**
  - Start point
  - Cast member: pick one from the adventure's cast; placing them again moves them.
  - Creature: any species you made, or a plain critter, hostile or peaceful.
  - Props: rock, tree, crate, crystal, ruined pillar, beacon, tower.
  - Collectibles
  - Act markers: one per act; reach and explore acts head for them.
- **Erase** removes the nearest object.
- **Controls:** left click/drag uses the tool, right drag turns the camera, the wheel zooms, WASD moves the camera.
- **Test play** plays your unsaved world and drops you back in the studio. **Save** stores the world inside the adventure.

**Play.** Choose who to play as:
- your current wanderer
- the Project BC and Sevirrus cast
- your uploaded characters
- any story companion whose Nostrapedia file you've opened

Controls: WASD to move, Shift to sprint, Space to jump (higher in low gravity), F or a click to attack, E to talk, drag to turn the camera, Esc to leave. The camera follows you third-person.
- **Talking:** cast members say their line when you press E near them. Enemy cast and hostile creatures chase and attack you, with damage set by the adventure's difficulty. You regenerate health out of combat. Fall off a cloud city and you're back at the start.
- **Objectives** come from your acts, in order. Each act opens with its title and story text.
  - **Reach:** step onto its marker.
  - **Explore:** spend a few seconds near its marker.
  - **Talk:** talk to the named cast member, or to anyone if no target is set.
  - **Collect:** pick up N collectibles.
  - **Defeat:** the named cast member, or N creatures.
  - **Survive:** 10 seconds × the amount.
- Finishing every act shows **Adventure complete**. Losing all your health shows **You were defeated**. Either way you can play again from scratch.
- **On phones and tablets:**
  - **Play:** a left stick moves you, with TALK, JUMP, SPRINT (toggle) and ATTACK buttons on the right. Drag the screen to turn the camera, pinch to zoom, and use ✕ to leave.
  - **Studio:** the tools become a bottom sheet you can hide (Hide ▾ / Tools ▴). One finger uses the tool, a second finger turns the camera and pinches to zoom, and **Move camera** lets one finger turn the view.

### Mobile pass
- Adventures now have full touch controls, in both play and the world studio (see above), with layouts sized for phones.
- The Alignment screen fits phones better: a smaller chart and model, the companion list scrolls, and the "press L" hint is hidden on touch screens. Open it from the pause menu.
- Everything else added recently already works by touch: companion orders, Share food and Intimidate (companion panel), the farmhouse door (TALK button), conversations (tap to continue), the map (tap the minimap), the Nostrapedia, Custom creations and the built-in worlds.

### Adventures now look like the main game
- **Playing an adventure** uses the same HUD as the main game, built from the same markup and styles:
  - **Top left:** the objective list (with ticks) and the red health bar.
  - **Top right:** the slanted pause button, which opens a pause panel with Resume, Restart and Leave adventure. Esc or P works too.
  - **Each new act:** opens with the big centred chapter-style title card, with the act's story text in the narration box.
  - **Talking:** uses the main dialogue box (name, line, *Tap to continue*) and the slanted **E** prompt.
  - **Feedback:** pickups and tips appear in the loot feed, and damage flashes red around the edges.
  - **On phones:** the stick appears under your thumb, with the same TALK / ATTACK / JUMP / SPRINT buttons as the story.
- **The world studio** uses the game's panel style, slanted chips for tools and the game's buttons.
- **Play as** lists characters with the main menu's numbered rows, and **Adventure complete** / **You were defeated** use the game's panels and buttons.

### Chapter II: Ad-Nostra, the harbour town
- **Where:** Ad-Nostra is the harbour town on the coast west of Orion's home. Its east gate is about 30 m from his porch, straight down the dirt road, and the town runs about 170 m west to the quay. The land is levelled across the town, and west of it the savanna runs down to the sea. Inside town there's a stone quay with deep water; outside town it's a sandy beach. You can't walk into the sea, but you can walk out along both piers.
- **The town** is fixed, so every wanderer gets the same streets. The wildlife and savanna around it are still each wanderer's own.
  - **East gate:** two pillars and a lintel with the town's name (AD-NOSTRA) on both sides, and a low wall either side.
  - **Main street:** flat-roofed, whitewashed and ochre houses of one to three storeys, with parapets, shuttered windows, doors onto the street, awnings, and rooftop water tanks, solar panels and dishes. There are back rows of houses behind the main street and a lane running north to south. Street lamps line the way.
  - **Named buildings, with signs:** the Harbour Office, The Salt Lantern (the cantina), the Clinic and General Supplies (crates stacked outside).
  - **The market square:** four cloth-covered stalls, an old stone signal tower with a red beacon, a baobab and palms. The **Erisian trader** has a stall here and buys and sells like the one in Antarctica, at Ad-Nostra's prices.
  - **The harbour:** a stone quay with bollards, two big corrugated warehouses, stacks of shipping containers, two quay cranes with their jibs over the water, and two wooden piers. Fishing dhows bob at the piers, and a container freighter rides at anchor offshore.
- **Day and night:** at night the street lamps, the square's lamps and about a third of the windows light up, and the tower's beacon blinks.
- **Townsfolk:** 15 people live their lives in town. Most are human, in work clothes. There's also an Erisian bodyguard, a Grek pilgrim from Archiostal and a Chompy spice seller who remembers the Empire whole. They stop and turn to you as you pass. Press **E** to talk (the prompt reads **Talk · name**, and TALK on phones); conversations use the cinematic camera.
  - **HFOS guards:** the town's guards are Human Federation of Sol infantry, in the HFOS model with the Federation's own blue armour and gold trim (not the black and cyan of the soldier on the ice). The gate warden and a sentry stand either side of the east gate, and a patrol walks the main street.
  - Some townsfolk walk the main street, the square, the quay or the pier. Others keep to their posts: the two gate guards, the shopkeeper, the cantina owner, the harbour clerk and a stall keeper.
  - Human townsfolk get proper shoulder and hip joints, so their arms swing from the shoulder and hang at their sides.
  - Some lines change with your species. A human wanderer hears the Grek pilgrim say all humans look in a hurry; other species hear "everyone in this town", and a Grek wanderer is greeted as kin of Archiostal. The sentry speaks differently to humans and to off-worlders.
- **Asking about Nico's husband:** walking through the gate shows **AD-NOSTRA** the first time. Once you've met Nico, it ticks off *Reach Ad-Nostra* and says **FIND NICO’S HUSBAND · Ask the townsfolk**. Each townsperson then adds a line about him, and the objective counts how many you've asked. Together, their answers make a trail: he came in through the gate yesterday morning with his cart, bought seed, lamp oil and a tin of formula at General Supplies, and was seen pushing the cart down the main street toward the harbour. The harbour clerk will have to check the boat log. Where he went from there hasn't been written yet. The objective stays open, and the save flag `ch2.husbandFound` is ready for that scene.
- **Map:** buildings show as pale blocks on the map and minimap, and the sea shows dark blue.
- The townsfolk's lines are text only for now (no voice files).
- **Phones:** each townsperson's parts are combined into one mesh per limb, and only people within 75 m are drawn (with shadows within 28 m). This cuts the town's draw calls by about 60%, so it runs about as smoothly as the open savanna. Talking uses the TALK button like everywhere else.

### Fix: human wanderers no longer stand in an A-pose
The human suit is modelled with its arms held about 34° out from the body, and the idle and walk animations left them there, so human wanderers stood and walked with their arms out. The arms now hang at the sides when standing and swing from there when walking, on the main menu and in every chapter. Other species were already fine. Poses that set the arms themselves (combat, collapsing, sleeping) are unchanged.

### Chapter II: the ferry and the Ad-Nostra teleporter
- **Discovering Ad-Nostra** (walking in through the gate the first time) unlocks two things, both announced in the loot feed:
  - **The Ad-Nostra teleporter:** a pad in the market square, just south of the signal tower. It appears and joins your teleporter network, alongside Orion's teleporter, any pads you've built in Africa, and the Antarctic ones (listed under *take the ferry to get here*).
  - **The ferry to Antarctica:** the Nostra Line ferry, white with a red waterline and funnel, moored on the north side of the main pier with its gangway down. A red FERRY · ANTARCTICA sign stands at the pier head.
- **Taking the ferry:** walk out along the main pier to the gangway and press **E** (*Board the ferry · Antarctica*, BOARD on phones).
  - The ship pulls away from the pier in a letterboxed shot, the screen fades to black, and a title card reads *Across the Southern Ocean · ANTARCTICA*.
  - You step off on the pier at the Antarctic ferry terminal, the one you escaped from. The ferry waits at the pier there, and boarding it at its gangway (*Board the ferry · Ad-Nostra*) brings you back to Ad-Nostra's main pier the same way.
- **In Antarctica in Chapter II:**
  - The ice, station, teleporters, your Antarctic builds and James's rover (if you drove it) are all there, and the station's teleporter takes you home to the station, where the lamps are on and the hatch is open.
  - James Brown is gone, and his trail and camp no longer appear.
  - Your Chapter II objectives stay on screen, and the chapter label reads *Chapter II · Antarctica*.
  - **Orion comes with you.** Once he's joined you, he boards with you and steps off beside you at either pier. In Antarctica he follows, mines, explores, wanders and shoots hostile animals just as he does in Africa, and you can walk up to him for orders (ORDER). On **Base** there, he waits by the station's door. He's also there if you load a save made in Antarctica.
- **Saving** in Antarctica (outside or inside the station) brings a Chapter II wanderer back there on Continue or Load.

### Chapter II: back on the pier (the flashback)
The first time you step off the ferry in Antarctica with Orion, it all comes back. It plays once per wanderer and is letterboxed. It runs about 46 seconds, because its timing is built from the voice recordings, so every line plays and is subtitled to its last word:
1. **Panic:** on the pier where James betrayed you, your wanderer grabs their helmet, shakes and drops to their knees. Their heart races, their breathing goes ragged, and the picture blurs and drains of colour while Orion stares.
2. **Flashes of Chapter I,** in near-black-and-white with white-flash cuts: James Brown at the gangway, his hand coming out of his coat, saying the whole of his last speech in his own voice ("This is where we part company… You should have learned to fear the man who kept telling you there was nothing to fear"). The shot changes angle every few seconds. As soon as he finishes, he goes over the side into the sea.
3. **Croxian Mascar, the heart of it:**
   - He steps off the ferry ("My name is Croxian Mascar…", his own voice).
   - He comes down the gangway at you far too fast, and his scythe swings again and again. Each hit lands with a red flash, a hard shake and a thud.
   - He leaps and slams down in front of you ("Run, wanderer…", "The ice keeps whatever I give it").
   - A slowed close-up of his mask as the scythe comes up ("Too close."), then one last swing straight at the camera and a red-and-black strobe.
4. **Black and ringing,** then Orion's voice from far away: "Hey. HEY!" (CH2ORIONANTARCTICA0, muffled and quieter, as if heard through the ringing).
5. **Orion,** angry, right in your face on the pier (six lines, with the cinematic camera). You were screaming and clawing at the boards, and there's nothing here. You screamed *that name* again, the one you whispered with the fever in his house. "Don't say it again. Not to me. Not anywhere I can hear it." Then: get up.

6. **Your reply,** chosen from two options in the dialogue box (click, tap, or press 1 / 2):
   - **"Got it."** gives **+10 influence with Orion.** He calms down: "Good." He apologises for shouting, says he's watched men come home from a war and lose themselves on a quiet street years later, and he won't let that happen to you. "Come on. Let's get off this pier."
   - **"I will find Croxian. And when I do…"** gives **−20 influence with Orion.** He's furious: "And when you do, what? You'll kill him?" You couldn't stand on this pier without falling apart, and he'd cut you down before you got close enough to say his name. "I told you not to say it. You heard me, and you said it anyway." He won't leave you on the ice, but you're done talking about him.
   - The choice is saved as `ch2.antChoice` (`calm` or `vengeance`) for later chapters. Influence shows in Orion's alignment panel and in the loot feed (*Orion · influence +10*).
   - Dialogue choices are new to the game. Any conversation can now offer them with `openChoice(speaker, options)`, and `influence(companion, amount)` changes one companion's influence directly.

**Flashback subtitles:** James's, Croxian's and Orion's words appear one at a time in time with their voices, in big uppercase text that shakes with the heartbeat and has a split-colour glow. Each line is shown in full: it's split into sentence pages (14 words at most), the words build up as they're spoken (timed by word length), and a page only turns once every word on it has been said. James's words are icy blue-white. Croxian's are blood red, shudder hardest, and now and then a word (sometimes his own name) glitches into symbols. Orion's are amber. They replace the normal subtitle bar for this scene only.

The flashback uses the voice lines James and Croxian already have. Orion's two replies are voiced and lip-synced: CH2ANTORIONGOOD1–3 for "Got it." and CH2ANTORIONBAD1–4 for the Croxian reply. They're packed as `data/antOrionVoices.js`, with the sources in `assets/audio/orion_ch2_antarctica/`. His six lines before the choice are voiced too: CH2ORIONANTARCTICA1–6 (and 0 for the far-off "Hey. HEY!"), packed as `data/antOrionFlashVoices.js`, with the sources in the same folder. The flag is `ch2.antFlashback`.
- **Fix:** the Chapter I super blizzard can never start again once you've escaped Antarctica.

### Fix: saves put you back exactly where you left off (both chapters)
- **Load** and **Continue** now always return you to the exact spot you saved or quit at, in Chapter I (in the station or out on the ice) and in Chapter II (in Africa or back in Antarctica).
- **What was wrong:**
  - Loading a Chapter II save, or pressing Continue, always restarted you at Orion's porch, because your saved position was never passed on.
  - The position from the last slot you loaded could also hang around and override where you'd actually got to since.
- Chapter II saves made before the ferry existed didn't record which region you were in. They're treated as Africa, where they could only have been.

### Chapter II: Daniel Brown and The Salt Lantern
Daniel Brown is Nico's husband, and no relation to James.
- **The trail (three clues):**
  - The **Gate Warden** saw him come in yesterday morning with his cart and never leave.
  - The **Shopkeeper** sold him seed, lamp oil and a tin of formula ("said his wife was due any day").
  - The **Old Man** in the square saw him pushing the cart toward the harbour.
  - You can ask them in any order. The objective reads *Find Daniel Brown in Ad-Nostra · clues n/3*, and each new clue shows in the loot feed. Other townsfolk still have something to say about him, but only these three count.
- **The Harbour Clerk** gives nothing away until you have all three clues (a gold marker then points to the harbour office). Once you do, he says Daniel never boarded a boat, and his cart has been outside The Salt Lantern since last night. The marker moves to the cantina door, and the objective becomes *Find Daniel Brown in The Salt Lantern*. The cantina owner is cagey: "I pour the drinks, friend. I don't keep track of who drinks them."
- **The Salt Lantern** now has a walk-in ground floor: a bar with shelves of bottles and stools, three tables with chairs, and hanging lamps. Daniel's cart (seed sacks and a tin of formula) is parked by the door. Shop awnings no longer block the doorways underneath them.
- **The scene:** walk in and Daniel is in the corner, kissing a woman who isn't Nico, with the regulars around the walls. Orion: "Daniel?" Daniel: "Orion?! Wait. Wait, this isn't what it looks like." Orion: "Your wife is lying in that farmhouse with your newborn son in her arms… And you are here." Then he goes for him.
- **The fight: you play as Orion.** A brawler in the packed cantina:
  - **Moves:** a three-hit combo (jab, cross, hook), an uppercut that can put Daniel down, block, a grab where Orion hauls Daniel overhead and slams him into the boards, and a **RAGE** finisher when the meter is full (a spinning lift and slam in slow motion).
  - **Daniel** closes in, throws jabs, crosses and telegraphed haymakers, blocks when he sees a punch coming, and gets knocked down and back up. Hits draw blood on the floor.
  - **HUD:** health bars (Orion 140, Daniel 160), the RAGE meter, combo counters, and big pop-up text (*FIGHT!*, *RAGE READY*, *K.O.!*).
  - **Controls:** WASD / arrows to move, J or left click to punch, K or right click for the uppercut, L / E to grab, hold Shift / Space to block, F / Q for RAGE. On phones, a thumbstick on the left and PUNCH, UPPER, GRAB, BLOCK and RAGE buttons on the right, laid out for small landscape screens and away from notches and rounded corners.
  - **The crowd** cheers from the walls, and **MC Irie**, a Jamaican hype man in red, stands on the bar pumping his fist and calling the fight in patois (with plenty of Jamaican swearing: bumbaclaat, bloodclaat, rassclaat, raas) for big hits, combos, slams, knockdowns, Orion getting hurt, RAGE and the K.O. The woman shouts "Get off him! Somebody help!"
  - If Daniel knocks Orion out, MC Irie calls "Run it back!" and the fight restarts.
- **After the K.O.:** a slow-motion orbit round Daniel on the floor, then Orion: "That's for Nico." / "Come on. He can explain the rest to her himself when he wakes up." The woman and the crowd are gone. Daniel is left lying where Orion put him, and the objective ticks off (`ch2.husbandFound`).
- **Performance:** while you're in the cantina scene, the savanna outside (which the walls hide) and the street townsfolk aren't drawn. This cuts each frame from about 3.2 million triangles to about 0.2 million, so the fight runs smoothly on phones. The townsfolk's merged meshes are also culled again when off screen, everywhere in town.
- **Music:** *Rotating Motors* (cheafpicproductions, made with Suno) is the fight track. It loops from *FIGHT!* through the K.O. (and through a retry without restarting), fades out after the fight, and follows the music volume setting. It's packed as `data/cantinaFightMusic.js`, with the source at `assets/audio/music_cantina/CANTINA_FIGHT_MUSIC.mp3`.
- **Voice:** the scene is fully voiced. *CH2CANTINA1–7* covers Orion, Daniel and the woman in the scene, the woman's scream during the fight, and Orion's two lines after the K.O. The scene's timing follows these recordings, so no line is cut off. *CH2CANTINAFIGHT1–20* are MC Irie's twenty lines (CH2HYPE1–20). Each plays with its caption, the caption stays up as long as he's talking, he isn't cut off by a routine line, and the woman waits for his opening line to finish. They're packed as `data/cantinaVoices.js` and `data/hypeVoices.js`, with the sources in `assets/audio/cantina_ch2/` and `assets/audio/hype_ch2/`. **Lip sync:** whoever is speaking moves their mouth with the voice. Orion's jaw opens with his lines (and stays shut while someone else talks), and the human townsfolk now have a mouth, so Daniel, the woman and MC Irie open theirs with the audio, MC Irie all through the fight.

### Fix: the pause menu shows the right chapter
The pause menu always said *Chapter I · Antarctica*. It now shows the chapter and place you're actually in, matching the in-game HUD: *Chapter II · Africa*, *Chapter II · Antarctica* after the ferry, or *Chapter I · Antarctica*.

## Chapter II · Arrested, and New London

After Daniel Brown goes down, four HFOS guards storm The Salt Lantern, train their rifles on you and Orion, and arrest you both (CH2ARREST1–6). A title card takes you north to **New London, Europe: the capital of the Human Federation of Sol**.

You arrive under escort in **Parliament Square**, then you're free to walk Westminster, rebuilt in Federation stone, bronze and light:
- **Houses of Parliament** with Gothic bays and pinnacles, St Stephen's Entrance, the Central Tower, and Victoria Tower flying the Federation flag
- **Elizabeth Tower (Big Ben)** with glowing seams, a halo, and four lit clock faces whose hands keep the in-game time
- **Portcullis House** with bronze chimneys and a lit window grid
- **Parliament Square** with founder statues, trees and a holographic Federation emblem
- **The London Eye** across the Thames: 32 lit pods on a turning wheel
- Westminster Bridge, the embankments, a skyline of towers, Whitehall, and hover traffic, with full day and night lighting

Objective: **Report to the Houses of Parliament.** The door guard tells you the Council isn't ready yet (CH2LONDON1–4). Saving in New London brings you back there.

### Voices, and the nightmare in New London
- The arrest and New London lines are voiced (`data/arrestVoices.js`: CH2ARREST1–6 for the arrest, CH2ARREST7–10 for the four New London lines).
- The Chapter II nightmare (James, then Croxian Mascar) happens **once**. You get it the first time you take Orion back to Antarctica, or, if you haven't done that before the arrest, in Parliament Square right after Orion mentions the war. Whichever comes first, it doesn't happen again in the other place. The New London version swaps Orion's pier and ice lines for Westminster ones (CH2ORIONALTVISION1–6, `data/lonOrionVoices.js`). The memories themselves still play out on the Antarctic pier.

### New London music, map, mobile and autosave
- **Music:** five New London tracks (`data/lonMusic1–5.js`, from CH2LONDON1–5) play in turn while you walk Westminster. Each is fetched only when it's about to play, and they fade out for the nightmare and cutscenes.
- **Map:** New London has its own drawn minimap and big map: the Thames, Westminster Bridge, the streets, the Palace, Big Ben with its halo, Portcullis House, Parliament Square and the London Eye. Landmark names appear on the big map. The research-station marker only shows in Antarctica.
- **Mobile:** on phones held sideways, the minimap sits left of the bag and menu buttons, clear of the action button, and the hotbar is a row along the bottom instead of a column through the attack buttons.
- **Saving:** only when you save. A save made between the cantina fight and the arrest goes on to New London.

## Chapter II · Thomas Hawthorne
After the door guard sends you back to wait, **Thomas Hawthorne**, Head of Government of the Human Federation of Sol, comes out to meet you with two HFOS guards. He uses the existing `tiHaw` model. How he treats you depends on your species:
- **Human:** fake friendly. Warm, apologetic, "New London looks after its own", and a soft warning to stay where his guards can see you (CH2HAWHUMAN1–8).
- **Anyone else:** openly hostile. "You will call me General", and the threat of chains (CH2HAWALIEN1–8).

Orion has known him since the war and gets the last word either way. Afterwards the objective is **Wait for the Council's summons**, and the codex's Third World War entry stops redacting Hawthorne's name. Voiced from `data/hawVoices.js` (CH2HAWTHORNEHUMAN1–8, then CH2HAWTHORNENONHUMAN1–8).

## Chapter II · The House of Commons, and the escape from New London
- **The summons:** after Hawthorne leaves, an HFOS guard takes you and Orion into the **House of Commons** (CH2SUMMON1). The chamber has green benches facing each other, the Speaker's chair under a Federation hologram, the Table with its despatch boxes and mace, and Members on their feet.
- **The trial (CH2TRIAL1–22):** President **Darius Ancin** and **Thomas Hawthorne** judge you, and the verdict is **guilty**. Then **Nico** bursts in. She exposes Hawthorne's spy (the woman with Daniel) and Terra Imperia hiring James Brown, then Croxian Mascar, to kill you. Orion speaks about the paranoia ("Croxian. Croxian. CROXIAN!"), and Hawthorne flies into a rage.
- **The escape:** you run from the Palace to a Federation ship in Parliament Square, with Orion and Nico.
  - **Hawthorne** chases you. He is level 55, has no health bar, can't be hurt, and smashes you if he catches you.
  - The whole escape is scored by **Wonders of Laniakea** (combat version), and it keeps playing when he summons his generals.
  - On the way he summons **Croxian Mascar** and **Malia de Toro** (level 20 each, with health bars). Croxian can't kill you in one blow here.
  - **Nico** (level 30, two pistols) beats them easily, with Orion backing her up.
  - Board the ship and it takes off, followed by "Escaped New London" and a Chapter II to-be-continued screen. If you die, the escape restarts from the Palace door.
- Voiced: the trial (`data/trialVoices.js`, CH2TRIAL1–22) and the escape shouts (`data/escapeVoices.js`, CH2ESCAPE1–9). The guard's summons (CH2SUMMON1) is text only for now.

### Lip sync for everyone who speaks
Hawthorne, Darius, Nico, Malia and the HFOS guards move their mouths with their lines, and Croxian's mask eyes flare as he speaks. Orion's mouth moves through the trial and the escape too. Recorded lines follow the voice; lines without a recording still move the mouth while the words appear. On phones, **Skip** during the trial jumps straight to the escape.

### Mobile, again
On phones the objective list shows only what's still to do, plus the step you just finished, so long chapters don't run over the joystick or push Orion's panel off screen. Held sideways, the dialogue box is slimmer so cutscenes like the trial and the arrest stay visible. The escape's boss bars fit between the task list and the minimap sideways, and sit above the controls upright.

## Chapter III · Sol (stage 1)
After the escape from New London, **Chapter III · Sol** begins in your ship, just off Earth.
- **Space:** the whole Sol system at game scale (planets a few kilometres across, as in No Man's Sky): the Sun, Mercury, Venus, Earth and the Moon, Mars, Jupiter, Saturn with its rings, Uranus and Neptune. Each planet has a name, faction and distance marker.
- **HD procedural planets:** cube-sphere terrain with three levels of detail, coloured by height, plus oceans, atmosphere glow and clouds (Earth, Venus). The gas giants have procedural banded skies (Jupiter's Great Red Spot, Saturn's rings).
- **Flying:** W/S thrust, A/D turn, ↑/↓ or drag to pitch, Shift for the **pulse drive** (crosses the system in seconds, off near planets). On phones: a stick, plus THRUST / PULSE / BRAKE buttons.
- **Seamless landing:** fly down onto any rocky planet (Mercury, Venus, Earth, the Moon, Mars). Below about 420 m you hit the air and the ship sets down. Then walk the surface with Orion, on the same terrain you saw from orbit. Walk back to the ship and press FLY to take off. Gas giants have no surface.
- Saves remember space (position and heading) and the planet you're on.
- **Next stages:** mining and traders.

## Chapter III · The galaxy map and the warp (stage 2)
- **Galaxy map:** press **M** in space (or tap **GALAXY MAP**). It shows the spiral disc at a tilt with all **500** systems on it. Drag to pan, scroll, pinch or use + / − to zoom, and tap a system to read about it: its star, faction, worlds and distance in light-years. Your system has a spinning marker, the one you've picked gets brackets and a dashed jump line, and systems you haven't visited have a faint ring. Faction space is tinted (Chompy Empire orange, the Order of Archamus gold, the Federation blue). The generated systems are small dots until you zoom in, get their glow as you get closer, and are all named once you're zoomed right in (zoom goes much further now). The top of the map counts how many you've visited.
- **Ten hand-made systems:**
  - **Sol:** now with **Eris**, the Erisians' frozen homeworld, and its moon **Dysnomia** beyond Neptune.
  - **Malana Prime** (the Order of Archamus): **Archiostal**, the Grek garden station, a slowly turning ring of forest under glass that orbits Malana (docking comes later); Malana, where Am-Grek was born; and a gas giant.
  - **Sagittarius A\*:** the black hole at the galaxy's core, with an accretion disc and photon ring. **Carax** circles it.
  - **Steca Prime** (Chompy Empire), in the galactic core a short jump from Sagittarius A\*: Aridaxx, the capital, volcanic Steca with lava seas, and a ringed gas giant.
  - **Janira Proxima** (Chompy Empire): a red dwarf with Janira Prime.
  - **Five uncharted systems:** Thalassa Reach (an ocean world), Cinder Vey (lava world Vey and its moon Ash), Nadir (a dying red sun and frozen worlds), Ossian Drift (a blue giant, a desert world and a ringed giant) and Halcyon (green Verdance and its moon Lull).
  - Every rocky world and moon can be landed on, and each star has its own colour and light.
- **490 more systems**, generated from a fixed seed, so the galaxy is the same on every device and in every save. The first 90 are unchanged from before, so saves made in them still work:
  - **Stars:** red, orange, yellow and white dwarfs, white stars, and blue and orange giants, each with a spectral class.
  - **Worlds:** 1 to 5 each, from lush and ocean worlds to arid, lava, toxic, frozen and barren ones, plus gas and ice giants (some ringed) and moons. Hot worlds sit close to their star and giants further out.
  - **Factions:** the 114 systems around Steca Prime and Janira Proxima belong to the Chompy Empire; the rest are unclaimed.
- **Lore:** the **Erisian Empire is a puppet state of the Chompy Empire**, and the **Order of Archamus** controls Archiostal and holds the **Grek Empire as its puppet state**. The Nostrapedia (Vishara, Hak Chompjak V, Am-Grek and Archamus), the species lore and the galaxy map all say so.
- **Warp:** pick a system and press **WARP**. The drive spools up, the stars stretch into a tunnel tinted towards the star you're heading for, there's a white-out, and you drop out beside the system's main world. You can't fly into stars or the black hole.
- **Hyperdrive range (as in No Man's Sky):** you can't jump anywhere you like. Each jump reaches only as far as your hyperdrive, so you hop from star to star.
  - **Starting drive, 3,000 ly:** reaches about a hundred systems along Sol's arm, but never the core. Sagittarius A\* and Carax, Steca Prime and Janira Proxima are all out of reach at the start.
  - **Hyperdrive Mk I, 6,000 ly:** opens the core (Sagittarius A\* is 7 hops from Sol). Costs 4 metal plates, 3 frost crystals and 1 warp cell.
  - **Mk II, 12,000 ly:** reaches all 500 systems. Costs the Mk I plus 8 metal plates, 6 frost crystals and 4 obsidian.
  - **Mk III, 25,000 ly:** costs the Mk II plus 12 metal plates, 10 frost crystals and 8 obsidian.
  - Upgrades are crafted in the inventory as **ship upgrades**. Each one replaces the last and doesn't take a hotbar slot.
- **Warp cells (fuel):** a jump burns one cell per **2,500 ly**, so most hops cost 1–2. The map's ring shows your **jump range**: your drive's reach, or less if you're short of cells. The jump line shows the cost, or turns red with *Out of range*. The panel explains what's stopping you: out of range (hop through nearer systems, or craft the next drive), or how many more cells you need. You start Chapter III with **5**. Craft more from the inventory: **2 metal plates, 2 frost crystals, 2 scrap metal** each.
- **Objectives:** after your first landing the task is *Warp to another star system*, then *Explore the galaxy*. Saves remember which system you're in, the systems you've visited, and the world you're standing on.
- **Fix:** loading a save straight onto a planet no longer shows the Antarctic sky in place of the planet's own.

## Chapter III · Mining and traders (stage 3)
- **Mining on every rocky world.** Deposits are scattered across the ground around where you land, and what's there depends on the world. Hit them (click / F, or the attack button) as you would in Antarctica:
  - **Rocks**, tinted to the planet, give stone and sometimes scrap.
  - **Metal ore** (dark boulders studded with gold-coloured metal) gives scrap metal, sometimes a ready-made metal plate. Volcanic worlds have the most.
  - **Crystal clusters** glow in the planet's own colour and give frost crystals, which go into warp cells and hyperdrives. Icy worlds have the most.
  - **Ice spires** grow on icy worlds and give ice.
  - **Obsidian** is on volcanic and toxic worlds (and rarely on barren ones). It needs an ice pick.
  - **Trees** grow in groves on lush worlds, with round crowns in the planet's own green, and give wood.
  - **Crashed supply pods** are half-buried and glowing. They give scrap, cloth and crystal, and about a third of the time a **warp cell**.
  - What you mine stays mined, separately on each planet.
- **Your ship's fabricator** counts as a crafting table within about 16 m of the ship. That means metal plates, warp cells and hyperdrive upgrades can all be crafted on any planet.
- **Traders.** Some worlds have a trader's stall near your landing spot, and you're told when you land. The minimap marks it and the galaxy map lists "trader" beside the world.
  - **Who trades where:** Chompy traders on Chompy worlds, Grek traders on Grek and Order of Archamus worlds. Erisians, the galaxy's wandering merchants, trade on Earth, on Eris and on about a quarter of uncharted worlds.
  - **Where they are:** every hand-made inhabited world has one, as do most generated Chompy worlds, about 620 worlds in all.
  - **What they sell:** warp cells, frost crystals, metal plates, obsidian, scrap and med kits.
  - **What they buy:** your ore, crystals and the rest. Warp cells can now be sold too.
  - **Prices** differ from world to world. Where a trader sells dear, they also buy cheap.

## Chapter III · Space combat (stage 4)
- **Dogfights, No Man's Sky style.** Out in space, away from planets, you'll sometimes be jumped. This starts after your first landing, roughly every minute or two when the dice say so. An alarm sounds, the combat music starts, and red markers lock onto each hostile, with name, distance and health bar. Hostiles off screen or behind you show as red dots on the screen edge.
  - **Pirates** attack across the galaxy, less often in Chompy Empire space, where the Emperor's patrols keep the peace.
  - **Terra Imperia interceptors** hunt you in Sol, in black and crimson: Hawthorne hasn't given up.
  - **In Chapter IV**, with Hawthorne gone over to the Catharsis, Sol's attackers are **Catharsis ships** instead of Terra Imperia. In Chapter V they're gone too, and only pirates are left. They look nothing like a built ship: black shards with a cold violet core and curled spines that fire violet bolts. They're tougher (85 health) and a little faster, and pay more when destroyed.
- **Your guns:** twin photon cannons. Fire with **Space**, **F** or the **left mouse button**, or the **FIRE** button on phones. When you point near a target, the crosshair turns red and your shots lead it a little.
- **Shields and hull:** hits drain your shields first, and shields recharge after 4 seconds without being hit. Once they're down, the hull takes damage and the screen flashes red. The hull doesn't recharge in space; it's patched up when you land.
- **The enemy** fly attack runs: they lead their shots, break away when they get close, and turn back for another pass.
- **Rewards:** each kill pays 40–110 units, XP, scrap metal, sometimes a frost crystal, and now and then a warp cell. Kills are counted in your save.
- **Getting away:** hostiles jam the pulse drive and the hyperdrive (no warping in combat). You can fight, outrun them (beyond 6 km they give up), or dive into a planet's atmosphere, where they break off.
- **Losing:** if your hull is destroyed, the ship is towed back to the system's main world with shields and hull restored, minus a quarter of your units.

## The core: the Grek Empire and the Catharsis
- **Chapter III:**
  - The **Grek Empire** holds Sagittarius A\* and Carax, its capital, plus a ring of 39 systems around the core (green on the galaxy map, with Grek traders).
  - Closer in, right round the black hole, are 8 **Catharsis** systems, violet on the map. The Catharsis is a **puppet state of the Grek Empire** (Am-Grek subjugated them; his Nostrapedia entry now says so).
  - In Chapter III the Catharsis is **neutral**. Their ships patrol their systems, marked *Catharsis · neutral*, and never attack. Pirates mostly stay out of their space.
  - Their worlds have **Catharsis traders**: tall robed figures with violet eyes and a hood of spines.
- **Chapter IV:**
  - The **Catharsis breaks free of the Grek Empire** and takes every Grek world but one. All 48 systems are theirs, and **Carax is their capital**.
  - **Malana** is the last Grek world.
  - Catharsis space is hostile: Catharsis ships attack there, as they do in Sol, and there are no Catharsis traders.
- **Chapter V:**
  - **The Catharsis no longer exists.** It was destroyed at the siege of Carax, at the end of Chapter IV.
  - **Its land is yours.** You defeated the Catharsis there, so all 48 systems it held (about 150 worlds, Carax and Sagittarius A\* included) become your realm's colonies, marked *won at the siege of Carax*, ready for governors in Diplomacy. Your own space has fewer pirates.
  - **Thomas Hawthorne is dead.** He died at the siege of Carax with the Catharsis. His Nostrapedia entry and the *Siege of Carax* lore event now say so.
  - The Grek Empire is back to Malana Prime (Malana and Archiostal).
  - No Catharsis ships attack anywhere; Sol and the core have only pirates.
  - The Catharsis drops out of Diplomacy. Any war you had with it ends, and a companion you'd lent to it comes home.
  - The galaxy map, system descriptions, planet factions and traders all switch with the chapter of the wanderer you're playing.

## Diplomacy (Chapters III–V)
Open **Diplomacy** from the pause menu, on foot or in space, or from the galaxy map. You can rename your own realm; the default is *The Wanderer's Dominion*.
- **Factions and leaders:**
  - **The Chompy Empire:** Emperor Hak Chompjak V.
  - **The Order of Archamus:** Archamus, in Chapter III only. In Chapters IV and V the Order is folded into the **Grek Empire**, co-led by **Archamus and Am-Grek**, and Archiostal and Malana Prime fly Grek colours.
  - **The Grek Empire:** Am-Grek in Chapter III.
  - **The Catharsis:** Lord Zark, in Chapters III and IV. In Chapter IV he's a story boss, so the Catharsis can't be warred on or defeated. In Chapter V the Catharsis is gone, destroyed at the siege of Carax, and its land is yours.
  - **The Erisian Empire:** Vishara Erisconos. Alexia Erisconos takes over once her mid-Chapter III coup happens, and Vishara returns in Chapters IV and V.
  - **Human Federation of Sol:** President Darius Ancin.
  - **Terra Imperia:** Thomas Hawthorne, in Chapter III only. Terra Imperia now holds **Mercury and Venus**.
- **War:** declare on any story faction. In Chapters III and IV you're warned first that it's not recommended because it can break quests. Win at 100 war score:
  - **+6** for each of their ships shot down. Their navy guards their space while you're at war, in their own colours.
  - **+15** for each world you occupy: land, stay within about 25 m of your ship, and hold for 30 seconds. Their capital gives **+25**.
  - You can make peace at any time, and occupied worlds go back.
  - Traders on their worlds won't deal with you during the war.
- **Casus belli:**
  - **Annihilation:** destroy them. Every world they held becomes your colony.
  - **Vassalisation:** they become your puppet. You choose their leader (their own, or one of your companions, who then leaves your crew to rule) and can rename them. Puppets can be renamed later or released.
  - **Subjugation:** like Annihilation, every world they held becomes your colony, but the **[Species] Resistance** rises from the ashes.
    - Its fighters jump you in their old space, roughly half the times you're attacked there, and your colonies there are marked *resistance active*.
    - Declare **War · Crush the resistance** (+6 per fighter shot down) to break it.
  - **Tribute:** like Vassalisation, but they keep their own leader and name and **pay you tribute**: 60–600 units, scaling with their worlds, every 5 minutes of play. You can end the tribute whenever you like.
  - **Restoration:** for 3,000 units, an annihilated empire (or one whose resistance you crushed) returns as the **[Species] Restoration** (Chompy Restoration, Grek Restoration and so on) and takes back the worlds you took from it.
- **Colonies:** land on an unclaimed world and colonise it for 500 units. Worlds taken in an Annihilation are colonies too. Appoint a **governor** to each: one of your companions, or anyone you name. Governors never rebel and never complain.
- **Lending companions:** offer a companion to another faction and they serve it until you call them home. If you go to war with that faction, they fly in its fleet as a named ace (150 health). Shoot their ship down and they eject and rejoin your crew. Win the war and they come home too. Companions never die.
- **Crew:** bring the **Project BC** characters (Josiah Richards, Peter Chambers, Gareth Williams, Kevin Murderhorn), **Lord Sevirrus**, or any character you've created aboard as companions. They follow you, fight with their own weapons, mine, and take the same five orders as Orion and James (1 Mine · 2 Explore · 3 Base · 4 Wander · 5 Follow, or the companion panel). Send them home whenever you like.

## Side quests (Chapters III–V)
**134 hand-written side quests** (119, plus 15 from the leaders in Chapter V), so the galaxy isn't empty. Each trader stall on the planets lists work under **Jobs**: two offers per stall (three on the Federation's worlds), chosen by who runs it:

| Offered by | Quests |
|---|---|
| Erisian merchants and bodyguards | 24 |
| The Chompy Empire | 24 |
| The Grek and the Order of Archamus | 20 |
| The Catharsis (Chapter III only, while it's neutral) | 10 |
| Earth's people, on the Federation's worlds of Sol | 15 |
| Anyone, anywhere | 26 |

- **Objectives:**
  - Bring materials you can mine (stone, scrap, crystal, ice, obsidian, wood, cloth, metal plates).
  - Shoot down a number of hostile ships.
  - Deliver something to a world in a nearby system. The quest ends when you land there.
  - Survey a nearby system. It ends when you drop out of warp there.
  - Settle a debt, donation or bribe at the stall.
  - Materials and bounties are handed in at the stall where you took the job.
- **Choices and alignment:** most quests end in a choice. The kind option moves you towards **hero** and the cruel one towards **villain**, by only **2 to 5 points**, and some choices are neutral. Reaching **100** either way takes dozens of quests down the same path. Your companions react to every choice, as with other good and evil deeds. Rewards are units and XP, and the cruel choice usually pays more.
- **Quest givers:** the people behind the jobs stand by the trader stalls, as Erisians, Chompies, Grek, robed Catharsis figures or humans in work clothes. Walk up, press **E** (TALK on phones) and they offer their job in their own words, or take it back when you've done it. The stall's Jobs list offers the same work.
- **Chapter V leaders:** five leaders give quests in person, three each (15 more, worth 3–6 alignment points), **one at a time from each leader**: finish Hak's current quest before he gives you his next. They won't if you're at war with their faction, or if it's been destroyed or subjugated.
  - **Emperor Hak Chompjak V** on Aridaxx.
  - **Vishara Erisconos** on Eris.
  - **President Darius Ancin** on Earth.
  - **Archamus** and **Am-Grek** on Malana.
- **Quest log:** **Side quests** in the pause menu shows your active quests (**only 5 at a time**) with their progress, lets you track or abandon them, lists what you've finished, and shows your alignment between villain and hero. The tracked quest appears under your objectives, on foot and in space, and the galaxy map marks every system where one of your quests ends with a gold diamond.


## Chapter III: the nightmare in space
Moments after escaping Earth, out over the planet, the wanderer has another episode, like the ones in Antarctica and New London. It happens once, and what they see depends on their species:

| Species | The nightmare |
|---|---|
| Chompy | **Sevirrus's cutscenes**: a fast montage of the game before this one, in its own dark and brutal style, cut together like the nightmare on the ice. It shows the Carax massacre, the siege of Aridaxx, the assassination of Damix and Jakal, and the Emperor coming apart, ending on "I am NOT WEAK!". Nostravector's subtitles, title cards and Skip button replace Sevirrus's own. |
| Erisian | A future that hasn't happened yet: **Alexia Erisconos overthrows her sister Vishara** in the Citadel el Eriscons. |
| Human | **Chapter II replayed**, with its own recordings: the farm, the cantina, the arrest, Hawthorne, the trial and the escape. |
| Am-Grek | A **prophecy** of what's coming, told without a single name: a man falling, a black banner, ships darkening the sky and an empire of glass. |

Then Orion and Nico bring them back. **Skip** jumps past the memories, then past the wake-up.

- **Music for the Chompy nightmare:** **Wonders of Laniakea** (combat version) plays across the whole montage, in place of Sevirrus's own score. That score isn't loaded at all now, which saves about 27 MB of memory on phones; the battle keeps time by its own clock. The staged fallback uses it too, with Fields of Carax only if it can't be decoded.
- **Skipping the Chompy nightmare:** **Skip** cuts to the next clip. Press it twice quickly to skip them all.
- **What was taken from Sevirrus:** only its cutscenes, with no gameplay, menus or saves. Their code sits at the bottom of `index.html` (`#sevCinePage`).
- **Assets:** the 5 models, the score and the 56 voice lines those cutscenes use are in `data/sevCine.js` (13 MB).
- **The Sevirrus game file:** `sevirrus.html` is not needed.
- **Fallback:** if the cutscenes can't load, the staged Chompy memories play instead.

- **Data for the fallback:**
  - `data/sevVoices.js`: 15 Sevirrus lines.
  - `data/sevCarax.js`: the music.
  - `data/sevDamix.js`, `data/sevJakal.js` and `data/sevSettler.js`: Damix Chompjak, Jakal Chompjak XVI and the Carax settlers, all with their Sevirrus models.
- **Loading:** these packs, and `data/sevCine.js`, load only when the Chompy nightmare plays.
- **Lines still to record:**
  - Erisian: `CH3NMERIS1–8`.
  - Grek: `CH3NMGREK1–6`.
  - Wake-ups: `CH3NMWAKECH1–4`, `ER1–3`, `HU1–3` and `GR1–3`.
