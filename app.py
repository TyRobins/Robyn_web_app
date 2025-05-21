import flask

import threading
import time
import requests

import dice
import rolls
import robyn

from markupsafe import Markup

app = flask.Flask(__name__, static_folder='static')
from flask import request, render_template

def keep_alive():
    while True:
        try:
            requests.get('https://robyn-pn23.onrender.com/')
            time.sleep(840)
        except:
            pass
keep_alive_thread = threading.Thread(target=keep_alive)
keep_alive_thread.daemon = True
keep_alive_thread.start()

@app.route('/get-dice-roll', methods=['POST'])
def get_dice_roll():
    roll_name = request.form['roll_name']
    if roll_name == "Four-Sided Dice":
        roll_result = f"Four-Sided Dice: {dice.randomer_fct_d4()}"
    elif roll_name == "Six-Sided Dice":
        roll_result = f"Six-Sided Dice: {dice.randomer_fct_d6()}"
    elif roll_name == "Eight-Sided Dice":
        roll_result = f"Eight-Sided Dice: {dice.randomer_fct_d8()}"
    elif roll_name == "Ten-Sided Dice":
        roll_result = f"Ten-Sided Dice: {dice.randomer_fct_d10()}"
    elif roll_name == "Twelve-Sided Dice":
        roll_result = f"Twelve-Sided Dice: {dice.randomer_fct_d12()}"
    elif roll_name == "Twenty-Sided Dice":
        roll_result = f"Twenty-Sided Dice: {dice.randomer_fct_d20()}"
    else:
        roll_result = "I'm sorry, I can't help with that yet."
    return render_template('index.html',   
        roll_result = roll_result, 
        level = robyn.level,
        max_hit_points = robyn.max_hit_points,
        armor_class = robyn.armor_class,
        spell_save_dc = robyn.spell_save_dc,
        daily_healing_light_dice = robyn.daily_healing_light_dice,
        passive_acrobatics = robyn.passive_acrobatics,
        passive_animal_handling = robyn.passive_animal_handling,
        passive_arcana = robyn.passive_arcana,
        passive_athletics = robyn.passive_athletics,
        passive_deception = robyn.passive_deception,
        passive_history = robyn.passive_history,
        passive_insight = robyn.passive_insight,
        passive_intimidation = robyn.passive_intimidation,
        passive_investigation = robyn.passive_investigation,
        passive_medicine = robyn.passive_medicine,
        passive_nature = robyn.passive_nature,
        passive_perception = robyn.passive_perception,
        passive_performance = robyn.passive_performance,
        passive_persuasion = robyn.passive_persuasion,
        passive_religion = robyn.passive_religion,
        passive_sleight_of_hand = robyn.passive_sleight_of_hand,
        passive_stealth = robyn.passive_stealth,
        passive_survival = robyn.passive_survival)

