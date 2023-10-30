from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'groundstation2', 'instrument1', 'groundstation4', 'phenomenon7', 'phenomenon18', 'thermograph3', 'star10', 'groundstation0', 'star22', 'groundstation3', 'instrument6', 'satellite5', 'phenomenon13', 'star19', 'instrument7', 'satellite0', 'star9', 'instrument8', 'planet21', 'instrument5', 'image1', 'instrument0', 'instrument3', 'instrument2', 'phenomenon11', 'instrument11', 'instrument4', 'planet15', 'planet16', 'satellite2', 'star24', 'thermograph0', 'star20', 'instrument10', 'satellite1', 'thermograph4', 'satellite3', 'groundstation1', 'image2', 'phenomenon6', 'instrument9', 'planet17', 'phenomenon12', 'planet23', 'planet8', 'phenomenon5', 'star14', 'satellite4'}
rigid.direction = {'groundstation2', 'phenomenon11', 'groundstation4', 'planet15', 'planet16', 'phenomenon7', 'phenomenon18', 'star10', 'star24', 'star20', 'groundstation0', 'star22', 'groundstation3', 'phenomenon13', 'groundstation1', 'star19', 'phenomenon6', 'star9', 'planet21', 'planet17', 'phenomenon12', 'planet23', 'planet8', 'phenomenon5', 'star14'}
rigid.mode = {'thermograph4', 'thermograph3', 'image2', 'thermograph0', 'image1'}
rigid.satellite = {'satellite2', 'satellite5', 'satellite4', 'satellite1', 'satellite3', 'satellite0'}
rigid.instrument = {'instrument0', 'instrument3', 'instrument6', 'instrument1', 'instrument11', 'instrument4', 'instrument7', 'instrument9', 'instrument8', 'instrument5', 'instrument10', 'instrument2'}
rigid.supports = set( [('instrument1', 'image2'), ('instrument5', 'thermograph4'), ('instrument10', 'thermograph3'), ('instrument0', 'thermograph0'), ('instrument4', 'thermograph4'), ('instrument7', 'thermograph3'), ('instrument10', 'image1'), ('instrument11', 'image2'), ('instrument8', 'thermograph4'), ('instrument9', 'image2'), ('instrument11', 'thermograph0'), ('instrument9', 'thermograph0'), ('instrument4', 'thermograph0'), ('instrument3', 'thermograph4'), ('instrument2', 'thermograph3'), ('instrument2', 'image1'), ('instrument8', 'thermograph0'), ('instrument7', 'image2'), ('instrument3', 'image2'), ('instrument6', 'thermograph3'), ('instrument3', 'thermograph0'), ('instrument2', 'thermograph4'), ('instrument6', 'image1'), ('instrument1', 'thermograph3'), ('instrument0', 'image1'), ('instrument9', 'image1'), ('instrument4', 'image1'), ] )
rigid.calibration_target = set( [('instrument4', 'groundstation1'), ('instrument7', 'groundstation4'), ('instrument0', 'groundstation2'), ('instrument3', 'groundstation2'), ('instrument2', 'groundstation2'), ('instrument6', 'groundstation0'), ('instrument11', 'groundstation1'), ('instrument10', 'groundstation0'), ('instrument8', 'groundstation2'), ('instrument1', 'groundstation0'), ('instrument5', 'groundstation4'), ('instrument9', 'groundstation2'), ] )
rigid.on_board = set( [('instrument4', 'satellite2'), ('instrument8', 'satellite3'), ('instrument10', 'satellite4'), ('instrument0', 'satellite0'), ('instrument1', 'satellite0'), ('instrument2', 'satellite0'), ('instrument11', 'satellite5'), ('instrument7', 'satellite3'), ('instrument3', 'satellite1'), ('instrument6', 'satellite2'), ('instrument9', 'satellite4'), ('instrument5', 'satellite2'), ] )
state.power_avail = set( [('satellite1',), ('satellite5',), ('satellite4',), ('satellite2',), ('satellite0',), ('satellite3',), ] )
state.pointing = set( [('satellite5', 'phenomenon11'), ('satellite1', 'groundstation1'), ('satellite2', 'groundstation2'), ('satellite3', 'groundstation4'), ('satellite4', 'planet15'), ('satellite0', 'phenomenon12'), ] )
rigid.goal_pointing = set( [('satellite5', 'planet17'), ('satellite2', 'star14'), ('satellite0', 'planet21'), ] )
rigid.goal_have_image = set( [('star19', 'thermograph4'), ('planet21', 'thermograph0'), ('star22', 'thermograph3'), ('planet23', 'image1'), ('phenomenon13', 'image1'), ('planet17', 'image2'), ('star20', 'thermograph4'), ('planet15', 'image2'), ('star14', 'thermograph4'), ('phenomenon12', 'thermograph0'), ('phenomenon5', 'image1'), ('star9', 'thermograph0'), ('planet8', 'image2'), ('phenomenon18', 'image1'), ('phenomenon7', 'thermograph0'), ('star10', 'thermograph3'), ] )
state.power_on = set( [] )
state.have_image = set( [] )
state.calibrated = set( [] )

task_list = [('main',)]
