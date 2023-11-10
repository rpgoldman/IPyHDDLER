from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'image0', 'planet16', 'satellite6', 'satellite2', 'image4', 'infrared3', 'satellite1', 'star21', 'satellite3', 'instrument23', 'planet11', 'instrument20', 'planet13', 'instrument7', 'satellite10', 'satellite5', 'phenomenon14', 'instrument6', 'instrument13', 'satellite8', 'instrument16', 'star18', 'groundstation0', 'instrument12', 'instrument22', 'star8', 'instrument19', 'planet12', 'star10', 'star1', 'instrument18', 'instrument17', 'star3', 'instrument4', 'phenomenon19', 'thermograph1', 'instrument11', 'planet6', 'phenomenon23', 'infrared2', 'instrument3', 'planet7', 'phenomenon24', 'instrument1', 'satellite7', 'satellite0', 'phenomenon15', 'instrument14', 'satellite9', 'instrument2', 'phenomenon20', 'instrument21', 'satellite4', 'planet5', 'phenomenon17', 'groundstation2', 'phenomenon9', 'instrument8', 'groundstation4', 'instrument5', 'instrument15', 'instrument0', 'star22', 'satellite11', 'instrument10', 'instrument9'}
rigid.direction = {'star3', 'planet16', 'phenomenon19', 'star21', 'planet6', 'planet11', 'phenomenon23', 'planet13', 'planet7', 'phenomenon24', 'phenomenon15', 'phenomenon14', 'phenomenon20', 'planet5', 'star18', 'phenomenon17', 'groundstation2', 'phenomenon9', 'groundstation0', 'groundstation4', 'star8', 'planet12', 'star1', 'star22', 'star10'}
rigid.satellite = {'satellite4', 'satellite6', 'satellite2', 'satellite7', 'satellite1', 'satellite8', 'satellite11', 'satellite3', 'satellite5', 'satellite10', 'satellite0', 'satellite9'}
rigid.instrument = {'instrument4', 'instrument11', 'instrument23', 'instrument20', 'instrument7', 'instrument3', 'instrument1', 'instrument14', 'instrument2', 'instrument6', 'instrument13', 'instrument21', 'instrument16', 'instrument8', 'instrument5', 'instrument12', 'instrument22', 'instrument19', 'instrument15', 'instrument0', 'instrument18', 'instrument17', 'instrument10', 'instrument9'}
rigid.mode = {'image0', 'infrared2', 'image4', 'infrared3', 'thermograph1'}
rigid.supports = set( [('instrument11', 'infrared2'), ('instrument2', 'image0'), ('instrument7', 'infrared3'), ('instrument13', 'image4'), ('instrument23', 'image4'), ('instrument7', 'image0'), ('instrument22', 'thermograph1'), ('instrument6', 'infrared2'), ('instrument10', 'image0'), ('instrument18', 'infrared2'), ('instrument19', 'infrared3'), ('instrument3', 'infrared3'), ('instrument10', 'image4'), ('instrument8', 'image0'), ('instrument1', 'image0'), ('instrument17', 'infrared3'), ('instrument16', 'image0'), ('instrument18', 'thermograph1'), ('instrument5', 'thermograph1'), ('instrument23', 'infrared2'), ('instrument15', 'thermograph1'), ('instrument4', 'infrared2'), ('instrument20', 'infrared2'), ('instrument12', 'image4'), ('instrument8', 'image4'), ('instrument4', 'thermograph1'), ('instrument23', 'thermograph1'), ('instrument21', 'thermograph1'), ('instrument2', 'thermograph1'), ('instrument1', 'infrared2'), ('instrument8', 'infrared2'), ('instrument6', 'image0'), ('instrument0', 'infrared3'), ('instrument16', 'infrared2'), ('instrument3', 'infrared2'), ('instrument14', 'infrared2'), ('instrument15', 'image0'), ('instrument9', 'infrared3'), ('instrument4', 'infrared3'), ('instrument14', 'thermograph1'), ('instrument18', 'image4'), ('instrument21', 'image0'), ] )
rigid.calibration_target = set( [('instrument12', 'groundstation0'), ('instrument11', 'star1'), ('instrument4', 'groundstation2'), ('instrument17', 'groundstation0'), ('instrument19', 'groundstation4'), ('instrument8', 'groundstation4'), ('instrument3', 'groundstation4'), ('instrument18', 'star1'), ('instrument22', 'groundstation0'), ('instrument9', 'star1'), ('instrument23', 'star3'), ('instrument13', 'star1'), ('instrument21', 'star1'), ('instrument20', 'star1'), ('instrument0', 'groundstation0'), ('instrument14', 'groundstation2'), ('instrument10', 'star3'), ('instrument5', 'groundstation4'), ('instrument1', 'star3'), ('instrument15', 'groundstation4'), ('instrument2', 'groundstation0'), ('instrument16', 'star1'), ('instrument7', 'groundstation0'), ('instrument6', 'groundstation2'), ] )
rigid.on_board = set( [('instrument1', 'satellite1'), ('instrument5', 'satellite2'), ('instrument12', 'satellite6'), ('instrument19', 'satellite9'), ('instrument8', 'satellite3'), ('instrument4', 'satellite2'), ('instrument14', 'satellite6'), ('instrument22', 'satellite10'), ('instrument23', 'satellite11'), ('instrument16', 'satellite8'), ('instrument17', 'satellite8'), ('instrument15', 'satellite7'), ('instrument0', 'satellite0'), ('instrument3', 'satellite2'), ('instrument6', 'satellite3'), ('instrument21', 'satellite10'), ('instrument20', 'satellite10'), ('instrument18', 'satellite9'), ('instrument9', 'satellite4'), ('instrument2', 'satellite1'), ('instrument13', 'satellite6'), ('instrument11', 'satellite5'), ('instrument10', 'satellite4'), ('instrument7', 'satellite3'), ] )
state.power_avail = set( [('satellite3',), ('satellite9',), ('satellite10',), ('satellite0',), ('satellite2',), ('satellite1',), ('satellite8',), ('satellite5',), ('satellite6',), ('satellite4',), ('satellite7',), ('satellite11',), ] )
state.pointing = set( [('satellite4', 'star22'), ('satellite10', 'star22'), ('satellite1', 'planet5'), ('satellite2', 'star21'), ('satellite9', 'phenomenon20'), ('satellite3', 'star21'), ('satellite0', 'planet5'), ('satellite8', 'phenomenon23'), ('satellite11', 'star8'), ('satellite5', 'groundstation2'), ('satellite7', 'planet12'), ('satellite6', 'phenomenon20'), ] )
rigid.goal_pointing = set( [('satellite4', 'phenomenon20'), ('satellite1', 'star22'), ('satellite8', 'planet16'), ] )
rigid.goal_have_image = set( [('phenomenon15', 'infrared2'), ('star22', 'image4'), ('phenomenon9', 'image4'), ('planet11', 'image4'), ('planet6', 'image4'), ('planet13', 'infrared3'), ('phenomenon17', 'thermograph1'), ('star21', 'thermograph1'), ('planet5', 'image0'), ('planet16', 'infrared2'), ('planet7', 'image4'), ('phenomenon14', 'infrared2'), ('star10', 'thermograph1'), ('star18', 'image4'), ('phenomenon24', 'infrared3'), ('planet12', 'thermograph1'), ('phenomenon23', 'infrared3'), ] )
state.power_on = set( [] )
state.have_image = set( [] )
state.calibrated = set( [] )

task_list = [('main',)]