@app.route('/get-ability-roll', methods=['POST'])
def get_ability_roll():
    roll_name = request.form['roll_name']
    if roll_name == "Strength Saving Throw":
        total_roll = rolls.strength_throw()
        roll_result = f"Strength Save: {total_roll} (Natural {total_roll - (robyn.strength_modifier + robyn.strength_save)})"
    elif roll_name == "Dexterity Saving Throw":
        total_roll = rolls.dexterity_throw()
        roll_result = f"Dexterity Save: {total_roll} (Natural {total_roll - (robyn.dexterity_modifier + robyn.dexterity_save)})"
    elif roll_name == "Constitution Saving Throw":
        total_roll = rolls.constitution_throw()
        roll_result = f"Constitution Save: {total_roll} (Natural {total_roll - (robyn.constitution_modifier + robyn.constitution_save)})"
    elif roll_name == "Intelligence Saving Throw":
        total_roll = rolls.intelligence_throw()
        roll_result = f"Intelligence Save: {total_roll} (Natural {total_roll - (robyn.intelligence_modifier + robyn.intelligence_save)})"
    elif roll_name == "Wisdom Saving Throw":
        total_roll = rolls.wisdom_throw()
        roll_result = f"Wisdom Save: {total_roll} (Natural {total_roll - (robyn.wisdom_modifier + robyn.wisdom_save)})"
    elif roll_name == "Charisma Saving Throw":
        total_roll = rolls.charisma_throw()
        roll_result = f"Charisma Save: {total_roll} (Natural {total_roll - (robyn.charisma_modifier + robyn.charisma_save)})"
    elif roll_name == "Concentration Saving Throw":
        total_roll = rolls.constitution_throw()
        roll_result = f"Concentration Save: {total_roll} (Natural {total_roll - (robyn.constitution_modifier + robyn.constitution_save)})"
    elif roll_name == "Strength Ability Check":
        total_roll = rolls.strength_check()
        roll_result = f"Strength Check: {total_roll} (Natural {total_roll - robyn.strength_modifier})"    
    elif roll_name == "Dexterity Ability Check":
        total_roll = rolls.dexterity_check()
        roll_result = f"Dexterity Check: {total_roll} (Natural {total_roll - robyn.dexterity_modifier})"
    elif roll_name == "Constitution Ability Check":
        total_roll = rolls.constitution_check()
        roll_result = f"Constitution Check: {total_roll} (Natural {total_roll - robyn.constitution_modifier})"    
    elif roll_name == "Intelligence Ability Check":
        total_roll = rolls.intelligence_check()
        roll_result = f"Intelligence Check: {total_roll} (Natural {total_roll - robyn.intelligence_modifier})"
    elif roll_name == "Wisdom Ability Check":
        total_roll = rolls.wisdom_check()
        roll_result = f"Wisdom Check: {total_roll} (Natural {total_roll - robyn.wisdom_modifier})"    
    elif roll_name == "Charisma Ability Check":
        total_roll = rolls.charisma_check()
        roll_result = f"Charisma Check: {total_roll} (Natural {total_roll - robyn.charisma_modifier})"
    elif roll_name == "Initiative Ability Check":
        total_roll = rolls.dexterity_check()
        roll_result = f"Initiative Check: {total_roll} (Natural {total_roll - robyn.dexterity_modifier})"
    elif roll_name == "Acrobatics Skill Check":
        total_roll = rolls.acrobatics_check()
        roll_result = f"Acrobatics Check: {total_roll} (Natural {total_roll - (robyn.acrobatics + robyn.dexterity_modifier)})"
    elif roll_name == "Animal Handling Skill Check":
        total_roll = rolls.animal_handling_check()
        roll_result = f"Animal Handling Check: {total_roll} (Natural {total_roll - (robyn.animal_handling + robyn.wisdom_modifier)})"
    elif roll_name == "Arcana Skill Check":
        total_roll = rolls.arcana_check()
        roll_result = f"Arcana Check: {total_roll} (Natural {total_roll - (robyn.arcana + robyn.intelligence_modifier)})"
    elif roll_name == "Athletics Skill Check":
        total_roll = rolls.athletics_check()
        roll_result = f"Athletics Check: {total_roll} (Natural {total_roll - (robyn.athletics + robyn.strength_modifier)})"
    elif roll_name == "Deception Skill Check":
        total_roll = rolls.deception_check()
        roll_result = f"Deception Check: {total_roll} (Natural {total_roll - (robyn.deception + robyn.charisma_modifier)})"
    elif roll_name == "History Skill Check":
        total_roll = rolls.history_check()
        roll_result = f"History Check: {total_roll} (Natural {total_roll - (robyn.history + robyn.intelligence_modifier)})"
    elif roll_name == "Insight Skill Check":
        total_roll = rolls.insight_check()
        roll_result = f"Insight Check: {total_roll} (Natural {total_roll - (robyn.insight + robyn.wisdom_modifier)})"
    elif roll_name == "Intimidation Skill Check":
        total_roll = rolls.intimidation_check()
        roll_result = f"Intimidation Check (Disadvantage): {total_roll} (Natural {total_roll - (robyn.intimidation + robyn.charisma_modifier)})"
    elif roll_name == "Investigation Skill Check":
        total_roll = rolls.investigation_check()
        roll_result = f"Investigation Check: {total_roll} (Natural {total_roll - (robyn.investigation + robyn.intelligence_modifier)})"
    elif roll_name == "Medicine Skill Check":
        total_roll = rolls.medicine_check()
        roll_result = f"Medicine Check: {total_roll} (Natural {total_roll - (robyn.medicine + robyn.wisdom_modifier)})"
    elif roll_name == "Nature Skill Check":
        total_roll = rolls.nature_check()
        roll_result = f"Nature Check: {total_roll} (Natural {total_roll - (robyn.nature + robyn.intelligence_modifier)})"
    elif roll_name == "Perception Skill Check":
        total_roll = rolls.perception_check()
        roll_result = f"Perception Check: {total_roll} (Natural {total_roll - (robyn.perception + robyn.wisdom_modifier)})"
    elif roll_name == "Performance Skill Check":
        total_roll = rolls.performance_check()
        roll_result = f"Performance Check: {total_roll} (Natural {total_roll - (robyn.performance + robyn.charisma_modifier)})"
    elif roll_name == "Persuasion Skill Check":
        total_roll = rolls.persuasion_check()
        roll_result = f"Persuasion Check: {total_roll} (Natural {total_roll - (robyn.persuasion + robyn.charisma_modifier)})"
    elif roll_name == "Religion Skill Check":
        total_roll = rolls.religion_check()
        roll_result = f"Religion Check: {total_roll} (Natural {total_roll - (robyn.religion + robyn.intelligence_modifier)})"
    elif roll_name == "Sleight of Hand Skill Check":
        total_roll = rolls.sleight_of_hand_check()
        roll_result = f"Sleight of Hand Check: {total_roll} (Natural {total_roll - (robyn.sleight_of_hand + robyn.dexterity_modifier)})"
    elif roll_name == "Stealth Skill Check":
        total_roll = rolls.stealth_check()
        roll_result = f"Stealth Check (Disadvantage): {total_roll} (Natural {total_roll - (robyn.stealth + robyn.dexterity_modifier)})"
    elif roll_name == "Survival Skill Check":
        total_roll = rolls.survival_check()
        roll_result = f"Survival Check: {total_roll} (Natural {total_roll - (robyn.survival + robyn.wisdom_modifier)})"
    else:
        roll_result = "I'm sorry, I can't help with that yet."
    return render_template('index.html',   
        roll_result = roll_result, 
        level = robyn.level,
        max_hit_points = robyn.max_hit_points,
        armor_class = robyn.armor_class,
        spell_save_dc = robyn.spell_save_dc,
        daily_healing_light_dice = robyn.daily_healing_light_dice,
        passive_acrobatics = robyn.passive_acrobatics,
        passive_animal_handling = robyn.passive_animal_handling,
        passive_arcana = robyn.passive_arcana,
        passive_athletics = robyn.passive_athletics,
        passive_deception = robyn.passive_deception,
        passive_history = robyn.passive_history,
        passive_insight = robyn.passive_insight,
        passive_intimidation = robyn.passive_intimidation,
        passive_investigation = robyn.passive_investigation,
        passive_medicine = robyn.passive_medicine,
        passive_nature = robyn.passive_nature,
        passive_perception = robyn.passive_perception,
        passive_performance = robyn.passive_performance,
        passive_persuasion = robyn.passive_persuasion,
        passive_religion = robyn.passive_religion,
        passive_sleight_of_hand = robyn.passive_sleight_of_hand,
        passive_stealth = robyn.passive_stealth,
        passive_survival = robyn.passive_survival)

