from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.direction = {'e', 'w', 's', 'n'}
rigid.location = {'l_5_1_0', 'l_5_5_3', 'l_5_2_2', 'l_1_5_4', 'l_5_1_1', 'l_6_1_4', 'l_5_4_4', 'l_6_3_5', 'l_0_4_2', 'l_3_4_0', 'l_0_3_5', 'l_4_2_2', 'l_6_5_0', 'l_0_2_5', 'l_6_5_5', 'l_0_3_4', 'l_5_1_5', 'l_0_4_1', 'l_6_4_1', 'l_1_0_1', 'l_2_0_4', 'l_3_4_1', 'l_2_4_0', 'l_3_5_4', 'l_0_5_1', 'l_1_4_2', 'l_0_2_4', 'l_3_3_0', 'l_5_5_2', 'l_6_2_4', 'l_4_4_4', 'l_0_3_2', 'l_0_0_5', 'l_0_0_1', 'l_6_3_1', 'l_2_3_5', 'l_3_0_1', 'l_0_1_2', 'l_4_3_5', 'l_5_3_1', 'l_6_2_3', 'l_0_5_3', 'l_0_4_5', 'l_1_1_3', 'l_1_3_2', 'l_4_2_3', 'l_2_1_0', 'l_0_3_3', 'l_3_2_5', 'l_5_3_4', 'l_1_0_5', 'l_1_1_2', 'l_4_4_3', 'l_4_5_5', 'l_5_5_0', 'l_0_5_4', 'l_6_2_5', 'l_0_1_4', 'l_6_0_4', 'l_5_4_3', 'l_2_5_5', 'l_1_4_5', 'l_4_0_5', 'l_3_3_4', 'l_1_4_0', 'l_0_1_0', 'l_6_3_3', 'l_6_2_1', 'l_6_5_2', 'l_4_2_5', 'l_2_2_3', 'l_2_3_3', 'l_3_0_2', 'l_2_2_2', 'l_3_1_4', 'l_6_0_3', 'l_2_2_5', 'l_4_1_4', 'l_5_1_2', 'l_6_4_2', 'l_2_3_1', 'l_0_0_4', 'l_4_0_2', 'l_5_4_5', 'l_0_2_1', 'l_5_0_2', 'l_3_4_5', 'l_0_5_0', 'l_0_5_2', 'l_2_2_1', 'l_2_5_2', 'l_3_5_1', 'l_2_4_4', 'l_5_3_2', 'l_6_2_0', 'l_3_5_2', 'l_4_2_1', 'l_5_5_4', 'l_0_0_2', 'l_0_4_3', 'l_2_5_1', 'l_1_2_5', 'l_3_2_2', 'l_6_0_5', 'l_0_4_0', 'l_1_3_1', 'l_5_2_5', 'l_1_2_4', 'l_5_1_3', 'l_5_4_2', 'l_2_5_0', 'l_6_5_3', 'l_2_1_1', 'l_6_1_2', 'l_5_0_5', 'l_6_5_4', 'l_3_1_0', 'l_3_2_0', 'l_2_2_4', 'l_0_3_0', 'l_4_1_2', 'l_4_0_1', 'l_5_2_1', 'l_1_5_5', 'l_1_0_4', 'l_1_3_0', 'l_1_3_3', 'l_6_0_2', 'l_6_3_0', 'l_5_1_4', 'l_4_3_4', 'l_6_0_0', 'l_1_0_2', 'l_5_0_3', 'l_3_1_1', 'l_2_4_2', 'l_4_1_1', 'l_6_0_1', 'l_6_1_3', 'l_3_0_0', 'l_2_1_5', 'l_5_3_3', 'l_1_4_3', 'l_3_0_5', 'l_4_2_4', 'l_5_5_5', 'l_0_0_3', 'l_4_0_4', 'l_6_1_5', 'l_6_4_3', 'l_1_1_1', 'l_3_3_5', 'l_6_1_0', 'l_0_2_2', 'l_1_5_2', 'l_4_1_0', 'l_2_3_4', 'l_2_0_5', 'l_0_5_5', 'l_2_2_0', 'l_2_5_3', 'l_0_0_0', 'l_3_2_1', 'l_4_1_3', 'l_3_0_4', 'l_2_0_0', 'l_6_4_5', 'l_4_3_1', 'l_0_2_3', 'l_1_1_4', 'l_3_1_2', 'l_3_3_1', 'l_4_1_5', 'l_1_0_3', 'l_3_5_0', 'l_3_3_3', 'l_1_0_0', 'l_1_2_3', 'l_5_0_4', 'l_6_3_4', 'l_2_0_3', 'l_0_4_4', 'l_5_0_1', 'l_5_2_3', 'l_2_3_2', 'l_1_2_2', 'l_6_1_1', 'l_4_4_2', 'l_1_3_5', 'l_1_2_1', 'l_1_4_4', 'l_4_5_2', 'l_5_2_0', 'l_0_1_1', 'l_1_5_1', 'l_5_3_5', 'l_2_1_2', 'l_1_5_3', 'l_0_2_0', 'l_5_0_0', 'l_4_3_3', 'l_0_3_1', 'l_2_1_4', 'l_3_4_2', 'l_1_1_0', 'l_3_5_5', 'l_2_5_4', 'l_1_1_5', 'l_4_5_0', 'l_1_4_1', 'l_0_1_3', 'l_3_1_5', 'l_3_5_3', 'l_4_3_0', 'l_4_2_0', 'l_5_4_1', 'l_3_2_4', 'l_2_3_0', 'l_2_4_5', 'l_4_4_0', 'l_3_2_3', 'l_4_0_0', 'l_0_1_5', 'l_2_1_3', 'l_3_3_2', 'l_5_3_0', 'l_1_2_0', 'l_4_5_3', 'l_4_5_1', 'l_3_0_3', 'l_3_4_4', 'l_4_3_2', 'l_4_5_4', 'l_1_5_0', 'l_6_4_4', 'l_5_4_0', 'l_3_1_3', 'l_6_5_1', 'l_2_4_3', 'l_6_3_2', 'l_2_0_2', 'l_4_0_3', 'l_5_2_4', 'l_2_4_1', 'l_4_4_5', 'l_4_4_1', 'l_6_2_2', 'l_6_4_0', 'l_5_5_1', 'l_3_4_3', 'l_2_0_1', 'l_1_3_4'}
rigid.blocktype = {'earth', 'wood', 'stone'}
rigid.numbers = {'n1', 'n2', 'n3', 'n4', 'n5', 'n0'}
rigid.neighbour = { ('l_1_1_4', 'l_1_0_4', 's'), ('l_5_2_3', 'l_5_2_4', 'e'), ('l_5_4_0', 'l_5_4_1', 'e'), ('l_3_0_3', 'l_3_0_2', 'w'), ('l_3_1_4', 'l_3_0_4', 's'), ('l_0_3_0', 'l_0_2_0', 's'), ('l_4_3_4', 'l_4_4_4', 'n'), ('l_4_4_1', 'l_4_4_0', 'w'), ('l_6_0_3', 'l_6_0_2', 'w'), ('l_5_2_3', 'l_5_3_3', 'n'), ('l_1_0_1', 'l_1_0_2', 'e'), ('l_3_3_4', 'l_3_3_3', 'w'), ('l_3_4_3', 'l_3_3_3', 's'), ('l_5_3_2', 'l_5_3_3', 'e'), ('l_4_4_4', 'l_4_5_4', 'n'), ('l_4_3_3', 'l_4_3_2', 'w'), ('l_3_1_3', 'l_3_1_4', 'e'), ('l_2_0_0', 'l_2_1_0', 'n'), ('l_5_3_3', 'l_5_2_3', 's'), ('l_2_2_2', 'l_2_3_2', 'n'), ('l_0_0_2', 'l_0_1_2', 'n'), ('l_3_1_4', 'l_3_1_3', 'w'), ('l_2_1_0', 'l_2_2_0', 'n'), ('l_0_4_1', 'l_0_5_1', 'n'), ('l_4_4_3', 'l_4_4_2', 'w'), ('l_4_5_4', 'l_4_5_3', 'w'), ('l_5_4_3', 'l_5_3_3', 's'), ('l_5_3_1', 'l_5_3_2', 'e'), ('l_2_0_1', 'l_2_0_0', 'w'), ('l_1_1_3', 'l_1_2_3', 'n'), ('l_6_1_0', 'l_6_2_0', 'n'), ('l_1_4_5', 'l_1_4_4', 'w'), ('l_2_3_1', 'l_2_3_0', 'w'), ('l_6_1_2', 'l_6_1_1', 'w'), ('l_4_3_3', 'l_4_2_3', 's'), ('l_5_5_1', 'l_5_5_0', 'w'), ('l_2_4_1', 'l_2_5_1', 'n'), ('l_4_1_5', 'l_4_1_4', 'w'), ('l_6_2_1', 'l_6_2_2', 'e'), ('l_4_2_1', 'l_4_3_1', 'n'), ('l_0_1_4', 'l_0_0_4', 's'), ('l_4_1_2', 'l_4_1_1', 'w'), ('l_1_2_3', 'l_1_2_4', 'e'), ('l_3_1_1', 'l_3_1_0', 'w'), ('l_6_1_1', 'l_6_1_0', 'w'), ('l_2_2_2', 'l_2_2_1', 'w'), ('l_2_4_3', 'l_2_5_3', 'n'), ('l_5_2_2', 'l_5_3_2', 'n'), ('l_2_0_4', 'l_2_0_3', 'w'), ('l_4_5_4', 'l_4_4_4', 's'), ('l_4_3_2', 'l_4_4_2', 'n'), ('l_0_4_0', 'l_0_4_1', 'e'), ('l_5_3_0', 'l_5_3_1', 'e'), ('l_1_1_0', 'l_1_0_0', 's'), ('l_3_2_4', 'l_3_2_5', 'e'), ('l_0_3_1', 'l_0_2_1', 's'), ('l_0_4_4', 'l_0_5_4', 'n'), ('l_6_5_4', 'l_6_4_4', 's'), ('l_2_2_1', 'l_2_2_2', 'e'), ('l_3_1_0', 'l_3_0_0', 's'), ('l_3_1_3', 'l_3_1_2', 'w'), ('l_0_3_3', 'l_0_4_3', 'n'), ('l_5_0_4', 'l_5_1_4', 'n'), ('l_3_2_2', 'l_3_2_3', 'e'), ('l_3_5_3', 'l_3_5_4', 'e'), ('l_2_4_5', 'l_2_3_5', 's'), ('l_6_0_5', 'l_6_1_5', 'n'), ('l_6_3_3', 'l_6_2_3', 's'), ('l_5_4_1', 'l_5_4_2', 'e'), ('l_5_1_4', 'l_5_2_4', 'n'), ('l_2_3_1', 'l_2_3_2', 'e'), ('l_4_3_0', 'l_4_2_0', 's'), ('l_3_1_2', 'l_3_2_2', 'n'), ('l_0_5_1', 'l_0_4_1', 's'), ('l_1_5_4', 'l_1_5_5', 'e'), ('l_3_3_5', 'l_3_3_4', 'w'), ('l_3_3_4', 'l_3_3_5', 'e'), ('l_6_4_4', 'l_6_5_4', 'n'), ('l_1_4_3', 'l_1_5_3', 'n'), ('l_5_1_5', 'l_5_1_4', 'w'), ('l_1_1_1', 'l_1_0_1', 's'), ('l_3_2_2', 'l_3_2_1', 'w'), ('l_2_4_1', 'l_2_4_0', 'w'), ('l_6_1_2', 'l_6_1_3', 'e'), ('l_1_4_0', 'l_1_4_1', 'e'), ('l_5_4_1', 'l_5_3_1', 's'), ('l_5_1_0', 'l_5_2_0', 'n'), ('l_1_5_4', 'l_1_4_4', 's'), ('l_5_3_4', 'l_5_2_4', 's'), ('l_2_1_5', 'l_2_2_5', 'n'), ('l_1_0_4', 'l_1_0_5', 'e'), ('l_4_2_4', 'l_4_1_4', 's'), ('l_3_2_4', 'l_3_1_4', 's'), ('l_3_0_3', 'l_3_1_3', 'n'), ('l_1_4_3', 'l_1_3_3', 's'), ('l_4_2_4', 'l_4_3_4', 'n'), ('l_4_5_0', 'l_4_4_0', 's'), ('l_2_3_1', 'l_2_2_1', 's'), ('l_6_1_4', 'l_6_1_5', 'e'), ('l_5_5_4', 'l_5_5_5', 'e'), ('l_2_2_0', 'l_2_1_0', 's'), ('l_2_2_3', 'l_2_2_2', 'w'), ('l_0_5_3', 'l_0_4_3', 's'), ('l_1_1_3', 'l_1_1_4', 'e'), ('l_4_1_0', 'l_4_2_0', 'n'), ('l_5_1_3', 'l_5_2_3', 'n'), ('l_4_0_1', 'l_4_0_2', 'e'), ('l_6_0_1', 'l_6_0_2', 'e'), ('l_4_0_4', 'l_4_1_4', 'n'), ('l_0_2_0', 'l_0_3_0', 'n'), ('l_3_4_5', 'l_3_5_5', 'n'), ('l_3_3_3', 'l_3_3_4', 'e'), ('l_0_3_5', 'l_0_3_4', 'w'), ('l_4_4_0', 'l_4_5_0', 'n'), ('l_3_4_0', 'l_3_3_0', 's'), ('l_3_4_2', 'l_3_3_2', 's'), ('l_0_3_4', 'l_0_3_5', 'e'), ('l_4_1_2', 'l_4_0_2', 's'), ('l_1_5_0', 'l_1_5_1', 'e'), ('l_6_2_4', 'l_6_1_4', 's'), ('l_3_1_3', 'l_3_2_3', 'n'), ('l_1_3_2', 'l_1_2_2', 's'), ('l_1_4_0', 'l_1_3_0', 's'), ('l_6_3_4', 'l_6_2_4', 's'), ('l_3_5_0', 'l_3_4_0', 's'), ('l_3_2_3', 'l_3_3_3', 'n'), ('l_6_1_4', 'l_6_0_4', 's'), ('l_0_0_2', 'l_0_0_3', 'e'), ('l_0_1_0', 'l_0_2_0', 'n'), ('l_0_0_1', 'l_0_1_1', 'n'), ('l_3_4_5', 'l_3_4_4', 'w'), ('l_3_4_2', 'l_3_4_3', 'e'), ('l_6_4_2', 'l_6_4_1', 'w'), ('l_5_0_1', 'l_5_0_0', 'w'), ('l_5_0_1', 'l_5_1_1', 'n'), ('l_5_2_1', 'l_5_2_2', 'e'), ('l_1_4_5', 'l_1_3_5', 's'), ('l_4_4_1', 'l_4_4_2', 'e'), ('l_2_3_4', 'l_2_4_4', 'n'), ('l_4_3_2', 'l_4_3_1', 'w'), ('l_3_5_5', 'l_3_5_4', 'w'), ('l_6_1_3', 'l_6_2_3', 'n'), ('l_0_1_1', 'l_0_0_1', 's'), ('l_0_4_4', 'l_0_4_3', 'w'), ('l_4_1_4', 'l_4_1_5', 'e'), ('l_3_0_5', 'l_3_0_4', 'w'), ('l_1_5_3', 'l_1_4_3', 's'), ('l_5_1_2', 'l_5_1_3', 'e'), ('l_5_5_4', 'l_5_4_4', 's'), ('l_1_1_4', 'l_1_2_4', 'n'), ('l_5_1_2', 'l_5_2_2', 'n'), ('l_3_3_3', 'l_3_2_3', 's'), ('l_2_1_4', 'l_2_1_3', 'w'), ('l_4_2_0', 'l_4_3_0', 'n'), ('l_6_3_4', 'l_6_4_4', 'n'), ('l_1_0_3', 'l_1_1_3', 'n'), ('l_2_4_3', 'l_2_3_3', 's'), ('l_2_1_0', 'l_2_0_0', 's'), ('l_0_0_1', 'l_0_0_0', 'w'), ('l_0_1_3', 'l_0_0_3', 's'), ('l_2_0_4', 'l_2_1_4', 'n'), ('l_2_4_4', 'l_2_5_4', 'n'), ('l_1_0_3', 'l_1_0_4', 'e'), ('l_2_3_4', 'l_2_2_4', 's'), ('l_5_3_5', 'l_5_3_4', 'w'), ('l_5_4_2', 'l_5_5_2', 'n'), ('l_2_0_0', 'l_2_0_1', 'e'), ('l_4_2_2', 'l_4_3_2', 'n'), ('l_6_3_5', 'l_6_3_4', 'w'), ('l_3_4_1', 'l_3_4_2', 'e'), ('l_5_4_3', 'l_5_4_4', 'e'), ('l_4_4_5', 'l_4_4_4', 'w'), ('l_2_1_4', 'l_2_1_5', 'e'), ('l_1_1_3', 'l_1_1_2', 'w'), ('l_6_2_1', 'l_6_3_1', 'n'), ('l_3_2_4', 'l_3_3_4', 'n'), ('l_4_3_0', 'l_4_4_0', 'n'), ('l_4_2_0', 'l_4_1_0', 's'), ('l_4_4_4', 'l_4_3_4', 's'), ('l_3_4_0', 'l_3_5_0', 'n'), ('l_5_5_1', 'l_5_4_1', 's'), ('l_2_0_4', 'l_2_0_5', 'e'), ('l_4_5_2', 'l_4_5_1', 'w'), ('l_5_0_2', 'l_5_0_1', 'w'), ('l_0_1_1', 'l_0_2_1', 'n'), ('l_6_5_5', 'l_6_5_4', 'w'), ('l_2_5_1', 'l_2_5_2', 'e'), ('l_6_3_3', 'l_6_4_3', 'n'), ('l_4_1_4', 'l_4_1_3', 'w'), ('l_2_2_4', 'l_2_1_4', 's'), ('l_4_1_1', 'l_4_0_1', 's'), ('l_1_2_1', 'l_1_3_1', 'n'), ('l_2_2_5', 'l_2_3_5', 'n'), ('l_4_0_5', 'l_4_0_4', 'w'), ('l_1_3_3', 'l_1_3_4', 'e'), ('l_0_2_5', 'l_0_3_5', 'n'), ('l_3_1_2', 'l_3_1_3', 'e'), ('l_0_4_3', 'l_0_3_3', 's'), ('l_3_2_2', 'l_3_3_2', 'n'), ('l_6_5_2', 'l_6_5_1', 'w'), ('l_0_3_5', 'l_0_4_5', 'n'), ('l_6_4_4', 'l_6_4_5', 'e'), ('l_6_4_5', 'l_6_3_5', 's'), ('l_1_3_0', 'l_1_3_1', 'e'), ('l_6_4_0', 'l_6_4_1', 'e'), ('l_1_5_5', 'l_1_5_4', 'w'), ('l_2_0_2', 'l_2_0_3', 'e'), ('l_2_1_3', 'l_2_0_3', 's'), ('l_6_5_3', 'l_6_5_2', 'w'), ('l_0_2_3', 'l_0_3_3', 'n'), ('l_5_4_5', 'l_5_4_4', 'w'), ('l_3_4_2', 'l_3_4_1', 'w'), ('l_2_0_3', 'l_2_1_3', 'n'), ('l_0_4_1', 'l_0_4_2', 'e'), ('l_2_5_0', 'l_2_5_1', 'e'), ('l_0_2_3', 'l_0_2_2', 'w'), ('l_5_2_1', 'l_5_1_1', 's'), ('l_2_3_0', 'l_2_4_0', 'n'), ('l_6_4_3', 'l_6_5_3', 'n'), ('l_3_3_4', 'l_3_2_4', 's'), ('l_6_3_2', 'l_6_3_3', 'e'), ('l_5_5_2', 'l_5_5_3', 'e'), ('l_2_2_1', 'l_2_2_0', 'w'), ('l_1_4_1', 'l_1_5_1', 'n'), ('l_6_5_4', 'l_6_5_3', 'w'), ('l_4_4_1', 'l_4_3_1', 's'), ('l_5_4_4', 'l_5_5_4', 'n'), ('l_1_4_4', 'l_1_4_3', 'w'), ('l_4_5_1', 'l_4_4_1', 's'), ('l_3_2_1', 'l_3_2_0', 'w'), ('l_5_4_1', 'l_5_5_1', 'n'), ('l_1_0_0', 'l_1_0_1', 'e'), ('l_3_5_1', 'l_3_4_1', 's'), ('l_5_4_5', 'l_5_3_5', 's'), ('l_6_0_3', 'l_6_0_4', 'e'), ('l_6_4_2', 'l_6_4_3', 'e'), ('l_1_1_5', 'l_1_1_4', 'w'), ('l_6_4_4', 'l_6_3_4', 's'), ('l_2_5_4', 'l_2_5_5', 'e'), ('l_5_5_1', 'l_5_5_2', 'e'), ('l_4_2_3', 'l_4_1_3', 's'), ('l_2_0_2', 'l_2_1_2', 'n'), ('l_6_1_3', 'l_6_1_4', 'e'), ('l_1_4_2', 'l_1_5_2', 'n'), ('l_0_3_1', 'l_0_4_1', 'n'), ('l_5_0_3', 'l_5_0_2', 'w'), ('l_0_3_2', 'l_0_3_3', 'e'), ('l_4_1_1', 'l_4_1_0', 'w'), ('l_4_4_2', 'l_4_5_2', 'n'), ('l_1_3_5', 'l_1_2_5', 's'), ('l_0_5_4', 'l_0_4_4', 's'), ('l_0_5_2', 'l_0_5_3', 'e'), ('l_2_2_0', 'l_2_3_0', 'n'), ('l_3_3_2', 'l_3_4_2', 'n'), ('l_6_4_3', 'l_6_4_4', 'e'), ('l_1_0_2', 'l_1_1_2', 'n'), ('l_0_2_4', 'l_0_3_4', 'n'), ('l_5_2_4', 'l_5_2_5', 'e'), ('l_6_2_3', 'l_6_3_3', 'n'), ('l_4_3_2', 'l_4_3_3', 'e'), ('l_6_2_3', 'l_6_2_4', 'e'), ('l_0_5_3', 'l_0_5_4', 'e'), ('l_1_4_4', 'l_1_4_5', 'e'), ('l_0_2_1', 'l_0_2_0', 'w'), ('l_2_4_2', 'l_2_3_2', 's'), ('l_3_1_5', 'l_3_2_5', 'n'), ('l_4_1_5', 'l_4_0_5', 's'), ('l_6_1_1', 'l_6_0_1', 's'), ('l_3_4_1', 'l_3_4_0', 'w'), ('l_0_1_1', 'l_0_1_2', 'e'), ('l_6_2_4', 'l_6_2_3', 'w'), ('l_1_0_2', 'l_1_0_1', 'w'), ('l_6_3_0', 'l_6_3_1', 'e'), ('l_0_4_2', 'l_0_4_1', 'w'), ('l_0_1_3', 'l_0_1_2', 'w'), ('l_3_1_4', 'l_3_1_5', 'e'), ('l_1_2_3', 'l_1_2_2', 'w'), ('l_4_3_4', 'l_4_3_3', 'w'), ('l_1_1_4', 'l_1_1_5', 'e'), ('l_2_1_4', 'l_2_0_4', 's'), ('l_3_0_3', 'l_3_0_4', 'e'), ('l_2_4_2', 'l_2_5_2', 'n'), ('l_0_2_1', 'l_0_2_2', 'e'), ('l_5_1_1', 'l_5_1_2', 'e'), ('l_2_4_1', 'l_2_4_2', 'e'), ('l_1_1_1', 'l_1_2_1', 'n'), ('l_2_0_3', 'l_2_0_4', 'e'), ('l_6_3_1', 'l_6_3_0', 'w'), ('l_1_4_1', 'l_1_3_1', 's'), ('l_4_1_4', 'l_4_0_4', 's'), ('l_0_3_2', 'l_0_2_2', 's'), ('l_6_0_5', 'l_6_0_4', 'w'), ('l_3_4_4', 'l_3_5_4', 'n'), ('l_0_0_5', 'l_0_0_4', 'w'), ('l_6_4_5', 'l_6_4_4', 'w'), ('l_1_0_1', 'l_1_0_0', 'w'), ('l_2_5_0', 'l_2_4_0', 's'), ('l_6_2_1', 'l_6_1_1', 's'), ('l_6_2_2', 'l_6_3_2', 'n'), ('l_6_4_3', 'l_6_3_3', 's'), ('l_2_0_1', 'l_2_1_1', 'n'), ('l_1_5_2', 'l_1_5_3', 'e'), ('l_1_1_1', 'l_1_1_2', 'e'), ('l_1_3_4', 'l_1_4_4', 'n'), ('l_3_0_1', 'l_3_1_1', 'n'), ('l_0_5_3', 'l_0_5_2', 'w'), ('l_3_3_1', 'l_3_2_1', 's'), ('l_6_3_2', 'l_6_4_2', 'n'), ('l_4_4_4', 'l_4_4_3', 'w'), ('l_0_4_2', 'l_0_4_3', 'e'), ('l_4_2_2', 'l_4_1_2', 's'), ('l_5_5_3', 'l_5_5_2', 'w'), ('l_1_4_3', 'l_1_4_2', 'w'), ('l_5_1_3', 'l_5_0_3', 's'), ('l_5_2_0', 'l_5_1_0', 's'), ('l_1_3_5', 'l_1_4_5', 'n'), ('l_0_5_0', 'l_0_4_0', 's'), ('l_2_4_0', 'l_2_5_0', 'n'), ('l_4_4_5', 'l_4_3_5', 's'), ('l_2_5_3', 'l_2_5_2', 'w'), ('l_2_4_4', 'l_2_4_5', 'e'), ('l_6_0_4', 'l_6_0_3', 'w'), ('l_2_4_5', 'l_2_5_5', 'n'), ('l_4_0_4', 'l_4_0_3', 'w'), ('l_1_1_2', 'l_1_1_3', 'e'), ('l_3_3_2', 'l_3_2_2', 's'), ('l_3_5_3', 'l_3_4_3', 's'), ('l_3_0_2', 'l_3_0_3', 'e'), ('l_3_4_2', 'l_3_5_2', 'n'), ('l_4_0_3', 'l_4_1_3', 'n'), ('l_5_4_4', 'l_5_4_5', 'e'), ('l_5_1_1', 'l_5_0_1', 's'), ('l_2_1_3', 'l_2_1_4', 'e'), ('l_4_5_0', 'l_4_5_1', 'e'), ('l_5_3_0', 'l_5_2_0', 's'), ('l_6_2_0', 'l_6_1_0', 's'), ('l_6_0_1', 'l_6_0_0', 'w'), ('l_0_4_4', 'l_0_3_4', 's'), ('l_6_2_2', 'l_6_1_2', 's'), ('l_0_1_5', 'l_0_0_5', 's'), ('l_1_2_0', 'l_1_3_0', 'n'), ('l_3_5_4', 'l_3_5_3', 'w'), ('l_5_5_2', 'l_5_5_1', 'w'), ('l_1_1_5', 'l_1_2_5', 'n'), ('l_5_3_4', 'l_5_3_3', 'w'), ('l_1_5_0', 'l_1_4_0', 's'), ('l_4_3_2', 'l_4_2_2', 's'), ('l_2_5_2', 'l_2_5_1', 'w'), ('l_5_2_2', 'l_5_2_3', 'e'), ('l_1_3_1', 'l_1_4_1', 'n'), ('l_1_2_4', 'l_1_1_4', 's'), ('l_2_3_3', 'l_2_3_4', 'e'), ('l_3_4_3', 'l_3_4_2', 'w'), ('l_2_2_3', 'l_2_2_4', 'e'), ('l_3_1_3', 'l_3_0_3', 's'), ('l_4_5_1', 'l_4_5_0', 'w'), ('l_2_2_0', 'l_2_2_1', 'e'), ('l_2_4_2', 'l_2_4_3', 'e'), ('l_0_3_3', 'l_0_3_4', 'e'), ('l_1_4_1', 'l_1_4_2', 'e'), ('l_6_1_1', 'l_6_1_2', 'e'), ('l_6_3_1', 'l_6_2_1', 's'), ('l_2_0_3', 'l_2_0_2', 'w'), ('l_0_2_2', 'l_0_2_3', 'e'), ('l_4_0_2', 'l_4_1_2', 'n'), ('l_5_0_3', 'l_5_1_3', 'n'), ('l_1_3_4', 'l_1_3_5', 'e'), ('l_0_4_2', 'l_0_3_2', 's'), ('l_1_0_2', 'l_1_0_3', 'e'), ('l_5_3_1', 'l_5_2_1', 's'), ('l_4_2_5', 'l_4_3_5', 'n'), ('l_2_5_2', 'l_2_5_3', 'e'), ('l_2_4_4', 'l_2_3_4', 's'), ('l_1_2_3', 'l_1_3_3', 'n'), ('l_2_5_3', 'l_2_5_4', 'e'), ('l_2_0_5', 'l_2_0_4', 'w'), ('l_5_4_2', 'l_5_4_1', 'w'), ('l_6_3_4', 'l_6_3_3', 'w'), ('l_4_4_2', 'l_4_4_3', 'e'), ('l_1_4_4', 'l_1_5_4', 'n'), ('l_4_1_4', 'l_4_2_4', 'n'), ('l_6_1_2', 'l_6_0_2', 's'), ('l_2_4_3', 'l_2_4_2', 'w'), ('l_5_2_1', 'l_5_2_0', 'w'), ('l_3_4_4', 'l_3_4_5', 'e'), ('l_4_1_1', 'l_4_2_1', 'n'), ('l_5_2_4', 'l_5_3_4', 'n'), ('l_1_5_1', 'l_1_5_0', 'w'), ('l_0_3_4', 'l_0_2_4', 's'), ('l_4_2_2', 'l_4_2_3', 'e'), ('l_3_5_2', 'l_3_5_1', 'w'), ('l_6_4_0', 'l_6_3_0', 's'), ('l_1_3_1', 'l_1_3_2', 'e'), ('l_1_3_0', 'l_1_4_0', 'n'), ('l_4_5_5', 'l_4_5_4', 'w'), ('l_5_3_2', 'l_5_2_2', 's'), ('l_2_2_2', 'l_2_1_2', 's'), ('l_0_2_2', 'l_0_1_2', 's'), ('l_0_4_1', 'l_0_3_1', 's'), ('l_5_0_1', 'l_5_0_2', 'e'), ('l_6_2_2', 'l_6_2_1', 'w'), ('l_4_3_0', 'l_4_3_1', 'e'), ('l_6_1_4', 'l_6_1_3', 'w'), ('l_5_4_0', 'l_5_5_0', 'n'), ('l_6_4_3', 'l_6_4_2', 'w'), ('l_1_5_2', 'l_1_4_2', 's'), ('l_2_4_1', 'l_2_3_1', 's'), ('l_2_3_4', 'l_2_3_5', 'e'), ('l_4_1_0', 'l_4_0_0', 's'), ('l_4_3_1', 'l_4_3_0', 'w'), ('l_1_4_4', 'l_1_3_4', 's'), ('l_3_1_2', 'l_3_1_1', 'w'), ('l_0_1_2', 'l_0_0_2', 's'), ('l_2_3_3', 'l_2_2_3', 's'), ('l_4_3_4', 'l_4_2_4', 's'), ('l_3_4_1', 'l_3_5_1', 'n'), ('l_0_2_4', 'l_0_1_4', 's'), ('l_5_3_4', 'l_5_3_5', 'e'), ('l_2_0_1', 'l_2_0_2', 'e'), ('l_6_4_1', 'l_6_3_1', 's'), ('l_5_0_5', 'l_5_1_5', 'n'), ('l_0_2_1', 'l_0_1_1', 's'), ('l_4_4_0', 'l_4_3_0', 's'), ('l_6_3_2', 'l_6_2_2', 's'), ('l_2_5_1', 'l_2_5_0', 'w'), ('l_0_3_3', 'l_0_3_2', 'w'), ('l_3_0_4', 'l_3_0_5', 'e'), ('l_2_4_0', 'l_2_4_1', 'e'), ('l_6_2_0', 'l_6_3_0', 'n'), ('l_5_2_4', 'l_5_1_4', 's'), ('l_0_0_0', 'l_0_1_0', 'n'), ('l_4_2_2', 'l_4_2_1', 'w'), ('l_0_1_5', 'l_0_2_5', 'n'), ('l_6_2_4', 'l_6_3_4', 'n'), ('l_5_2_2', 'l_5_2_1', 'w'), ('l_0_3_4', 'l_0_4_4', 'n'), ('l_5_5_3', 'l_5_5_4', 'e'), ('l_0_2_3', 'l_0_1_3', 's'), ('l_1_4_0', 'l_1_5_0', 'n'), ('l_4_0_3', 'l_4_0_4', 'e'), ('l_6_4_1', 'l_6_4_2', 'e'), ('l_1_2_5', 'l_1_2_4', 'w'), ('l_0_0_3', 'l_0_0_2', 'w'), ('l_0_4_5', 'l_0_4_4', 'w'), ('l_3_2_4', 'l_3_2_3', 'w'), ('l_5_3_2', 'l_5_4_2', 'n'), ('l_5_3_1', 'l_5_4_1', 'n'), ('l_3_3_1', 'l_3_3_0', 'w'), ('l_4_0_0', 'l_4_1_0', 'n'), ('l_6_2_5', 'l_6_3_5', 'n'), ('l_2_1_0', 'l_2_1_1', 'e'), ('l_1_3_1', 'l_1_3_0', 'w'), ('l_2_2_3', 'l_2_3_3', 'n'), ('l_1_2_4', 'l_1_2_5', 'e'), ('l_5_3_4', 'l_5_4_4', 'n'), ('l_4_1_2', 'l_4_2_2', 'n'), ('l_4_2_3', 'l_4_3_3', 'n'), ('l_2_0_2', 'l_2_0_1', 'w'), ('l_1_3_1', 'l_1_2_1', 's'), ('l_6_2_3', 'l_6_2_2', 'w'), ('l_5_3_2', 'l_5_3_1', 'w'), ('l_0_1_3', 'l_0_1_4', 'e'), ('l_1_2_1', 'l_1_1_1', 's'), ('l_5_1_3', 'l_5_1_2', 'w'), ('l_2_5_1', 'l_2_4_1', 's'), ('l_5_1_0', 'l_5_0_0', 's'), ('l_6_2_4', 'l_6_2_5', 'e'), ('l_6_1_1', 'l_6_2_1', 'n'), ('l_4_2_5', 'l_4_2_4', 'w'), ('l_0_0_2', 'l_0_0_1', 'w'), ('l_2_1_3', 'l_2_2_3', 'n'), ('l_6_4_5', 'l_6_5_5', 'n'), ('l_4_3_3', 'l_4_4_3', 'n'), ('l_6_3_0', 'l_6_4_0', 'n'), ('l_3_4_1', 'l_3_3_1', 's'), ('l_0_2_0', 'l_0_1_0', 's'), ('l_0_1_4', 'l_0_1_3', 'w'), ('l_6_3_3', 'l_6_3_4', 'e'), ('l_5_2_0', 'l_5_2_1', 'e'), ('l_5_4_4', 'l_5_3_4', 's'), ('l_0_1_4', 'l_0_1_5', 'e'), ('l_2_1_1', 'l_2_1_0', 'w'), ('l_2_2_1', 'l_2_3_1', 'n'), ('l_0_1_4', 'l_0_2_4', 'n'), ('l_2_3_2', 'l_2_3_3', 'e'), ('l_3_5_0', 'l_3_5_1', 'e'), ('l_1_5_2', 'l_1_5_1', 'w'), ('l_1_1_5', 'l_1_0_5', 's'), ('l_1_3_2', 'l_1_4_2', 'n'), ('l_3_3_0', 'l_3_3_1', 'e'), ('l_0_4_4', 'l_0_4_5', 'e'), ('l_5_1_3', 'l_5_1_4', 'e'), ('l_5_0_0', 'l_5_1_0', 'n'), ('l_3_4_5', 'l_3_3_5', 's'), ('l_5_0_5', 'l_5_0_4', 'w'), ('l_0_4_0', 'l_0_5_0', 'n'), ('l_2_1_2', 'l_2_1_3', 'e'), ('l_5_0_0', 'l_5_0_1', 'e'), ('l_1_1_2', 'l_1_1_1', 'w'), ('l_2_3_0', 'l_2_3_1', 'e'), ('l_4_4_3', 'l_4_5_3', 'n'), ('l_3_2_2', 'l_3_1_2', 's'), ('l_4_1_3', 'l_4_1_2', 'w'), ('l_5_1_1', 'l_5_2_1', 'n'), ('l_6_5_1', 'l_6_5_0', 'w'), ('l_0_1_2', 'l_0_2_2', 'n'), ('l_0_3_0', 'l_0_4_0', 'n'), ('l_5_4_2', 'l_5_3_2', 's'), ('l_3_2_5', 'l_3_3_5', 'n'), ('l_3_5_1', 'l_3_5_0', 'w'), ('l_3_2_1', 'l_3_2_2', 'e'), ('l_0_3_0', 'l_0_3_1', 'e'), ('l_0_4_3', 'l_0_4_2', 'w'), ('l_1_2_2', 'l_1_1_2', 's'), ('l_6_1_0', 'l_6_0_0', 's'), ('l_1_3_2', 'l_1_3_3', 'e'), ('l_0_5_1', 'l_0_5_0', 'w'), ('l_6_3_2', 'l_6_3_1', 'w'), ('l_4_2_1', 'l_4_2_0', 'w'), ('l_6_0_3', 'l_6_1_3', 'n'), ('l_2_5_4', 'l_2_4_4', 's'), ('l_3_3_4', 'l_3_4_4', 'n'), ('l_2_2_4', 'l_2_3_4', 'n'), ('l_6_0_1', 'l_6_1_1', 'n'), ('l_4_3_1', 'l_4_4_1', 'n'), ('l_2_1_1', 'l_2_1_2', 'e'), ('l_1_2_0', 'l_1_1_0', 's'), ('l_2_5_5', 'l_2_4_5', 's'), ('l_4_0_3', 'l_4_0_2', 'w'), ('l_4_3_5', 'l_4_3_4', 'w'), ('l_3_0_1', 'l_3_0_0', 'w'), ('l_4_1_1', 'l_4_1_2', 'e'), ('l_5_3_5', 'l_5_2_5', 's'), ('l_0_3_1', 'l_0_3_2', 'e'), ('l_0_0_4', 'l_0_0_3', 'w'), ('l_4_0_2', 'l_4_0_1', 'w'), ('l_3_5_3', 'l_3_5_2', 'w'), ('l_6_5_2', 'l_6_4_2', 's'), ('l_6_3_1', 'l_6_3_2', 'e'), ('l_1_2_4', 'l_1_2_3', 'w'), ('l_6_2_5', 'l_6_2_4', 'w'), ('l_3_4_4', 'l_3_3_4', 's'), ('l_1_4_2', 'l_1_4_3', 'e'), ('l_4_1_0', 'l_4_1_1', 'e'), ('l_0_5_5', 'l_0_5_4', 'w'), ('l_5_1_2', 'l_5_1_1', 'w'), ('l_1_5_1', 'l_1_5_2', 'e'), ('l_1_3_0', 'l_1_2_0', 's'), ('l_6_3_4', 'l_6_3_5', 'e'), ('l_1_4_2', 'l_1_4_1', 'w'), ('l_2_2_4', 'l_2_2_3', 'w'), ('l_0_1_0', 'l_0_1_1', 'e'), ('l_4_5_2', 'l_4_5_3', 'e'), ('l_6_1_5', 'l_6_1_4', 'w'), ('l_2_3_5', 'l_2_2_5', 's'), ('l_4_2_4', 'l_4_2_3', 'w'), ('l_5_2_3', 'l_5_1_3', 's'), ('l_3_2_3', 'l_3_2_4', 'e'), ('l_6_5_4', 'l_6_5_5', 'e'), ('l_6_0_4', 'l_6_1_4', 'n'), ('l_1_5_5', 'l_1_4_5', 's'), ('l_5_1_4', 'l_5_1_3', 'w'), ('l_1_3_4', 'l_1_3_3', 'w'), ('l_0_1_5', 'l_0_1_4', 'w'), ('l_3_1_5', 'l_3_1_4', 'w'), ('l_5_2_5', 'l_5_2_4', 'w'), ('l_6_1_5', 'l_6_0_5', 's'), ('l_6_0_2', 'l_6_0_3', 'e'), ('l_3_3_2', 'l_3_3_1', 'w'), ('l_2_4_2', 'l_2_4_1', 'w'), ('l_4_2_1', 'l_4_2_2', 'e'), ('l_6_4_0', 'l_6_5_0', 'n'), ('l_1_5_4', 'l_1_5_3', 'w'), ('l_1_2_5', 'l_1_1_5', 's'), ('l_2_1_3', 'l_2_1_2', 'w'), ('l_2_2_2', 'l_2_2_3', 'e'), ('l_5_0_3', 'l_5_0_4', 'e'), ('l_6_0_4', 'l_6_0_5', 'e'), ('l_0_3_1', 'l_0_3_0', 'w'), ('l_6_3_1', 'l_6_4_1', 'n'), ('l_4_5_1', 'l_4_5_2', 'e'), ('l_0_5_1', 'l_0_5_2', 'e'), ('l_2_0_5', 'l_2_1_5', 'n'), ('l_6_2_5', 'l_6_1_5', 's'), ('l_1_2_2', 'l_1_2_3', 'e'), ('l_0_0_3', 'l_0_0_4', 'e'), ('l_3_4_4', 'l_3_4_3', 'w'), ('l_5_3_3', 'l_5_3_2', 'w'), ('l_2_2_4', 'l_2_2_5', 'e'), ('l_0_5_4', 'l_0_5_3', 'w'), ('l_5_2_5', 'l_5_3_5', 'n'), ('l_6_4_1', 'l_6_4_0', 'w'), ('l_0_2_2', 'l_0_2_1', 'w'), ('l_1_0_0', 'l_1_1_0', 'n'), ('l_3_1_1', 'l_3_1_2', 'e'), ('l_3_4_3', 'l_3_4_4', 'e'), ('l_6_2_2', 'l_6_2_3', 'e'), ('l_4_3_1', 'l_4_2_1', 's'), ('l_4_3_1', 'l_4_3_2', 'e'), ('l_1_5_1', 'l_1_4_1', 's'), ('l_4_2_5', 'l_4_1_5', 's'), ('l_6_1_3', 'l_6_0_3', 's'), ('l_2_5_5', 'l_2_5_4', 'w'), ('l_2_1_2', 'l_2_2_2', 'n'), ('l_3_1_0', 'l_3_2_0', 'n'), ('l_2_3_4', 'l_2_3_3', 'w'), ('l_4_5_3', 'l_4_5_2', 'w'), ('l_1_0_1', 'l_1_1_1', 'n'), ('l_1_4_2', 'l_1_3_2', 's'), ('l_5_4_0', 'l_5_3_0', 's'), ('l_4_1_5', 'l_4_2_5', 'n'), ('l_6_1_2', 'l_6_2_2', 'n'), ('l_1_1_3', 'l_1_0_3', 's'), ('l_3_2_0', 'l_3_2_1', 'e'), ('l_1_0_4', 'l_1_0_3', 'w'), ('l_4_0_4', 'l_4_0_5', 'e'), ('l_5_1_2', 'l_5_0_2', 's'), ('l_3_0_2', 'l_3_1_2', 'n'), ('l_4_0_5', 'l_4_1_5', 'n'), ('l_1_1_0', 'l_1_1_1', 'e'), ('l_5_0_4', 'l_5_0_5', 'e'), ('l_1_3_3', 'l_1_2_3', 's'), ('l_0_2_4', 'l_0_2_5', 'e'), ('l_4_3_3', 'l_4_3_4', 'e'), ('l_1_1_0', 'l_1_2_0', 'n'), ('l_1_5_3', 'l_1_5_4', 'e'), ('l_3_0_0', 'l_3_0_1', 'e'), ('l_4_0_1', 'l_4_1_1', 'n'), ('l_2_5_2', 'l_2_4_2', 's'), ('l_3_2_5', 'l_3_2_4', 'w'), ('l_6_4_1', 'l_6_5_1', 'n'), ('l_5_1_1', 'l_5_1_0', 'w'), ('l_3_3_0', 'l_3_2_0', 's'), ('l_1_0_5', 'l_1_0_4', 'w'), ('l_6_0_2', 'l_6_0_1', 'w'), ('l_6_4_2', 'l_6_3_2', 's'), ('l_5_2_0', 'l_5_3_0', 'n'), ('l_5_1_5', 'l_5_0_5', 's'), ('l_2_4_5', 'l_2_4_4', 'w'), ('l_0_3_2', 'l_0_4_2', 'n'), ('l_3_3_1', 'l_3_4_1', 'n'), ('l_4_5_4', 'l_4_5_5', 'e'), ('l_1_0_3', 'l_1_0_2', 'w'), ('l_5_4_1', 'l_5_4_0', 'w'), ('l_6_2_1', 'l_6_2_0', 'w'), ('l_0_0_1', 'l_0_0_2', 'e'), ('l_1_3_3', 'l_1_4_3', 'n'), ('l_1_3_3', 'l_1_3_2', 'w'), ('l_6_5_2', 'l_6_5_3', 'e'), ('l_3_3_3', 'l_3_3_2', 'w'), ('l_3_3_0', 'l_3_4_0', 'n'), ('l_6_5_3', 'l_6_4_3', 's'), ('l_6_1_3', 'l_6_1_2', 'w'), ('l_1_0_5', 'l_1_1_5', 'n'), ('l_4_5_2', 'l_4_4_2', 's'), ('l_2_1_2', 'l_2_1_1', 'w'), ('l_4_1_3', 'l_4_2_3', 'n'), ('l_4_4_2', 'l_4_4_1', 'w'), ('l_2_3_3', 'l_2_3_2', 'w'), ('l_0_0_0', 'l_0_0_1', 'e'), ('l_4_3_4', 'l_4_3_5', 'e'), ('l_1_4_5', 'l_1_5_5', 'n'), ('l_6_0_0', 'l_6_0_1', 'e'), ('l_1_2_5', 'l_1_3_5', 'n'), ('l_2_1_2', 'l_2_0_2', 's'), ('l_4_2_0', 'l_4_2_1', 'e'), ('l_1_3_2', 'l_1_3_1', 'w'), ('l_6_3_5', 'l_6_4_5', 'n'), ('l_5_5_0', 'l_5_5_1', 'e'), ('l_3_3_3', 'l_3_4_3', 'n'), ('l_4_2_4', 'l_4_2_5', 'e'), ('l_0_1_0', 'l_0_0_0', 's'), ('l_1_2_3', 'l_1_1_3', 's'), ('l_0_1_2', 'l_0_1_1', 'w'), ('l_4_2_3', 'l_4_2_4', 'e'), ('l_4_4_4', 'l_4_4_5', 'e'), ('l_6_4_2', 'l_6_5_2', 'n'), ('l_1_0_4', 'l_1_1_4', 'n'), ('l_3_1_0', 'l_3_1_1', 'e'), ('l_0_4_1', 'l_0_4_0', 'w'), ('l_0_2_3', 'l_0_2_4', 'e'), ('l_4_0_0', 'l_4_0_1', 'e'), ('l_5_1_5', 'l_5_2_5', 'n'), ('l_6_0_2', 'l_6_1_2', 'n'), ('l_2_4_0', 'l_2_3_0', 's'), ('l_2_2_1', 'l_2_1_1', 's'), ('l_2_2_3', 'l_2_1_3', 's'), ('l_5_2_5', 'l_5_1_5', 's'), ('l_1_4_3', 'l_1_4_4', 'e'), ('l_0_5_2', 'l_0_4_2', 's'), ('l_5_0_4', 'l_5_0_3', 'w'), ('l_5_3_3', 'l_5_4_3', 'n'), ('l_4_1_3', 'l_4_1_4', 'e'), ('l_0_5_2', 'l_0_5_1', 'w'), ('l_0_2_0', 'l_0_2_1', 'e'), ('l_6_0_0', 'l_6_1_0', 'n'), ('l_3_5_1', 'l_3_5_2', 'e'), ('l_5_4_3', 'l_5_4_2', 'w'), ('l_1_2_0', 'l_1_2_1', 'e'), ('l_6_5_1', 'l_6_5_2', 'e'), ('l_1_5_3', 'l_1_5_2', 'w'), ('l_2_1_5', 'l_2_1_4', 'w'), ('l_6_1_4', 'l_6_2_4', 'n'), ('l_2_3_1', 'l_2_4_1', 'n'), ('l_0_0_4', 'l_0_1_4', 'n'), ('l_3_1_2', 'l_3_0_2', 's'), ('l_1_1_1', 'l_1_1_0', 'w'), ('l_3_4_3', 'l_3_5_3', 'n'), ('l_2_3_2', 'l_2_2_2', 's'), ('l_3_0_1', 'l_3_0_2', 'e'), ('l_3_2_3', 'l_3_1_3', 's'), ('l_1_2_4', 'l_1_3_4', 'n'), ('l_5_1_4', 'l_5_1_5', 'e'), ('l_3_3_5', 'l_3_4_5', 'n'), ('l_5_4_4', 'l_5_4_3', 'w'), ('l_3_1_4', 'l_3_2_4', 'n'), ('l_0_4_3', 'l_0_4_4', 'e'), ('l_5_3_0', 'l_5_4_0', 'n'), ('l_6_1_5', 'l_6_2_5', 'n'), ('l_1_2_2', 'l_1_3_2', 'n'), ('l_5_5_3', 'l_5_4_3', 's'), ('l_5_5_5', 'l_5_5_4', 'w'), ('l_4_1_3', 'l_4_0_3', 's'), ('l_0_2_4', 'l_0_2_3', 'w'), ('l_2_5_4', 'l_2_5_3', 'w'), ('l_3_0_0', 'l_3_1_0', 'n'), ('l_4_2_1', 'l_4_1_1', 's'), ('l_2_3_2', 'l_2_4_2', 'n'), ('l_3_3_1', 'l_3_3_2', 'e'), ('l_5_1_4', 'l_5_0_4', 's'), ('l_3_1_1', 'l_3_2_1', 'n'), ('l_0_4_0', 'l_0_3_0', 's'), ('l_4_5_3', 'l_4_4_3', 's'), ('l_0_5_0', 'l_0_5_1', 'e'), ('l_4_0_1', 'l_4_0_0', 'w'), ('l_2_3_5', 'l_2_4_5', 'n'), ('l_4_5_5', 'l_4_4_5', 's'), ('l_3_0_2', 'l_3_0_1', 'w'), ('l_0_4_5', 'l_0_5_5', 'n'), ('l_6_5_1', 'l_6_4_1', 's'), ('l_5_2_2', 'l_5_1_2', 's'), ('l_3_5_2', 'l_3_4_2', 's'), ('l_0_4_5', 'l_0_3_5', 's'), ('l_4_1_2', 'l_4_1_3', 'e'), ('l_0_5_5', 'l_0_4_5', 's'), ('l_2_1_4', 'l_2_2_4', 'n'), ('l_5_3_3', 'l_5_3_4', 'e'), ('l_3_0_5', 'l_3_1_5', 'n'), ('l_4_3_5', 'l_4_2_5', 's'), ('l_3_5_4', 'l_3_5_5', 'e'), ('l_0_0_4', 'l_0_0_5', 'e'), ('l_3_3_2', 'l_3_3_3', 'e'), ('l_5_5_2', 'l_5_4_2', 's'), ('l_5_1_0', 'l_5_1_1', 'e'), ('l_3_2_1', 'l_3_3_1', 'n'), ('l_1_1_2', 'l_1_0_2', 's'), ('l_3_4_0', 'l_3_4_1', 'e'), ('l_0_1_2', 'l_0_1_3', 'e'), ('l_5_3_5', 'l_5_4_5', 'n'), ('l_3_2_0', 'l_3_1_0', 's'), ('l_3_1_5', 'l_3_0_5', 's'), ('l_3_2_0', 'l_3_3_0', 'n'), ('l_1_3_5', 'l_1_3_4', 'w'), ('l_4_4_3', 'l_4_4_4', 'e'), ('l_0_2_5', 'l_0_2_4', 'w'), ('l_4_3_5', 'l_4_4_5', 'n'), ('l_4_4_5', 'l_4_5_5', 'n'), ('l_2_1_1', 'l_2_0_1', 's'), ('l_4_4_2', 'l_4_3_2', 's'), ('l_5_0_2', 'l_5_1_2', 'n'), ('l_1_2_2', 'l_1_2_1', 'w'), ('l_5_5_4', 'l_5_5_3', 'w'), ('l_3_5_2', 'l_3_5_3', 'e'), ('l_0_0_5', 'l_0_1_5', 'n'), ('l_3_0_4', 'l_3_1_4', 'n'), ('l_2_5_3', 'l_2_4_3', 's'), ('l_2_1_1', 'l_2_2_1', 'n'), ('l_1_2_1', 'l_1_2_2', 'e'), ('l_5_3_1', 'l_5_3_0', 'w'), ('l_6_5_0', 'l_6_4_0', 's'), ('l_2_1_5', 'l_2_0_5', 's'), ('l_0_3_5', 'l_0_2_5', 's'), ('l_5_5_5', 'l_5_4_5', 's'), ('l_3_3_5', 'l_3_2_5', 's'), ('l_0_4_3', 'l_0_5_3', 'n'), ('l_1_1_4', 'l_1_1_3', 'w'), ('l_0_0_3', 'l_0_1_3', 'n'), ('l_5_2_1', 'l_5_3_1', 'n'), ('l_5_4_5', 'l_5_5_5', 'n'), ('l_3_1_1', 'l_3_0_1', 's'), ('l_5_5_0', 'l_5_4_0', 's'), ('l_6_2_3', 'l_6_1_3', 's'), ('l_4_4_1', 'l_4_5_1', 'n'), ('l_0_2_1', 'l_0_3_1', 'n'), ('l_6_3_0', 'l_6_2_0', 's'), ('l_5_4_3', 'l_5_5_3', 'n'), ('l_2_3_2', 'l_2_3_1', 'w'), ('l_6_3_5', 'l_6_2_5', 's'), ('l_4_5_3', 'l_4_5_4', 'e'), ('l_4_0_2', 'l_4_0_3', 'e'), ('l_0_3_4', 'l_0_3_3', 'w'), ('l_0_4_2', 'l_0_5_2', 'n'), ('l_6_4_4', 'l_6_4_3', 'w'), ('l_0_3_2', 'l_0_3_1', 'w'), ('l_1_2_1', 'l_1_2_0', 'w'), ('l_2_2_5', 'l_2_2_4', 'w'), ('l_1_4_1', 'l_1_4_0', 'w'), ('l_6_5_0', 'l_6_5_1', 'e'), ('l_1_1_2', 'l_1_2_2', 'n'), ('l_1_3_4', 'l_1_2_4', 's'), ('l_2_3_3', 'l_2_4_3', 'n'), ('l_0_5_4', 'l_0_5_5', 'e'), ('l_3_0_4', 'l_3_0_3', 'w'), ('l_6_5_5', 'l_6_4_5', 's'), ('l_3_5_5', 'l_3_4_5', 's'), ('l_2_2_5', 'l_2_1_5', 's'), ('l_2_4_3', 'l_2_4_4', 'e'), ('l_6_1_0', 'l_6_1_1', 'e'), ('l_3_2_5', 'l_3_1_5', 's'), ('l_0_2_5', 'l_0_1_5', 's'), ('l_6_5_3', 'l_6_5_4', 'e'), ('l_2_3_0', 'l_2_2_0', 's'), ('l_0_1_3', 'l_0_2_3', 'n'), ('l_0_3_3', 'l_0_2_3', 's'), ('l_5_4_2', 'l_5_4_3', 'e'), ('l_5_2_4', 'l_5_2_3', 'w'), ('l_3_2_3', 'l_3_2_2', 'w'), ('l_2_4_4', 'l_2_4_3', 'w'), ('l_4_2_3', 'l_4_2_2', 'w'), ('l_4_4_0', 'l_4_4_1', 'e'), ('l_0_2_2', 'l_0_3_2', 'n'), ('l_4_4_3', 'l_4_3_3', 's'), ('l_3_5_4', 'l_3_4_4', 's'), ('l_0_1_1', 'l_0_1_0', 'w'), ('l_5_2_3', 'l_5_2_2', 'w'), ('l_2_3_5', 'l_2_3_4', 'w'), ('l_3_2_1', 'l_3_1_1', 's'), ('l_5_0_2', 'l_5_0_3', 'e'), ('l_6_3_3', 'l_6_3_2', 'w'), ('l_6_2_0', 'l_6_2_1', 'e'), }
rigid.on_top = { ('l_1_3_1', 'l_2_3_1'), ('l_3_5_4', 'l_4_5_4'), ('l_0_5_5', 'l_1_5_5'), ('l_5_5_2', 'l_6_5_2'), ('l_0_2_1', 'l_1_2_1'), ('l_2_3_1', 'l_3_3_1'), ('l_5_1_4', 'l_6_1_4'), ('l_3_0_2', 'l_4_0_2'), ('l_0_5_4', 'l_1_5_4'), ('l_2_5_4', 'l_3_5_4'), ('l_3_0_3', 'l_4_0_3'), ('l_3_2_0', 'l_4_2_0'), ('l_1_5_5', 'l_2_5_5'), ('l_1_4_5', 'l_2_4_5'), ('l_1_3_5', 'l_2_3_5'), ('l_3_1_1', 'l_4_1_1'), ('l_0_2_3', 'l_1_2_3'), ('l_2_2_4', 'l_3_2_4'), ('l_5_3_3', 'l_6_3_3'), ('l_4_5_2', 'l_5_5_2'), ('l_2_0_1', 'l_3_0_1'), ('l_1_1_0', 'l_2_1_0'), ('l_4_4_1', 'l_5_4_1'), ('l_0_3_4', 'l_1_3_4'), ('l_5_4_5', 'l_6_4_5'), ('l_1_5_4', 'l_2_5_4'), ('l_4_0_4', 'l_5_0_4'), ('l_2_5_0', 'l_3_5_0'), ('l_0_5_1', 'l_1_5_1'), ('l_5_1_0', 'l_6_1_0'), ('l_2_1_3', 'l_3_1_3'), ('l_5_0_0', 'l_6_0_0'), ('l_3_2_4', 'l_4_2_4'), ('l_2_4_4', 'l_3_4_4'), ('l_5_3_2', 'l_6_3_2'), ('l_3_3_4', 'l_4_3_4'), ('l_1_3_3', 'l_2_3_3'), ('l_3_4_4', 'l_4_4_4'), ('l_1_1_5', 'l_2_1_5'), ('l_1_2_2', 'l_2_2_2'), ('l_1_1_3', 'l_2_1_3'), ('l_0_3_2', 'l_1_3_2'), ('l_0_0_3', 'l_1_0_3'), ('l_1_2_1', 'l_2_2_1'), ('l_5_3_5', 'l_6_3_5'), ('l_0_1_0', 'l_1_1_0'), ('l_0_3_0', 'l_1_3_0'), ('l_5_2_0', 'l_6_2_0'), ('l_2_3_5', 'l_3_3_5'), ('l_3_1_0', 'l_4_1_0'), ('l_1_4_2', 'l_2_4_2'), ('l_5_3_4', 'l_6_3_4'), ('l_5_5_4', 'l_6_5_4'), ('l_0_3_5', 'l_1_3_5'), ('l_0_5_2', 'l_1_5_2'), ('l_1_4_0', 'l_2_4_0'), ('l_1_0_3', 'l_2_0_3'), ('l_4_2_1', 'l_5_2_1'), ('l_3_4_1', 'l_4_4_1'), ('l_3_2_5', 'l_4_2_5'), ('l_3_5_1', 'l_4_5_1'), ('l_0_0_4', 'l_1_0_4'), ('l_4_5_0', 'l_5_5_0'), ('l_5_0_1', 'l_6_0_1'), ('l_5_4_1', 'l_6_4_1'), ('l_3_3_2', 'l_4_3_2'), ('l_2_2_5', 'l_3_2_5'), ('l_5_2_4', 'l_6_2_4'), ('l_4_4_3', 'l_5_4_3'), ('l_0_4_0', 'l_1_4_0'), ('l_2_4_3', 'l_3_4_3'), ('l_4_2_0', 'l_5_2_0'), ('l_2_1_5', 'l_3_1_5'), ('l_0_4_3', 'l_1_4_3'), ('l_0_1_5', 'l_1_1_5'), ('l_0_0_2', 'l_1_0_2'), ('l_4_0_5', 'l_5_0_5'), ('l_0_4_1', 'l_1_4_1'), ('l_1_5_3', 'l_2_5_3'), ('l_2_2_1', 'l_3_2_1'), ('l_4_0_2', 'l_5_0_2'), ('l_2_0_3', 'l_3_0_3'), ('l_0_2_5', 'l_1_2_5'), ('l_2_4_2', 'l_3_4_2'), ('l_4_2_4', 'l_5_2_4'), ('l_0_1_1', 'l_1_1_1'), ('l_0_0_5', 'l_1_0_5'), ('l_4_0_1', 'l_5_0_1'), ('l_3_0_5', 'l_4_0_5'), ('l_5_1_1', 'l_6_1_1'), ('l_3_1_3', 'l_4_1_3'), ('l_4_1_3', 'l_5_1_3'), ('l_4_2_2', 'l_5_2_2'), ('l_2_1_4', 'l_3_1_4'), ('l_0_0_0', 'l_1_0_0'), ('l_1_0_4', 'l_2_0_4'), ('l_5_1_5', 'l_6_1_5'), ('l_5_5_1', 'l_6_5_1'), ('l_5_3_0', 'l_6_3_0'), ('l_0_5_0', 'l_1_5_0'), ('l_1_3_0', 'l_2_3_0'), ('l_0_1_4', 'l_1_1_4'), ('l_4_5_1', 'l_5_5_1'), ('l_5_4_2', 'l_6_4_2'), ('l_4_3_0', 'l_5_3_0'), ('l_5_2_2', 'l_6_2_2'), ('l_5_2_3', 'l_6_2_3'), ('l_2_0_5', 'l_3_0_5'), ('l_1_5_0', 'l_2_5_0'), ('l_1_0_1', 'l_2_0_1'), ('l_2_2_3', 'l_3_2_3'), ('l_3_3_1', 'l_4_3_1'), ('l_5_3_1', 'l_6_3_1'), ('l_2_0_2', 'l_3_0_2'), ('l_1_5_2', 'l_2_5_2'), ('l_2_5_5', 'l_3_5_5'), ('l_3_5_5', 'l_4_5_5'), ('l_5_5_5', 'l_6_5_5'), ('l_5_2_1', 'l_6_2_1'), ('l_2_3_4', 'l_3_3_4'), ('l_2_2_0', 'l_3_2_0'), ('l_0_2_4', 'l_1_2_4'), ('l_0_1_3', 'l_1_1_3'), ('l_5_1_2', 'l_6_1_2'), ('l_3_4_5', 'l_4_4_5'), ('l_4_1_2', 'l_5_1_2'), ('l_3_5_0', 'l_4_5_0'), ('l_3_0_1', 'l_4_0_1'), ('l_1_3_4', 'l_2_3_4'), ('l_5_5_3', 'l_6_5_3'), ('l_4_3_4', 'l_5_3_4'), ('l_1_2_3', 'l_2_2_3'), ('l_1_1_2', 'l_2_1_2'), ('l_3_0_0', 'l_4_0_0'), ('l_2_5_2', 'l_3_5_2'), ('l_0_3_1', 'l_1_3_1'), ('l_4_1_4', 'l_5_1_4'), ('l_3_2_3', 'l_4_2_3'), ('l_3_3_0', 'l_4_3_0'), ('l_3_2_1', 'l_4_2_1'), ('l_3_1_4', 'l_4_1_4'), ('l_4_3_5', 'l_5_3_5'), ('l_1_1_1', 'l_2_1_1'), ('l_4_2_5', 'l_5_2_5'), ('l_1_2_5', 'l_2_2_5'), ('l_4_0_0', 'l_5_0_0'), ('l_0_4_5', 'l_1_4_5'), ('l_2_5_1', 'l_3_5_1'), ('l_5_0_4', 'l_6_0_4'), ('l_5_4_3', 'l_6_4_3'), ('l_2_4_1', 'l_3_4_1'), ('l_1_4_3', 'l_2_4_3'), ('l_3_4_0', 'l_4_4_0'), ('l_1_4_4', 'l_2_4_4'), ('l_4_3_1', 'l_5_3_1'), ('l_1_0_0', 'l_2_0_0'), ('l_1_2_4', 'l_2_2_4'), ('l_5_0_2', 'l_6_0_2'), ('l_5_2_5', 'l_6_2_5'), ('l_2_1_1', 'l_3_1_1'), ('l_0_1_2', 'l_1_1_2'), ('l_2_0_0', 'l_3_0_0'), ('l_4_4_5', 'l_5_4_5'), ('l_1_1_4', 'l_2_1_4'), ('l_1_0_2', 'l_2_0_2'), ('l_3_0_4', 'l_4_0_4'), ('l_0_0_1', 'l_1_0_1'), ('l_4_0_3', 'l_5_0_3'), ('l_2_2_2', 'l_3_2_2'), ('l_4_4_0', 'l_5_4_0'), ('l_0_3_3', 'l_1_3_3'), ('l_0_5_3', 'l_1_5_3'), ('l_4_3_2', 'l_5_3_2'), ('l_2_3_0', 'l_3_3_0'), ('l_5_5_0', 'l_6_5_0'), ('l_5_4_4', 'l_6_4_4'), ('l_4_3_3', 'l_5_3_3'), ('l_0_2_2', 'l_1_2_2'), ('l_1_4_1', 'l_2_4_1'), ('l_2_5_3', 'l_3_5_3'), ('l_0_4_2', 'l_1_4_2'), ('l_4_1_5', 'l_5_1_5'), ('l_1_0_5', 'l_2_0_5'), ('l_3_4_3', 'l_4_4_3'), ('l_2_3_2', 'l_3_3_2'), ('l_3_3_3', 'l_4_3_3'), ('l_4_4_4', 'l_5_4_4'), ('l_5_1_3', 'l_6_1_3'), ('l_2_1_2', 'l_3_1_2'), ('l_2_4_0', 'l_3_4_0'), ('l_0_4_4', 'l_1_4_4'), ('l_4_1_0', 'l_5_1_0'), ('l_2_3_3', 'l_3_3_3'), ('l_4_5_5', 'l_5_5_5'), ('l_2_1_0', 'l_3_1_0'), ('l_4_5_3', 'l_5_5_3'), ('l_2_0_4', 'l_3_0_4'), ('l_2_4_5', 'l_3_4_5'), ('l_1_2_0', 'l_2_2_0'), ('l_5_0_3', 'l_6_0_3'), ('l_3_2_2', 'l_4_2_2'), ('l_4_5_4', 'l_5_5_4'), ('l_3_5_2', 'l_4_5_2'), ('l_3_5_3', 'l_4_5_3'), ('l_5_4_0', 'l_6_4_0'), ('l_3_4_2', 'l_4_4_2'), ('l_1_5_1', 'l_2_5_1'), ('l_3_1_5', 'l_4_1_5'), ('l_4_4_2', 'l_5_4_2'), ('l_4_2_3', 'l_5_2_3'), ('l_3_3_5', 'l_4_3_5'), ('l_3_1_2', 'l_4_1_2'), ('l_5_0_5', 'l_6_0_5'), ('l_0_2_0', 'l_1_2_0'), ('l_4_1_1', 'l_5_1_1'), ('l_1_3_2', 'l_2_3_2'), }
state.blockat = { ('l_0_1_4', 'earth'), ('l_0_0_1', 'earth'), ('l_0_5_1', 'earth'), ('l_0_1_1', 'earth'), ('l_0_2_2', 'earth'), ('l_0_4_0', 'earth'), ('l_0_4_1', 'earth'), ('l_0_0_0', 'earth'), ('l_0_2_5', 'earth'), ('l_0_4_5', 'earth'), ('l_0_0_4', 'earth'), ('l_0_5_3', 'earth'), ('l_0_5_0', 'earth'), ('l_0_0_2', 'earth'), ('l_0_3_1', 'earth'), ('l_0_1_0', 'earth'), ('l_0_5_2', 'earth'), ('l_0_1_5', 'earth'), ('l_0_5_5', 'earth'), ('l_0_3_3', 'earth'), ('l_0_0_3', 'earth'), ('l_0_2_1', 'earth'), ('l_0_4_4', 'earth'), ('l_0_3_2', 'earth'), ('l_0_3_4', 'earth'), ('l_0_4_2', 'earth'), ('l_0_2_3', 'earth'), ('l_0_0_5', 'earth'), ('l_0_3_5', 'earth'), ('l_0_1_2', 'earth'), ('l_0_3_0', 'earth'), ('l_0_2_4', 'earth'), ('l_0_5_4', 'earth'), ('l_0_2_0', 'earth'), ('l_0_4_3', 'earth'), ('l_0_1_3', 'earth'), }
state.empty = { ('l_1_2_4',), ('l_4_0_0',), ('l_3_5_0',), ('l_4_0_1',), ('l_1_4_0',), ('l_4_4_2',), ('l_2_2_1',), ('l_4_3_1',), ('l_5_3_4',), ('l_3_0_3',), ('l_3_3_3',), ('l_2_3_4',), ('l_6_1_3',), ('l_4_5_4',), ('l_1_5_1',), ('l_4_2_2',), ('l_3_0_0',), ('l_4_2_3',), ('l_4_0_5',), ('l_4_4_1',), ('l_5_3_3',), ('l_6_5_0',), ('l_1_0_0',), ('l_4_5_1',), ('l_2_5_4',), ('l_2_3_5',), ('l_5_3_5',), ('l_2_1_2',), ('l_3_5_1',), ('l_3_3_2',), ('l_2_0_0',), ('l_4_5_5',), ('l_5_1_3',), ('l_6_3_3',), ('l_4_0_4',), ('l_3_5_4',), ('l_6_5_5',), ('l_5_0_4',), ('l_5_4_1',), ('l_4_3_3',), ('l_1_2_0',), ('l_2_1_5',), ('l_5_5_4',), ('l_1_3_2',), ('l_6_0_4',), ('l_6_1_5',), ('l_3_5_5',), ('l_2_3_2',), ('l_2_4_1',), ('l_4_5_3',), ('l_3_2_3',), ('l_5_5_3',), ('l_3_1_3',), ('l_6_4_4',), ('l_5_4_2',), ('l_5_1_0',), ('l_4_5_0',), ('l_5_0_2',), ('l_5_1_5',), ('l_6_1_2',), ('l_1_4_1',), ('l_1_4_3',), ('l_3_5_2',), ('l_4_4_5',), ('l_1_2_1',), ('l_3_1_1',), ('l_4_2_5',), ('l_1_1_0',), ('l_5_3_0',), ('l_1_2_3',), ('l_6_5_3',), ('l_2_2_5',), ('l_2_0_5',), ('l_5_4_5',), ('l_3_4_5',), ('l_2_5_0',), ('l_1_4_2',), ('l_2_0_3',), ('l_4_3_0',), ('l_3_5_3',), ('l_5_4_4',), ('l_6_2_1',), ('l_5_5_2',), ('l_3_4_4',), ('l_6_1_0',), ('l_4_1_5',), ('l_1_5_0',), ('l_6_0_0',), ('l_5_1_1',), ('l_3_0_5',), ('l_6_2_3',), ('l_1_4_4',), ('l_5_3_2',), ('l_3_0_1',), ('l_2_0_1',), ('l_1_5_3',), ('l_5_0_0',), ('l_2_4_4',), ('l_6_5_1',), ('l_4_1_4',), ('l_1_3_0',), ('l_4_2_4',), ('l_1_3_1',), ('l_4_3_2',), ('l_5_1_2',), ('l_1_0_3',), ('l_2_4_0',), ('l_3_0_4',), ('l_5_3_1',), ('l_2_2_3',), ('l_1_2_2',), ('l_5_0_3',), ('l_5_0_5',), ('l_6_1_1',), ('l_6_3_1',), ('l_3_4_3',), ('l_3_1_5',), ('l_1_2_5',), ('l_5_1_4',), ('l_6_1_4',), ('l_3_1_2',), ('l_5_4_3',), ('l_2_4_3',), ('l_4_4_4',), ('l_2_3_3',), ('l_1_5_2',), ('l_1_4_5',), ('l_2_3_0',), ('l_6_3_0',), ('l_1_3_3',), ('l_1_1_1',), ('l_5_2_3',), ('l_2_2_4',), ('l_6_0_1',), ('l_5_0_1',), ('l_3_3_1',), ('l_4_0_2',), ('l_6_0_3',), ('l_2_2_0',), ('l_4_1_1',), ('l_4_1_0',), ('l_3_3_5',), ('l_6_4_2',), ('l_2_4_5',), ('l_2_3_1',), ('l_3_1_0',), ('l_5_5_1',), ('l_6_2_0',), ('l_4_1_2',), ('l_3_3_4',), ('l_6_0_5',), ('l_5_2_5',), ('l_3_4_2',), ('l_2_4_2',), ('l_3_2_1',), ('l_6_3_2',), ('l_4_5_2',), ('l_2_5_2',), ('l_4_4_3',), ('l_1_0_1',), ('l_1_0_2',), ('l_3_4_1',), ('l_4_4_0',), ('l_1_5_4',), ('l_2_0_2',), ('l_2_0_4',), ('l_1_1_2',), ('l_3_2_4',), ('l_5_4_0',), ('l_5_2_1',), ('l_3_3_0',), ('l_6_5_4',), ('l_4_2_1',), ('l_4_0_3',), ('l_5_2_4',), ('l_5_2_0',), ('l_2_1_4',), ('l_3_0_2',), ('l_3_2_2',), ('l_1_3_4',), ('l_4_3_5',), ('l_3_1_4',), ('l_2_5_3',), ('l_6_3_5',), ('l_3_2_0',), ('l_6_2_2',), ('l_6_0_2',), ('l_6_4_1',), ('l_6_4_5',), ('l_5_2_2',), ('l_1_1_5',), ('l_1_0_5',), ('l_2_5_5',), ('l_6_4_3',), ('l_4_2_0',), ('l_1_0_4',), ('l_2_2_2',), ('l_1_1_4',), ('l_6_5_2',), ('l_2_1_1',), ('l_2_1_3',), ('l_6_2_5',), ('l_5_5_0',), ('l_2_5_1',), ('l_6_4_0',), ('l_5_5_5',), ('l_4_1_3',), ('l_2_1_0',), ('l_6_3_4',), ('l_3_2_5',), ('l_1_3_5',), ('l_1_1_3',), ('l_4_3_4',), ('l_6_2_4',), ('l_3_4_0',), ('l_1_5_5',), }
rigid.isone = { ('n1',), }
rigid.prev = { ('n4', 'n3'), ('n2', 'n1'), ('n1', 'n0'), ('n5', 'n4'), ('n3', 'n2'), }

task_list = [('buildhouse', 'l_1_0_0', 'l_1_0_4', 'l_1_3_4', 'l_1_3_0', 'l_1_1_0', 'l_6_0_0', 'n5', 'n4', 'n5', 'stone')]
