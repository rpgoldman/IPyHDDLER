from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'p17', 'n2', 'o5', 'o2', 'o26', 'p22', 'o14', 'n1', 'p20', 'p16', 'n8', 'o11', 'p19', 'o21', 'p7', 'n14', 'p28', 'n6', 'o7', 'p18', 'n11', 'o1', 'n5', 'n24', 'p10', 'n0', 'n20', 'n19', 'n18', 'o8', 'n9', 'p26', 'p2', 'n17', 'o10', 'p15', 'n15', 'o16', 'p24', 'p23', 'o12', 'p6', 'n25', 'o24', 'n28', 'p21', 'p3', 'n16', 'o27', 'o15', 'o3', 'o6', 'p27', 'p29', 'n26', 'n3', 'n23', 'n21', 'p9', 'o23', 'n27', 'n4', 'p8', 'o22', 'o19', 'n10', 'p5', 'n30', 'n29', 'o28', 'p1', 'p25', 'p14', 'p12', 'o20', 'o4', 'n22', 'o17', 'n7', 'o30', 'o29', 'o13', 'o18', 'n12', 'o9', 'p30', 'n13', 'p13', 'p11', 'o25', 'p4'}
rigid.product = {'p12', 'p17', 'p27', 'p29', 'p18', 'p10', 'p3', 'p26', 'p9', 'p2', 'p22', 'p15', 'p30', 'p21', 'p8', 'p13', 'p20', 'p16', 'p24', 'p19', 'p5', 'p23', 'p6', 'p11', 'p7', 'p28', 'p1', 'p25', 'p14', 'p4'}
rigid.order = {'o1', 'o20', 'o4', 'o27', 'o15', 'o3', 'o6', 'o17', 'o5', 'o30', 'o2', 'o29', 'o8', 'o13', 'o18', 'o26', 'o9', 'o23', 'o10', 'o14', 'o16', 'o11', 'o19', 'o22', 'o12', 'o21', 'o25', 'o24', 'o28', 'o7'}
rigid.count = {'n11', 'n5', 'n24', 'n2', 'n22', 'n26', 'n7', 'n0', 'n3', 'n20', 'n23', 'n19', 'n18', 'n9', 'n12', 'n21', 'n27', 'n17', 'n15', 'n13', 'n4', 'n1', 'n8', 'n10', 'n25', 'n30', 'n14', 'n28', 'n29', 'n6', 'n16'}
rigid.goal__shipped = set( [('o29',), ('o8',), ('o23',), ('o27',), ('o5',), ('o4',), ('o21',), ('o11',), ('o6',), ('o25',), ('o15',), ('o30',), ('o3',), ('o20',), ('o2',), ('o9',), ('o13',), ('o24',), ('o26',), ('o1',), ('o22',), ('o7',), ('o17',), ('o19',), ('o16',), ('o10',), ('o14',), ('o28',), ('o12',), ('o18',), ] )
rigid.next__count = set( [('n10', 'n11'), ('n19', 'n20'), ('n27', 'n28'), ('n21', 'n22'), ('n13', 'n14'), ('n1', 'n2'), ('n25', 'n26'), ('n16', 'n17'), ('n9', 'n10'), ('n29', 'n30'), ('n17', 'n18'), ('n0', 'n1'), ('n3', 'n4'), ('n4', 'n5'), ('n15', 'n16'), ('n11', 'n12'), ('n23', 'n24'), ('n18', 'n19'), ('n20', 'n21'), ('n28', 'n29'), ('n6', 'n7'), ('n2', 'n3'), ('n5', 'n6'), ('n14', 'n15'), ('n24', 'n25'), ('n26', 'n27'), ('n8', 'n9'), ('n22', 'n23'), ('n12', 'n13'), ('n7', 'n8'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o29',), ('o8',), ('o23',), ('o27',), ('o5',), ('o4',), ('o21',), ('o11',), ('o6',), ('o25',), ('o15',), ('o30',), ('o3',), ('o20',), ('o2',), ('o9',), ('o13',), ('o24',), ('o26',), ('o1',), ('o22',), ('o7',), ('o17',), ('o19',), ('o16',), ('o10',), ('o14',), ('o28',), ('o12',), ('o18',), ] )
rigid.includes = set( [('o24', 'p13'), ('o28', 'p12'), ('o27', 'p21'), ('o22', 'p2'), ('o8', 'p9'), ('o26', 'p23'), ('o23', 'p16'), ('o12', 'p22'), ('o23', 'p3'), ('o20', 'p6'), ('o26', 'p28'), ('o6', 'p4'), ('o22', 'p20'), ('o27', 'p27'), ('o13', 'p7'), ('o8', 'p8'), ('o5', 'p1'), ('o3', 'p13'), ('o6', 'p12'), ('o5', 'p6'), ('o15', 'p30'), ('o9', 'p6'), ('o7', 'p23'), ('o4', 'p16'), ('o4', 'p13'), ('o21', 'p15'), ('o4', 'p10'), ('o14', 'p6'), ('o29', 'p15'), ('o20', 'p7'), ('o2', 'p22'), ('o16', 'p13'), ('o27', 'p26'), ('o17', 'p14'), ('o19', 'p18'), ('o15', 'p13'), ('o25', 'p7'), ('o18', 'p30'), ('o27', 'p17'), ('o10', 'p18'), ('o21', 'p19'), ('o26', 'p20'), ('o20', 'p29'), ('o18', 'p25'), ('o1', 'p11'), ('o28', 'p11'), ('o15', 'p18'), ('o11', 'p24'), ('o5', 'p5'), ('o30', 'p21'), ] )
state.shipped = set( [] )
state.made = set( [] )
state.started = set( [] )

task_list = [('plan',)]