@app.route('/get-attack-roll', methods=['POST'])
def get_attack_roll():
    roll_name = request.form['roll_name']
    if roll_name == "Hel-ish Rebuke Damage":
        roll_result = f"Hel-ish Rebuke Damage (if Dexterity save < {robyn.spell_save_dc}): {rolls.hel_ish_rebuke_damage()} (Cold)"
    elif roll_name == "Offhand Dagger":
        total_roll = rolls.off_dagger_attack()
        roll_result = f"Offhand Dagger Attack: {total_roll} (Natural {total_roll-(robyn.dexterity_modifier + robyn.proficiency_bonus)})<br> <br>Offhand Dagger Damage: <span class='spoiler'>{rolls.off_dagger_damage()} (Piercing)</span>"
    elif roll_name == "Offhand Light Hammer":
        total_roll = rolls.off_light_hammer_attack()
        roll_result = f"Offhand Light Hammer Attack: {total_roll} (Natural {total_roll-(robyn.strength_modifier + robyn.proficiency_bonus)})<br> <br>Offhand Light Hammer Damage: <span class='spoiler'>{rolls.off_light_hammer_damage()} (Bludgeoning)</span>"
    elif roll_name == "Offhand Shadow Blade":
        total_roll = rolls.off_shadow_blade_attack()
        roll_result = f"Offhand Shadow Blade Attack: {total_roll} (Natural {total_roll-(robyn.dexterity_modifier + robyn.proficiency_bonus)})<br> <br>Offhand Shadow Blade Damage: <span class='spoiler'>{rolls.off_shadow_blade_damage()} (Psychic)</span>"
    elif roll_name == "Mainhand Dagger":
        total_roll = rolls.main_dagger_attack()
        roll_result = f"Mainhand Dagger Attack: {total_roll} (Natural {total_roll-(robyn.dexterity_modifier + robyn.proficiency_bonus)})<br> <br>Mainhand Dagger Damage: <span class='spoiler'>{rolls.main_dagger_damage()} (Piercing)</span>"
    elif roll_name == "Mainhand Light Hammer":
        total_roll = rolls.main_light_hammer_attack()
        roll_result = f"Mainhand Light Hammer Attack: {total_roll} (Natural {total_roll-(robyn.strength_modifier + robyn.proficiency_bonus)})<br> <br>Mainhand Light Hammer Damage: <span class='spoiler'>{rolls.main_light_hammer_damage()} (Bludgeoning)</span>"
    elif roll_name == "Mainhand Shadow Blade":
        total_roll = rolls.main_shadow_blade_attack()
        roll_result = f"Mainhand Shadow Blade Attack: {total_roll} (Natural {total_roll-(robyn.dexterity_modifier + robyn.proficiency_bonus)})<br> <br>Mainhand Shadow Blade Damage: <span class='spoiler'>{rolls.main_shadow_blade_damage()} (Psychic)</span>"
    elif roll_name == "Light Crossbow":
        total_roll = rolls.light_crossbow_attack()
        roll_result = f"Light Crossbow Attack: {total_roll} (Natural {total_roll-(robyn.dexterity_modifier + robyn.proficiency_bonus)})<br> <br>Light Crossbow Damage: <span class='spoiler'>{rolls.light_crossbow_damage()} (Piercing)</span>"
    elif roll_name == "Agonizing Eldritch Blast":
        total_roll = rolls.agonizing_eldritch_attack()
        roll_result = f"Eldritch Blast Attack: {total_roll} (Natural {total_roll-(robyn.charisma_modifier + robyn.proficiency_bonus)})<br> <br>Eldritch Blast Damage: <span class='spoiler'>{rolls.agonizing_eldritch_damage()} (Force)</span>"
    elif roll_name == "Sacred Flame Damage":
        roll_result = f"Sacred Flame Damage (if Dexterity save < {robyn.spell_save_dc}): {rolls.sacred_flame_damage()} (Radiant)"
    elif roll_name == "Sword Burst Damage":
        roll_result = f"Sword Burst Damage (if Dexterity save < {robyn.spell_save_dc}): {rolls.sword_burst_damage()} (Force)"
    else:
        roll_result = "I'm sorry, I can't help with that yet."
    return render_template('index.html',   
        roll_result = Markup(roll_result), 
        level = robyn.level,
        max_hit_points = robyn.max_hit_points,
        armor_class = robyn.armor_class,
        spell_save_dc = robyn.spell_save_dc,
        daily_healing_light_dice = robyn.daily_healing_light_dice,
        inspiring_leader_temp_hp = robyn.inspiring_leader_temp_hp,
        passive_acrobatics = robyn.passive_acrobatics,
        passive_animal_handling = robyn.passive_animal_handling,
        passive_arcana = robyn.passive_arcana,
        passive_athletics = robyn.passive_athletics,
        passive_deception = robyn.passive_deception,
        passive_history = robyn.passive_history,
        passive_insight = robyn.passive_insight,
        passive_intimidation = robyn.passive_intimidation,
        passive_investigation = robyn.passive_investigation,
        passive_medicine = robyn.passive_medicine,
        passive_nature = robyn.passive_nature,
        passive_perception = robyn.passive_perception,
        passive_performance = robyn.passive_performance,
        passive_persuasion = robyn.passive_persuasion,
        passive_religion = robyn.passive_religion,
        passive_sleight_of_hand = robyn.passive_sleight_of_hand,
        passive_stealth = robyn.passive_stealth,
        passive_survival = robyn.passive_survival)

