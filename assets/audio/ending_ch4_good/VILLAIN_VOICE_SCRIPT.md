# The good ending, as a villain lives it · voice script

Plays when you reach the good ending with a villain alignment (−34 or lower). Preview: `?ending=goodvillain`.

**Cutscene: `data/c4eGoodVillainVoices.js` (CH4GOODENDINGEVIL1–17, in this order)**

1. Archamus: Wanderer. Stand down. He is beaten. He answers to the worlds he burned, not to your blade.
2. Lord Zark: Look at its eyes, Archamus. You did not bring a champion into my hall. You brought my replacement.
3. Darius Ancin: Guards! Seal the doors! Wanderer, drop the sword. That is an order!
4. Lord Zark: Go on, then. Do what I would have done. The dark will remember you kindly.
5. Lord Zark (run through): Heir… at last…
6. Vishara Erisconos: The lights… where did they go? I can't see them. Darius? Darius, answer me!
7. Am-Grek: Archamus, guide me! Archamus… why won't you answer me?!
8. Timpur IV: No, no, no! Timpur never wronged you! We came here at your side! We came—
9. Darius Ancin: A hundred years running from one monster… and I walked another one right into the room.
10. Archamus: I pulled you out of the ice. I set you on this road. Is this… what I made?
11. Archamus (dying): The light… does not… go out…
12. Hak Chompjak V: Archamus. Darius. Vishara. All of them, in the time it takes to breathe.
13. Hak Chompjak V: Look at you. Standing in their blood like it's nothing. Like it's warm water. You're sick. Do you hear me? You are sick.
14. Hak Chompjak V: They fought for you. Darius put his name to yours in front of the whole Federation. Vishara sang for you on the way here. Archamus pulled you out of the ice with his own light. And you cut them down like animals.
15. Hak Chompjak V: I told you it wasn't time. I should have told you it was never time. I should have left you in the snow to freeze.
16. Hak Chompjak V: Zark at least had the decency to call himself a monster. You let us call you a hero. You let us hope. That's what makes you disgusting.
17. Hak Chompjak V: Come on, then. I'm the last one standing on this floor, and I won't go down on my knees like he did.

**Then a box, your reply:** "You of ALL PEOPLE should keep your mouth shut, SEVIRRUS."

**The boss fight: `data/c4eGoodVillainHakVoices.js` (recorded as CH4HAKFINALBOSSFIGHT1–12, the 12 lines below in order; music: Terra Imperium)**

18. Hak (half health): Is that all? Zark hit harder, and Zark is dead.
19. Hak (near the end): For Aridaxx! For every one of them!
20. Hak (defeated): Then it's yours. All of it. Gods help whoever's left to live in it.
21. Hak (his answer to "SEVIRRUS", as the fight starts): Sevirrus. Yes. I was him. I killed my own father, and I spent fifty years learning what that costs. You learned nothing in one night.
22. Hak (taunt): I spent twenty-six years in a cell for what I did. You won't live long enough to see one.
23. Hak (taunt): Every one of them would have died for you. You didn't even let them.
24. Hak (taunt): Archamus saw something in you. I'll cut out whatever it was and bury it with him.
25. Hak (taunt): You fight like Zark taught you. He taught me too. It took me fifty years to unlearn it.
26. Hak (taunt): My father begged me, at the end. I still hear him. If you live, you'll hear all of them. Every night.
27. Hak (taunt): Vishara sang their names all the way here. Now someone will have to sing hers.
28. Hak (taunt): Stay down! Stay down, you sick animal!
29. Hak (taunt): Aridaxx will know what you did tonight. Every world will know.

The taunts come one at a time, every 12–17 seconds while you fight, in this order.

Line 20 no longer plays when he's beaten the first time: he goes down on one knee and becomes Hak Chompjak, Prince of Zark (the second phase; script in `assets/audio/hak_prince_of_zark/VOICE_SCRIPT.md`).

Test the fight on its own: `?hakchompjakbossfightevilgoodending`. Straight to the second phase: `?hakprinceofzark`.
