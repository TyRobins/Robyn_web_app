#Imports below:
import dice
import robyn

#Saving Throws (I believe this should use d20 instead of d12+d8, but I should confirm)
def strength_throw():
    return dice.randomer_fct_d20() + robyn.strength_modifier + robyn.strength_save
def dexterity_throw():
    return dice.randomer_fct_d20() + robyn.dexterity_modifier + robyn.dexterity_save
def constitution_throw():
    return dice.randomer_fct_d20() + robyn.constitution_modifier + robyn.constitution_save
def intelligence_throw():
    return dice.randomer_fct_d20() + robyn.intelligence_modifier + robyn.intelligence_save
def wisdom_throw():
    return dice.randomer_fct_d20() + robyn.wisdom_modifier + robyn.wisdom_save
def charisma_throw():
    return dice.randomer_fct_d20() + robyn.charisma_modifier + robyn.charisma_save

#Ability Checks
def strength_check():
    return dice.randomer_fct_d12() + dice.randomer_fct_d8() + robyn.strength_modifier
def dexterity_check():
    return dice.randomer_fct_d12() + dice.randomer_fct_d8() + robyn.dexterity_modifier
def constitution_check():
    return dice.randomer_fct_d12() + dice.randomer_fct_d8() + robyn.constitution_modifier
def intelligence_check():
    return dice.randomer_fct_d12() + dice.randomer_fct_d8() + robyn.intelligence_modifier
def wisdom_check():
    return dice.randomer_fct_d12() + dice.randomer_fct_d8() + robyn.wisdom_modifier
def charisma_check():
    return dice.randomer_fct_d12() + dice.randomer_fct_d8() + robyn.charisma_modifier

#Skill Checks
def acrobatics_check():
    return dexterity_check() + robyn.acrobatics
def animal_handling_check():
    return wisdom_check() + robyn.animal_handling
def arcana_check():
    return intelligence_check() + robyn.arcana
def athletics_check():
    return strength_check() + robyn.athletics
def deception_check():
    return charisma_check() + robyn.deception
def history_check():
    return intelligence_check() + robyn.history
def insight_check():
    return wisdom_check() + robyn.insight
def intimidation_check():
    return charisma_check() + robyn.intimidation
def investigation_check():
    return intelligence_check() + robyn.investigation
def medicine_check():
    return wisdom_check() + robyn.medicine
def nature_check():
    return intelligence_check() + robyn.nature
def perception_check():
    return wisdom_check() + robyn.perception
def performance_check():
    return charisma_check() + robyn.performance
def persuasion_check():
    return charisma_check() + robyn.persuasion
def religion_check():
    return intelligence_check() + robyn.religion
def sleight_of_hand_check():
    return dexterity_check() + robyn.sleight_of_hand
def stealth_check():
    return dexterity_check() + robyn.stealth
def survival_check():
    return wisdom_check() + robyn.survival

#Attack Rolls
def agonizing_eldritch_attack():
    return dice.randomer_fct_d20() + robyn.charisma_modifier + robyn.proficiency_bonus
def main_dagger_attack():
    return dice.randomer_fct_d20() + robyn.dexterity_modifier + robyn.proficiency_bonus
def off_dagger_attack():
    return dice.randomer_fct_d20() + robyn.dexterity_modifier + robyn.proficiency_bonus
def main_shadow_blade_attack():
    return dice.randomer_fct_d20() + robyn.dexterity_modifier + robyn.proficiency_bonus
def off_shadow_blade_attack():
    return dice.randomer_fct_d20() + robyn.dexterity_modifier + robyn.proficiency_bonus
def main_light_hammer_attack():
    return dice.randomer_fct_d20() + robyn.strength_modifier + robyn.proficiency_bonus
def off_light_hammer_attack():
    return dice.randomer_fct_d20() + robyn.strength_modifier + robyn.proficiency_bonus
def light_crossbow_attack():
    return dice.randomer_fct_d20() + robyn.dexterity_modifier + robyn.proficiency_bonus

#Attack Damage
def agonizing_eldritch_damage():
    return dice.randomer_fct_d10() + robyn.charisma_modifier
def main_dagger_damage():
    return dice.randomer_fct_d4() + robyn.dexterity_modifier
def off_dagger_damage():
    return dice.randomer_fct_d4()
def main_shadow_blade_damage():
    return sum(dice.randomer_fct_d8() for _ in range(2)) + robyn.dexterity_modifier
def off_shadow_blade_damage():
    return sum(dice.randomer_fct_d8() for _ in range(2))
def main_light_hammer_damage():
    return dice.randomer_fct_d4() + robyn.strength_modifier
def off_light_hammer_damage():
    return dice.randomer_fct_d4()
def light_crossbow_damage():
    return dice.randomer_fct_d8() + robyn.dexterity_modifier
def sacred_flame_damage():
    return dice.randomer_fct_d8()
def hel_ish_rebuke_damage():
    return sum(dice.randomer_fct_d10() for _ in range(3))

#Healing Hit Points (all dice is controversial, particularly for healing light as it is max 4)
def short_rest_hit_dice():
    return dice.randomer_fct_d8() + robyn.constitution_modifier
def all_short_rest_hit_dice():
    return sum((dice.randomer_fct_d8() + robyn.constitution_modifier) for _ in range(robyn.level))
def healing_light_dice():
    return dice.randomer_fct_d6()
def max_healing_light_dice():
    return sum(dice.randomer_fct_d6() for _ in range(robyn.charisma_modifier))

#Fearful Symmetry Talisman
def talisman_ability_check_buff():
    return dice.randomer_fct_d4()