@app.route('/get-buff-roll', methods=['POST'])
def get_buff_roll():
    roll_name = request.form['roll_name']
    if roll_name == "Single Healing Light":
        roll_result = f"Single Healing Light Charge: A creature in line of sight recovers {rolls.healing_light_dice()} hit points"
    elif roll_name == "Max Healing Light":
        roll_result = f"Maximum Healing Light Charges ({robyn.charisma_modifier}): A creature in line of sight recovers {rolls.max_healing_light_dice()} hit points"
    elif roll_name == "Single Hit Dice":
        roll_result = f"Single Hit Dice: Recover {rolls.short_rest_hit_dice()} hit points"
    elif roll_name == "All Hit Dice":
        roll_result = f"All Hit Dice ({robyn.level}): Recover {rolls.all_short_rest_hit_dice()} hit points"
    elif roll_name == "Baseline Talisman Buff":
        roll_result = f"Talisman Buff: Add {rolls.talisman_ability_check_buff()} to a failed ability or skill check"
    else:
        roll_result = "I'm sorry, I can't help with that yet."
    return render_template('index.html',   
        roll_result = roll_result, 
        level = robyn.level,
        max_hit_points = robyn.max_hit_points,
        armor_class = robyn.armor_class,
        spell_save_dc = robyn.spell_save_dc,
        daily_healing_light_dice = robyn.daily_healing_light_dice,
        inspiring_leader_temp_hp = robyn.inspiring_leader_temp_hp,
        passive_acrobatics = robyn.passive_acrobatics,
        passive_animal_handling = robyn.passive_animal_handling,
        passive_arcana = robyn.passive_arcana,
        passive_athletics = robyn.passive_athletics,
        passive_deception = robyn.passive_deception,
        passive_history = robyn.passive_history,
        passive_insight = robyn.passive_insight,
        passive_intimidation = robyn.passive_intimidation,
        passive_investigation = robyn.passive_investigation,
        passive_medicine = robyn.passive_medicine,
        passive_nature = robyn.passive_nature,
        passive_perception = robyn.passive_perception,
        passive_performance = robyn.passive_performance,
        passive_persuasion = robyn.passive_persuasion,
        passive_religion = robyn.passive_religion,
        passive_sleight_of_hand = robyn.passive_sleight_of_hand,
        passive_stealth = robyn.passive_stealth,
        passive_survival = robyn.passive_survival)

