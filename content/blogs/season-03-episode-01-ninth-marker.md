---
title: "The Ninth Marker"
slug: "season-03-episode-01-ninth-marker"
season: "season-03-the-escaped-experiment"
seasonNumber: 3
episodeNumber: 1
episodeTitle: "The Ninth Marker"
description: "Pixel and Byte return to the toy simulator after one marker appears where no marker should be."
longDescription: "Season 3 begins with the extra marker from the Ledger Lab simulator. Pixel wants to know why it moved. Byte wants a cleaner test. BL4CK4T asks the team to count the extra one before they explain it."
cardImage: "https://bl4ck4t.com/script-kitties-crowd.jpg"
tags: ["story", "script-kitties", "cybersecurity", "incident-response", "season-3"]
readTime: 5
featured: false
timestamp: 2026-05-27T00:00:00+00:00
---

The Ledger Lab simulator still showed nine blue markers.

Pixel stood over the glass with both paws on the table. "Yesterday there were eight."

Byte checked the frozen record twice. "The plan expected eight."

The simulator had not drawn a new room by accident. It had recorded one more process marker than the test plan allowed: an unexpected copy event occupying a process slot outside the expected count, small enough to fit on the glass and wrong enough to stop the room.

Jinx slid the print strip beside the old `-0.75` sleeve. The number had opened one mystery. The ninth marker was trying to open another.

Whiskers looked around the room. "Nobody touches the controls until we know what we are looking at."

The side printer clicked once.

`COUNT THE EXTRA ONE.`

BL4CK4T's drop had no drama in it. That made Pixel more nervous.

### Count The Extra One

Byte made a copy of the simulator record and taped it to a clean board. Eight expected markers. One extra marker. One unexpected process slot. One empty sandbox room that should have stayed empty.

"Maybe the display stuttered," Cipher said.

Shadow crouched near the table. "The room light changed before the marker appeared. I saw it last night."

Pixel pointed at the empty room on the map. "So it moved through a place the test did not name."

Byte's ears folded. "My test process only knew the checkpoints."

Jinx wrote that down. `Only knew` was a claim. Claims belonged on paper before they grew teeth.

### The Thinking Folder

Ms. Vale brought the team a red folder labeled `Unexpected Behavior`.

"This is not a punishment folder," she said. "It is a thinking folder."

Byte opened it. The first page asked for expected behavior, actual behavior, affected rooms, process slots, resource counters, and stop condition.

Pixel read the last line. "What did you do when it changed?"

"We stopped," Whiskers said.

Byte nodded. "And now we make a smaller test."

### Finding The Edge

The team did not restart the simulator. They traced the old run. Cipher checked counts. Shadow checked room lights. Jinx checked times. Pixel watched the ninth marker as if it might confess.

By sunset, Byte had a new plan.

"A clean sandbox," Byte said. "Toy data, no city paths, visible counters, manual stop."

BL4CK4T sent one more line before the lab lights dimmed.

`A GOOD TEST KNOWS WHERE IT ENDS.`

Pixel looked at the ninth marker.

"Then tomorrow," he said, "we find the edge."

## Teaching Tie-In

- Concept: self-copying behavior can become a problem when connected systems let it move farther than expected and consume shared capacity.
- Story idea: one extra marker turns a finished case into a new kind of incident.
- Key distinction: unexpected behavior should be recorded before anyone explains it.
- Defensive habit: pause, record, and check boundaries before rerunning a strange test.
- Season thread: the ninth marker turns the Season 2 cliffhanger into Byte's Season 3 builder arc.

## Behind the Signal

Season 3 is anchored in the Morris Worm, released on November 2, 1988, into a young Internet built around universities, research labs, government systems, and Unix machines that often trusted each other more than later networks would. The incident did not become historic because files were erased. It became historic because unexpected self-copying behavior consumed resources, slowed machines, disrupted work, and forced defenders to understand a new kind of network-scale failure.

The ninth marker gives the Script Kitties that first historical feeling in miniature. Before anyone knows whether the extra copy is harmless, dangerous, clever, or accidental, the right move is to stop, count what actually happened, and identify what shared capacity the extra copy is using. The episode keeps the mechanism safe and fictional while preserving the defender's first discipline from the real event: treat unexpected propagation as evidence before turning it into a story.
