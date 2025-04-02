#Imports below:
import math

#Abilities
strength = 13
dexterity = 18
constitution = 12
intelligence = 10
wisdom = 7
charisma = 18

#Ability Modifiers
strength_modifier = math.floor((strength - 10) / 2) #1
dexterity_modifier = math.floor((dexterity - 10) / 2) #4
constitution_modifier = math.floor((constitution - 10) / 2) #1
intelligence_modifier = math.floor((intelligence - 10) / 2) #0
wisdom_modifier = math.floor((wisdom - 10) / 2) #-2
charisma_modifier = math.floor((charisma - 10) / 2) #4

#Saving Throw Proficiencies
strength_save = 0
dexterity_save = 0
constitution_save = 0
intelligence_save = 0
wisdom_save = 2
charisma_save = 2

#Skill Proficiencies
acrobatics = 0
animal_handling = 0
arcana = 0
athletics = 0
deception = 2
history = 2
insight = 0
intimidation = 0
investigation = 0
medicine = 0
nature = 0
perception = 0
performance = 0
persuasion = 4
religion = 2
sleight_of_hand = 0
stealth = 0
survival = 0

#Passive Skills
passive_acrobatics = 10 + dexterity_modifier + acrobatics #14
passive_animal_handling = 10 + wisdom_modifier + animal_handling #8
passive_arcana = 10 + intelligence_modifier + arcana #10
passive_athletics = 10 + strength_modifier + athletics #11
passive_deception = 10 + charisma_modifier + deception #16
passive_history = 10 + intelligence_modifier + history #12
passive_insight = 10 + wisdom_modifier + insight #8
passive_intimidation = 10 + charisma_modifier + intimidation #14
passive_investigation = 10 + wisdom_modifier + investigation #8
passive_medicine = 10 + wisdom_modifier + medicine #8
passive_nature = 10 + intelligence_modifier + nature #10
passive_perception = 10 + wisdom_modifier + perception #8
passive_performance = 10 + charisma_modifier + performance #14
passive_persuasion = 10 + charisma_modifier + persuasion #18
passive_religion = 10 + intelligence_modifier + religion #12
passive_sleight_of_hand = 10 + dexterity_modifier + sleight_of_hand #14
passive_stealth = 10 + dexterity_modifier + stealth #14
passive_survival = 10 + wisdom_modifier + survival #8

#Leveling
level = 3
max_hit_points = 3 + (level * (5 + constitution_modifier))
long_rest_hit_dice = math.floor(level / 2)
proficiency_bonus = math.ceil((level / 4) + 1)
spell_attack_bonus = charisma_modifier + proficiency_bonus
spell_save_dc= 8 + spell_attack_bonus
daily_healing_light_dice = 1 + level


#Padded Armor
armor_bonus = 1
stealth_disadvantage = True
armor_class = 10 + dexterity_modifier + armor_bonus

#Invocations
concentration_advantage = True

#Homebrew
intimidation_disadvantage = True



