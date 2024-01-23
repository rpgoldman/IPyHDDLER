from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = OrderedSet(['n0', 'n1', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19', 'n2', 'n20', 'n21', 'n22', 'n23', 'n24', 'n25', 'n26', 'n27', 'n28', 'n29', 'n3', 'n30', 'n31', 'n32', 'n33', 'n34', 'n35', 'n36', 'n37', 'n38', 'n39', 'n4', 'n40', 'n5', 'n6', 'n7', 'n8', 'n9', 'o1', 'o10', 'o11', 'o12', 'o13', 'o14', 'o15', 'o16', 'o17', 'o18', 'o19', 'o2', 'o20', 'o21', 'o22', 'o23', 'o24', 'o25', 'o26', 'o27', 'o28', 'o29', 'o3', 'o30', 'o31', 'o32', 'o33', 'o34', 'o35', 'o36', 'o37', 'o38', 'o39', 'o4', 'o40', 'o5', 'o6', 'o7', 'o8', 'o9', 'p1', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p2', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p3', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p4', 'p40', 'p5', 'p6', 'p7', 'p8', 'p9'])
rigid.order = OrderedSet(['o1', 'o10', 'o11', 'o12', 'o13', 'o14', 'o15', 'o16', 'o17', 'o18', 'o19', 'o2', 'o20', 'o21', 'o22', 'o23', 'o24', 'o25', 'o26', 'o27', 'o28', 'o29', 'o3', 'o30', 'o31', 'o32', 'o33', 'o34', 'o35', 'o36', 'o37', 'o38', 'o39', 'o4', 'o40', 'o5', 'o6', 'o7', 'o8', 'o9'])
rigid.product = OrderedSet(['p1', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p2', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29', 'p3', 'p30', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p4', 'p40', 'p5', 'p6', 'p7', 'p8', 'p9'])
rigid.count = OrderedSet(['n0', 'n1', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19', 'n2', 'n20', 'n21', 'n22', 'n23', 'n24', 'n25', 'n26', 'n27', 'n28', 'n29', 'n3', 'n30', 'n31', 'n32', 'n33', 'n34', 'n35', 'n36', 'n37', 'n38', 'n39', 'n4', 'n40', 'n5', 'n6', 'n7', 'n8', 'n9'])
rigid.goal__shipped = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ('o6',), ('o7',), ('o8',), ('o9',), ('o10',), ('o11',), ('o12',), ('o13',), ('o14',), ('o15',), ('o16',), ('o17',), ('o18',), ('o19',), ('o20',), ('o21',), ('o22',), ('o23',), ('o24',), ('o25',), ('o26',), ('o27',), ('o28',), ('o29',), ('o30',), ('o31',), ('o32',), ('o33',), ('o34',), ('o35',), ('o36',), ('o37',), ('o38',), ('o39',), ('o40',), ] )
rigid.next__count = OrderedSet( [('n0', 'n1'), ('n1', 'n2'), ('n2', 'n3'), ('n3', 'n4'), ('n4', 'n5'), ('n5', 'n6'), ('n6', 'n7'), ('n7', 'n8'), ('n8', 'n9'), ('n9', 'n10'), ('n10', 'n11'), ('n11', 'n12'), ('n12', 'n13'), ('n13', 'n14'), ('n14', 'n15'), ('n15', 'n16'), ('n16', 'n17'), ('n17', 'n18'), ('n18', 'n19'), ('n19', 'n20'), ('n20', 'n21'), ('n21', 'n22'), ('n22', 'n23'), ('n23', 'n24'), ('n24', 'n25'), ('n25', 'n26'), ('n26', 'n27'), ('n27', 'n28'), ('n28', 'n29'), ('n29', 'n30'), ('n30', 'n31'), ('n31', 'n32'), ('n32', 'n33'), ('n33', 'n34'), ('n34', 'n35'), ('n35', 'n36'), ('n36', 'n37'), ('n37', 'n38'), ('n38', 'n39'), ('n39', 'n40'), ] )
state.stacks__avail = OrderedSet( [('n0',), ] )
state.waiting = OrderedSet( [('o1',), ('o2',), ('o3',), ('o4',), ('o5',), ('o6',), ('o7',), ('o8',), ('o9',), ('o10',), ('o11',), ('o12',), ('o13',), ('o14',), ('o15',), ('o16',), ('o17',), ('o18',), ('o19',), ('o20',), ('o21',), ('o22',), ('o23',), ('o24',), ('o25',), ('o26',), ('o27',), ('o28',), ('o29',), ('o30',), ('o31',), ('o32',), ('o33',), ('o34',), ('o35',), ('o36',), ('o37',), ('o38',), ('o39',), ('o40',), ] )
rigid.includes = OrderedSet( [('o1', 'p6'), ('o2', 'p22'), ('o2', 'p25'), ('o2', 'p28'), ('o3', 'p34'), ('o4', 'p7'), ('o4', 'p22'), ('o4', 'p31'), ('o5', 'p2'), ('o6', 'p29'), ('o7', 'p13'), ('o7', 'p16'), ('o7', 'p27'), ('o8', 'p8'), ('o9', 'p35'), ('o10', 'p30'), ('o11', 'p9'), ('o12', 'p5'), ('o13', 'p17'), ('o13', 'p21'), ('o13', 'p26'), ('o14', 'p9'), ('o15', 'p4'), ('o15', 'p25'), ('o15', 'p28'), ('o16', 'p4'), ('o16', 'p10'), ('o17', 'p10'), ('o18', 'p15'), ('o19', 'p15'), ('o19', 'p20'), ('o20', 'p1'), ('o20', 'p12'), ('o20', 'p14'), ('o20', 'p21'), ('o21', 'p15'), ('o22', 'p22'), ('o22', 'p25'), ('o23', 'p9'), ('o23', 'p10'), ('o24', 'p17'), ('o25', 'p17'), ('o26', 'p31'), ('o27', 'p34'), ('o28', 'p31'), ('o29', 'p35'), ('o30', 'p12'), ('o31', 'p19'), ('o31', 'p24'), ('o31', 'p33'), ('o32', 'p3'), ('o32', 'p9'), ('o32', 'p29'), ('o32', 'p37'), ('o32', 'p38'), ('o33', 'p27'), ('o34', 'p8'), ('o34', 'p15'), ('o34', 'p36'), ('o34', 'p40'), ('o35', 'p28'), ('o36', 'p16'), ('o36', 'p17'), ('o37', 'p23'), ('o37', 'p32'), ('o37', 'p34'), ('o38', 'p11'), ('o38', 'p28'), ('o39', 'p3'), ('o39', 'p18'), ('o39', 'p39'), ('o40', 'p14'), ] )
state.started = OrderedSet( [] )
state.shipped = OrderedSet( [] )
state.made = OrderedSet( [] )

task_list = [('plan',)]
