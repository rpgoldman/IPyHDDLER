from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'n10', 'p6', 'n2', 'o2', 'n5', 'o16', 'o18', 'p7', 'o8', 'p9', 'p20', 'p5', 'n17', 'o1', 'n12', 'p4', 'n0', 'p8', 'p10', 'o6', 'o14', 'p3', 'n14', 'n6', 'n16', 'o9', 'o20', 'o7', 'p2', 'o10', 'n13', 'n11', 'n7', 'p16', 'p15', 'p17', 'p18', 'p14', 'p11', 'o11', 'o5', 'p19', 'n15', 'o12', 'p13', 'n1', 'o3', 'n3', 'o17', 'o19', 'n4', 'o4', 'o13', 'n19', 'n18', 'o15', 'n8', 'p12', 'n9', 'n20', 'p1'}
rigid.order = {'o2', 'o16', 'o18', 'o8', 'o11', 'o5', 'o1', 'o12', 'o3', 'o6', 'o14', 'o17', 'o19', 'o4', 'o13', 'o15', 'o9', 'o20', 'o7', 'o10'}
rigid.count = {'n10', 'n2', 'n5', 'n17', 'n12', 'n15', 'n0', 'n1', 'n3', 'n4', 'n14', 'n6', 'n19', 'n18', 'n16', 'n8', 'n9', 'n20', 'n13', 'n11', 'n7'}
rigid.product = {'p17', 'p6', 'p18', 'p15', 'p7', 'p9', 'p14', 'p20', 'p5', 'p11', 'p19', 'p4', 'p13', 'p8', 'p10', 'p3', 'p12', 'p2', 'p1', 'p16'}
rigid.goal__shipped = set( [('o5',), ('o15',), ('o14',), ('o2',), ('o4',), ('o16',), ('o9',), ('o18',), ('o17',), ('o10',), ('o13',), ('o8',), ('o20',), ('o3',), ('o19',), ('o6',), ('o7',), ('o12',), ('o11',), ('o1',), ] )
rigid.next__count = set( [('n9', 'n10'), ('n8', 'n9'), ('n13', 'n14'), ('n14', 'n15'), ('n5', 'n6'), ('n2', 'n3'), ('n6', 'n7'), ('n16', 'n17'), ('n19', 'n20'), ('n18', 'n19'), ('n1', 'n2'), ('n10', 'n11'), ('n11', 'n12'), ('n12', 'n13'), ('n15', 'n16'), ('n3', 'n4'), ('n4', 'n5'), ('n17', 'n18'), ('n7', 'n8'), ('n0', 'n1'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o5',), ('o15',), ('o14',), ('o2',), ('o4',), ('o16',), ('o9',), ('o18',), ('o17',), ('o10',), ('o13',), ('o8',), ('o20',), ('o3',), ('o19',), ('o6',), ('o7',), ('o12',), ('o11',), ('o1',), ] )
rigid.includes = set( [('o15', 'p14'), ('o10', 'p12'), ('o5', 'p17'), ('o9', 'p15'), ('o13', 'p11'), ('o14', 'p7'), ('o13', 'p12'), ('o7', 'p11'), ('o18', 'p16'), ('o17', 'p16'), ('o16', 'p5'), ('o6', 'p9'), ('o19', 'p14'), ('o15', 'p12'), ('o4', 'p2'), ('o19', 'p4'), ('o14', 'p9'), ('o12', 'p3'), ('o2', 'p1'), ('o5', 'p20'), ('o12', 'p1'), ('o4', 'p3'), ('o11', 'p19'), ('o18', 'p8'), ('o20', 'p19'), ('o15', 'p10'), ('o15', 'p13'), ('o3', 'p4'), ('o4', 'p11'), ('o8', 'p14'), ('o13', 'p18'), ('o7', 'p6'), ('o19', 'p10'), ('o1', 'p4'), ] )
state.shipped = set( [] )
state.started = set( [] )
state.made = set( [] )

task_list = [('plan',)]