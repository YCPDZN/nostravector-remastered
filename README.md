# NOSTRAVECTOR Remastered

*Exploration Division*

A story-driven 3D sci-fi exploration game that runs in the browser on phones and desktops. It's set in **2125 AD**.

## Play

Open `index.html` in a modern browser, keeping the `data/` folder next to it. It needs an internet connection the first time, because the 3D engine (Three.js) and the fonts load from public CDNs. Everything else is in `data/`: the models, music and voice lines, one script file per asset. These are plain `<script>` files rather than fetched files, so the game still runs when you double-click `index.html` (file://) with no web server.

**itch.io:** zip `index.html` together with the `data/` folder and upload the zip as an HTML game. `index.html` must sit at the top of the zip.

## What's in the game

- **Main menu** with the wandering astronaut, Continue, New Game, Wanderers, Mission Brief and Settings.
- **Up to 500 wanderers** per save (the Wanderers screen shows how many you have, e.g. 499/500), and **up to 500 residents** living in the world (the resident list shows e.g. 312/500).
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
  - **Resident empires (Chapter III on) are OFF by default.** Switch them on with **Residents found empires** in the Resident empires panel. While off, nobody founds or expands an empire and no new wars start (any war already under way still plays out). While on, at most one empire is founded every couple of minutes, the number of empires is capped (4 to 24, scaled to your resident count) and at most six wars run at once, so a big population never spams empires.
  - When on, residents found empires on unclaimed worlds once they reach level 35 (villains first, heroes last), expand nearby, and go to war with each other using the same casus belli you have (Annihilation, Subjugation, Vassalisation, Tribute, Restoration). They **never attack the story factions** or your colonies. Wars play out over time; outcomes match the casus belli (worlds change hands, puppets, tributaries, resistances, restorations).
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
- **Commanding companions:** the companion panel and the 1–5 keys work for any companion in your party. With more than one companion, the panel shows who you're commanding; tap a name, choose Everyone, or press V to switch. Orion joins in Chapter II and Nico in Chapter III; the others join in later chapters.
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
- Each wanderer remembers exactly where they were, in every chapter, and saving, loading, Continue and going to the main menu all put you back on that spot (never a chapter's starting point):
  - **Chapter I:** in the station or out on the ice, and **behind the wheel of the rover** if you saved while driving (the rover stays exactly where you left it).
  - **Chapter II:** in Africa and Ad-Nostra, back in Antarctica, in New London, and **partway through the escape from New London** (the chase picks up where you saved, with Orion and Nico beside you).
  - **Chapters III–V:** in space, in a world's sky, on any planet, at Ad-Nostra, and **aboard the Nostra**: on the same deck, where you stood, in flight or landed.
  - Scenes you can't pause in (conversations, cutscenes, the trial) can't be saved partway through either. A boss fight saved partway through starts that fight again.
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

### Nico, companion (Chapter III on)
- **Orders, just like Orion:** **1 Mine · 2 Explore · 3 Base · 4 Wander · 5 Follow**, through the companion panel (shown as **NICO · LV n**; tap her name, or press **V** to switch between Orion, Nico and Everyone) or by walking up to her (**ORDER**). Each order gets a reply in her own words (text only for now).
- **Level 30** at the escape, and rising with you.
- **Fighting:** she draws both pistols on anything hostile nearby and fires fast, with muzzle flashes and tracers. When she mines, she swaps them for an obsidian pickaxe, then draws again when she's done.
- She shows as a pink marker on the minimap, can be lent or put on a puppet's throne in Diplomacy like Orion and James, and reacts to your good and evil deeds.
- **Main menu:** she stands on your right, with Orion on your left (beyond James, if he's still with you), and walks with you the same steady way Orion does.

### Fix: shooting animations (Orion, Nico, James and others)
- **What was wrong:** models without a skeleton are split into arms, legs and head by where each part sits. Hands, gloves and fingers hang below hip height, so they were put with the **legs**: when Orion or Nico raised their guns, their arms went up and their hands stayed at their hips. Nico's coat tails and hair were put with her **arms**, so they flew up in a black mass when she aimed, while her real upper arms stayed on her body.
- **Now:** parts are sorted by name first (hands, gloves, fingers, sleeves and shoulders go with their arm; capes, coat tails, hair and hips stay on the body), and each shoulder pivots at the top of its upper arm, not at a guessed height. Orion shoulders his rifle with both hands, Nico aims both pistols straight ahead with her coat left where it is, and James's hands come up with his rifle too.
- **Carrying a rifle:** when not firing, Orion (and anyone with a rifle) holds it at a low ready, muzzle forward and down, instead of hanging straight down into the ground.

### Fix: where you are, everywhere it's shown (Chapter III on)
- **The big map** (M on foot, or tap the minimap) is titled with the planet you're on (ARCHIOSTAL, VENUS…), with its system and faction underneath. It used to say EARTH everywhere.
- **The chapter line** (HUD and pause menu) names the planet you're on, or the system you're flying through: *Chapter III · Venus*, *Chapter III · Malana Prime*.
- **Saves** are named the same way: *Chapter III · Venus*, with *On Venus · Sol* (or *In space · Steca Prime*) underneath, instead of "Antarctic wilds" or "Station". **Continue** on the main menu says where it will put you.

### Fix: Orion missing after loading a save
- A Chapter III save always resumes in Chapter III (in space, or on the planet you were on), even if it's missing older story flags. Before, such a save could drop you back into Chapter I's Antarctica, without Orion.
- Once he's joined you, Orion now comes into every world you arrive in, however you got there, just as Nico and your crew do.
- **Only one Orion:** arriving somewhere asks for Orion twice in quick succession (entering the world, then the area's own setup). On a first visit both calls used to load him, leaving a second, frozen Orion standing in New London (and anywhere else this happened). Now every call shares the one load.

### Music in space (Chapters III, IV before the time skip, and V)
- Nine tracks play in a shuffled loop, never the same one twice in a row, while you fly and on every world you land on, carrying on unbroken through landings and take-offs: **Space Theme I–III, Vast Horizons, Wonders of the Galaxies, Inner Tranquility** and **Free Roam I–III**.
- They play in Chapter III, in Chapter IV until the two-year time skip, and again in Chapter V. Combat music takes over in dogfights, as it does on the ground.
- Each track is its own `data/spN.js` (sp1–sp9, in the order above; sources in `assets/audio/music_space/`), fetched only when it's about to play, with the next one loaded behind it, so the game's first load isn't any slower.

### The Nostra (NV1): your ship
- **The ship:** from Chapter III you fly the **NV1 Nostra**: a long black hull with gold trim, **NOSTRA** down both flanks and **NV1** on the nose and engine pods, mandible prongs at the bow, twin raked dorsal fins, open-frame wings carrying two big engine pods, and twin main engines, all glowing blue. Three rows of amber windows are her three decks. She replaces the old dropship in space, on the ground and on the main menu's space backdrop (the nightmare's prophecy fleet keeps the old silhouette).
- **Rigged:** four landing legs fold out as she sets down and tuck away on take-off, the boarding ramp lowers at the stern once she's down, her engine flames follow the throttle, and the wingtip nav lights blink red and green.
- **Aboard: three decks you can walk.** Walk up the ramp (**Board the Nostra**), or press **E** / tap **DECKS** in space (not while hostiles are about; the ship holds her position).
  - **Deck 1 · Cargo & engines:** the cargo bay, the ramp, a **crafting bench** (counts as a crafting table), a weapon rack and the reactor (check it for warp cells, drive and hull).
  - **Deck 2 · Crew deck:** bunks (**rest** to restore your health), the galley (cook), the mess table and a lounge. Companions you've dismissed wait here.
  - **Deck 3 · Bridge:** the great bow window, side stations, the **holo-table** (the galaxy map, in flight) and the **pilot's seat**: take off from the ground, or take the helm again in space.
  - A **lift** joins the decks.
  - **Tap or click anything you can use:** the lift, bench, galley, bunks, reactor, ramp, pilot's seat, holo-table and companions waiting aboard. Close by, it's used straight away; further off, you walk over (steering round tables and crates) and use it when you get there. Moving yourself cancels the walk. With a mouse, the cursor turns to a hand over anything usable. E / the action button still work as before. The hotbar and health bars stay on screen aboard.
  - **Save anywhere:** in space, aboard or on the ground. A save made aboard is called *Aboard the Nostra · Venus · Bridge* (for example) and loads you back aboard, on the same deck, where you stood, in flight or landed. The chapter line reads *Chapter III · The Nostra · Venus* (or the system, in space); it used to show the HUD's placeholder, *Chapter I · Antarctica*.

### Sol, expanded: moons and dwarf planets
Every one is landable, with its own look:
- **Mars:** Phobos, Deimos.
- **The belt:** **Ceres** (a Federation mining colony).
- **Jupiter:** **Io** (yellow sulphur plains and lava lakes, deadly), **Europa** (an ice shell with rust-brown lineae, split by cracks of open ocean you can swim in), Ganymede, Callisto.
- **Saturn:** Mimas, **Enceladus** (white ice with a few open cracks), Rhea, **Titan** (orange haze over dunes, with methane lakes you can swim in), Iapetus (two-toned).
- **Uranus:** Miranda, Titania, Oberon. **Neptune:** Triton.
- **The far dark:** **Pluto** and Charon, Haumea, Makemake, joining Eris and Dysnomia.

The galaxy map marks moons, dwarf planets and worlds with open water. Inner moons fly the Federation's flag; the outer ones are unclaimed. Icy shells use a new terrain type (`ice` in `PKIND`). Coming down over open water (Earth's oceans, Europa's cracks), the Nostra sets down on the nearest shore.

### Phones, both ways up

Every screen was checked on a phone held upright (390×844) and sideways (844×390): the menus, the Nostrapedia, Custom creations, all four chapters' play screens, inventory, crafting, the map, shops, teleporters, dialogue, the companion orders, diplomacy, side quests, Resident empires, Options, the cantina brawl, space, the galaxy map, the ship decks and the cutscenes. What changed:

- **Title screen, sideways:** the logo shrinks and the rows tighten, so all eight menu items fit (Custom creations, Nostrapedia and Settings used to fall off the bottom). The mission brief wraps instead of running off the edge, and the screen scrolls if a list is ever too long.
- **Nostrapedia tabs:** on phones the eight tabs are one row you swipe, which keeps the open tab in view and gives the file itself more room.
- **Companion orders, sideways:** the list opens as a scrollable panel beside the Following companions box, instead of running over the move stick and off the screen. Upright, it stops above the stick and scrolls.
- **Pickup messages, sideways:** they sit above the move stick, not on it.
- **Shops and other menus, sideways:** less padding and a compact header, so the lists get the height.
- **Custom creations, sideways:** a compact header and tabs, so the editor form gets the room. Sliders are taller and easier to grab on touch screens.
- "New species" no longer reads "New specie".
- The game can be added to a phone's home screen and opens full screen.

Desktop is unchanged.

### Your story in the Nostrapedia

The Nostrapedia's **Lore events** tab now records your own story from Chapters I and II, plus the nightmare at the start of Chapter III. Each event stays hidden until you finish its mission, and a toast tells you when a new one has been added. Once you are past a chapter, all of its events are there.

| Event | Appears when you… |
|---|---|
| The Survivor of the Drop | sleep at the research station (it names the leader you dreamt of) |
| The Meeting in the Snow | find James Brown out on the ice (the soldier's masters stay redacted until the trial) |
| The Super Blizzard | wait out the storm with James |
| The Betrayal at the Pier | escape Antarctica on the ferry |
| The Man Who Asked No Questions | speak to Orion |
| The Night of the Lions | check on the woman at the farmhouse |
| The Brawl at the Salt Lantern | are arrested by the Federation |
| The Trial in the House of Commons | stand trial (Hawthorne's greeting depends on your species) |
| The Escape from New London | escape to the ship in Parliament Square |
| *Your* Chapter III nightmare | have the nightmare above Earth. There are four (The Nightmare of Sevirrus for Chompy, The Vision of the Citadel for Erisians, The Nightmare of New London for humans, The Prophecy in the Dark for Grek), but your species is fixed for the whole game, so you only ever see your own |

Each event shows the people who were there, as they were at the time.

### Companions, all the same way
- **One walk for everyone:** every companion now walks with Nico's and Orion's walk: legs swinging, arms swinging against them, a gentle sway at rest. That includes James Brown (his lantern arm swings too, less when he's holding it up), the crew you recruit, and anyone who joins later. It's one shared function (`compWalkPose`), so a new companion gets it for free.
- **Give [name] orders:** walk up to any companion and the prompt names them: "Give Orion orders", "Give Nico orders", "Give Peter orders" and so on, for the crew too (before, only Orion and Nico had a prompt). Pressing E opens their orders with them already chosen. When someone joins you, the banner says "GIVE [NAME] ORDERS".
- **The Following companions box:** the box under your objectives is now called **FOLLOWING COMPANIONS**, with how many are with you. Tap or click it to see each companion's **level** and what they're doing (Following, Mining, Exploring...). Tap one (or Everyone) to give them orders. V still cycles through them on a keyboard.
- **Ready for later:** a story companion from the Nostrapedia (Khazglar, Charon, Kizna and the rest) only needs adding to your party to walk, fight, follow orders and show up in the box, using its Nostrapedia model.

### Into the atmosphere, and the real Earth (No Man's Sky style)
Coming down to a planet no longer drops you straight onto the ground. Below 420 m you fly **into its sky**, and you choose where to land.
- **Flying in a world's sky:**
  - The whole planet is there to fly over. Its ground is drawn as six faces of tiles that split finer the closer you are, so mountains rise on the horizon and the world curves away below you.
  - You get the sea, drifting clouds, a sky that's blue by day and black by night (the same 20-minute day as on the ground), and stars when you climb.
  - **W / S** throttle, **A / D** turn, **↑ / ↓** (or drag) pitch, **Shift** afterburner. On a phone: the stick, THRUST, BRAKE and BOOST.
  - The ship levels itself, and won't let you fly into the ground ("Terrain · pull up").
  - **Climb above the ceiling** (about 4 km over Earth, less over small worlds) and you're back in space.
  - The galaxy map and the decks wait until you're out of the atmosphere.
  - **Small worlds are drawn bigger** on the ground and in the air, at least 2.4 km in radius (the Moon is nearly four times its old size, a little moonlet eight), so there's room to fly. Their hills are a little gentler for it.
- **Landing where you like:**
  - Press **E** (or tap **LAND**) anywhere below about 1.5 km. The Nostra sets down a little ahead of you.
  - Over water, she finds the nearest shore.
  - Over a city or a wonder, the button names it ("LAND · PARIS") and she sets down on its landing ground.
- **Taking off** lifts you back into the sky over the same spot, ready to fly on and land somewhere new.
- **Saves:** a save made in the sky puts you back in the sky.
- **Capitals:** Alphinos, Karribassa and Citadel el Erisconos now stand at fixed places on their worlds. You can see them lit up from the air, with a marker, and fly to them. Land near one and you set down at its edge.
- **The ground is no longer a mirror image:** east is east and north is north, so what you saw from the air is where you land. Older saves on a planet are moved to match.

**Earth, as it really is.**
- **The real continents:** Earth's coastlines come from Natural Earth's 1:50m land map (public domain). Over them, by hand:
  - **Mountains and plateaus:** the Himalaya and Tibet, the Andes and Altiplano, the Rockies, Alps, Atlas, Urals, Ethiopian Highlands, Kilimanjaro, Fuji and the Southern Alps.
  - **Ice and climate:** the ice sheets of Antarctica and Greenland, plus the deserts and rainforests.
  - **Rivers:** the Nile, Amazon, Mississippi, Yangtze, Danube, Ganges, Yamuna, Congo and Seine, each carved down to the water.
- **Scale:** on the ground and in the air, Earth is drawn at 14 times its space scale (33.6 km across the middle), so crossing the Atlantic takes about a minute on afterburner. Every city and wonder sits at its real latitude and longitude.
- **Eight continents:** the HUD names the one you're over, with a banner as you cross into it: Africa, Antarctica, Asia, Europe, North America, Oceania, South America, and **Zealandia**, the drowned eighth continent (New Zealand and New Caledonia are its peaks).
- **The cities:** each has hover traffic and sights you can walk up to and read about.
  - **New Paris:**
    - The Seine runs through it, with the Île de la Cité and Notre-Dame.
    - The Eiffel Spire is re-forged in lattice with light down its edges.
    - The Champ de Mars is the landing ground. The Trocadéro faces the Spire across the river.
    - From the Arc de Triomphe at the Étoile, the tree-lined Champs-Élysées runs to the Concorde's obelisk, then the Tuileries and the Louvre with its glass pyramid.
    - Sacré-Cœur stands on Montmartre and the Grande Arche at La Défense.
    - Haussmann blocks have zinc mansards, there are bridges with gilded statues, and a maglev ring circles the city.
  - **New York:**
    - Manhattan sits between the Hudson and the East River.
    - Lady Liberty stands on her star fort in the harbour, with a fusion torch.
    - Towers include One World Trade Center (a square that turns as it rises) and the memorial pools, the Flatiron, the Empire State with its mast, and the Chrysler's steel sunbursts.
    - The Brooklyn and Manhattan bridges cross the East River. Times Square is a canyon of light.
    - Central Park, with the Reservoir, is the landing ground.
  - **New Beijing:**
    - Tiananmen Square holds the Monument, the Mausoleum, the Great Hall and the Museum.
    - Tiananmen Gate leads into the Forbidden City: red walls and moat, corner towers, and the great halls on their marble terraces.
    - Also: Jingshan's pavilion, the Temple of Heaven, the Bird's Nest, the CCTV loop, a vase-shaped supertall and hutong courtyards.
  - **New Tokyo:**
    - The Skytree stands by the Sumida, and Tokyo Tower in orange and white.
    - Sensō-ji has the Thunder Gate and its lantern, Nakamise and the pagoda.
    - Also: the Imperial Palace and its moat, the Shibuya scramble with its screens and Hachikō, and the Shinjuku towers with the twin-spired Government Building.
    - The Rainbow Bridge crosses to Odaiba, the city is full of neon, and Fuji is on the horizon.
  - **New Cairo:**
    - The Nile runs past Gezira Island and the lotus-lattice Cairo Tower.
    - Also: Tahrir and the Egyptian Museum, and the Citadel with the domes and pencil minarets of the Mosque of Muhammad Ali.
    - New glass pyramids rise in the east.
    - On the Giza plateau stand **the Great Pyramid** (the last ancient wonder still standing), Khafre with its casing cap, Menkaure, the queens' pyramids and the Sphinx.
- **The town of New Kingston** (Jamaica), on the north shore of Kingston Harbour:
  - Pastel houses with water tanks on their roofs, palms along the waterfront, and New Kingston's glass towers round Emancipation Park, where Redemption Song rises from its pool.
  - Downtown: the Parade with its fountain, the sky-blue Ward Theatre and the Parish Church. National Heroes Park, with its seven heroes and the white arch over the flame, is the landing ground.
  - Also: Devon House on its lawn, the Bob Marley Museum at 56 Hope Road with its red, gold and green gate, the National Stadium with Usain Bolt in bronze, and Hope Gardens.
  - Gantry cranes and a container ship at the port. Across the water, the Palisadoes carry the airport's runway and the Plumb Point lighthouse out to Port Royal, Fort Charles and the leaning Giddy House.
  - The green foothills of the Blue Mountains rise behind the town.
- **The New Seven Wonders:**
  - **The Great Wall:** about 3 km of wall and watchtowers over the Yanshan mountains, from the desert's edge to the sea at Shanhaiguan. You can walk along its top.
  - **Petra:** rose-red cliffs and the narrow Siq lit with candles. Al-Khazneh (the Treasury) is carved into the rock, with the Royal Tombs, the colonnaded street and the Monastery high above.
  - **Christ the Redeemer:** on Corcovado above Rio, with Sugarloaf and its cable car in Guanabara Bay. There are favelas on the slopes, and Copacabana's beach and its wave-mosaic promenade.
  - **Machu Picchu:** on its saddle between Huayna Picchu and Machu Picchu mountain, with terraces, the stone houses, the Temple of the Sun and Intihuatana.
  - **Chichén Itzá:** El Castillo with its serpent stairs, the Great Ball Court, the Temple of the Warriors and the Thousand Columns, El Caracol and the Sacred Cenote, in the Yucatán jungle.
  - **The Colosseum:** half-ruined, with the arena and its hypogeum, the Arch of Constantine, the Forum and the pines of the Palatine.
  - **The Taj Mahal:** on the Yamuna, with its minarets, the mosque and its twin, the long pool and cypresses of the garden, and the Great Gate.
- **Ad-Nostra** is marked on Kenya's coast. Land there and you set down outside the town, as before.
- **New London** is Federation airspace: you can fly past its skyline, but you're still wanted there, so you can't land.
- **Continent enemies:** away from the cities, every continent has its own wildlife, hunting in packs, alone or from the air, with neutral herds that charge if you attack them and prey that bolts.
  - **Europe:** wolf packs, brown bears, wild boar and red deer.
  - **Asia:** Bengal tigers, dhole packs, wild yaks, deer and black kites.
  - **Africa:** lions, hyena packs, buffalo, gazelles and kites.
  - **North America:** grizzlies, coyote packs, bison stampedes, deer and bald eagles.
  - **South America:** jaguars, peccary herds, tapirs, capybaras and Andean condors.
  - **Oceania:** saltwater crocodiles, dingo packs, feral camels and brumbies.
  - **Zealandia:** boar and Haast's eagles, brought back from extinction.
  - **Antarctica:** leopard seals, elephant seal bulls, skuas and penguins.
- **Trees on Earth** grow where the climate does: thick in the rainforests, sparse on the steppe, none in the Sahara or on the ice. The land beyond the ground near you is drawn out to the horizon, so you can see the city skylines and the mountains from the street.
- **Saves:** a save on Earth from before this update sets you down near where you were.

### Planet types and weather (No Man's Sky style)
Every world now has a scanner description: its **type** and its **weather**. You see it on the galaxy map, in the space HUD as you approach, on the card when you land, on the big map, and under the minimap.
- **Types** include Paradise, Faux Paradise, Lush, Verdant, Temperate, Ocean, Desert, Arid, Dusty, Scorched, Volcanic, Magma, Toxic, Caustic, Noxious, Frozen, Glacial, Arctic, Barren, Dead, Desolate, Gas Giant and Ice Giant, with "Moon", "Moonlet" or "Dwarf Planet" swapped in where it fits. Sol's worlds are written by hand (Venus: Toxic Planet · caustic acid storms; Mars: Dusty Planet · planet-wide dust storms; Titan: Hazy Moon · methane rainstorms; Io: Volcanic Moon · sulphur ash storms). The 490 generated systems get theirs from their world type and seed, the same every time.
- **True paradise** worlds have **no storms at all**: Verdance and the new **Arcadia** (golden skies) in Halcyon, plus about 30 out in the generated galaxy.
- **Faux paradise** worlds look exactly like paradise until the weather turns: the new **Siren** (Halcyon, flash superstorms with lightning), **Lorelei** (Thalassa Reach, hurricane-force storms over white beaches and lagoons) and **Mirage** (Ossian Drift, scorching firestorms), plus about 30 generated ones. Their first storm comes soon after you land.
- **Storms** come and go: calm for a minute and a half to three minutes, a **weather warning** ten seconds before, then 45 to 75 seconds of storm. Each kind looks different: rain, superstorm (with lightning and thunder), dust, blizzard, ash, firestorm, toxic rain and methane rain. The sky darkens, the haze closes in and the wind picks up.
- **Shelter:** a dangerous storm wears down your suit (the heat bar). Shelter under the Nostra (within about 10 m of it), in a shelter you built, by a heater, in a vehicle, or under water. If your suit runs out, the exosuit's emergency recovery puts you back at your ship. Gentle rain on lush worlds like Earth and Malana does no harm.
- The minimap shows the weather: the type and "calm for now", then "⚠ Flash superstorm incoming", then the storm and how long it has left.

### Fixes and phone polish (after the cantina and city update)
- **Cantinas left behind:** taking off now clears the last world's cantina, with its regulars, bartender, fighter and blood. Before, the regulars stayed standing in the world, and flying from Earth to Ad-Nostra brought Earth's cantina along next to Orion's farm.
- **Ad-Nostra state:** the Nostra parked outside Ad-Nostra now belongs to that visit only. Before, loading another save afterwards could leave the ship parked in Chapter II's Africa, with the ferry closed.
- **Storms:**
  - A cantina is now shelter from a storm, and rain no longer falls inside it.
  - A lightning flash can't follow you off a planet any more.
- **Brawls:**
  - A **FORFEIT** button sits on the fight screen (or press **Esc**), so you can walk out of a fight on a phone, where there's no pause during a brawl.
  - Whatever you were holding is put away for the fight.
  - Afterwards you're set down clear of the furniture.
- **At Ad-Nostra** the nav line points to the Nostra instead of the old station.
- **Lighter on phones:**
  - Each cantina is merged into a handful of draw calls and no longer adds a real light (which recompiled every material and cost every frame).
  - Each capital's landmarks are merged too.
  - New London's new districts share materials, so the city merges into fewer draw calls.
- **Phone layout:**
  - The galaxy map panel fits on short landscape screens instead of running off the bottom.
  - Space markers near the edge of the screen keep their names on screen.
  - Checked on a phone-sized touch screen: the weather line, MC prompt, fight choice, fight pad, stick and forfeit button, the storm HUD, New London's sights, and the Salt Lantern.

### Cantina brawls (Chapter III on)
You can now step into the ring yourself, the way Orion did in The Salt Lantern. The fight is Chapter II's: **J / click** punch (jab, cross, hook), **K / right-click** uppercut, **L** grab and slam, hold **Shift** to block, and **F** for RAGE once the meter's full. On a touch screen you get the same pad and stick.
- **Every cantina has a ladder of three fighters:** a contender, a bruiser and the house champion. Beat one to unlock the next. Each win pays a purse and XP (more in the tougher houses), and rematches pay a third. Lose and you can always run it back. Brawl health is separate from your real health.
- **The MC** stands on the bar (talk to them to fight) and shouts their own lines through the fight. **The bartender** sells a drink: 15 units for +30 health.
- **The Salt Lantern:** after Chapter II the regulars are back, and **MC Irie** runs fights from the bar. His recorded lines play wherever they fit, and the cantina owner points you at him. The fighters are Kofi ‘Big K’ Mensah, Zawadi Okafor and the Harbour Bull. Daniel's no longer on the floor.
- **On inhabited worlds:** a cantina stands a short walk from where you land, with its door facing your ship. Each species builds its own:
  - **Chompy:** violet walls, gold spikes and a dome.
  - **Erisian:** crystal spires.
  - **Grek:** timber beams and a mossy roof.
  - **Human:** steel, pipes and orange neon.

  Inside there's a ring with ropes, a bar and shelves of glowing bottles, tables, the regulars and the MC.
  - **Named houses:** The Gilded Fang (Alphinos, MC Gravvik the Loud), The Violet Tide (Karribassa, Mistress Ollara), The Billionth Year (Eris, Serelith of the Long Bar) and The Quiet Root (Malana, Old Maag).
  - **Everywhere else**, every other world with traders gets a house of its own, named from its seed (The Iron Drift, The Rusty Comet and so on), with its own fighters and MC.
- Indoors, the roof lifts away and the camera stays inside the room.

### Ad-Nostra from the Nostra
Land on Earth, board the Nostra and sit at the helm: **Fly to Ad-Nostra, East Africa** sets you down in the open ground north of Orion's farm. The town, the harbour and The Salt Lantern are a short walk west. Board the Nostra there and take off to return to orbit over Earth. Saves made at Ad-Nostra, or aboard there, come back to Ad-Nostra. The ferry south is closed while the Nostra waits outside town.

### The capitals, rebuilt
Every tower's windows are now mapped by world position, so every tower has properly sized floors of lit rooms instead of stretched noise. Windows and street lines brighten as the sun goes down. Each city has a style of its own:
- **Alphinos (imperial):** amethyst towers in gold-edged setbacks with gold crowns. At its heart is a stepped ziggurat palace with four minarets, the great spire, a beam of light into the sky, the Imperial crest turning overhead and searchlights sweeping the clouds. The **Boulevard of Emperors** runs from the palace to the **Grand Gate** facing the spaceport, with a canal down the middle, statues, braziers and crest banners. A ring road circles the city.
- **Karribassa (garden):** rounded teal towers with glass domes and terraces of gardens, glowing violet trees along the streets, and floating lanterns. At its heart is the **Hall of Oaths**, a great ribbed dome on a ring of columns with a lantern spire and an oath-flame, inside a circular canal with four bridges. Twin arches form its gate.
- **Citadel el Erisconos (crystal, new, on Eris):** a walkable city of pale lilac crystal spires. At its heart is a great crystal spire crowned by six more, with the Matriarch's faceted hall at their feet. A ring of crystal blades with four gates surrounds the plaza, shards drift overhead and **an aurora** ripples high over it all.
- **The vision's Citadel** (the Erisian nightmare) is richer too, with a polished processional floor, crystal columns, pointed windows full of aurora, the throne on three steps with a crown of crystal, and banners of the house.

### New London, expanded
Westminster now runs all the way to the Palace, rebuilt in Federation stone with light in its seams:
- **Downing Street:** a gated street west off Whitehall, with security pylons and a shimmer of a barrier. **Number 10** has its black door, white numerals, fanlight, lamp and a faint shield across the door. **Number 11** stands next door. The Georgian terrace has white-framed windows, railings, chimney stacks and aerials. The **Foreign Office** stands across the street.
- **Horse Guards Parade:** gravel, with Federation flags round it.
- **Trafalgar Square:** **Nelson's Column** with its four bronze lions and rings of light climbing the column, and two fountains with rising and falling jets lit from beneath. **The National Gallery** has a portico, dome and glowing name, **St Martin-in-the-Fields** has its spire and clock, and a Federation screen hangs on the buildings round the square.
- **Admiralty Arch and The Mall:** a red avenue lined with plane trees, lamps and Federation flags, with hover traffic overhead.
- **St James's Park:** lawns, trees, the lake with its lit bridge, and lights drifting over the water.
- **The Victoria Memorial:** white marble tiers and fountains, with a gilded figure under a turning halo.
- **Buckingham Palace:** the east front with its balustrade, centre portico and balcony with a crimson drape, a holographic crest and the Federation flag. The forecourt has black and gold railings, open gates and a shimmer of a field, and **sentries** in crimson and bearskins with a line of light across the visor.
- You can **look** at Number 10, Number 11, Nelson's Column, the National Gallery, the Palace and the Memorial. The big map names them all, and the city's bounds are bigger to fit them.

### Carax: singularity storms
Carax circles Sagittarius A*, and when the accretion disc flares the fortress world gets the deadliest weather in the galaxy (Fortress World · Singularity storms · catastrophic).
- **Warning:** 18 seconds ahead, triple alarm, "CATASTROPHIC WEATHER WARNING · GET UNDER YOUR SHIP". Storms last 70 to 100 seconds, with only one to two minutes of calm between them (the first comes 40 to 70 seconds after you land).
- **The sky:** blood-red haze two and a half times as thick as a normal storm, burning embers streaming sideways, orange flashes, and a constant rumble and camera shake.
- **Falling debris:** burning rocks come down out of the sky every second or two, sometimes three at once, often right on top of you. A pulsing red ring marks each impact a second before it lands, so you can dodge. A direct hit does up to 44 damage and knocks you flying.
- **Gravity surges:** every 6 to 13 seconds the black hole's tide lifts you off your feet and throws you sideways.
- **Radiation:** your suit lasts about 30 seconds in the open. Then there's no emergency recovery: the radiation burns straight through at 9 HP a second until you black out (you come to by the Nostra).
- **The only safe place** is under the Nostra (within about 10 m of the hull). The hull takes the debris, the surges can't reach you, and your suit recharges.

### The giants' smaller moons
Forty-nine more moons, also all landable: little grey, red, dark or icy rocks, most of them lumpy rather than round.
- **Jupiter:** Metis, Adrastea, Amalthea and Thebe close in; Leda, Himalia, Lysithea, Elara, Ananke, Carme, Pasiphae and Sinope far out.
- **Saturn:** the shepherds Pan, Daphnis, Atlas, Prometheus, Pandora, Epimetheus and Janus in and around the rings; **Tethys** with Telesto and Calypso sharing its orbit; **Dione** with Helene and Polydeuces; Hyperion, Phoebe and Ymir.
- **Uranus:** **Ariel** and **Umbriel**; Cordelia, Ophelia, Bianca, Cressida, Desdemona, Juliet, Portia, Rosalind, Belinda and Puck close in; Caliban and Sycorax far out.
- **Neptune:** Naiad, Thalassa, Despina, Galatea, Larissa, Hippocamp and Proteus; Nereid, Halimede, Sao and Neso far out.

So space doesn't fill with labels, a small moon is only marked once you're within about 15 km. The galaxy map lists the main worlds and counts the small ones under their planet (Saturn · +14 smaller moons, and so on). Every inner moon sits well clear of its planet's push-back zone, so you can always reach it and land.

### Swimming
- Walk (or fall) into deep water and you **swim**: head out, a front crawl when you move, treading water when you don't. Slower than on land; Shift / SPRINT for a hard crawl.
- **Space / UP** swims up, **C / Ctrl / DIVE** dives (on a touch screen, JUMP and DODGE become UP and DIVE). Let go and you drift back to the surface.
- **Air:** under the surface your suit's air runs down (the blue **AIR** bar); at the surface it fills again. Run out and you start to drown.
- Underwater the world closes in, tinted the colour of that sea. You can swim in Earth's seas, Europa's and Enceladus's cracks, Titan's methane lakes and any ocean world's seas. Lava is never water, and companions wait for you on the shore.

### Fix: getting stuck on the Nostra
- **The lift to the bridge** let you off inside the holo-table's footprint, so every step was refused and you were stuck for good. It now lets you off in open floor beside the table.
- **Never stuck aboard:** if you're ever standing inside something (a table, a bunk, a crate), you step straight out to the nearest open floor.
- **Never stuck outside:** on the ground, if you end up inside something you can't walk out of (the ship, deep water, a capital's tower), you're set down on the nearest open ground. Before, only things like rocks and buildings let you walk out.
- **The landed ship's footprint** matches the Nostra (her long hull, her wings and engine pods), not the old dropship's box, so you no longer walk through her wings or get caught on invisible corners. The ramp end stays open to board. Landing, blacking out and coming down the ramp all set you down by the ramp, clear of her.

### Dismissing companions
- Once you have the Nostra (Chapter III on), the companion panel has **Dismiss · wait aboard the Nostra** (or key **8**). Each companion says their own goodbye (Orion: *"I'll wait aboard the Nostra. Put the kettle on when you get back…"*; Nico: *"I'll keep the Nostra warm. Try not to get yourself shot without me."*; anyone else has a line of their own), and goes to wait on the crew deck. Future companions just add their lines to `DISMISS_LINES`.
- Walk up to them aboard and **talk** to bring them back (*"Come with me."*), or leave them be.

### Rifles and armour (craftable from Chapter I)
- **Rifles**, each upgrading the last: **Scrap rifle** (scrap, stone, cloth · 14 damage, 28 m), **Plasma rifle** (needs a crafting table · 26 damage, 38 m), **Rail rifle** (needs a crafting table · 46 damage, 55 m). Select one in the hotbar and click / tap to fire: it aims a little for you at the nearest hostile ahead, with a muzzle flash and a tracer. You carry it at a low ready and shoulder it to fire. It works on the escape's generals too.
- **Armour sets**, each upgrading the last, worn as soon as you craft them: **Scrap plate** (15% off every hit, +10 max health), **Frostguard** (25%, +20), **Obsidian plate** (needs a crafting table · 35%, +35) and **Nostra exo-armour** (needs a crafting table · 50%, +50, black and gold with a glowing core). Each set shows on you as shoulder plates, a chest plate and shin guards in its colours.

### Editing a resident
- Tap a resident on the Wanderers screen: edit their **personality**, or **Name, looks & species…** opens the full character creator for them, species included. Their level, personality, bases and empire stay theirs, and they turn up in their new look.

### Fix: the camera keeps up with the ship
- The chase camera used to ease towards its spot behind the ship at a fixed rate, so the faster you flew, the further it fell behind: at full pulse drive it trailed **over a kilometre** back and the ship shrank to a dot. It now moves with the ship every frame and only eases the turns, so it sits about 40–50 m behind at any speed, on the pulse drive and through the warp's spool-up alike.

### Fix: the helm and the holo-table aboard the Nostra
- In flight, pressing **E** (or Enter / Space) at the **pilot's seat** or the **holo-table** seemed to do nothing. The seat did hand you back to the helm, but the space controls then read that same key press as "walk the ship" and put you straight back on the bridge, so you could never fly off, and the galaxy map never got the chance to open. That key press now stops at the ship: the pilot's seat puts you back in control, and the holo-table opens the galaxy map. (Tapping or clicking them was never affected.)
- **Phones: tapping the pilot's seat from across the bridge.** Tap something aboard that's out of reach and you walk over to it, giving up with *"Can't get there from here"* if you stop getting closer. That limit counted real seconds, but on a slow phone the walk itself runs slower, so a tap on the pilot's seat from where you arrive on the bridge (behind the holo-table) often gave up halfway round the table. It now counts game time, so a slow phone walks you all the way, as a fast one does.

### Fix: saves carry on from wherever you saved (every chapter)
- **Aboard the Nostra, then the main menu:** quitting to the main menu while aboard used to forget you were aboard, so Continue put you at the helm (or at the foot of the ramp). Where you stood is now remembered before you step off.
- **The escape from New London:** a save made during the chase, loaded after reopening the game, started the escape again from the Commons doors. It now carries on from where you saved.
- **The rover:** a save made while driving came back with you on foot, standing where the rover was, and the rover as much as a second's drive behind. You're now back behind the wheel, and the rover is exactly where you saved.
- Tested by saving and loading (from the pause menu, Continue, and after reopening the game) in the station, on the ice, in the rover, in Africa, Ad-Nostra, Antarctica in Chapter II, New London, mid-escape, in space, in a world's sky, on Mars and on Earth, and aboard the Nostra in flight and landed.

### The wind, turned down
- The ambient wind (on the ice, on the savanna, on every planet, and in the blizzard) plays at about a third of its old volume, with less hiss. Calm and stormy weather keep the same difference between them; it's all just quieter.

### Fix: loading a save made in space
- Loading a save from inside the game used to show the white Antarctic landscape for a moment before space appeared: in the second between leaving where you were and the save starting, the game treated you as standing in the Antarctic station. Now it's loading from that moment. A Chapter III save shows black, then goes straight to space (or the planet you saved on), and Continue from the main menu does the same.
- In a session that had never visited Antarctica, that same moment could freeze the game. That's fixed too.

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
- **Nico joins as a companion from Chapter III**, in her normal (not pregnant) model, with her two pistols. See *Nico, companion (Chapter III on)*.
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
| Erisian | A future that hasn't happened yet: **Alexia Erisconos overthrows her sister Vishara** in the Citadel el Erisconos. |
| Human | **Chapter II replayed**, with its own recordings: the farm, the cantina, the arrest, Hawthorne, the trial and the escape. |
| Am-Grek | A **prophecy** of what's coming, told without a single name: a man falling, a black banner, ships darkening the sky and an empire of glass. |

Then Orion and Nico bring them back. **Skip** jumps past the memories, then past the wake-up.

- **Music for the Chompy nightmare:** **Wonders of Laniakea** (combat version) plays across the whole montage, in place of Sevirrus's own score. That score isn't loaded at all now, which saves about 27 MB of memory on phones; the battle keeps time by its own clock. The staged fallback uses it too, with Fields of Carax only if it can't be decoded.
- **What the montage shows, with every line voiced:** the duel at Carax ("Turn back, prince", "Everyone kneels", and "Look at your hands. Empty. Like your homes will be by nightfall."), the settlers, the siege of Aridaxx, the assassination (Jakal's "Hak. Put it down. You are still my son.", "DAMIX!" and "…I loved you."), "Long live the Emperor." and the Emperor coming apart. Each clip jumps into its scene by running it ahead silently; a line that was already starting at the jump is now said from the top, where before it only showed as a subtitle (this is what silenced Jakal's "…I loved you").
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
- **Erisian nightmare voices:** `data/nmErisVoices.js` holds `CH3NMERIS1–8` in order (sources in `assets/audio/nightmare_ch3/`), and loads only when the Erisian nightmare plays. Slot 1 (The Vision) is left empty on purpose, so that card is text only.
- **Grek nightmare voices:** `data/nmGrekVoices.js` holds `CH3NMGREK1–6` in order (sources in `assets/audio/nightmare_ch3/`), and loads only when the Grek nightmare plays.
- **Wake-up voices:** `data/nmWakeVoices.js` holds the 13 wake-up lines (`CH3NMWAKECH1–4`, `ER1–3`, `HU1–3`, `GR1–3`, in that order; sources in `assets/audio/nightmare_ch3/`), and loads when the wake-up starts. Orion's opening "Hey! HEY!" is still his recording from the ice.
- **Fully voiced.** The one exception is on purpose: the Erisian nightmare's opening card (THE VISION: "Citadel el Erisconos. Not yet. But soon.", `CH3NMERIS1`) is text only.

## Chapter III: Olympus Mons, eight floors, and Khazglar
After the nightmare in space (whichever of the four you had), the next stop is Mars. These episodes aren't stopping, and the one person who might understand them is **Khazglar**, the hermit of Olympus Mons. He's not the welcoming sort.

- **The way there:**
  - The wake-up dialogue is unchanged. Once it ends, a card reads **FIND KHAZGLAR ON MARS** and the objective becomes **Find Khazglar on Olympus Mons, Mars**.
  - In Sol a **gold marker** sits on Mars at Olympus Mons. In Mars's sky the mountain is marked in gold, and over it the land button reads **LAND · OLYMPUS MONS**.
  - Land anywhere else on Mars and the pilot's seat offers **Fly to Olympus Mons · Khazglar's hermitage**.
- **Olympus Mons** is a real feature of Mars, at its real latitude and longitude (18.65° N, 133.8° W). It's a broad shield volcano about 1.3 km across and 130 m high, with a caldera, a cliff round its foot and lava terraces. You can see it from space, fly over it and walk up it.
- **The hermitage** is empty. His stone hut, his telescope and his fire are all there, but he isn't. Behind the hut a door is cut into the rock: **Enter Olympus Mons**. A gold beacon hangs over it until you've found him.

### The dungeon: eight floors inside the mountain
- **Eight floors**, each with its own name:
  1. The Lava Tubes
  2. The Ash Galleries
  3. The Obsidian Halls
  4. The Ember Vaults
  5. The Glass Gardens
  6. The Magma Gallery
  7. The Hermit's Stair
  8. The Caldera Throne, at the summit
- **The layout:** each floor is a run of rooms and corridors, with lava cracks and pools, obsidian pillars and torches. A few of the rooms are side rooms off the main route.
- **Martian creatures** live in the dark:
  - **Rust hounds** (packs)
  - **Dust stalkers**, which stalk you
  - **Ash wings**, which fly
  - **Basalt brutes** (heavy)
  - **Cinder crawlers**
- **Getting harder:** creatures run from **level 5** on the first floor to **level 14** on the seventh. Each floor brings in new kinds.
- **Wardens:** each floor's stairs up are held by a **warden**, a huge elite brute or crawler (4 × the health, better loot). Kill it and the stairs open, and stay open.
- **The stairs:**
  - The stairs down take you back a floor. On the first floor they lead out of the mountain.
  - Coming back later, the door asks whether to climb to the highest floor you've reached or start from the bottom.
- **Healing spring:** by the stairs down on every floor. It heals you fully and needs 15 seconds to refill.
- **Grinding:** **XP is worth 1.9 × inside the mountain** (the XP toasts show "×1.9"). Everywhere else it's normal. Creatures keep coming back: a fresh pack turns up every half a minute or so, away from you, while there are few about.
- **Falling:** if you go down on a floor, Orion drags you back to its stairs with 60% health. The floor's progress is kept.
- The objective tracks the climb (*Climb Olympus Mons · floor 3 of 8 · defeat the warden*), and the minimap and marker point to the warden, then the stairs. The location line reads *Olympus Mons · floor 3 of 8 · The Obsidian Halls*.
- **No weather or cold inside.** The mountain is warm, and the planet's sky and weather are switched off while you're in it.

### The summit: Khazglar, level 15 raid boss
- **All three of you, or not at all:**
  - A curtain of fire blocks the way into the caldera, and it only parts when **Orion and Nico are both with you**. If either is dismissed to the Nostra, call them back.
  - In the fight, his hammer's **ward** turns aside three quarters of every blow unless Orion and Nico are both close by and fighting.
- **The meeting is his alone, and he tests you:**
  - He leaps down off his throne and lands in front of you.
  - Twelve lines, with only him speaking: he heard every step of your climb, sizes up all three of you, and says the voice from the core wants whoever is still standing at the end.
    - A line for your species.
    - Orion carries his past "like a stone in your pocket", and Nico's luck "does not climb mountains".
  - Each line lands with something: thuds, red flashes, the arena lights flaring, a quake, his hammer raised. It ends on **"COME. AND. FACE ME."** with a hammer slam that whites out the screen.
- **The fight** (5,000 health, under a minute with Orion and Nico pulling their weight):
  - **Hammer slam** in front of him (red ring, 25 damage)
  - **Quake**: hammer high, then a shockwave across 11 m. Jump it, dodge it, or be well clear (19 damage).
  - **Leap** onto whoever he's after, which isn't always you (32 damage)
  - **Hammer throw**: it flies end over end along a line of rings straight at you, then comes back (21 damage).
  - He switches targets every few seconds, between you, Nico and Orion. Blows that land on them make them stagger and say so.
  - **Phase 2 (60%):** *"Hounds of Olympus! Wake, and hunt!"* Three rust hounds join, and he speeds up.
  - **Phase 3 (30%):** *"Feel that? The mountain is angry. Look to the sky."* Two dust stalkers join, rock falls out of the dark on all three of you (red circles: get out), and he gets faster still.
  - The boss bar shows his level, the phase, and what to watch for.
- **Wipe and retry:** fall and the fight starts again from the top, with his health full and you back at the arena's edge. He skips the speech the second time: *"Up again? Good. The mountain is not finished with you."*
- **Beaten:**
  - He kneels: *"…Hold. Hold. That is enough."*
  - Five lines, all his. Not one of you broke, he's waited a long time for someone worth the climb, and whatever calls from the core will need more than luck. Then: "So I will come down from my mountain. Lead on. I will follow."
  - Then he **joins your crew** (+1,200 XP for the fight and +200 for joining, both at 1.9 ×).
  - He fights with his **legendary hammer**: an obsidian head bound in brass, runes burning in it.
  - **As a companion he's level 15** when he joins (the level you fought him at) and rises with you after. His hammer swings slowly but hits hard (14 + 1.1 × his level), and every blow also lands at half strength on anything within 3 m of its target.
  - The way back down is at the foot of the throne. His Nostrapedia file opens, and his old side quest is retired.
- **Next objective:** Warp to another star system.

### Meanwhile: Hawthorne on Mars
- The first time you come out of Olympus Mons with Khazglar (Chapter III), the screen goes dark and cuts away to the plain below the mountain.
- **The scene:** a red dust storm at dusk, lightning in the dust, widescreen bars and a dark vignette. The **Cygnus Terra Imperius**, Terra Imperia's capital ship, stands on its struts in the dust: a long gunmetal hull, a crescent of armour round its prow, a ring at its heart burning orange and teal, three engines, the bridge tower with its red beacon and her name in crimson on her flank. Banners of Terra Imperia stand either side of the ramp.
- **The speech:** Thomas Hawthorne, alone at the foot of the ramp under a red spotlight, gives ten paragraphs to an empty plain. The xenos go: first **Hak Chompjak**, then **Vishara Erisconos**, Matriarch of Eris, then anyone else who dares to challenge Terra Imperia. It ends: *"Sol. Is. MINE!"*
- **The army:** a white flash, and the plain behind him fills, rank after rank, in violet flashes: Terra Imperia's infantry in black and crimson armour with red eyes, rifles raised. *"HAIL THE GRAND IMPERARCH! HAIL TERRA IMPERIA!"*
- **Subtitles:** the big shaking, word-by-word subtitles of the nightmares, in **cyan** for Hawthorne (the army's chant in crimson).
- About three minutes, with no dead air: his voice and model load while you walk out of the mountain, each paragraph follows straight on from the last, and the army arrives, chants and fades out in about six seconds. **Skip** (or Escape) ends it. It plays once (`ch3.hawMars`).
- **Voiced:** Hawthorne's ten paragraphs are `CH3HAWTHORNEMARS1`–`10` in `assets/audio/hawthorne_mars_ch3`, packed into `data/hawMarsVoices.js`.

### After the speech: two new quests
- When Hawthorne's cutscene ends, two cards come up and both join your objectives:
  - **Main quest · Head to Charon.** Charon is Pluto's moon, at the edge of Sol. In space it's marked in **gold** (with its distance), and the goal line reads *Head to Charon*. Landing on Charon completes it (*YOU HAVE REACHED CHARON*). Chapter III only.
  - **Side quest (optional) · Recruit Nyrexia Erisconos on Eris.** Eris is marked in **violet** in space. Nyrexia is in the **Citadel el Erisconos**: from Eris's sky, fly to the Citadel's marker and land. She stands in the plaza before the Matriarch's crystal hall, beside her sisters **Vishara** (the Matriarch, in the middle) and **Alexia** (who hasn't turned on them yet; once Alexia's coup has happened she isn't there). The objective marker points at her. If you come down elsewhere on Eris, a message tells you to fly to the Citadel. Talk to her (*Talk · Nyrexia Erisconos*): she's heard Hawthorne's speech, her sister has sealed their gates, and she wants to come with you. Say *Welcome aboard* and she **joins your crew** (+300 XP) with the same five orders as everyone else; say *Not yet* ("Then I'll be right here. Don't take too long.") and she waits.
  - **Voiced:** `RECRUITNYREXIA1`–`5` (her three lines, then the two answers) in `assets/audio/nyrexia_ch3`, packed into `data/nyxVoices.js`.
- **On the main menu:** once they've joined you, **Khazglar** (with his hammer) stands on your left beyond Orion, and **Nyrexia** on your right beyond James and Nico. They follow your wanderer the same way Orion and Nico do. Like the others, they aren't on the Chapter IV menu.
- Saves: `ch3.charonLanded`, `ch3.nyxJoined`. A save that has already seen the cutscene gets both quests straight away.

### Khalmar, brother of Khazglar (the mountain refills every 7 days)
- **7 in-game days** after the summit is cleared (a day is 20 minutes of play, so about 2 hours 20 minutes; time on the ground and in space both count, pauses don't), Olympus Mons fills again:
  - Every floor's **warden is back**, and the climb starts from floor 1.
  - **Khalmar**, Khazglar's older brother, sits on the throne: Khazglar's build, a head taller, darker stone and a cold blue glow, with an iron hammer of his own.
  - You hear about it wherever you are, and if Khazglar is with you he feels it ("My brother is home").
  - It never happens while you're inside the mountain; it waits until you leave.
- **The fight:** level 22, 6,500 health, the same moves as his brother with harder hits (70% of their original damage, where Khazglar's are 55%). He has **no ward** and the fire lets anyone through, so you don't need Orion and Nico (bring Khazglar: he'll fight his brother). His barks: *"Children of the deep! To me!"* at 60%, *"The fire answers ME. Look up!"* at 30%.
- **What he says:** the first time, six lines (he's Khazglar's brother, "older by a winter, and wiser by a lifetime", and he wants to see why Khazglar chose you; he greets his brother if Khazglar is in your party). After that, a short greeting each time he's back. Retry line: *"Again. And this time, try to last."*
- **Beaten:** he yields, says three lines, and goes back into the fire. +1,500 XP and his hoard (obsidian, crystals, warp cells, medkits). The clock restarts: he's back in another 7 days.
- **Saves:** `wanderer.playS` (seconds of play), `ch3.khzBase`, `ch3.olyNext` (when the mountain refills), `ch3.khal` (he's on the throne), `ch3.khalMet`, `ch3.khalWins`. A save from before this update starts its 7-day clock the first time you play it.
- Khalmar's lines are text only for now.

### Saves and voices
- **Saves:** flags `ch3.khzCall`, `ch3.dgnMax` (the highest floor whose warden has fallen) and `ch3.khzMet`. A save made inside the mountain loads back onto the same floor, where you stood. A boss fight saved partway through starts that fight again.
- **Voices:** every line is voiced: 23 clips, `CH3KHAZ01`–`CH3KHAZ23` in `assets/audio/khazglar_ch3`, packed in play order into `data/khazVoices.js`:
  - `01–02`: the opening. `03–06`: the species line (human, Chompy, Erisian, Grek). `07–15`: the rest of the speech.
  - `16`: the retry line. `17–18`: the phase barks. `19–23`: beaten.

### Fix: Mars's rust hounds
- The hounds inside Olympus Mons were killing players in a few seconds. They now bite for half as much (4 at floor 1), bite less often, and run a little slower.
- Their damage also grows more slowly as you climb (+12% a floor instead of +20%), and packs on the first two floors are two hounds.
- A pack takes turns: only one hound bites in any 0.7 seconds, so a whole pack can't land at once.
- Khazglar's hounds at 60% get the same changes.
- Fix: the wardens are now drawn at their full size (they were shrinking back to normal size after spawning).

## Native species and lairs across the Milky Way (Chapter III on)
- **The galaxy map is now titled MILKY WAY GALAXY.** Its subtitle counts the lairs you've cleared.
- **A species for every system:** each of the 490 generated systems and the five uncharted ones has its own native species (495 in all), each with its own name. They're built from a seed with the species editor's body plan:
  - Legless, two, four or six legs, arms on the upright ones, and one to eight eyes.
  - Horns, tails, spikes, ears or fins, five skin patterns, and colours from their world. Some glow.
  - Each species has a temperament and a way of living ("ravenous; it feeds on heat").
  - Every species comes in castes: pack **runners**, **stalkers**, heavy **bulwarks**, sometimes flying **gliders**, and in the lairs a **matriarch**.
- **Wildlife:** the generated worlds that can hold life (lush, ocean, arid, toxic and frozen) now have their species roaming the surface, at a level that fits the system.
- **Lairs: 3,060 of them.** Every landable world in those systems holds lairs: two on a planet, one on a moon. The story systems (Sol, Malana Prime, Sagittarius A\*, Steca Prime and Janira Proxima) keep their own content.
  - **Where:** when you land, a world's lairs stand 60–110 m from your ship. Each is a stone gate glowing in its world's colour, with a beacon you can see from far off. A message says how many are nearby and names the species. The marker points to the nearest lair you haven't cleared, and the beacon turns green once it's cleared.
  - **Levels:** from level 14 near Sol to level 85 on the far arms, and higher for a world's second lair.
  - **Inside:** one to three floors of rooms full of that species, and a **matriarch** guarding the way down. The **heart**, an arena where the boss waits, is at the bottom. There's a healing spring by the stairs on every floor, and progress is kept, so you can go straight down to a floor you've reached.
  - **Themes:** each lair is themed after its world: overgrown, drowned, sunken, molten, blighted, frozen or hollow, each with its own colours, light and fog. The names fit, e.g. *The Drowned Grottoes of Ithrak*.
- **3,060 bosses, all different.** Each has its own name and title (e.g. *Morskuna the Shrike*), a giant, glowing body of its species, and lines for its intro, both phases and its death. No two have the same fight. Each one gets:
  - **Four core attacks** from thirteen, always with at least one melee attack, with their own sizes, damage, timing and counts.
  - **Its own rhythm:** a fixed order of five to seven attacks that it repeats.
  - **Phase two (66%):** one or two new attacks join the rotation, it speeds up, and it calls its young.
  - **Phase three (33%):** its signature attack joins, and it gets faster still.
  - **The attacks:**
    - *Slam*: a red ring in front of it.
    - *Nova*: jump it or get clear.
    - *Leap* onto you.
    - *Charge* along a marked line.
    - *Volley*: fans of bolts.
    - *Spiral*: arms of bolts that turn.
    - *Falling stars*: circles around you.
    - *Pools*: lingering puddles that hurt while you stand in them.
    - *Sweep*: a rotating beam.
    - *Eruptions*: lines of blasts going out in a plus or a star.
    - *Brood*: it summons runners.
    - *Vortex*: it pulls you in, then a nova.
    - *Blink*: it vanishes and comes down behind you.
  - The boss bar shows its level, its phase and what's coming next ("Next: Charge · step off the line").
  - **Wipe and retry:** if you fall, the boss is back on its perch at full health and its brood is gone.
  - **Beaten:** XP (260 + 18 per level), med kits, warp cells, frost crystals and metal or obsidian. The beacon turns green. You can go back in to grind the brood.
- **The galaxy map** lists each system's native species, how many lairs it has, their level range and how many you've cleared.
- **Saves:** cleared floors are kept per lair in `lairs` on your wanderer (`{ "<lair id>": highest floor cleared }`, and floors + 1 means the boss is dead). A save made inside a lair loads back onto the same floor.

### Lairs on the story worlds (optional, Chapters III–V)
- **20 optional lairs** on the story's own worlds, one each, playable from Chapter III to Chapter V. None of them is needed for the story.
  - **Sol:** Mercury, Venus, the Moon, Mars (separate from Olympus Mons), Phobos, Ceres, Io, Europa, Ganymede, Callisto, Enceladus, Titan, Triton, Pluto and Eris.
  - **Beyond Sol:** Malana, Carax, Aridaxx, Steca and Janira Prime.
- They range from level 16 (the Moon) to level 60 (Carax), with the same procedural bosses and themes as the rest of the galaxy. The galaxy now has 3,080 lairs.

### Chapter IV: five endgame dungeons and race armour
- **Five dungeons that open only in Chapter IV.** Each is marked with a large gold beacon near where you land, and a message names the dungeon, its boss and its armour.
- **Inside:** three floors of level 88 creatures, then a **level 90 boss** (14,000 health) on that boss's own model, at 1.45 × size. Draven is his own Chompy (bearded, not Sevirrus's model). The ghosts are pale and glowing, and float.
- **Each boss has a fixed fight:** its own attacks, its own rhythm, its own phase-three signature and its own lines.

| Where | Dungeon | Boss | Fight (core · phase 2 · signature) | Armour (level 90) | Who can wear it |
|---|---|---|---|---|---|
| Aridaxx | The Usurper's Crypt | Draven, Disciple of Sevirrus: a bearded Chompy of his own, in his master's black and red armour | slam, charge, blink, volley · his legion, nova · sweep | Armor of Lord Sevirrus: 62% off every hit, +85 health | Chompy |
| Eris | The Tomb of Lianna | Ghost of Lianna Erisconos | blink, spiral, falling stars, pools · eruptions, vortex · spiral | Armor of Lianna Erisconos: 60%, +100 | Erisian |
| Malana | The Halls of Grekicus | Grekicus I | slam, leap, nova, charge · brood, falling stars · eruptions | Armor of Grekicus I: 60%, +105 | Grek |
| Janira Prime | The Founder's Vault | Ghost of Shakhak Chompjak | charge, slam, volley, leap · nova, sweep · falling stars | Armor of Shakhak Chompjak: 58%, +115 | Chompy |
| Earth | The Last Marshal's Bunker | Field Marshal Konrad Hale (Third World War) | volley, artillery, charge, gas pools · reinforcements, minefield · minigun spiral | Armor of Field Marshal Hale: 60%, +100 | Human |

- **The armour is locked to one race.** A Chompy can't wear an Erisian's set, and so on, and each set also needs level 90. You always get the set when you beat its boss. If you can't wear it yet, it waits in your bag and goes on as soon as you can.
- If you own two sets you can wear (a Chompy with both Chompy sets), the one later in the armour list (Sevirrus's) is the one you wear.
- These sets are the best armour in the game. They show on your suit in their own colours.
- The Earth dungeon's gate stands near wherever you land on Earth.

### Mobile: lairs and dungeons on phones
- **The boss bar on phones:** held upright, it sits under the companions button, clear of the objectives, the minimap and the side hotbar. Held sideways, it sits low in the middle, between the joystick and the buttons. Long boss names stay on one line and end in "…", and the level, phase and next attack are smaller.
- **The right button label:** the action button now reads **ENTER** at a lair's gate (and at Olympus Mons's door), **GO** at the stairs and **DRINK** at the healing spring. Before, it said "Pick up · …" and **TAKE**.
- **Lair names before you choose:** using a lair's gate shows its name, level and species on a card above the choice. The choice box has no title of its own, so on a phone you couldn't see which lair it was.

### Nostrapedia: Disciples of Sevirrus
- A new lore event, **Disciples of Sevirrus** (1800 AD to the present), comes after *Sevirrus' Redemption*. It's about the outlawed order that follows the usurper Sevirrus was, not the emperor he became:
  - The last of his guard carry his black plate out of burning Alphinos in 1800.
  - They wait 26 years for him, then see him come out of prison as Hak Chompjak, break the Cult of Zark and ask forgiveness. To them, that is the real betrayal.
  - They swear Hak will never wear the Usurper's armour again, and build the Usurper's Crypt around it beneath Aridaxx.
  - Their master today is Draven.
- **On the stage:** Lord Sevirrus, with Draven beside him from Chapter IV.
- **What you can see when:** Draven's name and the crypt are blacked out until Chapter IV. Once you've beaten Draven, a last paragraph tells of his death and the wanderer who walked out carrying the Armor of Lord Sevirrus.

## Equipment, ores and the furnace (every chapter)
- **Equipment slots:** armour now goes on and comes off piece by piece in four slots: **Head, Chest, Legs and Feet**. You can mix pieces from different sets.
  - **Inventory → Equipment** shows what you're wearing, your total protection and bonus health. Each slot has a **Take off** button, and each piece in your bag has **Put on**, which is greyed out with the reason if you can't wear it.
  - **New pieces go on by themselves** if their slot is free or they're better than what's there. A single piece never pulls off a suit you're wearing.
  - **Suits:** the old whole sets (scrap, Frostguard, obsidian, Nostra exo-armour and the five Chapter IV race sets) are **suits**, and a suit fills all four slots. Putting a piece on takes the suit off, and putting a suit on takes the pieces off.
  - Protection from everything you wear adds up, to a maximum of 85% off every hit.
  - **Older saves** put on the suit you were already wearing, so nothing changes until you choose.
  - Each piece shows on your suit: a helmet (a band above the brow, cheek guards, a cap and a crest), a chestplate front and back with shoulder plates, leggings (plates all round the thigh, knee cops) and boots (greaves and armoured toes). Suits look as they did.
  - **Fix:** armour now shows at the right size on Chompy, Erisian and Grek wanderers. Their arm and leg plates used to shrink to almost nothing inside their models, and that included the old suits' shoulder and shin plates.
- **Five new armour sets** with four pieces each: helmet, chestplate, leggings and boots. The ingots each piece costs follow the classic 5 / 8 / 7 / 4.

| Set | Made from | Full set | Notes |
|---|---|---|---|
| Padded | cloth | 10% · +8 health | early, before any ore |
| Copper | copper ingots | 20% · +14 | |
| Iron | iron ingots | 32% · +24 | |
| Gold | gold ingots | 26% · +45 | less protection, much more health |
| Titanium | titanium ingots | 46% · +60 | needs a crafting table |

- **The hotbar:** under **Gear · hotbar** in the inventory, every tool, weapon, food and placeable has **Put on** and **Take off** for the hotbar, and shows which slot it's in.
- **The Craft list** has filters: All, Tools, Armour, Food · med, Build and Materials.
- **Ores:** new veins appear on every rocky world. Each is a dark boulder shot through with the ore's colour.

| Vein | Gives | You need |
|---|---|---|
| Coal seam | coal (furnace fuel) | bare hands |
| Copper vein | copper ore | bare hands |
| Iron vein | iron ore | an ice pick |
| Gold vein | gold ore | an ice pick |
| Titanium vein | titanium ore | an obsidian pickaxe |

  - **Where:** lush worlds have the most coal, volcanic worlds the most gold, and barren and icy worlds the most titanium. Antarctica has coal, copper and iron in its rock too.
  - The ores, ingots and alien meat sell to traders.
- **The furnace** (build menu → Structures; 8 stone and 2 scrap). Walk up and press E (**SMELT**).
  - **Fuel:** a lump of coal smelts 8 things and a piece of wood smelts 2.
  - **Smelting:** copper, iron, gold and titanium ore into ingots (4–7 seconds each), and 3 scrap into a metal plate (6 seconds, no crafting table needed).
  - **Cooking:** raw meat into roast meat, alien meat into a **Seared alien steak** (restores 45 health), and blubber into a seal ration.
  - **How it works:** queue one, or **All** that you have. The furnace works through the queue one item at a time while it has fuel, and **keeps going while you're away**, so come back and **Collect all**. You can cancel a queued job for its ingredients back. It glows while it burns.
- **Alien meat:** the native species of the generated worlds now drop alien meat. Matriarchs and bulwarks drop two.
- **Titanium pickaxe:** upgrades the obsidian pickaxe (3 titanium ingots and 2 wood, at a crafting table). It does four times the mining and melee damage.
- **Saves:** what you're wearing is kept in `inv.eq` (`head`, `chest`, `legs`, `feet`, or `suit`). Each furnace keeps its fuel, queue and finished items with what you've built.

## Residents: their gear and their guilds
- **Residents craft armour too.** As they level, they forge the same sets you can, a piece at a time, in their own order, over what they had before:
  - **Padded** from level 8, **Copper** from 16, **Iron** from 28, **Gold** from 44 (about half of them prefer iron), and **Titanium** from 60.
  - **At level 90** they wear their own race's endgame suit: Field Marshal Hale's (Human), Lianna's (Erisian), Grekicus I's (Grek), or Shakhak's or Sevirrus's (Chompy; the villains wear Sevirrus's).
  - They wear it on their own bodies, piece by piece, and tell the zone chat when they finish one ("just forged my iron chestplate!").
  - Now and then one stops to work at the forge, hammering with sparks flying ("smelting some iron ingot", "hammering out a new helmet").
  - "What are you up to?" in their talk menu shows their gear and protection.
  - **Fix:** residents no longer appear wearing a copy of your armour. Their bodies are copied from your model, and your armour used to come along with it.
- **Guilds.** Residents band together in guilds with other residents, from level 6.
  - Every guild has a name, a tag (e.g. *The Iron Covenant [IC]*), a leader and up to 30 members. There can be about one guild per 12 residents (around 42 with 500).
  - Built for a big world: guild activity works through 60 residents at a time, with at most 6 joins, 1 new guild, 2 departures and 2 dungeon runs per update, so the chat never floods. Guild lookups, resident lookups and base collisions are indexed, and only the 40 nearest bases are built as 3D models (the rest stay solid).
  - A guild takes the alignment of its founder. Heroes and villains never share a guild, but neutrals can join either.
  - Members come and go, a guild passes to a new leader when the old one leaves, and an empty guild disbands.
  - Joins, departures and new guilds appear in the zone chat with a ⚑, and members' names carry their guild tag there.
- **Invites.** A resident in a guild may walk over and ask you to join, with three answers:
  - **Join** the guild.
  - **Not right now:** that guild won't ask again for 20 minutes.
  - **Stop asking me:** this turns guild invites off.
  - A guild only asks if it has room and would take someone of your alignment. Invites are a per-wanderer option and can be turned back on in **Pause → Guilds**.
- **In their talk menu:** *About <guild>…*, *Ask to join <guild>* (they may turn you down over your alignment, or because they're full), and, if you lead or belong to a guild, *Invite them to <your guild>* (they may prefer to stay solo for now).
- **Pause → Guilds** (once you have residents):
  - The invites toggle.
  - Your guild with its members, and **Leave the guild**.
  - **Found a guild** of your own, which residents can then be invited to.
  - Every other guild, with members' levels, alignment and gear, and **Join** where they'd have you.
  - The recent guild news.
- **Guildmates:** residents in your guild greet you with the guild tag when they arrive, hand you gifts more often (villains in your guild too), and never grab deposits near you.
- **Saves:** guilds are saved with the slot (`resGuild`). Your guild and your invite setting are saved on your wanderer (`guild`, `guildInv`).

### Tested on phones
- Upright and sideways (iPhone size), with no errors: the inventory with its Equipment slots and craft filters, the furnace, the Guilds panel, and a resident's guild invite all fit the screen and scroll.

## Dungeon runs and guild wars
- **Residents go dungeon exploring.**
  - **With you:** residents near you fight hostile creatures, including lair creatures and **lair bosses**, running in and trading blows ("BOSS! everyone on it"). Heroes are the keenest, villains the least. They follow you into lairs as they follow you anywhere.
  - **While you're away:** a resident of level 14 or more sometimes runs a lair on the world they're on (or one at their level), taking up to three guildmates of a similar level. Whether they clear it depends on their level against the lair's and how many of them go.
  - Runs are announced in the zone chat with ⚔ ("[VW] Drax and Korr cleared The Rooted Thicket of Ryrognor · Ryrognor is dead"), or they wipe.
  - **Where it shows:** their talk menu ("Lairs cleared: 5"), the Guilds panel (every member's count, and a **Dungeon runs** list), and the galaxy map ("residents cleared 2" beside a system's lairs).
- **Your companions go dungeon exploring.** There's a new order, **9 · Explore a dungeon · clear a lair here**, in the companion menu. It shows on worlds with a lair, from Chapter III.
  - The selected companion (or **Everyone**) heads into the nearest lair you haven't cleared (or a cleared one, for the loot) and leaves your party while they're gone.
  - **How long:** about 1–4 minutes depending on the lair. More companions are faster, and more companions and higher levels give a better chance.
  - **If they win:** they come back with XP for you (half for a lair you'd already cleared), med kits, crystals, metal or obsidian, ore, alien meat and sometimes a warp cell. The lair counts as cleared.
  - **If they lose:** they come back empty-handed and tell you the boss was too strong.
  - The Chapter IV dungeons are yours alone: companions won't take them.
  - **Saves:** kept in `dungeon` on your wanderer, so a run carries on through a save and finishes when you're next playing.
- **Guild wars.** When two residents from different guilds come to blows, **their guilds go to war**. A fight can also break out when a hero and a villain from rival guilds argue.
  - **The brawl:** every member of both guilds who's around piles in, paired off against each other, and anyone left over runs in to back up their guildmate ("GUILD FIGHT", "nobody touches my guild"). A "Guild war" banner shows the two tags.
  - **During the war:** members of the two guilds fight whenever they meet. Skirmishes play out while you're away, weighted by the guilds' levels, and after 30 minutes the guild that won more of them wins the war (or it's a draw). All of it goes in the zone chat.
  - **The Guilds panel** shows each war with its score and time left, and a **Broker peace** button (a small good deed).
  - **Saves:** wars are saved with the guilds (`resGuild.wars`, and runs in `resGuild.dun`).

## Mobile pass (every screen, four phone sizes, both ways up)
I checked every major screen and mode on four phone sizes, upright and sideways: a small iPhone (375 × 667), a small Android (360 × 740), a standard iPhone (390 × 844) and a large Android (412 × 915).
- **What was covered:**
  - **Menus:** the main menu, Wanderers, Settings, Mission brief, Save / Load, character creation (all three tabs), the Nostrapedia (tabs and an entry), and Custom creations (all four tabs and the species, planet and adventure editors).
  - **On a planet:** the HUD, the companion menu, pause, inventory, build menu, trader, teleporter, map, dialogue and choices, Alignment, Side quests, Diplomacy, Resident empires, Guilds, the furnace and a lair gate.
  - **Space:** flight, pause, the galaxy map and a system's panel.
  - **Your ship:** walking the decks.
- **How:** an automatic check looked for controls you can't reach (off the screen, or covered by another control), text too small to read and sideways page scrolling, and I looked over the screenshots by eye.
- **Fixed:**
  - **Space, paused:** the flight controls (FIRE, THRUST, PULSE, BRAKE, the stick) and readouts were drawn on top of the pause menu and covered its buttons. They're hidden while you're paused.
  - **Companion menu (upright phones):** with two or more companions it ran down over the action buttons, and ORDER, BUILD, BLOCK, SPRINT and DODGE sat on top of it. It's now a panel of its own above the controls, with the companions in one row and the orders two to a row, so all of them fit without scrolling.
  - **Action button vs hotbar (upright phones):** the ORDER / TAKE / ENTER button sat on top of hotbar slots 5 and 6. It's now just left of the hotbar column.
  - **Galaxy map (upright phones):** the title's second line ran under the Diplomacy, Residents and Empires buttons, which now sit below it.
  - **Galaxy map's system panel (phones):** the warp button and its explanation covered most of the panel and you could see the text through them. The footer is now compact and solid, and upright the panel is taller.
  - **Map:** the place name ran under the Close button.
  - **Space (upright):** the target's name and distance ran under the DECKS button.
  - **Sideways on small phones:**
    - The pause menu's bottom row (Options, Main menu) and the inventory's Close button were off the screen. The pause menu, inventory and furnace now fit, or scroll.
    - The residents' chat printed over your objectives and health bars. It now sits below the companion button.
    - The space readout now stays clear of the GALAXY MAP button.
    - "Drag to rotate" no longer overlaps the character-creation heading.
  - **Nostrapedia and Custom creations, sideways:** the characters and creations stood hidden behind the text panel, because a sideways phone was being framed as if it were upright. They now stand beside the panel.
  - **Inventory on phones:** new jump buttons (Equipment · Resources · Gear · Craft) take you straight to each section of the long single column.
  - **Bigger touch targets:** the furnace's fuel buttons, the craft filters and the inventory's buttons are at least 34 px tall.
  - **Readable text:** the minimap's distance and weather lines went up from 6–6.5 px to 7.5–8 px.
  - **Long boss names:** upright, they wrap onto two lines instead of being cut short.
  - **Very short upright phones:** the small logo on the main menu steps aside to leave room.
- **Not covered:** this was done in a desktop browser emulating each phone, not on real devices. Touch feel, frame rate, battery and memory on a real phone, and the Chapter I–II story scenes (they need their own saves), weren't checked.

### Olympus Mons, made easier
- Creatures are **level 5–14** (were 10–30), with about a quarter less health on the first floor, much slower growth up the mountain, and roughly **half the damage**.
- **Wardens** have about half the health they did and hit only a little harder than their floor.
- **Fewer creatures:** fewer rooms hold anything, packs are smaller, and fresh ones trickle back about every minute (was every half minute), with fewer alive at once.
- **Khazglar:** 5,000 health (was 9,000) and 55% of his old damage. His ward without Orion and Nico now lets half of each blow through (was a quarter).
- **Khalmar:** level 22, 6,500 health (was 11,000) and 70% of the old damage.
- The **healing spring** refills in 15 seconds (was 40).

## The Taredesibans (residents only)
- A people of their own that only **residents** can belong to: they're **not a playable race**, so they never appear in the wanderer creator.
- **Their look:** tall (about 1.98 m), smooth pale-blue skin, a tall cranium with swept-back pointed ears, a short dark beard, and dark indigo armour engraved with curves, with glowing teal inlays (a V across the chest, a gem at the heart, lines down the gauntlets and greaves), violet lines on the thighs and spine, three flared plates on each shoulder, and a sheer teal cape.
- **The model** is fully rigged (the same 18-bone skeleton as the other rigged characters), so they walk, wave, dance, mine and spar like every other resident. It's built by `nightmare/tools/build_taredesiban.py` (`python3 build_taredesiban.py out.glb`) and lives in `data/taredGlb.js` (the GLB is also in `assets/models/characters/taredesiban.glb`). It only loads when a Taredesiban is around.
- **Making one:** in the personality panel, when you **send a wanderer into the world** or **edit a resident**, pick **Their people: Taredesiban** (or keep the species they were made as). Changing it on an existing resident takes effect the next time they turn up.
- They keep their own armour (crafted armour isn't put on over it), and their talk menu and the resident list say *Taredesiban*.

## The Republic of Timpur
- A faction at the **far edge of the galaxy**: the tip of the outer spiral arm beyond Janira Proxima, on the opposite side of the galaxy from Sol (38 systems).
- **A puppet of the Chompy Empire:** it elects its own senate and First Consul, but Aridaxx decides its wars and treaties.
- Its capital is **Timpur** (the outermost of its systems), with its capital world **Timpur Prime**.
- On the galaxy map its space is washed in teal, and its systems and worlds read *The Republic of Timpur · puppet of the Chompy Empire*. Its traders are Chompy traders.
- Resident empires never expand into it (it isn't unclaimed).

## Phones and tablets (today's additions)
- **Hawthorne on Mars:** on a phone the widescreen bars are thinner (thinner still held upright) and sit under the game's controls, so **Skip** is always visible (this also fixes Skip being hidden behind the bottom bar on computers). Held upright, the camera uses a wider lens so Hawthorne and his ship stay in frame. Phones get a lighter scene: a smaller army (4 ranks of 7 instead of 6 of 9, built a few at a time, without shadows), less dust, fewer rocks, a simpler ground and smaller shadows.
- **Main menu:** held upright, Khazglar and Nyrexia (the outermost of your crew) step in closer so they stay on screen.
- **Residents:** phones build the 16 nearest resident bases as 3D models (40 on computers); Taredesibans are drawn without shadows like every other resident on a phone.
- **Nyrexia, Khalmar and the new panels** use the game's existing touch prompts (*TALK*) and the panels' own wrap-around buttons, so they work by tap.

## Diplomacy: the Republic of Timpur and the resident empires
- **The Republic of Timpur is a diplomacy faction** (Chapters III–V), like the story's factions: led by *the First Consul, answering to Aridaxx*, teal, with its 38 worlds and its capital Timpur Prime (+25 war score when occupied). You can lend it companions, and declare any casus belli on it (Annihilation, Subjugation, Vassalisation, Tribute; Restoration afterwards). Its fleet is the **Timpur Republic Guard**. It's a separate faction from the Chompy Empire: a war on one isn't a war on the other.
- **Resident empires in the Factions tab:** a *Resident empires* card (how many stand, or that founding is off, with **Open Resident empires**), then a card per empire: its ruler (level and alignment), its worlds, whether it's a puppet, a tributary or a resistance, who it's at war with, which of your companions serve it, and **Demand they disband** (tap twice).
- **Offer companions to resident empires:** in the Crew tab, the *Offer to a faction…* list has the story factions and, below them, every resident empire. A companion serving a resident empire:
  - leaves your crew and fights in its wars: each one adds a lot to its war strength (+10 power, about as much as two and a half worlds), so they swing who wins.
  - shows up on its card in Diplomacy and on its row in the Resident empires panel (*serving them: …*), and the empire's log notes their arrival.
  - comes home when you call them back, or by themselves if the empire is annihilated or disbanded.

## Faction leaders: fight them in their halls (Chapters III–V)
- **At war with a faction?** Land on the world where its leader holds court and a **hall** stands near your ship (gold beacon, *Enter · The Hall of …*). Inside is a lair arena with the leader on the throne. **Beat them and the war is won** (100 war score); then settle it in Diplomacy as usual. Each war has its own hall, so a new war means a new fight. Diplomacy's war card says who waits and where. Fall, and the fight starts again from the top, as in any lair.
- **The leaders** (level · health · where · theme):

| Leader | Level | Health | Where | Theme |
|---|---|---|---|---|
| Emperor Hak Chompjak V | 95 | 26,200 | Aridaxx | *The Descendant of Shakhak* |
| Archamus (Order of Archamus, Chapter III) | 100 | 30,000 | Archiostal | *The Prime Good* while hooded; at phase two **he unmasks** (his unhooded model) and *The Light Egg* begins |
| Am-Grek (Grek Empire) | 85 | 17,000 | Carax in Chapter III (alone); Archiostal in IV–V | *Wonders of Laniakea (Combat)*, for now |
| Archamus, unmasked (Grek co-leader, IV–V) | 100 | 30,000 | Archiostal, straight after Am-Grek falls | *The Light Egg* |
| Vishara Erisconos | 80 | 14,800 | Eris | *The Child of Eris* |
| Alexia Erisconos (Chapter III, once she's taken the throne) | 80 | 14,800 | Eris | combat music |
| President Darius Ancin | 75 | 11,000 | Earth | *The Guardian of Humanity* |
| Taredesiba VI, First Consul of Timpur | 90 | 22,400 | Timpur Prime | combat music |
| Lord Zark (Catharsis, Chapter III) | 100 | 30,000 | the Catharsis's capital world | *The Prime Evil* |
| A companion you put on a puppet's throne | their own level | | the puppet's capital | *The Wrong Enemy* |

- Hak is far tougher than Draven (level 90, 14,000 health). Each leader has their own moves, words for the start, phase two, phase three and their defeat, and their own model (Taredesiba VI is a Taredesiban), a little larger than life. Leaders **yield**, they don't die.
- **Resident empire rulers:** each resident empire's card in Diplomacy has **Challenge <ruler> (lv …)**. Use it on any world's surface: you face the ruler (at their level, as their species or a Taredesiban) to *The Wrong Enemy*. Win and their empire falls: its worlds are unclaimed again.
- **Your own companions in an enemy fleet:** when a companion you lent to a faction you're at war with comes at you in space, *The Wrong Enemy* plays until they're shot down.
- **Not yet:** the **Final Boss theme** (`data/thFinal.js`) is stored for Lord Zark's Chapter IV story battle (level 60, on Carax), which isn't built yet. Hawthorne (Terra Imperia) has no hall.
- Files: themes in `data/thHak.js`, `thPrimeGood.js`, `thEris.js`, `thDarius.js`, `thLightEgg.js`, `thWrong.js`, `thPrimeEvil.js`, `thFinal.js` (originals in `assets/audio/leaders_themes`); Archamus unhooded in `data/prArchamusU.js` (`assets/models/primes/archamus_unhooded.glb`). They load only when needed.

## Croxian, without his helmet
- **As your companion**, Croxian Mascar no longer wears his helmet. Under it he has his father's face (Orion's, without the beard or the cybernetic eye) and Orion's short brushed hair, cut shorter and **black**. He keeps his armour, collar, cloak and scythe.
- This is the companion's model only (`data/cpCroxianU.js`, also `assets/models/companions/croxian_unhelmeted.glb`): wherever your companion Croxian appears (your crew, his Nostrapedia companion page). The story's Croxian (Chapters I and II, the nightmare, Terra Imperia's general) keeps his helmet.
- Built from the two original models by `nightmare/tools/croxian_unhelmet.py` (`python3 croxian_unhelmet.py data/cpCroxian.js data/cpOrion.js out.glb`).
- **His height:** your companion Croxian now stands **1.85 m, the same as his father Orion**. He used to come out at about 1.34 m: the game sized characters by everything in their model, and his scythe reaches far above his head, so the scythe was being fitted to his height (and pulled him off-centre). A first fix missed most of the scythe's parts (the loader spells their names with underscores), so he still came out short; now the whole scythe is left out of the measurement. Carried weapons no longer count toward anyone's height, in the game and in the Nostrapedia; Croxian was the only character affected. (The story's Croxian in Chapters I and II is unchanged.)
- **Nostrapedia too:** Croxian's entry in the Companions section of the Nostrapedia now shows him at 1.85 m, beside Orion at the same height (it sized him by his scythe as well).

## Javek, and meeting Chapter III's people

- **Javek** joins the Nostrapedia twice: under **Companions** and under **Ancient Figures**. Both files stay **[Redacted] until Chapter IV**, when he appears. He's the last leader of the Grob Robotic Collective, the one Shakhak Chompjak beat at Steca, written to fit the lore already in the Nostrapedia (Shakhak, Lianna, Obsidnia).
- **His model** (`data/cpJavek.js`, `assets/models/companions/javek.glb`) is your rigged Javek with the **red optical sensor and the smoked lens taken out** (and their glints). **Green eyes** now sit in both goggle rings: a white eyeball, a glowing green iris and a dark pupil, skinned to his head bone so they move with him. Built by `nightmare/tools/javek_green_eyes.py`.
- **Chapter III's people are classified until you meet them.** Reaching Chapter III no longer opens their files on its own. Each file reads *"Unlocks in Chapter III, when you meet them"* until you do:
  - **Terra Imperia:** Hawthorne opens at the trial, in the Human nightmare or after his Mars speech. Alexia opens in the Erisian vision or at the Citadel. James, Malia and Croxian open where the story put you face to face with them.
  - **Companions:** Charon and Kizna open once you land on Charon. Nyrexia opens when you speak to her in the Citadel. Croxian, Malia and James open as above.
  - **The four leaders** open when you meet them (a dream, the story, the Citadel for Vishara) or face them in their hall. Your own race's leader still opens after Chapter I's first night.
  - Once you're past Chapter III, everyone from it is open, apart from leaders you have never met or fought.
- **Green eyes in both files:** the Ancient Figures Javek uses the same green-eyed model as the companion. Nothing in the game uses the red optic.
- **Javek the fugitive (companion):** the companion Javek wears **Hak Chompjak's style of glasses** (taken from Hak's own model: round lenses, navy frames, a V bridge, a glint; the blue tint is lighter so his green eyes show through) over a matching pair of green eyes, a **black hood** (open at the face, his long ears out through the sides) and a **black cape** to the backs of his knees. The hood is skinned to his head; the cape follows his chest, spine and hips as he walks. The goggles, their bolts and strap are gone. Model: `data/cpJavekC.js` / `assets/models/companions/javek_fugitive.glb`, built by `nightmare/tools/javek_fugitive.py` from the green-eyed model and `data/leader_chompy.js` (for Hak's glasses). The **Ancient Figures** Javek keeps his goggles with green eyes.
- **2014:** both files now say Javek came face to face with **Director Josiah Richards**, a British civil servant in the Cabinet Office, over a set of schematics. That's this world's Josiah Richards, the great-grandfather of Josiah Williams II, not the Prime Secretary.


## Phones

- **Lighter start-up:** Javek's two models and the helmetless Croxian (about 9 MB together) no longer download when the game starts. Each one loads the first time it's actually shown: in the Nostrapedia, as a companion, or as an Adventure hero.
- **Classified labels fit:** on a phone, the "when you meet them" labels shorten to *Ch. III · once met* / *Ch. III · meet or fight them*, and every Nostrapedia label wraps instead of widening the list.

## Javek's family

- **Javek's Ancient Figures file** now gives his birth (7,000,000,000 BC) and his family: his mother **Marissa** (deceased), his father **Jaximus, the Destroyer of Haeca** (deceased) and his grandfather **Roximus, the Builder of Haeca** (deceased). It also says he met **Maraxos II** as a child, rose to be his trusted royal chancellor, and then overthrew him.
- **Jaximus has his own Ancient Figures file**, redacted until Chapter IV like Javek's. He was a subordinate of the Xyperion Communist Grob Republic who destroyed the Haecan Republic by causing a nuclear winter, and was killed by Maragroxis VIII. The file also covers his father Roximus, the Builder of Haeca, killed by Maragroxis VII. Jaximus is shown with **red skin, like Roximus**, and a dark red coat over his torso instead of Javek's navy one: it's Javek's model recoloured in the game, so there's nothing extra to download.


## Chapter III: Charon, James Brown's revival, and the Pontifex Maximus

- **Charon and Kizna.** When you land on Charon, the two robots are waiting by your ship. Talk to them: they can't leave yet (the moon's reactor needs them until the next alignment) and **they'll join you later**. Their Nostrapedia files open when you meet them.
- **The cutscene.** Straight after, a dark, cold scene (its own stage, letterboxed, skippable): off the Antarctic coast, Hawthorne's gunship hangs over the black water with searchlights on the waves. His men winch **James Brown's frozen body** out of the sea, where the wanderer pushed him off the pier and he died of hypothermia. Hawthorne lays him on a steel slab, has his chest opened, and burns him back to life with a **Terra Imperia reactor heart**. James rises in the Pontifex Maximus's armour. Hawthorne's lines use the cyan nightmare subtitle style and James's the crimson one. There's no voice yet: send recordings and I'll wire them in.
- **The Antarctic station.** New main quest: *Defeat James Brown at the Antarctic station.* Fly to Earth (gold marker) and land anywhere on Antarctica. The old research station is a Terra Imperia stronghold now, with barricades, crimson banners, red floodlights, guards at the door and a crimson beacon. Go in to fight **James Brown, Pontifex Maximus** (level: yours + 2, at least 22). Beat him and choose:
  - **Spare him:** he joins your crew as James Brown of Terra Imperia.
  - **Kill him:** he's gone for good. He never joins you, and he disappears from the Nostrapedia's Companions section.
  - Either way, the title of Pontifex is free.
- **The Pontifex Maximus (works like Warframe's Kuva Liches).** From then on, whenever you land anywhere in Sol in Chapter III there's a chance a **Terra Imperia patrol** has landed nearby (crimson beacon). Beat its leader, a male soldier, then:
  - **Anoint him:** he rises as a Pontifex Maximus and **hunts you across Sol**. On later landings he may find you (a beacon in his armour's colour). Beat him again and **take him into your crew**, or let him go and he keeps hunting.
  - **Finish him:** he dies.
- **As many as you like.** In **Diplomacy → Crew → Pontifex Maximus**, each one you've won has:
  - **rename**;
  - **armour colour**: ten swatches or any colour you pick. The plates change colour; the crimson trim, reactor heart and visor stay Terra Imperia's;
  - **bring aboard / leave on the Nostra**;
  - **make him a resident**: he lives in the world for good, in his armour and colour.

  They level with you, take the same five orders as the rest of your crew, and can be lent to other factions like any companion. Hunters still on your trail are listed there too.
- **Nostrapedia:** a new **Pontifex Maximus** companion entry, open once James's fate is decided.
- **Phones:** the model (`data/cpPontifex.js`, 1.7 MB) only downloads the first time it's needed. Patrols are two soldiers instead of three. The cutscene uses a lighter sea, fewer floes, less snow and fewer soldiers. The Diplomacy controls wrap, and the colour swatches are thumb-sized.

### Sisters of Hawthorne, hunters and alignment

- **Sisters of Hawthorne.** Patrol leaders can be men or women. Anoint a woman and she rises as a **Sister of Hawthorne**: the same armour cut slimmer, the great horns off the helm, ivory by default. She hunts you and joins you exactly like a Pontifex. Rename her, recolour her, bring her aboard, or make her a resident (it takes a resident slot).
- **One of each at a time.** One Pontifex and one Sister can hunt you at once. While a slot is taken, a beaten soldier of that sex can't be anointed.
- **They hunt you in space too.** In Sol, a hunter can join any attack on your ship (a bigger fighter in their armour colour). Shoot them down and they eject and escape, and you still have to beat them on the ground.
- **Every time they kill you they get much stronger.** On the ground or in space, each kill adds about 8 levels plus 12% of their current level (lv 20 → 30 → 42 → 55…), capped at **lv 100**. They then leave you for dead. Kill them early: when you beat one you can **take them into your crew**, **kill them for good**, or **let them go**.
- **Their own alignments.** Each has their own alignment chart (a Pontifex starts Lawful Evil, a Sister Neutral Evil), shown in the Alignment screen and in Diplomacy → Crew.
  - Evil acts please them, raise influence and pull them further.
  - Good acts cost influence and only sway them slowly. The more they trust you, the more they listen.
- **After Terra Imperia.** Terra Imperia is gone by 2127, and the Catharsis is the threat in Chapter IV, so patrols only come in Chapter III. But a Pontifex or Sister who is a resident and **rules a resident empire** keeps a guard of their own. Challenge them from Diplomacy and beat them, and you can anoint one of their guard, a man or a woman, if that slot is free. That's how you keep making them in later chapters.

### The revival, as horror
- **The reconstruction is now a horror sequence.** James wakes on the slab mid-operation, **screaming**, strapped down. He bucks against the restraints while Hawthorne's men pin his arms. Drills come down into his chest with sparks flying and steam rising off his frozen body, and something dark spreads across the slab. The operating light flickers, a red strobe pulses, black frames cut in, and the picture warps and shakes like handheld footage while he screams. Then a hard cut to **silence**: black, then nothing but his new heartbeat, before he rises in the armour with its lights stuttering on.
- **New lines:**
  - Hawthorne: *"Hold him down. HOLD HIM!"* and *"Pain means the heart has taken. Bolt the armour on. Every plate. Into the bone."*
  - James: *"STOP— please— it's inside me— I can feel it— STOP—"*
- **Synthesised screams for now:** a distorted, voice-like synth, with new drill and searing sounds. Send recordings and I'll swap them in.
- **Patrols, hunters and anointing** (on the ground and in space) still only begin once James is defeated, whether you spare him or kill him.
- **Voiced:**
  - Charon and Kizna's talk uses **CH3CHARON1–5** (`data/chnVoices.js`), one per line.
  - The revival cutscene uses **CH3HAWTHORNE1–13** (`data/jrvVoices.js`), every spoken line in order, Hawthorne's and James's: 1–5 Hawthorne, 6 James's scream, 7 *"Hold him down"*, 8 James *"STOP— please…"*, 9 *"Pain means the heart has taken…"*, 10 James's scream, 11 *"There. Breathe, James…"*, 12 James *"…Grand… Imperarch."*, 13 the final order.
  - The synthesised scream now only plays if the voices fail to load. Both packs download only when they're needed.
- **Croxian Mascar and Malia de Toro** stand at Hawthorne's side through the revival: Croxian helmeted with his scythe, as Terra Imperia's soldier, and Malia in her armour. Hawthorne never names them or speaks to them. When James wakes screaming, **they're the ones who step in and pin him to the slab** (Croxian on the left, Malia on the right). They let go when the heart takes, and return to Hawthorne's side. His soldiers keep further back.

### Fix: twitching arms
- Humans carrying a rifle or pistols (Peter Chambers, soldiers, armed residents and townsfolk) kept twitching their supporting arm. The game decided which way that arm swings in by comparing the two arms' positions **in the world**, so whenever someone faced sideways the arms were almost level and the answer flipped every frame. It now compares them in the character's own space and remembers the result, so the arm holds steady whichever way they face.

### James Brown's scythe
- **James now carries the Pontifex scythe** (the crescent polearm with its crimson reactor channel) in his right hand, everywhere his Terra Imperia armour appears: the revival cutscene, the Antarctic station fight, as your companion if you spare him, the Nostrapedia and Adventures. It was copied from the Pontifex model into his own (`data/cpJamesTI.js`, built by `nightmare/tools/james_scythe.py`). In the station fight he swings it instead of the sword he used to get.
- A weapon built into a model now never counts toward that character's height however they're loaded, so the scythe doesn't shrink him.
- **A realistic recovery:** James is no longer flung into the air. A recovery crane (a davit on the edge of the ice) lowers its cable, and a rescue litter is slid under him in the water. He's hoisted slowly out of the sea, face down, swaying and turning a little on the cable. The boom swings in over the ice and lowers him onto the slab; on the next shot he's on his back. The camera pulls wide to follow it.

### Back to Antarctica: the real station, your Chapter I camp, and a furious James
- **Fly to your Chapter I base.** From Chapter III, Chapter I's Antarctica (the research station and everything you built there) can be reached from the sky, like Ad-Nostra: fly to the **research station landmark** on the Antarctic plateau and LAND there. You can also pick **Fly to Antarctica** at your ship's helm when you're landed on Earth. The Nostra parks on the ice, your camp is as you left it, and taking off puts you back in Earth's sky over the station.
- **Trackers.** From Chapter III, a marker shows the station from space and while flying over Earth: **ANTARCTICA · YOUR BASE · CHAPTER I CAMP**, or in gold **ANTARCTICA · THE STATION · JAMES BROWN · MAIN QUEST** while that quest is on. The old gold marker on the Earth planet itself is gone.
- **James's stronghold is now the real station,** the same one where he first met you, not a copy on Earth's generated ground. While he holds it: crimson banners on the door, barricades, red floodlights, guards outside and a crimson beacon over the roof. The door is his: landing anywhere else on Earth just points you to the marker.
- **James is furious.** Through the door, before the fight:
  - *"I can hear you out there. I'd know those footsteps anywhere. I listened to them walk away down that pier while the water filled my lungs."*
  - *"Do you know what the cold does? It takes your fingers. Then your voice. Then you can't even scream. I screamed for you anyway. Every second, until I couldn't."*
  - *"Hawthorne cut me open and put a furnace where my heart used to be. It burns every time I think of you. So come in. Come in and let me show you what you made."*
  - If you walk away: *"Run, then. You're good at that."*
- **In the fight:**
  - *"You shoved me off that pier and walked away while I drowned. I'm going to rip you apart for every second of it."*
  - *"I FROZE in that water! I felt my own heart STOP! And you didn't even look back!"*
  - *"I'LL DRAG YOU DOWN INTO THE DARK WITH ME!"*
  - Beaten: *"Go on… finish it. You've killed me once already."*
  - Spared: *"Why…? I'd have gutted you. I'd have enjoyed it. …Fine. I owe you a life, wanderer. Don't make me regret paying it back."*

### Teleporting between your bases
- **From Chapter III on (and in Chapters IV and V), the teleporter network reaches all your bases,** not just the ones in the area you're standing in. Use any teleporter (yours, the station's, Orion's or Ad-Nostra's) and the list now lets you jump to:
  - **Chapter I's Antarctica**: the station teleporter and your camp's teleporters;
  - **Africa**: Orion's teleporter, Ad-Nostra's, and any you built there;
  - **every planet where you've built a teleporter**, in any star system.
  Destinations in another area are marked *across the network · the Nostra follows you*. You arrive by the teleporter, with your ship set down nearby and your crew with you. New London's teleporter still can't be reached this way.
- **Planet bases stay where you built them.** A teleporter built on a planet now remembers the ground it stands on, so teleporting back puts you, and the base, in the same place. Teleporters built before this update land on a fixed dry spot on that planet, with your base laid out around you.

### Mission brief, and the teleporter on phones
- **The Mission brief follows your chapter.** It used to show only the opening (2125, Antarctica) or the 2127 time skip, so Chapters II and III, and Chapter IV before the time skip, read like Chapter I, out of step with the year shown in the corner. It now has its own text for each part of the story:
  - Chapter I: Antarctica.
  - Chapter II: Africa, Orion and New London.
  - Chapter III: Hawthorne on Mars and the hunt for allies across Sol, with no spoilers past where you are.
  - Chapter IV after the time skip: the Catharsis.
  - Chapter V: Lord Zark and Carax.
- **The teleporter menu on phones:**
  - Thumb-sized Teleport buttons, and the name field fits the screen.
  - The list scrolls inside the menu without dragging the page.
  - With the phone on its side, the header shrinks so the list and Close both fit.
  - Planet bases are labelled simply, e.g. *Kepler-442 b · Your base*.


### Fix: the Mission brief on desktop
- **On desktop the Mission brief was one endless line** running off the screen. The title screen takes the class `sub` while a sub-menu is open, and that's also the name of the logo's subtitle style, which forbids wrapping, so every sub-menu inherited it. The subtitle style now applies only to the subtitle under the logo, so the brief wraps into the menu column as it does on phones. The Wanderers, Save / Load and Settings menus wrap again too.

### James Brown, voiced at the station
- **The Antarctic station fight is voiced** with **CH3JB1–8** and **CH3JBREFUSAL** (`data/jbfVoices.js`, sources in `assets/audio/james_ch3/`):
  - 1–3: the three lines through the door;
  - 4: the fight starts (*"You shoved me off that pier…"*);
  - 5: phase two (*"I FROZE in that water!…"*);
  - 6: phase three (*"I'LL DRAG YOU DOWN INTO THE DARK WITH ME!"*);
  - 7: beaten (*"Go on… finish it…"*);
  - 8: spared (*"Why…? I'd have gutted you…"*);
  - REFUSAL: walking away from the door (*"Run, then. You're good at that."*).
- His lines stay on screen until he's finished saying them. Killing him is still silent.
- The pack (about 1.7 MB) starts downloading when the stronghold appears, so it's ready by the time you reach the door.

### James's fate: what your crew thinks
- **Orion, Khazglar and Nico react** once you decide James's fate (only the ones who have joined you, one after another):
  - **Spare him** and they call you out: he's been through too much, and you've left him to suffer. Each loses **12 influence** with you.
  - **Kill him** and they praise it as a mercy killing. Each gains **10 influence**.
- Then, either way, a line nobody speaks: ***YOUR ACTIONS WILL BE REMEMBERED.***

### Chapter III's choices and Chapter IV's ending
- The game now keeps a record of the choices that decide Chapter IV's ending:
  - **James Brown:** killed or spared (recorded now).
  - **Nyrexia:** whether you'd recruited her before you defeated James (recorded now, when his fate is decided).
  - **Croxian Mascar:** killed or spared. Kill him and **Orion turns villain and takes command of Terra Imperia**, the only way Pontifexes serve Terra Imperia in Chapter IV.
  - **Malia de Toro:** killed or spared.
  - **Orion Mascar:** killed or left alive. This choice only comes if you killed Croxian.
- **Good ending:** James, Croxian and Malia all spared.
- **Bad ending:** all four the other way: James, Croxian and Malia killed, and Orion left alive.
- **Neutral ending:** anything in between. Get even one choice "wrong" either way and it's neutral.
- The Croxian, Malia and Orion choices aren't in the game yet; the record is ready for them.

### Chapter IV's endings (waiting for the Siege of Carax)
- **The three endings are built** as cutscenes in the burning throne room of Carax, with Lord Zark on his knees among the ruins. The Siege of Carax isn't in the game yet; when it is, its Lord Zark fight calls **`ch4EndingPlay()`** as he falls, and your Chapter III choices pick the ending.
- **Good ending:** Zark collapses ("This changes… nothing…"). Archamus comes down out of the light, and Hak Chompjak, Vishara Erisconos and Darius Ancin walk in out of the smoke. The four of them stand around him and look down, and Hak says: *"Look at your empire now, Zark. Empty. Like your Catharsis will be by nightfall."* Ends on *THE CATHARSIS FALLS*.
- **Neutral ending:** Zark is beaten. Archamus comes down through the broken roof: *the damage has been done, and we need to keep going.* The game goes on into **Chapter V**.
- **Bad ending:**
  - **Zark's death:** Zark taunts you, and you charge and leap at him in slow motion. A white flash and shockwaves follow, light tears out of the cracks in his body, and he comes apart into embers (*LORD ZARK IS DEAD*). Then silence, with ash falling.
  - **Orion:** he walks out of the smoke in **black Terra Imperia armour with crimson trim**, blames you for Croxian's death, takes you by the throat and lifts you off the ground. He talks you through it while you kick and claw at his hand. Your sight closes in, darkens, drains of colour and keeps blacking out, under strangled breathing and a racing heartbeat. His last words are *"…no one will remember you were ever here."*
  - **Game over:** the **save slot you played to get there is erased.** Loaded or last saved to slot 1, slot 1 is gone, and so on; the other slots are untouched. If the playthrough was never saved, there's nothing to erase.
- **Skip** (or Esc) jumps straight to the outcome. Skipping the bad ending still ends in game over and still erases the save.
- **Watch them now:** add `?ending=good`, `?ending=neutral` or `?ending=bad` to the game's address, then tap once the title screen is up. **A preview never erases a save** and returns to the title when it ends.
- The lines have no voices yet: send recordings and I'll wire them in.
- **You're in the good and neutral endings too.** Once Zark falls, your wanderer walks up to him.
  - **Neutral:** Archamus comes down beside you, turns to you and speaks to you face to face. The last shot pulls away from the two of you standing over Zark.
  - **Good:** you take your place in the ring with Archamus, Hak, Vishara and Darius, all five looking down at him. He sees you from the floor too.
- **Hak looks like himself:**
  - No stray sword in his hand.
  - Once Zark is down, a clean light comes up on everyone in the good and neutral endings, so the hall's red firelight no longer turns Hak (or anyone else) pink.
  - His line is shot square on, with Darius beside him.
- **The endings on phones:**
  - Held upright, the lens widens and every shot steps back from what it's looking at, so nobody is cut off the sides of the screen.
  - Turn the phone mid-scene and the framing follows.
  - Sideways, phones frame the scenes like a computer screen.
  - Phones get half the fires (each one is a light) and no blur while you choke, so the endings stay smooth.
  - The game over screen sits inside the screen's safe area, with a thumb-sized button.

### Fix: Chapter III's nightmare not starting or getting stuck
- **It now always comes:**
  - **When:** the first time you're out in open space in Chapter III without having had it, after a few seconds of flying.
  - **Old bug:** it used to start only if you came into space at the very start of Chapter III. A save made in space, on a planet or in a planet's sky before it came never got it, and Khazglar's quest (which waits on it) could never begin.
  - **Saves on planets:** load one and it comes once you're back in open space.
  - **Never mid-warp:** it won't start in a world's sky, mid-warp, on the galaxy map or mid-landing either.
- **Waking up no longer seems stuck:**
  - Orion's "Hey! HEY! Look at me!" and the lines after it move on with **Space, E or Enter**, or a tap/click anywhere, like every other conversation. Before, only a click on the dialogue box itself worked.
  - **Esc** skips the nightmare's memories.
