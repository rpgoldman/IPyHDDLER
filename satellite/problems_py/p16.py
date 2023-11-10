from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'satellite1', 'instrument9', 'star16', 'instrument5', 'planet11', 'instrument12', 'star20', 'instrument11', 'satellite4', 'satellite7', 'instrument16', 'phenomenon18', 'star15', 'satellite6', 'phenomenon5', 'groundstation0', 'instrument15', 'instrument4', 'instrument6', 'planet8', 'satellite8', 'thermograph1', 'star12', 'planet10', 'planet21', 'star24', 'instrument20', 'instrument0', 'planet19', 'phenomenon9', 'planet22', 'instrument17', 'instrument3', 'phenomenon23', 'instrument2', 'instrument18', 'groundstation4', 'star3', 'instrument13', 'satellite5', 'satellite3', 'satellite2', 'instrument22', 'spectrograph3', 'instrument8', 'satellite9', 'planet7', 'groundstation1', 'instrument14', 'satellite0', 'planet6', 'image0', 'instrument19', 'instrument21', 'star2', 'image2', 'star14', 'infrared4', 'star13', 'instrument7', 'phenomenon17', 'instrument10', 'instrument1'}
rigid.mode = {'thermograph1', 'image0', 'image2', 'infrared4', 'spectrograph3'}
rigid.satellite = {'satellite1', 'satellite8', 'satellite5', 'satellite3', 'satellite2', 'satellite9', 'satellite4', 'satellite7', 'satellite6', 'satellite0'}
rigid.direction = {'star3', 'star16', 'planet11', 'star20', 'planet7', 'groundstation1', 'phenomenon18', 'star15', 'phenomenon5', 'groundstation0', 'planet6', 'planet8', 'star12', 'planet10', 'planet21', 'star2', 'star24', 'star14', 'planet19', 'phenomenon9', 'planet22', 'star13', 'phenomenon17', 'phenomenon23', 'groundstation4'}
rigid.instrument = {'instrument9', 'instrument5', 'instrument22', 'instrument8', 'instrument12', 'instrument11', 'instrument16', 'instrument15', 'instrument14', 'instrument4', 'instrument6', 'instrument19', 'instrument21', 'instrument13', 'instrument20', 'instrument0', 'instrument17', 'instrument7', 'instrument3', 'instrument10', 'instrument2', 'instrument1', 'instrument18'}
rigid.supports = set( [('instrument9', 'image2'), ('instrument17', 'image0'), ('instrument5', 'spectrograph3'), ('instrument9', 'thermograph1'), ('instrument12', 'infrared4'), ('instrument2', 'image0'), ('instrument13', 'spectrograph3'), ('instrument0', 'infrared4'), ('instrument21', 'thermograph1'), ('instrument14', 'image0'), ('instrument16', 'image2'), ('instrument17', 'thermograph1'), ('instrument7', 'infrared4'), ('instrument17', 'image2'), ('instrument19', 'infrared4'), ('instrument22', 'thermograph1'), ('instrument2', 'image2'), ('instrument6', 'image0'), ('instrument2', 'thermograph1'), ('instrument3', 'image0'), ('instrument18', 'image2'), ('instrument18', 'thermograph1'), ('instrument14', 'thermograph1'), ('instrument16', 'spectrograph3'), ('instrument12', 'image0'), ('instrument22', 'spectrograph3'), ('instrument3', 'thermograph1'), ('instrument10', 'image0'), ('instrument14', 'spectrograph3'), ('instrument15', 'image0'), ('instrument10', 'image2'), ('instrument11', 'image0'), ('instrument22', 'infrared4'), ('instrument15', 'image2'), ('instrument19', 'thermograph1'), ('instrument20', 'thermograph1'), ('instrument8', 'spectrograph3'), ('instrument15', 'thermograph1'), ('instrument5', 'thermograph1'), ('instrument5', 'image2'), ('instrument9', 'image0'), ('instrument4', 'image2'), ('instrument10', 'spectrograph3'), ('instrument4', 'thermograph1'), ('instrument1', 'spectrograph3'), ] )
rigid.calibration_target = set( [('instrument15', 'groundstation4'), ('instrument18', 'star3'), ('instrument14', 'star3'), ('instrument5', 'groundstation4'), ('instrument22', 'groundstation1'), ('instrument2', 'groundstation1'), ('instrument21', 'star2'), ('instrument6', 'groundstation1'), ('instrument16', 'groundstation0'), ('instrument0', 'star3'), ('instrument7', 'star3'), ('instrument17', 'groundstation4'), ('instrument11', 'star3'), ('instrument4', 'star3'), ('instrument3', 'groundstation4'), ('instrument8', 'groundstation0'), ('instrument10', 'star2'), ('instrument9', 'star3'), ('instrument12', 'groundstation4'), ('instrument19', 'star2'), ('instrument1', 'groundstation0'), ('instrument13', 'star2'), ('instrument20', 'groundstation4'), ] )
rigid.on_board = set( [('instrument13', 'satellite5'), ('instrument11', 'satellite5'), ('instrument8', 'satellite4'), ('instrument22', 'satellite9'), ('instrument2', 'satellite0'), ('instrument10', 'satellite4'), ('instrument5', 'satellite1'), ('instrument17', 'satellite7'), ('instrument21', 'satellite8'), ('instrument4', 'satellite1'), ('instrument16', 'satellite6'), ('instrument18', 'satellite7'), ('instrument14', 'satellite6'), ('instrument0', 'satellite0'), ('instrument9', 'satellite4'), ('instrument1', 'satellite0'), ('instrument7', 'satellite3'), ('instrument12', 'satellite5'), ('instrument3', 'satellite1'), ('instrument19', 'satellite8'), ('instrument20', 'satellite8'), ('instrument15', 'satellite6'), ('instrument6', 'satellite2'), ] )
state.power_avail = set( [('satellite8',), ('satellite1',), ('satellite6',), ('satellite5',), ('satellite2',), ('satellite3',), ('satellite4',), ('satellite7',), ('satellite9',), ('satellite0',), ] )
state.pointing = set( [('satellite9', 'planet11'), ('satellite0', 'star15'), ('satellite6', 'planet11'), ('satellite5', 'planet10'), ('satellite7', 'planet11'), ('satellite2', 'star24'), ('satellite1', 'planet10'), ('satellite4', 'planet19'), ('satellite3', 'phenomenon9'), ('satellite8', 'groundstation4'), ] )
rigid.goal_pointing = set( [('satellite5', 'planet6'), ('satellite9', 'star16'), ('satellite8', 'star15'), ('satellite7', 'star3'), ] )
rigid.goal_have_image = set( [('planet6', 'infrared4'), ('star20', 'image0'), ('star15', 'image0'), ('star14', 'thermograph1'), ('planet7', 'image0'), ('phenomenon17', 'infrared4'), ('star12', 'image0'), ('phenomenon18', 'spectrograph3'), ('planet22', 'image2'), ('planet10', 'image0'), ('planet11', 'infrared4'), ('star13', 'image0'), ('phenomenon23', 'image0'), ('phenomenon9', 'image2'), ('planet8', 'thermograph1'), ('star24', 'infrared4'), ('star16', 'thermograph1'), ('planet21', 'thermograph1'), ('phenomenon5', 'thermograph1'), ] )
state.power_on = set( [] )
state.calibrated = set( [] )
state.have_image = set( [] )

task_list = [('main',)]
