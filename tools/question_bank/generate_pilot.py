#!/usr/bin/env python3
"""Generate original Phase-0 test MCQs for Physics 2nd Paper chapters 1–2."""

from __future__ import annotations

import csv
import random
from pathlib import Path

from paths import CSV_HEADERS, PILOT_CSV_PATH

SOURCE = "original-test"


def q(
    stem: str,
    a: str,
    b: str,
    c: str,
    d: str,
    correct: str,
    topic_ids: str,
    difficulty: str,
    qtype: str,
    verified: str = "true",
    explanation: str = "",
) -> dict[str, str]:
    return {
        "stem": stem,
        "option_a": a,
        "option_b": b,
        "option_c": c,
        "option_d": d,
        "correct": correct,
        "topic_ids": topic_ids,
        "difficulty": difficulty,
        "type": qtype,
        "source": SOURCE,
        "verified": verified,
        "explanation": explanation,
    }


def thermodynamics_questions() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    # t01 Heat and temperature
    tid = "phy2_ch01_t01"
    rows += [
        q("Which quantity measures the hotness or coldness of a body?", "Heat", "Temperature", "Internal energy", "Entropy", "B", tid, "easy", "factual"),
        q("Heat is a form of:", "Mass", "Force", "Energy", "Momentum", "C", tid, "easy", "factual"),
        q("The SI unit of temperature is:", "Celsius", "Fahrenheit", "Kelvin", "Calorie", "C", tid, "easy", "factual"),
        q("Absolute zero corresponds to:", "0 °C", "0 °F", "0 K", "273 K", "C", tid, "easy", "factual"),
        q("0 °C is equal to:", "0 K", "273 K", "100 K", "373 K", "B", tid, "easy", "numerical"),
        q("100 °C is equal to:", "273 K", "300 K", "373 K", "473 K", "C", tid, "easy", "numerical"),
        q("Temperature difference of 1 K is equal to a difference of:", "1 °C", "1 °F", "273 °C", "5/9 °C", "A", tid, "medium", "conceptual"),
        q("Heat flows spontaneously from:", "Cold to hot body", "Hot to cold body", "Either direction equally", "Only in vacuum", "B", tid, "easy", "conceptual"),
        q("Which device is used to measure temperature?", "Barometer", "Thermometer", "Manometer", "Galvanometer", "B", tid, "easy", "factual"),
        q("Thermal equilibrium means two bodies have the same:", "Mass", "Volume", "Temperature", "Density", "C", tid, "easy", "conceptual"),
        q("Zeroth law of thermodynamics is the basis of:", "Thermometers", "Heat engines", "Refrigerators", "Capacitors", "A", tid, "medium", "conceptual"),
        q("Calorie is a unit of:", "Temperature", "Heat", "Power", "Pressure", "B", tid, "easy", "factual"),
        q("1 calorie is approximately:", "0.42 J", "4.2 J", "42 J", "420 J", "B", tid, "medium", "factual"),
        q("Which scale has the same size degree as Celsius?", "Fahrenheit", "Rankine", "Kelvin", "None", "C", tid, "medium", "conceptual"),
        q("If two bodies are each in thermal equilibrium with a third, they are in equilibrium with each other. This is the:", "First law", "Second law", "Zeroth law", "Third law", "C", tid, "medium", "factual"),
    ]

    # t02 Thermal expansion
    tid = "phy2_ch01_t02"
    rows += [
        q("Most solids expand on:", "Cooling", "Heating", "Compression only", "Freezing", "B", tid, "easy", "factual"),
        q("Linear expansion coefficient α relates change in:", "Area", "Volume", "Length", "Density only", "C", tid, "easy", "factual"),
        q("For isotropic solids, volume expansion coefficient γ is approximately:", "α", "2α", "3α", "α/3", "C", tid, "medium", "conceptual"),
        q("Area expansion coefficient β is approximately:", "α", "2α", "3α", "α/2", "B", tid, "medium", "conceptual"),
        q("A metal rod of length L0 expands by ΔL when heated by ΔT. Then α equals:", "ΔL/(L0 ΔT)", "L0/(ΔL ΔT)", "ΔT/(L0 ΔL)", "ΔL L0 ΔT", "A", tid, "medium", "numerical"),
        q("Water shows anomalous expansion near:", "0 °C to 4 °C", "4 °C to 100 °C", "Below −10 °C", "Above 100 °C", "A", tid, "medium", "factual"),
        q("Density of water is maximum at about:", "0 °C", "4 °C", "10 °C", "100 °C", "B", tid, "easy", "factual"),
        q("Bimetallic strip bends on heating because metals have different:", "Masses", "Expansion coefficients", "Colors", "Resistivities only", "B", tid, "easy", "conceptual"),
        q("Apparent expansion of a liquid depends on expansion of:", "Liquid only", "Container only", "Both liquid and container", "Neither", "C", tid, "medium", "conceptual"),
        q("Real expansion of liquid = apparent expansion +:", "Linear expansion of vessel", "Volume expansion of vessel", "Area expansion of vessel", "Zero always", "B", tid, "medium", "factual"),
        q("Gaps are left in railway tracks to allow for:", "Contraction only", "Thermal expansion", "Vibration damping only", "Electrical insulation", "B", tid, "easy", "application"),
        q("If a hole is cut in a metal plate and the plate is heated, the hole:", "Shrinks", "Expands", "Remains same", "Disappears", "B", tid, "medium", "conceptual"),
        q("Unit of linear expansion coefficient is:", "K", "K⁻¹", "m/K", "J/K", "B", tid, "easy", "factual"),
        q("A steel bridge expands more on a hot day than a cool night mainly due to:", "Humidity", "Temperature rise", "Wind", "Traffic load only", "B", tid, "easy", "application"),
        q("For the same temperature rise, the material with larger α expands:", "Less", "More", "Equally always", "Not at all", "B", tid, "easy", "conceptual"),
    ]

    # t03 Calorimetry
    tid = "phy2_ch01_t03"
    rows += [
        q("Specific heat capacity is heat required to raise temperature of unit mass by:", "1 K", "10 K", "100 K", "0 K", "A", tid, "easy", "factual"),
        q("SI unit of specific heat capacity is:", "J/kg", "J/K", "J kg⁻¹ K⁻¹", "W/K", "C", tid, "easy", "factual"),
        q("Water has a relatively:", "Low specific heat", "High specific heat", "Zero specific heat", "Infinite specific heat", "B", tid, "easy", "factual"),
        q("Heat gained or lost without phase change is Q =:", "mL", "mcΔT", "mgh", "½mv²", "B", tid, "easy", "factual"),
        q("Calorimeter is used to measure:", "Electric charge", "Heat exchange", "Magnetic field", "Light intensity", "B", tid, "easy", "factual"),
        q("If m = 2 kg, c = 4200 J kg⁻¹ K⁻¹, ΔT = 5 K, heat Q is:", "2100 J", "8400 J", "42000 J", "84000 J", "C", tid, "medium", "numerical"),
        q("Two bodies in a calorimeter reach the same final temperature by:", "Momentum conservation only", "Heat exchange", "Charge flow", "Nuclear reaction", "B", tid, "easy", "conceptual"),
        q("Heat capacity of a body equals:", "mc", "m/c", "c/m", "m + c", "A", tid, "medium", "factual"),
        q("The substance that needs more heat for the same ΔT (same mass) has:", "Smaller c", "Larger c", "Same c always", "Zero c", "B", tid, "easy", "conceptual"),
        q("Principle of calorimetry assumes:", "No heat loss to surroundings", "Infinite heat loss", "No temperature change", "Vacuum only", "A", tid, "medium", "conceptual"),
        q("Molar heat capacity is heat to raise 1 mole by:", "1 K", "1 °F", "10 K", "100 K", "A", tid, "medium", "factual"),
        q("Which typically has higher specific heat?", "Iron", "Copper", "Water", "Lead", "C", tid, "easy", "factual"),
        q("If two equal masses of different metals absorb equal heat, the one with smaller c shows:", "Smaller ΔT", "Larger ΔT", "Zero ΔT", "Negative ΔT", "B", tid, "medium", "conceptual"),
        q("Thermal capacity depends on:", "Mass and specific heat", "Color only", "Shape only", "Charge only", "A", tid, "easy", "conceptual"),
        q("In mixing hot and cold water (no loss), heat lost by hot water equals:", "Work done", "Heat gained by cold water", "Change in mass", "Entropy always zero", "B", tid, "easy", "conceptual"),
    ]

    # t04 Latent heat
    tid = "phy2_ch01_t04"
    rows += [
        q("Latent heat is associated with:", "Temperature change only", "Phase change", "Pressure only", "Color change", "B", tid, "easy", "factual"),
        q("During melting of ice at 0 °C, temperature:", "Increases", "Decreases", "Remains constant", "Oscillates", "C", tid, "easy", "conceptual"),
        q("Q = mL is used when:", "Only temperature changes", "Phase changes at constant T", "Only volume changes", "Charge flows", "B", tid, "easy", "factual"),
        q("Latent heat of fusion of ice is heat to convert ice at 0 °C to:", "Steam at 100 °C", "Water at 0 °C", "Ice at −10 °C", "Water at 100 °C", "B", tid, "easy", "factual"),
        q("Latent heat of vaporization converts water at 100 °C to:", "Ice", "Water at 0 °C", "Steam at 100 °C", "Water at 50 °C", "C", tid, "easy", "factual"),
        q("For ice of mass 0.1 kg with L = 3.34×10⁵ J/kg, heat to melt fully is about:", "3.34×10³ J", "3.34×10⁴ J", "3.34×10⁵ J", "3.34×10⁶ J", "B", tid, "medium", "numerical"),
        q("Boiling occurs throughout the liquid while evaporation occurs:", "Only at the surface", "Only at the bottom", "Nowhere", "Only in solids", "A", tid, "medium", "conceptual"),
        q("Sublimation is change from:", "Liquid to gas", "Solid to gas", "Gas to liquid", "Liquid to solid", "B", tid, "easy", "factual"),
        q("Condensation releases:", "Latent heat", "No energy", "Only kinetic energy of Earth", "Nuclear energy", "A", tid, "medium", "conceptual"),
        q("Why does steam at 100 °C burn more severely than water at 100 °C?", "Steam has lower energy", "Steam releases latent heat on condensation", "Steam is denser", "Steam has no heat", "B", tid, "medium", "application"),
        q("Regelation is related to:", "Melting under pressure", "Only boiling", "Only radiation", "Capacitance", "A", tid, "hard", "factual"),
        q("Unit of latent heat is:", "J/kg", "J/K", "W", "N/m", "A", tid, "easy", "factual"),
        q("Melting point of a substance is the temperature at which:", "It always vaporizes", "Solid and liquid coexist in equilibrium", "It becomes plasma", "Density is zero", "B", tid, "medium", "conceptual"),
        q("Heat required to convert 2 kg water at 100 °C to steam (L=2.26×10⁶ J/kg) is:", "2.26×10⁶ J", "4.52×10⁶ J", "1.13×10⁶ J", "2.26×10³ J", "B", tid, "medium", "numerical"),
        q("During boiling at constant pressure, added heat mainly increases:", "Temperature continuously", "Internal energy related to phase change", "Mass of liquid", "Charge", "B", tid, "medium", "conceptual"),
    ]

    # t05 Kinetic theory
    tid = "phy2_ch01_t05"
    rows += [
        q("Kinetic theory relates gas pressure to:", "Molecular collisions with walls", "Color of gas", "Only gravity", "Nuclear forces", "A", tid, "easy", "conceptual"),
        q("Average kinetic energy of an ideal gas molecule is proportional to:", "Pressure only", "Absolute temperature", "Volume only", "Mass of container", "B", tid, "easy", "factual"),
        q("RMS speed of gas molecules increases when temperature:", "Decreases", "Increases", "Stays zero", "Becomes negative", "B", tid, "easy", "conceptual"),
        q("For an ideal gas, PV =:", "(1/3)Nm c̄² related form / (1/3)Mn c_rms²", "mgh", "qV", "IR", "A", tid, "medium", "factual"),
        q("Pressure of an ideal gas is:", "P = (1/3)ρ c_rms²", "P = ρ c_rms", "P = (1/2)ρ c_rms²", "P = 3ρ c_rms²", "A", tid, "medium", "factual"),
        q("Mean kinetic energy per molecule is:", "(1/2)kT", "(3/2)kT", "kT", "2kT", "B", tid, "medium", "factual"),
        q("Boltzmann constant relates energy scale to:", "Temperature", "Charge", "Magnetic field", "Wavelength only", "A", tid, "easy", "conceptual"),
        q("Assumptions of kinetic theory include molecules being:", "Point masses with elastic collisions", "Sticky always", "At rest always", "Charged always", "A", tid, "medium", "factual"),
        q("Heavier gas molecules (same T) have:", "Higher rms speed", "Lower rms speed", "Same rms speed always", "Zero speed", "B", tid, "medium", "conceptual"),
        q("Absolute temperature is proportional to:", "Total potential energy only", "Average translational KE of molecules", "Color", "Number of neutrons", "B", tid, "medium", "conceptual"),
        q("If T is doubled (ideal gas, same gas), rms speed becomes:", "Half", "Same", "√2 times", "2 times", "C", tid, "medium", "numerical"),
        q("Brownian motion supports the idea that:", "Molecules are in random motion", "Molecules are at rest", "Heat is a fluid called caloric only", "Gases have no pressure", "A", tid, "easy", "conceptual"),
        q("Most probable speed, average speed, and rms speed are:", "Always identical", "Different statistical speeds", "Undefined", "Only for solids", "B", tid, "hard", "conceptual"),
        q("Gas pressure increases with temperature at fixed volume mainly because molecules:", "Move slower", "Hit walls harder/more often", "Disappear", "Lose mass", "B", tid, "easy", "conceptual"),
        q("k in (3/2)kT is:", "Coulomb constant", "Boltzmann constant", "Spring constant", "Decay constant", "B", tid, "easy", "factual"),
    ]

    # t06 Ideal gas
    tid = "phy2_ch01_t06"
    rows += [
        q("Ideal gas equation is:", "PV = nRT", "F = ma", "V = IR", "E = mc²", "A", tid, "easy", "factual"),
        q("In PV = nRT, T must be in:", "Celsius", "Fahrenheit", "Kelvin", "Any unit", "C", tid, "easy", "factual"),
        q("R is the:", "Universal gas constant", "Resistance", "Reynolds number always", "Radius", "A", tid, "easy", "factual"),
        q("Boyle's law: at constant T, PV is:", "Proportional to V²", "Constant", "Zero", "Infinite", "B", tid, "easy", "factual"),
        q("Charles's law: at constant P, V is proportional to:", "1/T", "T", "T²", "P", "B", tid, "easy", "factual"),
        q("Avogadro's law relates equal volumes of gases (same T,P) to equal:", "Masses", "Densities", "Numbers of molecules", "Colors", "C", tid, "medium", "factual"),
        q("If n is doubled at fixed T and V, pressure:", "Halves", "Doubles", "Unchanged", "Becomes zero", "B", tid, "medium", "numerical"),
        q("STP often refers to conditions near:", "0 K and zero pressure", "273 K and 1 atm", "373 K and 2 atm", "Room color", "B", tid, "medium", "factual"),
        q("One mole of ideal gas at STP occupies about:", "2.24 L", "22.4 L", "224 L", "0.224 L", "B", tid, "easy", "factual"),
        q("If T doubles and V doubles at constant n, pressure:", "Doubles", "Halves", "Remains same", "Becomes four times", "C", tid, "medium", "numerical"),
        q("Partial pressure concept appears in:", "Dalton's law", "Hooke's law", "Snell's law", "Ohm's law", "A", tid, "medium", "factual"),
        q("Real gases approach ideal behavior at:", "High pressure and low T", "Low pressure and high T", "Near liquefaction always", "Absolute zero only", "B", tid, "hard", "conceptual"),
        q("n in PV=nRT is amount of substance in:", "Grams always", "Moles", "Newtons", "Coulombs", "B", tid, "easy", "factual"),
        q("If P is constant and T increases, density of ideal gas:", "Increases", "Decreases", "Stays fixed always", "Becomes infinite", "B", tid, "medium", "conceptual"),
        q("Combined gas law can be written as:", "P1V1/T1 = P2V2/T2", "P1/T1 = V2/T2 only", "V = constant always", "P = T/V²", "A", tid, "medium", "factual"),
    ]

    # t07 First law
    tid = "phy2_ch01_t07"
    rows += [
        q("First law of thermodynamics is essentially conservation of:", "Charge", "Momentum", "Energy", "Mass number", "C", tid, "easy", "factual"),
        q("ΔU = Q − W (common sign convention) relates:", "Internal energy, heat, work", "Only voltage", "Only entropy", "Only charge", "A", tid, "easy", "factual"),
        q("Internal energy of an ideal gas depends primarily on:", "Volume only", "Temperature", "Path shape only", "Color", "B", tid, "medium", "conceptual"),
        q("In a cyclic process, net change in internal energy is:", "Maximum", "Minimum", "Zero", "Infinite", "C", tid, "medium", "conceptual"),
        q("If Q = 100 J and W = 40 J (work by system), ΔU is:", "140 J", "60 J", "40 J", "100 J", "B", tid, "medium", "numerical"),
        q("Work done by gas in expansion is often:", "Positive in that convention", "Always zero", "Negative always", "Infinite", "A", tid, "easy", "conceptual"),
        q("Heat absorbed by system is often taken as:", "Positive Q", "Negative Q always", "Zero", "Undefined", "A", tid, "easy", "factual"),
        q("Adiabatic process means:", "Q = 0", "W = 0", "ΔU = 0", "T = 0", "A", tid, "easy", "factual"),
        q("Isochoric process means:", "Constant pressure", "Constant volume", "Constant temperature", "Q = 0", "B", tid, "easy", "factual"),
        q("For isochoric process, work done by gas is typically:", "Maximum", "Zero (no volume change)", "Equal to Q always only if isothermal", "Infinite", "B", tid, "medium", "conceptual"),
        q("Isobaric means constant:", "Volume", "Temperature", "Pressure", "Entropy only", "C", tid, "easy", "factual"),
        q("First law forbids:", "Energy creation from nothing", "Heat flow", "Work", "Temperature", "A", tid, "medium", "conceptual"),
        q("If a system absorbs 50 J heat and does 50 J work, ΔU is:", "100 J", "50 J", "0 J", "−50 J", "C", tid, "easy", "numerical"),
        q("State function among the following is:", "Heat Q", "Work W", "Internal energy U", "Path length", "C", tid, "medium", "conceptual"),
        q("Q and W are:", "State functions", "Path functions", "Always equal", "Always zero", "B", tid, "medium", "conceptual"),
    ]

    # t08 Processes
    tid = "phy2_ch01_t08"
    rows += [
        q("In an isothermal process for ideal gas, ΔU is:", "Positive", "Negative", "Zero", "Infinite", "C", tid, "easy", "conceptual"),
        q("For isothermal ideal gas, Q equals:", "0", "W", "ΔU", "P only", "B", tid, "medium", "conceptual"),
        q("In adiabatic expansion of ideal gas, temperature generally:", "Increases", "Decreases", "Stays fixed always", "Becomes absolute zero immediately", "B", tid, "medium", "conceptual"),
        q("Slope of P–V diagram for adiabatic is steeper than isothermal because:", "γ > 1 related behavior", "γ < 0", "R = 0", "n = 0", "A", tid, "hard", "conceptual"),
        q("Isobaric expansion work is:", "PΔV", "VΔP", "0", "nRT always only", "A", tid, "easy", "factual"),
        q("Which process has constant temperature?", "Isothermal", "Adiabatic always", "Isochoric always", "Isobaric always", "A", tid, "easy", "factual"),
        q("In a free expansion into vacuum (ideal gas), work and heat are often taken as zero so ΔU is:", "Zero", "Maximum", "Negative large", "Undefined always", "A", tid, "hard", "conceptual"),
        q("Polytropic process follows:", "PV^n = constant", "P = constant only", "V = 0", "T = ∞", "A", tid, "medium", "factual"),
        q("For adiabatic process of ideal gas, TV^(γ−1) is:", "Constant", "Zero", "Infinite", "Random", "A", tid, "hard", "factual"),
        q("γ for ideal gas is:", "Cp/Cv", "Cv/Cp", "R/n", "P/V", "A", tid, "medium", "factual"),
        q("Work in a process equals area under:", "P–V curve", "T–S only always", "V–T only always", "Charge–time", "A", tid, "easy", "conceptual"),
        q("Isochoric heating increases:", "Pressure (for ideal gas in closed system)", "Volume only", "Neither P nor T", "Mass", "A", tid, "medium", "conceptual"),
        q("Quasi-static process is idealized as:", "Infinitely slow, near equilibrium", "Explosive always", "Impossible always", "Only adiabatic", "A", tid, "hard", "conceptual"),
        q("In isobaric cooling, volume of ideal gas:", "Increases", "Decreases", "Must stay fixed", "Becomes imaginary", "B", tid, "easy", "conceptual"),
        q("Which quantity is zero for a cyclic process?", "Net work always", "ΔU", "Heat always", "Pressure", "B", tid, "medium", "conceptual"),
    ]

    # t09 Second law / engines
    tid = "phy2_ch01_t09"
    rows += [
        q("Second law of thermodynamics restricts:", "Direction of processes / efficiency limits", "Only Newton's laws", "Only Coulomb force", "Only optics", "A", tid, "easy", "conceptual"),
        q("A heat engine converts:", "Heat partly into work", "Work wholly into mass", "Charge into light only", "Nothing", "A", tid, "easy", "factual"),
        q("Efficiency of heat engine is:", "W/Q_in", "Q_in/W", "Q_out/Q_in only always 1", "T_cold/T_hot always", "A", tid, "easy", "factual"),
        q("Carnot engine operates between:", "Two heat reservoirs", "One reservoir only", "No temperatures", "Only vacuum", "A", tid, "easy", "factual"),
        q("Carnot efficiency is:", "1 − T_c/T_h", "T_c/T_h", "1 + T_c/T_h", "T_h/T_c − 1 only wrong form", "A", tid, "medium", "factual"),
        q("Temperatures in Carnot efficiency formula must be:", "Celsius", "Kelvin", "Fahrenheit", "Any", "B", tid, "easy", "factual"),
        q("No engine can be more efficient than Carnot engine between same temperatures. This is related to:", "Second law", "Ohm's law", "Hooke's law", "Snell's law", "A", tid, "medium", "conceptual"),
        q("Refrigerator transfers heat from:", "Cold to hot with work input", "Hot to cold without work always", "Nowhere", "Only radiation in space", "A", tid, "medium", "conceptual"),
        q("Clausius statement concerns impossibility of heat flowing from cold to hot:", "Without external work", "Always freely", "Only in solids", "Never stated", "A", tid, "medium", "factual"),
        q("Kelvin–Planck statement says you cannot convert heat entirely into work in a:", "Cyclic process from a single reservoir", "Any process ever", "Only adiabatic case", "Only isobaric case", "A", tid, "hard", "factual"),
        q("If T_h = 600 K and T_c = 300 K, Carnot efficiency is:", "25%", "50%", "75%", "100%", "B", tid, "medium", "numerical"),
        q("Waste heat rejected to sink is:", "Q_out", "Always zero for real engines", "W only", "U only", "A", tid, "easy", "conceptual"),
        q("Higher T_h (fixed T_c) tends to make Carnot efficiency:", "Lower", "Higher", "Unchanged", "Negative", "B", tid, "easy", "conceptual"),
        q("A perpetual motion machine of the second kind would violate:", "Second law", "Only geometry", "Only optics", "Nothing", "A", tid, "medium", "conceptual"),
        q("Working substance in Carnot cycle returns to:", "Initial state each cycle", "Absolute zero", "Infinite volume", "Plasma", "A", tid, "easy", "conceptual"),
    ]

    # t10 Entropy
    tid = "phy2_ch01_t10"
    rows += [
        q("Entropy is a measure related to:", "Disorder / unavailable energy", "Only electric charge", "Only mass", "Only color", "A", tid, "easy", "conceptual"),
        q("For a reversible heat transfer, dS =:", "đQ_rev/T", "đQ/P", "W/T", "PV", "A", tid, "medium", "factual"),
        q("In an isolated system, entropy of the universe for irreversible processes:", "Decreases", "Increases", "Stays exactly zero always", "Is undefined always", "B", tid, "medium", "conceptual"),
        q("For a reversible adiabatic process, change in entropy is:", "Zero", "Maximum", "Negative large", "Infinite", "A", tid, "medium", "conceptual"),
        q("Entropy is a:", "Path function", "State function", "Force", "Vector always", "B", tid, "medium", "conceptual"),
        q("Unit of entropy is:", "J/K", "J", "W", "N", "A", tid, "easy", "factual"),
        q("Melting of ice at 0 °C increases entropy of the system because:", "Heat is absorbed at constant T", "Heat is rejected", "Mass decreases", "Charge increases", "A", tid, "medium", "conceptual"),
        q("Third law implies entropy approaches a minimum as T approaches:", "Infinity", "Absolute zero", "100 °C", "Room temperature only", "B", tid, "hard", "factual"),
        q("Irreversible processes generate:", "Entropy", "Only perfect order", "Negative absolute T", "Perpetual work without heat", "A", tid, "easy", "conceptual"),
        q("Heat death idea is linked to maximum:", "Entropy", "Pressure", "Charge", "Luminosity only", "A", tid, "hard", "conceptual"),
        q("For free expansion of ideal gas into vacuum, ΔU=0 but entropy of gas:", "Decreases", "Increases", "Is unchanged", "Becomes negative", "B", tid, "hard", "conceptual"),
        q("ΔS of universe for a reversible cycle is:", "Zero", "Positive always", "Negative always", "Infinite", "A", tid, "medium", "conceptual"),
        q("Which process is more irreversible typically?", "Frictionless quasi-static", "Free expansion / with friction", "Ideal Carnot", "Reversible isothermal carefully done", "B", tid, "easy", "conceptual"),
        q("Entropy change when heat Q enters a reservoir at T (approx) is:", "Q/T", "QT", "T/Q", "Q−T", "A", tid, "medium", "numerical"),
        q("Second law can be stated in terms of:", "Entropy increase principles", "Only Coulomb's law", "Only Snell's law", "Only Hooke's law", "A", tid, "easy", "conceptual"),
    ]

    return rows