@app.route('/')
def index():
    return flask.render_template(
        'index.html',
        level = robyn.level,
        max_hit_points = robyn.max_hit_points,
        armor_class = robyn.armor_class,
        spell_save_dc = robyn.spell_save_dc,
        daily_healing_light_dice = robyn.daily_healing_light_dice,
        inspiring_leader_temp_hp = robyn.inspiring_leader_temp_hp,
        passive_acrobatics = robyn.passive_acrobatics,
        passive_animal_handling = robyn.passive_animal_handling,
        passive_arcana = robyn.passive_arcana,
        passive_athletics = robyn.passive_athletics,
        passive_deception = robyn.passive_deception,
        passive_history = robyn.passive_history,
        passive_insight = robyn.passive_insight,
        passive_intimidation = robyn.passive_intimidation,
        passive_investigation = robyn.passive_investigation,
        passive_medicine = robyn.passive_medicine,
        passive_nature = robyn.passive_nature,
        passive_perception = robyn.passive_perception,
        passive_performance = robyn.passive_performance,
        passive_persuasion = robyn.passive_persuasion,
        passive_religion = robyn.passive_religion,
        passive_sleight_of_hand = robyn.passive_sleight_of_hand,
        passive_stealth = robyn.passive_stealth,
        passive_survival = robyn.passive_survival
    )

if __name__ == '__main__':
    app.run()