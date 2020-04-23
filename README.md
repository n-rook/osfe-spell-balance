# Spell Balance

This is a mod to adjust the spells available in One Step From Eden. I've noticed a lot of spells that seem to be way too weak, as well as a few that are outrageously strong. The goal of this mod is to make sure all spells are at least usable, and to tone down a few of the more ridiculous ones.

# How to build

Right now the build process is very simple and manual. Create a new directory called "Spell Balance". Copy Spells.xml into this directory, as well as workshopIcon.png and WorkshopItemInfo.png. Then copy that into "Mods" in the OSFE directory to test it out.

# General Principles

Spells with higher rarity can be more powerful (though they don't have to be). It's okay, for example, that Fimbulveter is more useful than Blizzard.

It costs time as well as mana to cast a spell. As such, Thunder is fine, but it would be inappropriate for "Quad Thunder" to deal 400 damage for 4 mana. Something like Ragnarok is better; it deals 350 damage and is higher rarity. However, you should get something for the extra mana: something like Thunderstorm, which does 75 damage per tile on average, is too weak in comparison to spells like Cold Snap or Anubis.

This should be obvious from the name, but I'm not going to adjust the power of weapons or artifacts. Trust me, this is enough work as it is. I'm also not going to change the basic function of spells.

## Reasonable spells

I'm honestly writing this for my own reference, so I have other spells to compare to.

For single-square damage, a spell like Thunder or Revenge is the baseline: 100 damage for 1 mana.

For AOE, 50 damage to all enemies for 1 mana is the baseline. Anubis is 70, but poison takes a long time to kick in.

# The Changes

## Anima

### Rarity 0

#### Cold Medicine

**No change**

Cold Medicine costs 0, heals for 40 HP, and applies 2 frost stacks. This is 100 frost damage if the opponent is at full health, 60 otherwise, but with a big downside. It feels a little weak but I'd rather not change it just yet.

#### Firewall

**40 -> 20 damage**

Firewall is extremely strong. 2 mana, and you get 40 damage and 4 flame tiles. At base, this is 180 damage with a downside (some enemies won't stand in the fire), but fire scales great, so it's often much better than that.

#### Frost Barrage

**No change**

1x40 with frost for 2 mana is not good but 2x40 with frost is. Leaving as-is.

#### Frostbolt

**40 -> 50 damage**

Frostbolt is anemic. In theory it's 90 damage and easy to aim, but in practice Frost isn't actually worth 50 damage, especially at the beginning of the game when you're likely to take it. I don't want to change it much because a number of other effects cast Frostbolt, but a small change like this should be fine.

#### Back Burner

**No change**

I rarely take this spell so I'm not sure if it's too weak or not. Leaving flames on your side is a big downside.

### Rarity 1

#### Ice Spikes

**60 -> 120 damage**

Ice Spikes is 60 damage plus 1 frost. The aiming gimmick is cool and fun, but it's a double-edged sword: If you dodge an attack fired down a row, your ice spikes will whiff.

I'd rather not make this deal 2 frost because that feels more like Frost Barrage or Blizzard. Instead, I'll increase the damage by a lot.

#### Thunderstorm

**50 -> 100 damage**

Thunderstorm deals 50 damage per hit, 4x6 times, at rarity 1. There are 16 tiles, so this deals an average of 75 damage per tile. At rarity 1, you shouldn't get much for a huge AOE, but 75 is just too low; the card looks horrible next to Cold Snap or Anubis.

I'll start by doubling the damage to 100. This is good thematically because Thunder does 100 damage too. More buffs might be necessary.

#### Twinferno

**50 -> 60 damage**

If you aim it properly, Twinferno is 50 damage twice for 2 mana, with the possibility of doing more damage to other things nearby. This is a little low, but it's not that bad, given the large AOE.

### Rarity 2

#### Carpet Bomb

**40 -> 200 damage**

40 damage in a wide path for 3 mana, with a downside. It leaves fire too but that's a wash, since it leaves a ton of fire in your own side of the field as well. Plus, it makes you fragile.

If this spell is saddled with multiple downsides it should at least be a powerful effect. Let's start with 200 damage for now.

#### Hailstorm

**10 -> 100 damage**

Similarly to Thunderstorm, Hailstorm just doesn't do enough. 18 hits, each one doing 10 damage plus frost. Changing Hailstorm is tough because it needs to be distinct from Cold Snap, Blizzard and Fimbulveter, all of which are big AOE frost effects. I think the way to do that with Hailstorm is to increase the fixed damage it deals. 100 damage feels about right; counting the frost, this means it's 150 damage per hit, or around 170 damage overall.

#### Ice Hockey

**No change**

I have no idea how to evaluate this spell.

#### Wildfire

**No change**

This is a little expensive for what it is. In a crowded normal enemy fight it's basically Firestorm: hit 4 enemies, put fire on their tiles. In a boss fight it's a lot worse than that. I'll leave it as-is for now but I think could probably use a little love.

### Rarity 3

#### Flamberge

**100 -> 150 damage in the cone**

It's a gimmick! 100 damage in a cone and fire everywhere for only 2 mana, but it's only good if you can hit something in the front row, or better yet, on your side of the field. Somebody who can pull this off regularly deserves more than 100 damage; let's increase it to 150 for now.

### Rarity 4

#### EXPLOSION!

**No change**

I want to buff EXPLOSION! but I need to make sure reducing the start- and end-lag doesn't make animations go out of sync, so I haven't done it yet.