def static_electricity_questions() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    tid = "phy2_ch02_t01"
    rows += [
        q("Electric charge is a:", "Scalar property of matter", "Vector always", "Unit of power", "Temperature", "A", tid, "easy", "factual"),
        q("SI unit of charge is:", "Ampere", "Volt", "Coulomb", "Ohm", "C", tid, "easy", "factual"),
        q("Charge of electron is approximately:", "−1.6×10⁻¹⁹ C", "+1.6×10⁻¹⁹ C", "1 C", "0", "A", tid, "easy", "factual"),
        q("Like charges:", "Attract", "Repel", "Ignore each other", "Always neutralize instantly", "B", tid, "easy", "factual"),
        q("Unlike charges:", "Repel", "Attract", "Have no force", "Produce only gravity", "B", tid, "easy", "factual"),
        q("Conservation of charge means total charge in an isolated system:", "Increases", "Decreases", "Remains constant", "Becomes fractional freely", "C", tid, "easy", "conceptual"),
        q("Quantization of charge means charge is:", "Continuous any value", "Integer multiple of e", "Always zero", "Only positive", "B", tid, "medium", "factual"),
        q("Conductors allow charges to:", "Move freely", "Never move", "Only vibrate as locked", "Disappear", "A", tid, "easy", "conceptual"),
        q("Insulators:", "Do not allow free charge flow easily", "Are perfect superconductors", "Have infinite free electrons always", "Cannot be charged", "A", tid, "easy", "factual"),
        q("Charging by friction typically transfers:", "Electrons", "Protons from nucleus easily", "Neutrons", "Photons as charge", "A", tid, "medium", "conceptual"),
        q("A body becomes positively charged when it:", "Gains electrons", "Loses electrons", "Gains protons from nowhere", "Gains neutrons", "B", tid, "easy", "conceptual"),
        q("Earthing a conductor can:", "Share charge with Earth", "Create mass", "Change color only", "Stop gravity", "A", tid, "medium", "application"),
        q("Charge is additive: total charge is algebraic sum. This treats charge as:", "Scalar with sign", "Vector cross product", "Tensor only", "Complex always", "A", tid, "medium", "conceptual"),
        q("1 μC equals:", "10⁻³ C", "10⁻⁶ C", "10⁶ C", "10⁻⁹ C", "B", tid, "easy", "numerical"),
        q("Neutral atom has:", "Equal protons and electrons", "Only neutrons", "Only protons", "No particles", "A", tid, "easy", "factual"),
    ]

    tid = "phy2_ch02_t02"
    rows += [
        q("Coulomb's law gives force between:", "Two point charges", "Two masses only", "Two currents only", "Two magnets only", "A", tid, "easy", "factual"),
        q("Coulomb force magnitude is proportional to:", "q1 q2 / r²", "q1 + q2", "r² / q1q2", "q1 q2 r", "A", tid, "easy", "factual"),
        q("Direction of Coulomb force is along the:", "Line joining charges", "Perpendicular always", "Random", "Velocity only", "A", tid, "easy", "conceptual"),
        q("In SI, Coulomb's constant k is about:", "9×10⁹ N m² C⁻²", "9×10⁻⁹", "1.6×10⁻¹⁹", "3×10⁸", "A", tid, "easy", "factual"),
        q("If distance between charges doubles, force becomes:", "Double", "Half", "One-fourth", "Four times", "C", tid, "medium", "numerical"),
        q("If both charges are doubled, force becomes:", "Half", "Double", "Four times", "Unchanged", "C", tid, "medium", "numerical"),
        q("Coulomb's law is analogous in form to:", "Newton's law of gravitation", "Ohm's law", "Snell's law", "Hooke's law only", "A", tid, "medium", "conceptual"),
        q("Force is attractive if charges have:", "Same sign", "Opposite signs", "Zero magnitude", "Infinite magnitude", "B", tid, "easy", "conceptual"),
        q("In vector form, F21 = k q1 q2 / r² * r̂21. The unit vector points from:", "2 to 1 or as defined from source to field point carefully", "Random", "Always upward", "Only left", "A", tid, "hard", "conceptual"),
        q("Superposition principle for electrostatic forces means:", "Net force is vector sum", "Forces multiply", "Only largest force counts", "Forces cancel always", "A", tid, "medium", "conceptual"),
        q("k = 1/(4πε0). ε0 is:", "Permittivity of free space", "Permeability of free space", "Electron charge", "Planck constant", "A", tid, "medium", "factual"),
        q("If r is halved, Coulomb force becomes:", "Half", "Double", "4 times", "1/4", "C", tid, "easy", "numerical"),
        q("Coulomb force is a:", "Contact force only", "Action-at-a-distance / field-mediated central force", "Nuclear force", "Friction only", "B", tid, "medium", "conceptual"),
        q("In a medium with dielectric constant K, force between charges is reduced by factor:", "K", "1/K", "K²", "√K", "A", tid, "hard", "factual"),
        q("Unit of k in SI involves:", "N m² C⁻²", "N only", "C only", "J/T", "A", tid, "easy", "factual"),
    ]

    tid = "phy2_ch02_t03"
    rows += [
        q("Electric field E at a point is force on a:", "Unit positive charge", "Unit negative charge only definition sometimes confusing", "Unit mass", "Unit current", "A", tid, "easy", "factual"),
        q("SI unit of electric field is:", "N/C or V/m", "J", "C", "Ω", "A", tid, "easy", "factual"),
        q("Field due to a point charge is:", "E = kq/r²", "E = kq/r", "E = kq²/r²", "E = q/r² only without k", "A", tid, "easy", "factual"),
        q("Electric field lines start on:", "Negative charges", "Positive charges", "Neutrons", "Only infinity always", "B", tid, "easy", "factual"),
        q("Electric field lines end on:", "Positive charges", "Negative charges", "Masses", "Photons", "B", tid, "easy", "factual"),
        q("Field lines never:", "Cross each other", "Exist", "Indicate direction", "Indicate relative strength by density", "A", tid, "easy", "conceptual"),
        q("Denser field lines mean:", "Weaker field", "Stronger field", "Zero field", "Undefined field", "B", tid, "easy", "conceptual"),
        q("Direction of E is the direction of force on a:", "Positive test charge", "Negative test charge", "Neutral atom always", "Neutron", "A", tid, "easy", "conceptual"),
        q("Electric field is a:", "Scalar", "Vector", "Tensor rank 0 only", "Dimensionless", "B", tid, "easy", "factual"),
        q("Inside a charged conductor in electrostatics, E is:", "Maximum", "Zero", "Infinite", "Equal to surface value always inside", "B", tid, "medium", "factual"),
        q("Field of an infinite line charge varies as:", "1/r", "1/r²", "1/r³", "Constant everywhere", "A", tid, "hard", "factual"),
        q("Uniform field between large parallel plates (approx) is:", "σ/ε0 related", "Zero always", "Infinite always", "Only magnetic", "A", tid, "medium", "factual"),
        q("A negative charge placed in an electric field experiences force:", "Opposite to E", "Along E", "Perpendicular always", "Zero always", "A", tid, "medium", "conceptual"),
        q("If q is positive, E points:", "Away from the charge", "Toward the charge", "Tangentially only", "Randomly", "A", tid, "easy", "conceptual"),
        q("Superposition applies to electric fields as:", "Vector sum", "Product", "Maximum only", "Minimum only", "A", tid, "easy", "conceptual"),
    ]

    tid = "phy2_ch02_t04"
    rows += [
        q("Electric flux through a surface involves:", "E · dA", "B · dl only", "I²R", "mgh", "A", tid, "easy", "factual"),
        q("SI unit of electric flux is:", "N m² C⁻¹", "C", "V", "T", "A", tid, "medium", "factual"),
        q("Gauss's law relates flux through closed surface to:", "Enclosed charge / ε0", "Enclosed mass", "Enclosed current only", "Temperature", "A", tid, "easy", "factual"),
        q("For a closed surface with no enclosed charge, net flux is:", "Zero", "Maximum", "Infinite", "Negative always", "A", tid, "easy", "conceptual"),
        q("Flux through a closed surface depends on charges:", "Outside only", "Inside", "Nowhere", "Only on the surface material color", "B", tid, "medium", "conceptual"),
        q("Gauss's law is useful for finding E with:", "High symmetry", "No symmetry ever", "Only gravity", "Only circuits", "A", tid, "easy", "application"),
        q("For a point charge at center of sphere, flux is:", "q/ε0", "0", "4πq", "ε0 q", "A", tid, "medium", "numerical"),
        q("If charge is moved outside a Gaussian surface, flux through it:", "Becomes zero (if nothing enclosed)", "Stays same always", "Doubles", "Becomes infinite", "A", tid, "medium", "conceptual"),
        q("ε0 appears in Gauss's law as:", "q_enc/ε0 = Φ", "q_enc ε0 = Φ", "Φ = q_enc", "Φ = ε0 only", "A", tid, "easy", "factual"),
        q("Field due to infinite plane sheet is:", "σ/(2ε0)", "σ/ε0 always half missing", "kσ/r²", "Zero", "A", tid, "hard", "factual"),
        q("For a charged conducting sphere, outside E behaves like:", "Point charge at center", "Zero", "Uniform forever", "Magnetic dipole only", "A", tid, "medium", "conceptual"),
        q("Inside a uniformly charged insulating sphere (r < R), E is proportional to:", "r", "1/r²", "1/r", "r² only always", "A", tid, "hard", "factual"),
        q("Net flux is independent of:", "Shape of Gaussian surface (for given enclosed q)", "Enclosed charge", "ε0", "Whether surface is closed", "A", tid, "medium", "conceptual"),
        q("Positive flux often means field lines:", "Leaving the surface", "Entering only", "Tangential only", "None exist", "A", tid, "easy", "conceptual"),
        q("Gauss's law is equivalent (in electrostatics) to Coulomb's law for:", "Inverse-square nature in 3D", "Any force law", "Only magnetism", "Only relativity", "A", tid, "hard", "conceptual"),
    ]

    tid = "phy2_ch02_t05"
    rows += [
        q("Electric potential is work to bring unit positive charge from:", "Infinity (usual ref) to the point", "The nucleus only", "Earth's core only", "A magnet", "A", tid, "easy", "conceptual"),
        q("SI unit of potential is:", "Volt", "Ampere", "Coulomb", "Watt", "A", tid, "easy", "factual"),
        q("Potential due to point charge is:", "V = kq/r", "V = kq/r²", "V = kq r", "V = q", "A", tid, "easy", "factual"),
        q("Potential difference V_ab equals work per unit charge from:", "a to b (sign conventions careful)", "Mass to weight", "Only current", "Only flux", "A", tid, "medium", "conceptual"),
        q("E is related to V by:", "E = −∇V", "E = V²", "E = ∫V dt", "E = qV", "A", tid, "medium", "factual"),
        q("In the direction of E, potential:", "Increases", "Decreases", "Stays fixed always", "Becomes complex", "B", tid, "medium", "conceptual"),
        q("1 volt equals:", "1 J/C", "1 J", "1 C/J", "1 N", "A", tid, "easy", "factual"),
        q("Potential is a:", "Scalar", "Vector", "Tensor only", "Force", "A", tid, "easy", "factual"),
        q("For positive point charge, V is:", "Positive around it (usual ref)", "Always negative", "Zero everywhere", "Infinite negative", "A", tid, "easy", "conceptual"),
        q("Electron-volt (eV) is a unit of:", "Energy", "Potential only", "Charge", "Current", "A", tid, "medium", "factual"),
        q("If V is constant in a region, E is:", "Zero", "Maximum", "Infinite", "Uniform nonzero always", "A", tid, "medium", "conceptual"),
        q("Work by electrostatic field on charge q moving is related to:", "qΔV", "q/E only", "Only mass", "Only flux", "A", tid, "medium", "conceptual"),
        q("Potential at infinity is often taken as:", "Zero", "Infinity", "1 V", "−1 V", "A", tid, "easy", "factual"),
        q("Two points with same potential have potential difference:", "Zero", "Maximum", "Equal to E", "Infinite", "A", tid, "easy", "conceptual"),
        q("If r doubles from a point charge, potential becomes:", "Half", "One-fourth", "Double", "Four times", "A", tid, "medium", "numerical"),
    ]

    tid = "phy2_ch02_t06"
    rows += [
        q("Equipotential surface is a surface where potential is:", "Same everywhere on it", "Zero only", "Maximum only", "Undefined", "A", tid, "easy", "factual"),
        q("Work to move a charge on an equipotential surface is:", "Zero", "Maximum", "qE always nonzero", "Infinite", "A", tid, "easy", "conceptual"),
        q("Electric field is perpendicular to:", "Equipotential surfaces", "Field lines", "Nothing", "Current only", "A", tid, "medium", "conceptual"),
        q("For a point charge, equipotentials are:", "Concentric spheres", "Planes only", "Lines only", "Cubes", "A", tid, "easy", "factual"),
        q("For uniform field, equipotentials are:", "Planes perpendicular to field", "Spheres centered anywhere", "Random curves", "Along the field", "A", tid, "medium", "factual"),
        q("No work by electrostatic field means motion along:", "Equipotential", "Field line always only", "Any path with ΔV≠0", "Closed nuclear orbit only", "A", tid, "medium", "conceptual"),
        q("Two equipotential surfaces cannot:", "Intersect (different potentials)", "Exist", "Be closed", "Be open", "A", tid, "medium", "conceptual"),
        q("Closer equipotentials mean:", "Stronger |E| roughly", "Weaker |E|", "Zero charge", "No field interpretation", "A", tid, "medium", "conceptual"),
        q("Conductor surface in electrostatics is:", "Equipotential", "Maximum potential gradient inside", "Non-equipotential always", "Magnetic only", "A", tid, "medium", "factual"),
        q("Inside a hollow conductor (no charge inside), potential is:", "Constant (equal to surface)", "Infinite", "Zero always regardless of surface", "Oscillating", "A", tid, "hard", "conceptual"),
        q("Moving charge between equipotentials requires external work if:", "ΔV ≠ 0 against electrostatics", "ΔV = 0", "E = 0 and ΔV=0", "Always never", "A", tid, "easy", "conceptual"),
        q("Equipotential drawing helps visualize:", "Potential landscape and E direction", "Only temperature", "Only mass density", "Only circuits with batteries absent meaninglessly", "A", tid, "easy", "application"),
        q("Field line crossing an equipotential does so:", "Orthonormal / at right angles", "At 0° always", "At 45° always", "Never", "A", tid, "medium", "factual"),
        q("All points of a connected conductor share:", "Same potential in electrostatics", "Same random potential", "Different potentials necessarily", "Zero charge only", "A", tid, "easy", "conceptual"),
        q("Earth is often treated as an equipotential of:", "Zero potential reference", "Infinite potential", "1 V fixed for all problems", "Negative infinity only", "A", tid, "medium", "application"),
    ]

    tid = "phy2_ch02_t07"
    rows += [
        q("Capacitance C is defined as:", "Q/V", "V/Q", "QV", "Q+V", "A", tid, "easy", "factual"),
        q("SI unit of capacitance is:", "Farad", "Henry", "Tesla", "Siemens", "A", tid, "easy", "factual"),
        q("1 μF equals:", "10⁻⁶ F", "10⁶ F", "10⁻³ F", "10⁻⁹ F", "A", tid, "easy", "numerical"),
        q("Capacitance of parallel plate capacitor is:", "ε0 A/d", "ε0 d/A", "A d /ε0", "ε0 A d", "A", tid, "easy", "factual"),
        q("Increasing plate area increases C:", "True", "False", "Only if d increases", "Never", "A", tid, "easy", "conceptual"),
        q("Increasing separation d decreases C:", "True", "False", "Only for electrolytes", "Never", "A", tid, "easy", "conceptual"),
        q("A capacitor stores:", "Charge and energy in electric field", "Only mass", "Only magnetic monopoles", "Only heat always", "A", tid, "easy", "conceptual"),
        q("Dielectric between plates generally:", "Increases capacitance", "Decreases capacitance always", "Removes capacitance", "Shorts always necessarily", "A", tid, "medium", "factual"),
        q("C depends on:", "Geometry and medium", "Only charge on it always linearly defining geometry away", "Only voltage rating color", "Only temperature never geometry", "A", tid, "medium", "conceptual"),
        q("Farad is a:", "Large unit practically", "Tiny unit never used as μF", "Unit of resistance", "Unit of current", "A", tid, "easy", "factual"),
        q("Spherical capacitor capacitance involves:", "ab/(b−a) type formula with 4πε0", "Only A/d for spheres wrongly", "Only R", "Zero always", "A", tid, "hard", "factual"),
        q("If d is halved, C of parallel plate becomes:", "Half", "Double", "Same", "Four times", "B", tid, "medium", "numerical"),
        q("Isolated sphere capacitance is:", "4πε0 R", "ε0 R", "4πε0 /R", "R/ε0", "A", tid, "hard", "factual"),
        q("Capacitor blocks steady:", "Current in DC after charging (open circuit behavior)", "Voltage always", "Charge forever from existing", "Electric field inside always to zero wrongly", "A", tid, "medium", "application"),
        q("Q = CV means for fixed C, more V means:", "More charge", "Less charge", "Same charge", "Zero charge", "A", tid, "easy", "conceptual"),
    ]

    tid = "phy2_ch02_t08"
    rows += [
        q("Capacitors in parallel share the same:", "Voltage", "Charge always equal", "Energy always equal", "Current forever", "A", tid, "easy", "factual"),
        q("Equivalent capacitance of parallel combination is:", "Sum of C's", "Sum of 1/C's", "Product only", "Difference", "A", tid, "easy", "factual"),
        q("Capacitors in series share the same:", "Charge (ideal series)", "Voltage always equal", "Area", "Dielectric always", "A", tid, "easy", "factual"),
        q("For two equal C in series, Ceq is:", "C/2", "2C", "C", "4C", "A", tid, "easy", "numerical"),
        q("For two equal C in parallel, Ceq is:", "2C", "C/2", "C", "C²", "A", tid, "easy", "numerical"),
        q("1/Ceq for series equals:", "Σ(1/Ci)", "Σ Ci", "Π Ci", "0", "A", tid, "easy", "factual"),
        q("Three 3 μF in parallel give:", "1 μF", "3 μF", "9 μF", "0.3 μF", "C", tid, "medium", "numerical"),
        q("Three 3 μF in series give:", "1 μF", "3 μF", "9 μF", "6 μF", "A", tid, "medium", "numerical"),
        q("In series, voltage divides:", "Inversely to capacitance (Q same)", "Equally always regardless of C", "Proportional to C only wrong", "Not at all", "A", tid, "medium", "conceptual"),
        q("In parallel, charge divides:", "Proportional to C", "Inversely to C", "Equally always", "Randomly", "A", tid, "medium", "conceptual"),
        q("Network reduction uses series-parallel rules when geometry allows:", "True", "False always", "Only for resistors not capacitors", "Only AC", "A", tid, "easy", "application"),
        q("Adding a capacitor in parallel to a circuit capacitor bank:", "Increases Ceq", "Decreases Ceq", "No effect", "Removes voltage", "A", tid, "easy", "conceptual"),
        q("Adding series capacitor to an existing capacitor:", "Decreases Ceq", "Increases Ceq", "No effect", "Makes C infinite", "A", tid, "easy", "conceptual"),
        q("Two capacitors 2 μF and 3 μF in series: Ceq =:", "1.2 μF", "5 μF", "6 μF", "1 μF", "A", tid, "medium", "numerical"),
        q("Two capacitors 2 μF and 3 μF in parallel: Ceq =:", "5 μF", "1.2 μF", "6 μF", "0.5 μF", "A", tid, "easy", "numerical"),
    ]

    tid = "phy2_ch02_t09"
    rows += [
        q("Energy stored in a capacitor is:", "½CV²", "CV", "C²V", "V/C", "A", tid, "easy", "factual"),
        q("Energy can also be written as:", "½ QV", "QV", "Q/V", "2QV", "A", tid, "medium", "factual"),
        q("Energy density in electric field in vacuum is:", "½ ε0 E²", "ε0 E", "E²/ε0", "σ E only always", "A", tid, "hard", "factual"),
        q("If V is doubled (C fixed), energy becomes:", "Double", "Half", "Four times", "Same", "C", tid, "medium", "numerical"),
        q("If C is doubled (V fixed), energy becomes:", "Double", "Half", "Four times", "Same", "A", tid, "medium", "numerical"),
        q("Charging a capacitor from a battery: energy from battery vs stored:", "Battery supplies more than stored (heat loss in resistance)", "Exactly equal always with no loss ever", "Stored more than supplied", "Zero supplied", "A", tid, "hard", "conceptual"),
        q("Energy is stored in the:", "Electric field between plates", "Wires only", "Battery chemistry only always", "Earth only", "A", tid, "easy", "conceptual"),
        q("Unit of energy is:", "Joule", "Farad", "Volt", "Coulomb", "A", tid, "easy", "factual"),
        q("½ Q²/C equals:", "Energy stored", "Force", "Flux", "Current", "A", tid, "medium", "factual"),
        q("Discharging through a resistor converts stored energy mainly to:", "Heat", "Rest mass", "Nuclear binding", "Gravitational PE only", "A", tid, "medium", "application"),
        q("For C=2 μF and V=100 V, energy is:", "0.01 J", "0.02 J", "1 J", "2 J", "A", tid, "medium", "numerical"),
        q("Increasing d while connected to battery (V fixed) makes energy:", "Decrease (since C↓)", "Increase", "Unchanged", "Infinite", "A", tid, "hard", "conceptual"),
        q("Increasing d for isolated capacitor (Q fixed) makes energy:", "Increase", "Decrease", "Unchanged", "Zero", "A", tid, "hard", "conceptual"),
        q("Energy formulas ½CV², ½QV, Q²/(2C) are:", "Equivalent", "Contradictory", "Only for inductors", "Only magnetic", "A", tid, "easy", "conceptual"),
        q("Sudden connecting of charged capacitors can involve:", "Energy redistribution / possible loss as heat/spark", "No energy concept", "Only nuclear energy", "Only sound without EM", "A", tid, "hard", "application"),
    ]

    tid = "phy2_ch02_t10"
    rows += [
        q("A dielectric is typically a:", "Insulating material", "Perfect conductor", "Superconductor only", "Plasma only", "A", tid, "easy", "factual"),
        q("Dielectric constant K is:", "εr = ε/ε0", "ε0/ε", "σ", "ρ", "A", tid, "easy", "factual"),
        q("Inserting dielectric (battery connected) generally:", "Increases C", "Decreases C", "Removes all charge instantly always", "Makes V infinite", "A", tid, "medium", "conceptual"),
        q("Polarization in dielectric means:", "Separation of bound charges", "Creation of monopoles free forever", "Nuclear fission", "Only heating", "A", tid, "medium", "conceptual"),
        q("With dielectric filled, capacitance becomes:", "K C0", "C0/K", "C0", "0", "A", tid, "easy", "factual"),
        q("Dielectric reduces effective field inside for given free charge because of:", "Bound charge polarization", "Gravity", "Magnetism only", "Nuclear force", "A", tid, "hard", "conceptual"),
        q("Dielectric strength is the maximum:", "Electric field before breakdown", "Current before melting wire only", "Temperature", "Pressure", "A", tid, "medium", "factual"),
        q("Paper, mica, ceramic are used as:", "Dielectrics in capacitors", "Electrode metals only", "Fuels", "Superconductors always", "A", tid, "easy", "application"),
        q("If dielectric is inserted with charge kept constant, V generally:", "Decreases", "Increases", "Stays same", "Becomes zero always", "A", tid, "medium", "conceptual"),
        q("If dielectric inserted with battery connected, Q generally:", "Increases", "Decreases", "Stays same", "Becomes zero", "A", tid, "medium", "conceptual"),
        q("K for vacuum is:", "1", "0", "∞", "−1", "A", tid, "easy", "factual"),
        q("Polar molecules reorient in an external field contributing to:", "Polarization", "Only gravity", "Only radioactivity", "Only sound", "A", tid, "medium", "conceptual"),
        q("Breakdown of dielectric leads to:", "Conducting path / spark", "Perfect insulation forever", "Cooling only", "Mass increase only", "A", tid, "easy", "application"),
        q("Effective ε =:", "K ε0", "ε0/K", "K/ε0", "ε0 only always", "A", tid, "easy", "factual"),
        q("Dielectrics allow capacitors to store more charge at given V mainly by:", "Increasing C", "Decreasing C", "Removing plates", "Shorting terminals", "A", tid, "easy", "conceptual"),
    ]

    return rows


