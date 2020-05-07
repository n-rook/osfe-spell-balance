# Glimmer

## Rarity 1

### Breakout

**Damage: 120 -> 150**

120 damage for 1 is already an extremely good rate, but against a lot of enemies it's not possible to connect with Breakout. I'm improving it further to tempt players into figuring out ways to use it effectively.

### Diag Beam

**No change**

Looking at the numbers Diag Beam is not very good; 100 damage in a weird, hard-to-aim piercing pattern. But in practice it always seems to turn out okay at least to use.

### Energizer

**No change**

The famously confusing Energizer buffs itself _before_ attacking, rather than after. This means your first attack does 120, the second does 150, and the third does 180. 150 damage for 2 mana is decent, and you get that on average once you've done three attacks, so it's fine for now.

### Shattersaw

**Damage: 20 -> 40**
**Shatter damage: 60 -> 80**

Shattersaw does 20 damage, plus 60 to three random enemies. In other words, it's kind of like 60 damage AOE, but with 20 bonus damage and a chance of whiffing. Spells like this are typically terrible in boss fights, and this one is worse because you still have to aim! So it should at least be strong enough to be scary in normal fights.

### Zenith

**No change**

It's hard to buff Zenith because it'd have weird effects on Selicy. Even so, though, I think it's in a decent spot: if step spells were actually good, 150 damage would make it a tempting pickup even without Selicy's weapons.

## Rarity 2

### Circuit

**Damage: 40 -> 60**

Circuit is gimmicky and not great. It's easy to aim, but that's just about its only virtue.

### Glaive

**No change**

Glaive is kind of a meme; it usually does nothing and randomly beats the Gate. Unfortunately I think that's a consequence of the design, so I'm not sure there's much I can do about it. I'll revisit it later.

### Resonate

**Damage: 50 -> 100**

Resonate is tough to use, and the payoff isn't great. Going through a lot of effort and waiting for an enemy to fall into position in order to be rewarded with 100 damage for 1 mana is not a good idea. Since it's rarity 2, it should be much more powerful in order to reward investing in the weird deck it wants.

## Rarity 3

### Eternity Cannon

**No change**

Eternity Cannon is awesome. It's a unique, powerful effect, with a Flow rider that tempts the player into investing in the archetype even late in the game. But 30 damage isn't very much, so I don't think it's overpowered. It's difficult to judge because there are very few persistent buffs in the game.

### Infinity Beam

**No change**

I don't think Infinity Beam is playable but a lot of good players seem to like it so I'll hold off on buffing it into the stratosphere.

### Spirit Sword

**Damage: 30 -> 50**

Spirit Sword is a very odd spell. It looks like it's intended to be held in front of you, but in reality you shimmy back and forth in order to connect more often. I'd like to make it attack more often, but it's not feasible to make it hit more often in XML alone, so I won't yet.

The damage is not good enough to make this card attractive.

## Rarity 4

### Sunshine

**Mana cost: 4 -> 5**
**Damage: 2 -> 4**
**Shots: 50 -> 25**
**Time between shots: 0.1 -> 0.2**

Sunshine scales incredibly hard. At base, it does 100 damage. With 8 spell power (that is, with Uranium or two of the other spell power artifacts), it does 500 damage. And, of course, defense works the other way: against an enemy with 7 defense, even the 8 SP version does only 150 damage. If the player has an enormous amount of SP, Sunshine will instantly win every hallway fight in the game, but it's easy to blame that on the artifacts they have and not this spell.

Sunshine should still be good; after all, it's a Calamity spell, right? But right now, its high scaling combined with the fact that you don't have to aim it makes it a problem. I've doubled its damage and halved the number of shots it deals in order to make it scale less hard, and increased its mana cost as well.

There's an issue with Sunshine where it can get "Frost on hit" upgrades. A single 25% Frost on Hit spell makes it do about 625 more damage. This is obviously way too strong. The developer has acknowledged this as not great, though, so I suspect it'll be resolved in the base game.

