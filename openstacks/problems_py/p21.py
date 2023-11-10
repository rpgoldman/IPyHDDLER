from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'p27', 'n15', 'p12', 'p30', 'o47', 'p37', 'p31', 'p9', 'n49', 'n22', 'o21', 'o28', 'p39', 'p19', 'n31', 'n42', 'p10', 'o39', 'o15', 'n2', 'o49', 'p22', 'n0', 'n35', 'o13', 'n3', 'n5', 'p13', 'p23', 'n21', 'o4', 'o46', 'n38', 'n45', 'p4', 'n48', 'o6', 'p43', 'p7', 'n24', 'n26', 'o40', 'p34', 'n36', 'n14', 'n47', 'n9', 'p1', 'o44', 'o10', 'o16', 'o36', 'o29', 'p15', 'p24', 'n44', 'o11', 'p20', 'p36', 'n7', 'n43', 'o17', 'o48', 'p6', 'o19', 'p16', 'o20', 'p38', 'n17', 'o43', 'n18', 'o24', 'o27', 'o7', 'n20', 'p33', 'n10', 'o25', 'o14', 'n34', 'o23', 'p17', 'o9', 'p2', 'p46', 'p32', 'o35', 'o41', 'n23', 'p28', 'o34', 'o33', 'p42', 'o1', 'n37', 'o30', 'p14', 'n16', 'n6', 'o12', 'p44', 'n19', 'o22', 'p11', 'n13', 'p21', 'n39', 'o42', 'o37', 'n1', 'o18', 'n27', 'n29', 'o38', 'o26', 'o5', 'p41', 'p5', 'p50', 'n11', 'p25', 'o31', 'o45', 'o8', 'n25', 'p26', 'p18', 'n46', 'n32', 'n8', 'n41', 'n28', 'n30', 'p35', 'n12', 'n4', 'o2', 'o32', 'o50', 'n33', 'p48', 'p3', 'p29', 'p40', 'p45', 'p49', 'o3', 'n40', 'p47', 'n50', 'p8'}
rigid.count = {'n15', 'n20', 'n10', 'n34', 'n49', 'n22', 'n31', 'n23', 'n42', 'n2', 'n0', 'n35', 'n3', 'n5', 'n37', 'n16', 'n21', 'n38', 'n45', 'n6', 'n48', 'n19', 'n24', 'n26', 'n13', 'n39', 'n36', 'n1', 'n27', 'n14', 'n29', 'n47', 'n9', 'n11', 'n25', 'n44', 'n46', 'n32', 'n8', 'n41', 'n28', 'n30', 'n7', 'n12', 'n43', 'n4', 'n33', 'n40', 'n17', 'n50', 'n18'}
rigid.product = {'p27', 'p12', 'p30', 'p33', 'p37', 'p31', 'p9', 'p17', 'p2', 'p39', 'p19', 'p32', 'p46', 'p10', 'p28', 'p22', 'p42', 'p13', 'p23', 'p14', 'p4', 'p44', 'p43', 'p7', 'p11', 'p34', 'p21', 'p1', 'p41', 'p5', 'p50', 'p25', 'p15', 'p24', 'p26', 'p20', 'p18', 'p36', 'p35', 'p6', 'p48', 'p3', 'p16', 'p29', 'p40', 'p45', 'p38', 'p49', 'p47', 'p8'}
rigid.order = {'o7', 'o25', 'o14', 'o47', 'o23', 'o21', 'o9', 'o28', 'o35', 'o41', 'o39', 'o15', 'o34', 'o33', 'o49', 'o13', 'o1', 'o30', 'o4', 'o46', 'o12', 'o6', 'o22', 'o40', 'o42', 'o37', 'o18', 'o38', 'o26', 'o44', 'o10', 'o16', 'o5', 'o36', 'o29', 'o31', 'o45', 'o8', 'o11', 'o17', 'o48', 'o2', 'o32', 'o19', 'o50', 'o20', 'o3', 'o43', 'o24', 'o27'}
rigid.goal__shipped = set( [('o9',), ('o7',), ('o23',), ('o35',), ('o40',), ('o36',), ('o4',), ('o38',), ('o31',), ('o47',), ('o45',), ('o25',), ('o24',), ('o15',), ('o42',), ('o30',), ('o10',), ('o46',), ('o22',), ('o34',), ('o1',), ('o48',), ('o33',), ('o18',), ('o12',), ('o19',), ('o3',), ('o37',), ('o8',), ('o39',), ('o11',), ('o20',), ('o32',), ('o28',), ('o26',), ('o29',), ('o21',), ('o13',), ('o41',), ('o49',), ('o5',), ('o16',), ('o2',), ('o17',), ('o14',), ('o44',), ('o50',), ('o27',), ('o6',), ('o43',), ] )
rigid.next__count = set( [('n14', 'n15'), ('n11', 'n12'), ('n31', 'n32'), ('n47', 'n48'), ('n34', 'n35'), ('n30', 'n31'), ('n45', 'n46'), ('n33', 'n34'), ('n36', 'n37'), ('n28', 'n29'), ('n5', 'n6'), ('n25', 'n26'), ('n18', 'n19'), ('n29', 'n30'), ('n17', 'n18'), ('n35', 'n36'), ('n39', 'n40'), ('n26', 'n27'), ('n1', 'n2'), ('n0', 'n1'), ('n42', 'n43'), ('n13', 'n14'), ('n49', 'n50'), ('n23', 'n24'), ('n38', 'n39'), ('n24', 'n25'), ('n32', 'n33'), ('n27', 'n28'), ('n40', 'n41'), ('n10', 'n11'), ('n44', 'n45'), ('n3', 'n4'), ('n4', 'n5'), ('n12', 'n13'), ('n8', 'n9'), ('n46', 'n47'), ('n41', 'n42'), ('n19', 'n20'), ('n22', 'n23'), ('n7', 'n8'), ('n6', 'n7'), ('n16', 'n17'), ('n48', 'n49'), ('n9', 'n10'), ('n2', 'n3'), ('n20', 'n21'), ('n43', 'n44'), ('n15', 'n16'), ('n37', 'n38'), ('n21', 'n22'), ] )
state.stacks__avail = set( [('n0',), ] )
state.waiting = set( [('o9',), ('o7',), ('o23',), ('o35',), ('o40',), ('o36',), ('o4',), ('o38',), ('o31',), ('o47',), ('o45',), ('o25',), ('o24',), ('o15',), ('o42',), ('o30',), ('o10',), ('o46',), ('o22',), ('o34',), ('o1',), ('o48',), ('o33',), ('o18',), ('o12',), ('o19',), ('o3',), ('o37',), ('o8',), ('o39',), ('o11',), ('o20',), ('o32',), ('o28',), ('o26',), ('o29',), ('o21',), ('o13',), ('o41',), ('o49',), ('o5',), ('o16',), ('o2',), ('o17',), ('o14',), ('o44',), ('o50',), ('o27',), ('o6',), ('o43',), ] )
rigid.includes = set( [('o5', 'p22'), ('o18', 'p38'), ('o39', 'p26'), ('o26', 'p38'), ('o30', 'p28'), ('o26', 'p1'), ('o40', 'p40'), ('o25', 'p25'), ('o30', 'p38'), ('o8', 'p15'), ('o32', 'p13'), ('o23', 'p38'), ('o27', 'p32'), ('o18', 'p23'), ('o15', 'p45'), ('o10', 'p18'), ('o21', 'p29'), ('o35', 'p7'), ('o14', 'p24'), ('o41', 'p4'), ('o19', 'p34'), ('o17', 'p4'), ('o23', 'p37'), ('o45', 'p48'), ('o3', 'p14'), ('o37', 'p9'), ('o5', 'p23'), ('o4', 'p20'), ('o11', 'p9'), ('o34', 'p43'), ('o47', 'p50'), ('o14', 'p25'), ('o21', 'p27'), ('o9', 'p16'), ('o46', 'p9'), ('o42', 'p35'), ('o8', 'p10'), ('o26', 'p30'), ('o47', 'p37'), ('o50', 'p27'), ('o17', 'p19'), ('o19', 'p30'), ('o7', 'p12'), ('o1', 'p1'), ('o12', 'p2'), ('o42', 'p39'), ('o18', 'p48'), ('o6', 'p34'), ('o18', 'p26'), ('o11', 'p31'), ('o5', 'p30'), ('o35', 'p3'), ('o49', 'p23'), ('o14', 'p16'), ('o13', 'p41'), ('o33', 'p6'), ('o43', 'p25'), ('o2', 'p44'), ('o14', 'p4'), ('o40', 'p14'), ('o12', 'p49'), ('o8', 'p24'), ('o18', 'p25'), ('o7', 'p49'), ('o19', 'p8'), ('o48', 'p21'), ('o25', 'p20'), ('o5', 'p24'), ('o9', 'p38'), ('o38', 'p25'), ('o42', 'p47'), ('o12', 'p13'), ('o29', 'p49'), ('o12', 'p11'), ('o15', 'p21'), ('o16', 'p12'), ('o31', 'p11'), ('o9', 'p36'), ('o1', 'p12'), ('o46', 'p17'), ('o44', 'p10'), ('o22', 'p48'), ('o42', 'p31'), ('o28', 'p37'), ('o24', 'p15'), ('o20', 'p10'), ('o22', 'p32'), ('o40', 'p42'), ('o10', 'p9'), ('o48', 'p32'), ('o36', 'p43'), ('o9', 'p5'), ('o13', 'p31'), ('o8', 'p17'), ('o15', 'p46'), ('o44', 'p23'), ('o8', 'p8'), ('o5', 'p33'), ('o15', 'p30'), ('o42', 'p4'), ('o24', 'p39'), ] )
state.started = set( [] )
state.shipped = set( [] )
state.made = set( [] )

task_list = [('plan',)]