def unverified_samples() -> list[dict[str, str]]:
    """A few unverified rows to prove they are excluded from eligible counts."""
    return [
        q(
            "UNVERIFIED PLACEHOLDER: Heat always flows from cold to hot spontaneously.",
            "True",
            "False",
            "Only in vacuum",
            "Only at 0 K",
            "B",
            "phy2_ch01_t01",
            "easy",
            "conceptual",
            verified="false",
            explanation="Included to test verified filter; do not use in exams.",
        ),
        q(
            "UNVERIFIED PLACEHOLDER: Capacitance unit is the Henry.",
            "True",
            "False",
            "Only in AC",
            "Only for inductors wrongly as C",
            "B",
            "phy2_ch02_t07",
            "easy",
            "factual",
            verified="false",
        ),
    ]


def cross_topic_samples() -> list[dict[str, str]]:
    """Questions tagged with two topics (strict filter requires both allowed)."""
    return [
        q(
            "Using PV=nRT and molecular KE~(3/2)kT, pressure relates to molecular motion. Which pair is most directly linked?",
            "Ideal gas law and kinetic theory",
            "Only optics",
            "Only capacitance",
            "Only magnetism",
            "A",
            "phy2_ch01_t05;phy2_ch01_t06",
            "hard",
            "conceptual",
        ),
        q(
            "Electric potential and field are related; equipotentials are perpendicular to field lines. This links:",
            "Potential and equipotentials",
            "Only heat engines",
            "Only latent heat",
            "Only Boyle's law",
            "A",
            "phy2_ch02_t05;phy2_ch02_t06",
            "medium",
            "conceptual",
        ),
    ]


def main() -> None:
    rows = thermodynamics_questions() + static_electricity_questions()
    rows += cross_topic_samples()
    rows += unverified_samples()

    # Light shuffle for less chapter clustering in the file (stable seed).
    rng = random.Random(42)
    rng.shuffle(rows)

    PILOT_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with PILOT_CSV_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(rows)

    verified = sum(1 for r in rows if r["verified"].lower() == "true")
    print(f"Wrote {len(rows)} questions ({verified} verified) to {PILOT_CSV_PATH}")


if __name__ == "__main__":
    main()
