# Spell Balance

This is a mod to adjust the spells available in One Step From Eden. I've noticed a lot of spells that seem to be way too weak, as well as a few that are outrageously strong. The goal of this mod is to make sure all spells are at least usable, and to tone down a few of the more ridiculous ones.

# General Principles

Spells with higher rarity can be more powerful (though they don't have to be). It's okay, for example, that Fimbulveter is more useful than Blizzard.

It costs time as well as mana to cast a spell. As such, Thunder is fine, but it would be inappropriate for "Quad Thunder" to deal 400 damage for 4 mana. Something like Ragnarok is better; it deals 350 damage and is higher rarity. However, you should get something for the extra mana: something like Thunderstorm, which does 75 damage per tile on average, is too weak in comparison to spells like Cold Snap or Anubis.

This should be obvious from the name, but I'm not going to adjust the power of weapons or artifacts. Trust me, this is enough work as it is.

## Damage numbers

For single-square damage, a spell like Thunder or Revenge is the baseline: 100 damage for 1 mana.

For AOE, 50 damage to all enemies is the baseline. Anubis is 70, but poison takes a long time to kick in.

# The Changes

## Anima

### Rarity 0

#### Cold Medicine

Cold Medicine costs 0, heals for 40 HP, and applies 2 frost stacks. This is 100 frost damage if the opponent is at full health, 60 otherwise, but with a big downside. This spell feels weak but I think it's not too terrible. Leaving it as is for now.

#### Firewall

Damn this spell is good. 40 damage for 2 + 4 flames tiles. And it's easy to aim, too! At base, this is "180 damage if the enemy stands in the fire"; 180 damage in a line with significant downside (the enemy might just leave the line) would be fine at cost 2. But it scales with both fire artifacts and spellpower, as all fire spells do. Start by turning it down to 20 damage; this isn't a big deal but it will make a small difference.

#### Frost Barrage

1x40 frost is not good but 2x40 frost is. Leaving as-is.

#### Frostbolt

This is underpowered but I'm afraid to change it because it affects a bunch of other effects (Coldstone, Frostmail, and so on).

#### Back Burner

This feels too weak (leaving flames on your side is a big downside) but I'm not really sure. I'll have to take it more to find out.

### Rarity 1

#### Ice Spikes

Ice Spikes is 60 damage plus 1 frost. The aiming gimmick is cool and fun, but it's a double-edged sword: If you dodge an attack fired down a row, your ice spikes will whiff. 

#### Thunderstorm

Thunderstorm deals 50 damage per hit, 4x6 times, at rarity 1. There are 16 tiles, so this deals an average of 75 damage per tile. Indescriminate AoE is 75 damage per tile for 4 mana is very bad.

The first change is to increase the damage to 100. This makes the spell feel better thematically; it's it's a storm of Thunder spells. The second change is to increase it from 4x6 to 6x6. This puts the damage per tile at 225. This is significantly worse than the Calamity spell Fimbulveter but it's good enough to hurt.

#### Twinferno

If you aim it properly, Twinferno is 60 damage twice for 2 mana, with the possibility of doing more damage to other things nearby. This is a little low.

### Rarity 2

#### Carpet Bomb

40 damage in a wide path for 3 mana, with a downside. It leaves fire too but that's a wash, since it leaves a ton of fire in your own side of the field as well. This needs a big buff; I think a bunch of damage is the right approach. After all, you're carpet bombing the bad guys. Let's start with 200.

#### Hailstorm

Similarly to Thunderstorm, Hailstorm just doesn't do enough. 18 hits, each one doing 10 damage plus frost. Changing Hailstorm is tough because it needs to be distinct from Cold Snap, Blizzard and Fimbulveter, all of which are big AOE frost effects. I think the way to do that with Hailstorm is to increase the fixed damage it deals. 100 damage feels about right; counting the frost, this means it's 150 damage per hit, or around 170 damage overall.

#### Ice Hockey

I don't know how to evaluate this spell.

#### Wildfire

This is a little expensive for what it is. In a crowded normal enemy fight it's basically Firestorm: hit 4 enemies, put fire on their tiles. In a boss fight it's a lot worse than that. I'll leave it as-is for now but I think could probably use a little love.

### Rarity 3

#### Flamberge

It's a gimmick! 100 damage in a cone and fire everywhere for only 2 mana, but it's only good if you can hit something in the front row, or better yet, on your side of the field. Somebody who can pull this off regularly deserves more than 100 damage; let's increase it to 150 for now.

### Rarity 4

#### EXPLOSION!

I actually think EXPLOSION! isn't that far off from being viable, but it's not there yet. To start, let's tone it down to 2 seconds of charge, plus 2 seconds of end lag.
