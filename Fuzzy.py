# -*- coding: utf-8 -*-
# importando bibliotecas necessárias para a execução do código
import sys

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def acc(*args):
    return np.sum(args)


def avaliar_covid(in_met_defuzz,
                  in_tosse, in_febre, in_coriza, in_dorGarganta,
                  in_dificuldadeRespirar, in_anosmia, in_disturbiosGastrintestinais,
                  in_astenia, in_hiporexia, in_dispneia, in_print_state=False):
    # DEFINIÇÃO
    # Tosse
    # Febre
    # Coriza
    # Dor de garganta
    # Dificuldade para respirar
    # Perda de olfato (anosmia)
    # Alteração do paladar (ageusia)
    # Distúrbios gastrintestinais (náuseas/vômitos/diarreia)
    # Cansaço (astenia)
    # Diminuição do apetite (hiporexia)
    # Dispnéia ( falta de ar)

    # ANTECEDENTES
    tosse = ctrl.Antecedent(np.arange(0, 100, 0.1), 'tosse')
    febre = ctrl.Antecedent(np.arange(0, 100, 0.1), 'febre')
    coriza = ctrl.Antecedent(np.arange(0, 100, 0.1), 'coriza')
    dorGarganta = ctrl.Antecedent(np.arange(0, 100, 0.1), 'dorGarganta')
    dificuldadeRespirar = ctrl.Antecedent(np.arange(0, 100, 0.1), 'dificuldadeRespirar')
    anosmia = ctrl.Antecedent(np.arange(0, 100, 0.1), 'anosmia')
    disturbiosGastrintestinais = ctrl.Antecedent(np.arange(0, 100, 0.1), 'disturbiosGastrintestinais')
    astenia = ctrl.Antecedent(np.arange(0, 100, 0.1), 'astenia')
    hiporexia = ctrl.Antecedent(np.arange(0, 100, 0.1), 'hiporexia')
    dispneia = ctrl.Antecedent(np.arange(0, 100, 0.1), 'dispneia')

    # CONSEQUENTE
    # Chance de estar com covid19
    chanceEstarContaminado = ctrl.Consequent(np.arange(0, 100, 0.1), 'chanceEstarContaminado',
                                             defuzzify_method=in_met_defuzz)
    chanceEstarContaminado.accumulation_method = acc



    #sim nao

    # ENTRADAS
    # Tosse
    tosse['nao'] = fuzz.trimf(tosse.universe, [0, 35, 45])
    tosse['sim'] = fuzz.trimf(tosse.universe, [50, 70, 100])


    # Febre
    febre['nao'] = fuzz.trimf(febre.universe, [0, 35, 45])
    febre['sim'] = fuzz.trimf(febre.universe, [50, 70, 100])


    # Coriza
    coriza['nao'] = fuzz.trimf(coriza.universe, [0, 35, 45])
    coriza['sim'] = fuzz.trimf(coriza.universe, [50, 70, 100])


    # DorGarganta
    dorGarganta['nao'] = fuzz.trimf(dorGarganta.universe, [0, 35, 45])
    dorGarganta['sim'] = fuzz.trimf(dorGarganta.universe, [50, 70, 100])


    # DificuldadeRespirar
    dificuldadeRespirar['nao'] = fuzz.trimf(dificuldadeRespirar.universe, [0, 35, 45])
    dificuldadeRespirar['sim'] = fuzz.trimf(dificuldadeRespirar.universe, [50, 70, 100])


    # Anosmia
    anosmia['nao'] = fuzz.trimf(anosmia.universe, [0, 35, 45])
    anosmia['sim'] = fuzz.trimf(anosmia.universe, [0, 70, 100])


    # DisturbiosGastrintestinais
    disturbiosGastrintestinais['nao'] = fuzz.trimf(disturbiosGastrintestinais.universe, [0, 35, 45])
    disturbiosGastrintestinais['sim'] = fuzz.trimf(disturbiosGastrintestinais.universe, [0, 70, 100])


    # Astenia
    astenia['nao'] = fuzz.trimf(astenia.universe, [0, 35, 45])
    astenia['sim'] = fuzz.trimf(astenia.universe, [0, 70, 100])


    # Hiporexia
    hiporexia['nao'] = fuzz.trimf(hiporexia.universe, [0, 35, 45])
    hiporexia['sim'] = fuzz.trimf(hiporexia.universe, [0, 70, 100])


    # Dispneia
    dispneia['nao'] = fuzz.trimf(dispneia.universe, [0, 35, 45])
    dispneia['sim'] = fuzz.trimf(dispneia.universe, [0, 70, 100])



    # SAÍDA
    chanceEstarContaminado['nao'] = fuzz.trimf(chanceEstarContaminado.universe, [0, 35, 45])
    chanceEstarContaminado['sim'] = fuzz.trimf(chanceEstarContaminado.universe, [0, 70, 100])




    # REGRAS COVID




    ## ------------- REGRAS -----------
    r0 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r1 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r2 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r3 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r4 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r5 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r6 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r7 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r8 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r9 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r10 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r11 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r12 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r13 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r14 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r15 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r16 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r17 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r18 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r19 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r20 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r21 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r22 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r23 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r24 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r25 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r26 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r27 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r28 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r29 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['nao'])
    r30 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['nao'])
    r31 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r32 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r33 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r34 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r35 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r36 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r37 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r38 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r39 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r40 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r41 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r42 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r43 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r44 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r45 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r46 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r47 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r48 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r49 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r50 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r51 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r52 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r53 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r54 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r55 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r56 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r57 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r58 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r59 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r60 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r61 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r62 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r63 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r64 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r65 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r66 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r67 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r68 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r69 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r70 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r71 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r72 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r73 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r74 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r75 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r76 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r77 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r78 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r79 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r80 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r81 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r82 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r83 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r84 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r85 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r86 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r87 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r88 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r89 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r90 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r91 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r92 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r93 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r94 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r95 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r96 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r97 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r98 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r99 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r100 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r101 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r102 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r103 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r104 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r105 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r106 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r107 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r108 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r109 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r110 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r111 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r112 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r113 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r114 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r115 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r116 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r117 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r118 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r119 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r120 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r121 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r122 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r123 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r124 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r125 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r126 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r127 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r128 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r129 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r130 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r131 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r132 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r133 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r134 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r135 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r136 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r137 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r138 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r139 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r140 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r141 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r142 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r143 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r144 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r145 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r146 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r147 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r148 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r149 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r150 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r151 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r152 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r153 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r154 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r155 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r156 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r157 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r158 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r159 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r160 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r161 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r162 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r163 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r164 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r165 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r166 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r167 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r168 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r169 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r170 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r171 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r172 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r173 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r174 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r175 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r176 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r177 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r178 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r179 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r180 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r181 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r182 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r183 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r184 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r185 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r186 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r187 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r188 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r189 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r190 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r191 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r192 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r193 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r194 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r195 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r196 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r197 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r198 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r199 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r200 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r201 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r202 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r203 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r204 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r205 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r206 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r207 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r208 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r209 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r210 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r211 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r212 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r213 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r214 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r215 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r216 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r217 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r218 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r219 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r220 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r221 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r222 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r223 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r224 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r225 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r226 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r227 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r228 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r229 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r230 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r231 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r232 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r233 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r234 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r235 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r236 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r237 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r238 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r239 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r240 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r241 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r242 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r243 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r244 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r245 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r246 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r247 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r248 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r249 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r250 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r251 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r252 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r253 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r254 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r255 = ctrl.Rule(
        tosse['nao'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r256 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r257 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r258 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r259 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r260 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r261 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r262 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r263 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r264 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r265 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r266 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r267 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r268 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r269 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r270 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r271 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r272 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r273 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r274 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r275 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r276 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r277 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r278 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r279 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r280 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r281 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r282 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r283 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r284 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r285 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r286 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r287 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r288 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r289 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r290 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r291 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r292 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r293 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r294 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r295 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r296 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r297 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r298 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r299 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r300 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r301 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r302 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r303 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r304 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r305 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r306 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r307 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r308 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r309 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r310 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r311 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r312 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r313 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r314 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r315 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r316 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r317 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r318 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r319 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r320 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r321 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r322 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r323 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r324 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r325 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r326 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r327 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r328 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r329 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r330 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r331 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r332 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r333 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r334 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r335 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r336 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r337 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r338 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r339 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r340 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r341 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r342 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r343 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r344 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r345 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r346 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r347 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r348 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r349 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r350 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r351 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r352 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r353 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r354 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r355 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r356 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r357 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r358 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r359 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r360 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r361 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r362 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r363 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r364 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r365 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r366 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r367 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r368 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r369 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r370 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r371 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r372 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r373 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r374 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r375 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r376 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r377 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r378 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r379 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r380 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r381 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r382 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r383 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r384 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r385 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r386 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r387 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r388 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r389 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r390 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r391 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r392 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r393 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r394 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r395 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r396 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r397 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r398 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r399 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r400 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r401 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r402 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r403 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r404 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r405 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r406 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r407 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r408 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r409 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r410 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r411 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r412 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r413 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r414 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r415 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r416 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r417 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r418 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r419 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r420 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r421 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r422 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r423 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r424 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r425 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r426 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r427 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r428 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r429 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r430 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r431 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r432 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r433 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r434 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r435 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r436 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r437 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r438 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r439 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r440 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r441 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r442 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r443 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r444 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r445 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r446 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r447 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r448 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r449 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r450 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r451 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r452 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r453 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r454 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r455 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r456 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r457 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r458 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r459 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r460 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r461 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r462 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r463 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r464 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r465 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r466 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r467 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r468 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r469 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r470 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r471 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r472 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r473 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r474 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r475 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r476 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r477 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r478 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r479 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r480 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r481 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r482 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r483 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r484 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r485 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r486 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r487 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r488 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r489 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r490 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r491 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r492 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r493 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r494 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r495 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r496 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r497 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r498 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r499 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r500 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r501 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r502 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r503 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r504 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r505 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r506 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r507 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r508 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r509 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r510 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r511 = ctrl.Rule(
        tosse['nao'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r512 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r513 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r514 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r515 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r516 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r517 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r518 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r519 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r520 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r521 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r522 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r523 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r524 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r525 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r526 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r527 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r528 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r529 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r530 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r531 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r532 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r533 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r534 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r535 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r536 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r537 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r538 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r539 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r540 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r541 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r542 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r543 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r544 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r545 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r546 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r547 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r548 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r549 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r550 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r551 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r552 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r553 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r554 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r555 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r556 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r557 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r558 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r559 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r560 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r561 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r562 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r563 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r564 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r565 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r566 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r567 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r568 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r569 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r570 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r571 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r572 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r573 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r574 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r575 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r576 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r577 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r578 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r579 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r580 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r581 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r582 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r583 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r584 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r585 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r586 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r587 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r588 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r589 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r590 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r591 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r592 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r593 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r594 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r595 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r596 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r597 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r598 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r599 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r600 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r601 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r602 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r603 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r604 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r605 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r606 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r607 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r608 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r609 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r610 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r611 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r612 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r613 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r614 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r615 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r616 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r617 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r618 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r619 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r620 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r621 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r622 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r623 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r624 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r625 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r626 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r627 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r628 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r629 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r630 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r631 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r632 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r633 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r634 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r635 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r636 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r637 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r638 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r639 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r640 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r641 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r642 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r643 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r644 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r645 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r646 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r647 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r648 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r649 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r650 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r651 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r652 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r653 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r654 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r655 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r656 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r657 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r658 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r659 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r660 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r661 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r662 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r663 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r664 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r665 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r666 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r667 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r668 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r669 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r670 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r671 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r672 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r673 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r674 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r675 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r676 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r677 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r678 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r679 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r680 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r681 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r682 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r683 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r684 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r685 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r686 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r687 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r688 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r689 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r690 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r691 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r692 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r693 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r694 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r695 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r696 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r697 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r698 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r699 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r700 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r701 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r702 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r703 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r704 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r705 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r706 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r707 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r708 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r709 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r710 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r711 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r712 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r713 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r714 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r715 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r716 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r717 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r718 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r719 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r720 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r721 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r722 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r723 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r724 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r725 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r726 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r727 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r728 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r729 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r730 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r731 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r732 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r733 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r734 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r735 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r736 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r737 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r738 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r739 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r740 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r741 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r742 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r743 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r744 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r745 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r746 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r747 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r748 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r749 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r750 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r751 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r752 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r753 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r754 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r755 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r756 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r757 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r758 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r759 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r760 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r761 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r762 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r763 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r764 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r765 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r766 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r767 = ctrl.Rule(
        tosse['sim'] & febre['nao'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r768 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r769 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r770 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r771 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r772 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r773 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r774 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r775 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r776 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r777 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r778 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r779 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r780 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r781 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r782 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r783 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r784 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r785 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r786 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r787 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r788 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r789 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r790 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r791 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r792 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r793 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r794 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r795 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r796 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r797 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r798 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r799 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r800 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r801 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r802 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r803 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r804 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r805 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r806 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r807 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r808 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r809 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r810 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r811 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r812 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r813 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r814 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r815 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r816 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r817 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r818 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r819 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r820 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r821 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r822 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r823 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r824 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r825 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r826 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r827 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r828 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r829 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r830 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r831 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r832 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r833 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r834 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r835 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r836 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r837 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r838 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r839 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r840 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r841 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r842 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r843 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r844 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r845 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r846 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r847 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r848 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r849 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r850 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r851 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r852 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r853 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r854 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r855 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r856 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r857 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r858 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r859 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r860 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r861 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r862 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r863 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r864 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r865 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r866 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r867 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r868 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r869 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r870 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r871 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r872 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r873 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r874 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r875 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r876 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r877 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r878 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r879 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r880 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r881 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r882 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r883 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r884 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r885 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r886 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r887 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r888 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r889 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r890 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r891 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r892 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r893 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r894 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r895 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['nao'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r896 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r897 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r898 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r899 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r900 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r901 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r902 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r903 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r904 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r905 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r906 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r907 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r908 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r909 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r910 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r911 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r912 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r913 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r914 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r915 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r916 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r917 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r918 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r919 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r920 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r921 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r922 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r923 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r924 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r925 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r926 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r927 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r928 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r929 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r930 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r931 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r932 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r933 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r934 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r935 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r936 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r937 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r938 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r939 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r940 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r941 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r942 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r943 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r944 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r945 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r946 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r947 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r948 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r949 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r950 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r951 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r952 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r953 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r954 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r955 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r956 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r957 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r958 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r959 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['nao'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r960 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r961 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r962 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r963 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r964 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r965 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r966 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r967 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r968 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r969 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r970 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r971 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r972 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r973 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r974 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r975 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r976 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r977 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r978 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r979 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r980 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r981 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r982 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r983 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r984 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r985 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r986 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r987 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r988 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r989 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r990 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r991 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['nao'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r992 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r993 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r994 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r995 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r996 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r997 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r998 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r999 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1000 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1001 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1002 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1003 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1004 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1005 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1006 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1007 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['nao'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1008 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1009 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1010 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1011 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1012 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1013 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1014 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1015 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['nao'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1016 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1017 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1018 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1019 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['nao'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1020 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1021 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['nao'] & dispneia['sim'],
        chanceEstarContaminado['sim'])
    r1022 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['nao'],
        chanceEstarContaminado['sim'])
    r1023 = ctrl.Rule(
        tosse['sim'] & febre['sim'] & coriza['sim'] & dorGarganta['sim'] & dificuldadeRespirar['sim'] & anosmia['sim'] &
        disturbiosGastrintestinais['sim'] & astenia['sim'] & hiporexia['sim'] & dispneia['sim'],
        chanceEstarContaminado['sim'])







    #AQUI DEVE SER PASSADA TODAS AS REGRAS
    chanceEstarContaminado_ctrl = ctrl.ControlSystem([r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,r34,r35,r36,r37,r38,r39,r40,r41,r42,r43,r44,r45,r46,r47,r48,r49,r50,r51,r52,r53,r54,r55,r56,r57,r58,r59,r60,r61,r62,r63,r64,r65,r66,r67,r68,r69,r70,r71,r72,r73,r74,r75,r76,r77,r78,r79,r80,r81,r82,r83,r84,r85,r86,r87,r88,r89,r90,r91,r92,r93,r94,r95,r96,r97,r98,r99,r100,r101,r102,r103,r104,r105,r106,r107,r108,r109,r110,r111,r112,r113,r114,r115,r116,r117,r118,r119,r120,r121,r122,r123,r124,r125,r126,r127,r128,r129,r130,r131,r132,r133,r134,r135,r136,r137,r138,r139,r140,r141,r142,r143,r144,r145,r146,r147,r148,r149,r150,r151,r152,r153,r154,r155,r156,r157,r158,r159,r160,r161,r162,r163,r164,r165,r166,r167,r168,r169,r170,r171,r172,r173,r174,r175,r176,r177,r178,r179,r180,r181,r182,r183,r184,r185,r186,r187,r188,r189,r190,r191,r192,r193,r194,r195,r196,r197,r198,r199,r200,r201,r202,r203,r204,r205,r206,r207,r208,r209,r210,r211,r212,r213,r214,r215,r216,r217,r218,r219,r220,r221,r222,r223,r224,r225,r226,r227,r228,r229,r230,r231,r232,r233,r234,r235,r236,r237,r238,r239,r240,r241,r242,r243,r244,r245,r246,r247,r248,r249,r250,r251,r252,r253,r254,r255,r256,r257,r258,r259,r260,r261,r262,r263,r264,r265,r266,r267,r268,r269,r270,r271,r272,r273,r274,r275,r276,r277,r278,r279,r280,r281,r282,r283,r284,r285,r286,r287,r288,r289,r290,r291,r292,r293,r294,r295,r296,r297,r298,r299,r300,r301,r302,r303,r304,r305,r306,r307,r308,r309,r310,r311,r312,r313,r314,r315,r316,r317,r318,r319,r320,r321,r322,r323,r324,r325,r326,r327,r328,r329,r330,r331,r332,r333,r334,r335,r336,r337,r338,r339,r340,r341,r342,r343,r344,r345,r346,r347,r348,r349,r350,r351,r352,r353,r354,r355,r356,r357,r358,r359,r360,r361,r362,r363,r364,r365,r366,r367,r368,r369,r370,r371,r372,r373,r374,r375,r376,r377,r378,r379,r380,r381,r382,r383,r384,r385,r386,r387,r388,r389,r390,r391,r392,r393,r394,r395,r396,r397,r398,r399,r400,r401,r402,r403,r404,r405,r406,r407,r408,r409,r410,r411,r412,r413,r414,r415,r416,r417,r418,r419,r420,r421,r422,r423,r424,r425,r426,r427,r428,r429,r430,r431,r432,r433,r434,r435,r436,r437,r438,r439,r440,r441,r442,r443,r444,r445,r446,r447,r448,r449,r450,r451,r452,r453,r454,r455,r456,r457,r458,r459,r460,r461,r462,r463,r464,r465,r466,r467,r468,r469,r470,r471,r472,r473,r474,r475,r476,r477,r478,r479,r480,r481,r482,r483,r484,r485,r486,r487,r488,r489,r490,r491,r492,r493,r494,r495,r496,r497,r498,r499,r500,r501,r502,r503,r504,r505,r506,r507,r508,r509,r510,r511,r512,r513,r514,r515,r516,r517,r518,r519,r520,r521,r522,r523,r524,r525,r526,r527,r528,r529,r530,r531,r532,r533,r534,r535,r536,r537,r538,r539,r540,r541,r542,r543,r544,r545,r546,r547,r548,r549,r550,r551,r552,r553,r554,r555,r556,r557,r558,r559,r560,r561,r562,r563,r564,r565,r566,r567,r568,r569,r570,r571,r572,r573,r574,r575,r576,r577,r578,r579,r580,r581,r582,r583,r584,r585,r586,r587,r588,r589,r590,r591,r592,r593,r594,r595,r596,r597,r598,r599,r600,r601,r602,r603,r604,r605,r606,r607,r608,r609,r610,r611,r612,r613,r614,r615,r616,r617,r618,r619,r620,r621,r622,r623,r624,r625,r626,r627,r628,r629,r630,r631,r632,r633,r634,r635,r636,r637,r638,r639,r640,r641,r642,r643,r644,r645,r646,r647,r648,r649,r650,r651,r652,r653,r654,r655,r656,r657,r658,r659,r660,r661,r662,r663,r664,r665,r666,r667,r668,r669,r670,r671,r672,r673,r674,r675,r676,r677,r678,r679,r680,r681,r682,r683,r684,r685,r686,r687,r688,r689,r690,r691,r692,r693,r694,r695,r696,r697,r698,r699,r700,r701,r702,r703,r704,r705,r706,r707,r708,r709,r710,r711,r712,r713,r714,r715,r716,r717,r718,r719,r720,r721,r722,r723,r724,r725,r726,r727,r728,r729,r730,r731,r732,r733,r734,r735,r736,r737,r738,r739,r740,r741,r742,r743,r744,r745,r746,r747,r748,r749,r750,r751,r752,r753,r754,r755,r756,r757,r758,r759,r760,r761,r762,r763,r764,r765,r766,r767,r768,r769,r770,r771,r772,r773,r774,r775,r776,r777,r778,r779,r780,r781,r782,r783,r784,r785,r786,r787,r788,r789,r790,r791,r792,r793,r794,r795,r796,r797,r798,r799,r800,r801,r802,r803,r804,r805,r806,r807,r808,r809,r810,r811,r812,r813,r814,r815,r816,r817,r818,r819,r820,r821,r822,r823,r824,r825,r826,r827,r828,r829,r830,r831,r832,r833,r834,r835,r836,r837,r838,r839,r840,r841,r842,r843,r844,r845,r846,r847,r848,r849,r850,r851,r852,r853,r854,r855,r856,r857,r858,r859,r860,r861,r862,r863,r864,r865,r866,r867,r868,r869,r870,r871,r872,r873,r874,r875,r876,r877,r878,r879,r880,r881,r882,r883,r884,r885,r886,r887,r888,r889,r890,r891,r892,r893,r894,r895,r896,r897,r898,r899,r900,r901,r902,r903,r904,r905,r906,r907,r908,r909,r910,r911,r912,r913,r914,r915,r916,r917,r918,r919,r920,r921,r922,r923,r924,r925,r926,r927,r928,r929,r930,r931,r932,r933,r934,r935,r936,r937,r938,r939,r940,r941,r942,r943,r944,r945,r946,r947,r948,r949,r950,r951,r952,r953,r954,r955,r956,r957,r958,r959,r960,r961,r962,r963,r964,r965,r966,r967,r968,r969,r970,r971,r972,r973,r974,r975,r976,r977,r978,r979,r980,r981,r982,r983,r984,r985,r986,r987,r988,r989,r990,r991,r992,r993,r994,r995,r996,r997,r998,r999,r1000,r1001,r1002,r1003,r1004,r1005,r1006,r1007,r1008,r1009,r1010,r1011,r1012,r1013,r1014,r1015,r1016,r1017,r1018,r1019,r1020,r1021,r1022,r1023])

    


    # define o simulador do covid
    chanceEstarContaminado_simul = ctrl.ControlSystemSimulation(chanceEstarContaminado_ctrl)
    chanceEstarContaminado_simul.input['tosse'] = in_tosse
    chanceEstarContaminado_simul.input['febre'] = in_febre
    chanceEstarContaminado_simul.input['coriza'] = in_coriza
    chanceEstarContaminado_simul.input['dorGarganta'] = in_dorGarganta
    chanceEstarContaminado_simul.input['dificuldadeRespirar'] = in_dificuldadeRespirar
    chanceEstarContaminado_simul.input['anosmia'] = in_anosmia
    chanceEstarContaminado_simul.input['disturbiosGastrintestinais'] = in_disturbiosGastrintestinais
    chanceEstarContaminado_simul.input['astenia'] = in_astenia
    chanceEstarContaminado_simul.input['hiporexia'] = in_hiporexia
    chanceEstarContaminado_simul.input['dispneia'] = in_dispneia

    chanceEstarContaminado_simul.compute()

    if (in_print_state):
        if (sys.version_info[0] == 2):
            chanceEstarContaminado_simul.print_state()
        else:
            print('Versão do Python não compatível para impressão de sumário.')

    print(chanceEstarContaminado_simul.output['chanceEstarContaminado'])
    chanceEstarContaminado.view(sim=chanceEstarContaminado_simul)


# adicione à chamada da função as variáveis linguísticas dos antecedentes
# Os dados aqui estão sendo passados setados, será interessante, trocalos por uma interface onde pergunta os parametros
avaliar_covid('centroid', 5, 5, 4, 6, 7, 8, 9, 4, 7, 8)
