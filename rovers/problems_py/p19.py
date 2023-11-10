from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'rover4store', 'objective3', 'waypoint8', 'waypoint11', 'objective2', 'objective4', 'waypoint7', 'waypoint15', 'rover2', 'objective7', 'low_res', 'rover2store', 'waypoint10', 'objective6', 'camera6', 'waypoint6', 'waypoint0', 'colour', 'rover3', 'rover0', 'waypoint9', 'rover5', 'camera2', 'waypoint19', 'rover5store', 'camera5', 'objective5', 'camera1', 'waypoint13', 'waypoint3', 'waypoint14', 'waypoint18', 'rover0store', 'waypoint17', 'rover1', 'high_res', 'camera0', 'objective1', 'waypoint4', 'general', 'waypoint2', 'objective0', 'rover1store', 'rover3store', 'waypoint12', 'camera3', 'waypoint16', 'camera4', 'waypoint1', 'rover4', 'waypoint5'}
rigid.lander = {'general'}
rigid.rover = {'rover1', 'rover3', 'rover0', 'rover5', 'rover2', 'rover4'}
rigid.location = {'objective3', 'waypoint8', 'waypoint11', 'waypoint13', 'waypoint3', 'waypoint7', 'waypoint15', 'waypoint14', 'waypoint18', 'objective2', 'objective4', 'objective7', 'waypoint17', 'objective1', 'waypoint10', 'objective6', 'waypoint4', 'waypoint6', 'waypoint0', 'waypoint2', 'objective0', 'waypoint9', 'waypoint12', 'waypoint16', 'waypoint19', 'waypoint1', 'objective5', 'waypoint5'}
rigid.objective = {'objective3', 'objective2', 'objective4', 'objective7', 'objective1', 'objective6', 'objective0', 'objective5'}
rigid.store = {'rover2store', 'rover1store', 'rover3store', 'rover4store', 'rover0store', 'rover5store'}
rigid.camera = {'camera0', 'camera4', 'camera2', 'camera3', 'camera5', 'camera6', 'camera1'}
rigid.mode = {'high_res', 'low_res', 'colour'}
rigid.waypoint = {'waypoint8', 'waypoint11', 'waypoint13', 'waypoint3', 'waypoint7', 'waypoint15', 'waypoint14', 'waypoint18', 'waypoint17', 'waypoint10', 'waypoint4', 'waypoint6', 'waypoint0', 'waypoint2', 'waypoint9', 'waypoint12', 'waypoint16', 'waypoint19', 'waypoint1', 'waypoint5'}
rigid.visible = set( [('waypoint14', 'waypoint11'), ('waypoint4', 'waypoint3'), ('waypoint13', 'waypoint7'), ('waypoint12', 'waypoint14'), ('waypoint1', 'waypoint4'), ('waypoint7', 'waypoint0'), ('waypoint16', 'waypoint5'), ('waypoint8', 'waypoint6'), ('waypoint16', 'waypoint18'), ('waypoint5', 'waypoint0'), ('waypoint9', 'waypoint11'), ('waypoint2', 'waypoint4'), ('waypoint12', 'waypoint1'), ('waypoint11', 'waypoint8'), ('waypoint12', 'waypoint7'), ('waypoint12', 'waypoint9'), ('waypoint0', 'waypoint2'), ('waypoint5', 'waypoint12'), ('waypoint7', 'waypoint9'), ('waypoint4', 'waypoint7'), ('waypoint6', 'waypoint0'), ('waypoint18', 'waypoint7'), ('waypoint7', 'waypoint13'), ('waypoint4', 'waypoint17'), ('waypoint9', 'waypoint0'), ('waypoint6', 'waypoint16'), ('waypoint7', 'waypoint11'), ('waypoint19', 'waypoint5'), ('waypoint10', 'waypoint12'), ('waypoint7', 'waypoint8'), ('waypoint14', 'waypoint12'), ('waypoint10', 'waypoint9'), ('waypoint12', 'waypoint4'), ('waypoint8', 'waypoint14'), ('waypoint3', 'waypoint9'), ('waypoint3', 'waypoint10'), ('waypoint14', 'waypoint10'), ('waypoint4', 'waypoint2'), ('waypoint9', 'waypoint1'), ('waypoint9', 'waypoint12'), ('waypoint18', 'waypoint2'), ('waypoint9', 'waypoint7'), ('waypoint11', 'waypoint17'), ('waypoint9', 'waypoint10'), ('waypoint8', 'waypoint7'), ('waypoint5', 'waypoint3'), ('waypoint6', 'waypoint13'), ('waypoint17', 'waypoint5'), ('waypoint17', 'waypoint18'), ('waypoint14', 'waypoint8'), ('waypoint6', 'waypoint15'), ('waypoint16', 'waypoint13'), ('waypoint2', 'waypoint5'), ('waypoint2', 'waypoint18'), ('waypoint16', 'waypoint11'), ('waypoint10', 'waypoint3'), ('waypoint14', 'waypoint3'), ('waypoint8', 'waypoint2'), ('waypoint10', 'waypoint4'), ('waypoint7', 'waypoint12'), ('waypoint19', 'waypoint0'), ('waypoint2', 'waypoint19'), ('waypoint9', 'waypoint3'), ('waypoint9', 'waypoint4'), ('waypoint5', 'waypoint17'), ('waypoint11', 'waypoint5'), ('waypoint0', 'waypoint5'), ('waypoint0', 'waypoint18'), ('waypoint10', 'waypoint14'), ('waypoint18', 'waypoint17'), ('waypoint3', 'waypoint14'), ('waypoint0', 'waypoint19'), ('waypoint15', 'waypoint5'), ('waypoint7', 'waypoint2'), ('waypoint13', 'waypoint5'), ('waypoint3', 'waypoint7'), ('waypoint5', 'waypoint2'), ('waypoint6', 'waypoint1'), ('waypoint0', 'waypoint13'), ('waypoint19', 'waypoint13'), ('waypoint3', 'waypoint17'), ('waypoint14', 'waypoint17'), ('waypoint13', 'waypoint19'), ('waypoint19', 'waypoint11'), ('waypoint7', 'waypoint3'), ('waypoint12', 'waypoint5'), ('waypoint15', 'waypoint11'), ('waypoint7', 'waypoint4'), ('waypoint2', 'waypoint0'), ('waypoint1', 'waypoint16'), ('waypoint16', 'waypoint12'), ('waypoint16', 'waypoint1'), ('waypoint12', 'waypoint19'), ('waypoint10', 'waypoint2'), ('waypoint3', 'waypoint2'), ('waypoint16', 'waypoint6'), ('waypoint6', 'waypoint8'), ('waypoint9', 'waypoint2'), ('waypoint17', 'waypoint11'), ('waypoint2', 'waypoint9'), ('waypoint11', 'waypoint16'), ('waypoint2', 'waypoint10'), ('waypoint3', 'waypoint4'), ('waypoint1', 'waypoint11'), ('waypoint13', 'waypoint0'), ('waypoint19', 'waypoint14'), ('waypoint13', 'waypoint16'), ('waypoint0', 'waypoint9'), ('waypoint11', 'waypoint19'), ('waypoint19', 'waypoint12'), ('waypoint2', 'waypoint8'), ('waypoint0', 'waypoint6'), ('waypoint15', 'waypoint12'), ('waypoint8', 'waypoint18'), ('waypoint12', 'waypoint16'), ('waypoint19', 'waypoint6'), ('waypoint15', 'waypoint6'), ('waypoint2', 'waypoint3'), ('waypoint13', 'waypoint6'), ('waypoint17', 'waypoint14'), ('waypoint5', 'waypoint16'), ('waypoint18', 'waypoint0'), ('waypoint8', 'waypoint11'), ('waypoint11', 'waypoint15'), ('waypoint12', 'waypoint10'), ('waypoint18', 'waypoint16'), ('waypoint19', 'waypoint2'), ('waypoint7', 'waypoint18'), ('waypoint4', 'waypoint1'), ('waypoint4', 'waypoint12'), ('waypoint1', 'waypoint12'), ('waypoint4', 'waypoint9'), ('waypoint1', 'waypoint9'), ('waypoint5', 'waypoint19'), ('waypoint4', 'waypoint10'), ('waypoint18', 'waypoint10'), ('waypoint2', 'waypoint7'), ('waypoint1', 'waypoint6'), ('waypoint5', 'waypoint13'), ('waypoint12', 'waypoint15'), ('waypoint5', 'waypoint11'), ('waypoint11', 'waypoint14'), ('waypoint2', 'waypoint17'), ('waypoint17', 'waypoint2'), ('waypoint10', 'waypoint18'), ('waypoint3', 'waypoint5'), ('waypoint11', 'waypoint1'), ('waypoint11', 'waypoint7'), ('waypoint11', 'waypoint9'), ('waypoint5', 'waypoint15'), ('waypoint0', 'waypoint7'), ('waypoint14', 'waypoint19'), ('waypoint18', 'waypoint8'), ('waypoint17', 'waypoint3'), ('waypoint6', 'waypoint19'), ('waypoint17', 'waypoint4'), ] )
state.at_soil_sample = set( [('waypoint3',), ('waypoint14',), ('waypoint15',), ('waypoint8',), ('waypoint5',), ('waypoint11',), ('waypoint17',), ('waypoint16',), ('waypoint18',), ('waypoint12',), ] )
state.at_rock_sample = set( [('waypoint19',), ('waypoint3',), ('waypoint6',), ('waypoint4',), ('waypoint17',), ('waypoint9',), ] )
rigid.at_lander = set( [('general', 'waypoint6'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover0', 'waypoint2'), ('rover1', 'waypoint6'), ('rover5', 'waypoint12'), ('rover2', 'waypoint13'), ('rover3', 'waypoint11'), ('rover4', 'waypoint0'), ] )
rigid.available = set( [('rover4',), ('rover2',), ('rover3',), ('rover5',), ('rover0',), ('rover1',), ] )
rigid.store_of = set( [('rover1store', 'rover1'), ('rover5store', 'rover5'), ('rover2store', 'rover2'), ('rover4store', 'rover4'), ('rover3store', 'rover3'), ('rover0store', 'rover0'), ] )
state.empty = set( [('rover5store',), ('rover0store',), ('rover1store',), ('rover3store',), ('rover2store',), ('rover4store',), ] )
rigid.equipped_for_imaging = set( [('rover4',), ('rover2',), ('rover3',), ('rover5',), ('rover0',), ('rover1',), ] )
rigid.can_traverse = set( [('rover2', 'waypoint9', 'waypoint0'), ('rover4', 'waypoint1', 'waypoint6'), ('rover1', 'waypoint4', 'waypoint2'), ('rover5', 'waypoint12', 'waypoint5'), ('rover3', 'waypoint5', 'waypoint16'), ('rover0', 'waypoint16', 'waypoint6'), ('rover2', 'waypoint3', 'waypoint5'), ('rover1', 'waypoint13', 'waypoint7'), ('rover2', 'waypoint13', 'waypoint0'), ('rover3', 'waypoint4', 'waypoint1'), ('rover5', 'waypoint7', 'waypoint18'), ('rover3', 'waypoint19', 'waypoint2'), ('rover0', 'waypoint2', 'waypoint5'), ('rover0', 'waypoint2', 'waypoint18'), ('rover1', 'waypoint3', 'waypoint2'), ('rover1', 'waypoint6', 'waypoint8'), ('rover2', 'waypoint13', 'waypoint16'), ('rover2', 'waypoint14', 'waypoint19'), ('rover3', 'waypoint7', 'waypoint18'), ('rover3', 'waypoint6', 'waypoint16'), ('rover5', 'waypoint1', 'waypoint12'), ('rover5', 'waypoint4', 'waypoint12'), ('rover2', 'waypoint9', 'waypoint10'), ('rover3', 'waypoint12', 'waypoint15'), ('rover2', 'waypoint6', 'waypoint13'), ('rover5', 'waypoint2', 'waypoint7'), ('rover5', 'waypoint1', 'waypoint6'), ('rover3', 'waypoint1', 'waypoint11'), ('rover4', 'waypoint4', 'waypoint3'), ('rover3', 'waypoint2', 'waypoint7'), ('rover4', 'waypoint16', 'waypoint5'), ('rover3', 'waypoint7', 'waypoint13'), ('rover5', 'waypoint12', 'waypoint15'), ('rover3', 'waypoint7', 'waypoint11'), ('rover3', 'waypoint11', 'waypoint1'), ('rover5', 'waypoint1', 'waypoint11'), ('rover3', 'waypoint11', 'waypoint9'), ('rover2', 'waypoint12', 'waypoint7'), ('rover2', 'waypoint13', 'waypoint6'), ('rover4', 'waypoint2', 'waypoint8'), ('rover4', 'waypoint6', 'waypoint13'), ('rover2', 'waypoint6', 'waypoint15'), ('rover5', 'waypoint11', 'waypoint1'), ('rover2', 'waypoint18', 'waypoint0'), ('rover0', 'waypoint8', 'waypoint18'), ('rover3', 'waypoint15', 'waypoint12'), ('rover1', 'waypoint0', 'waypoint5'), ('rover0', 'waypoint5', 'waypoint2'), ('rover1', 'waypoint0', 'waypoint18'), ('rover2', 'waypoint7', 'waypoint12'), ('rover4', 'waypoint5', 'waypoint0'), ('rover4', 'waypoint2', 'waypoint3'), ('rover4', 'waypoint14', 'waypoint8'), ('rover5', 'waypoint15', 'waypoint12'), ('rover5', 'waypoint17', 'waypoint4'), ('rover4', 'waypoint5', 'waypoint16'), ('rover4', 'waypoint18', 'waypoint0'), ('rover5', 'waypoint4', 'waypoint3'), ('rover0', 'waypoint0', 'waypoint2'), ('rover5', 'waypoint13', 'waypoint5'), ('rover0', 'waypoint2', 'waypoint0'), ('rover2', 'waypoint0', 'waypoint5'), ('rover2', 'waypoint0', 'waypoint18'), ('rover2', 'waypoint2', 'waypoint7'), ('rover3', 'waypoint14', 'waypoint8'), ('rover5', 'waypoint12', 'waypoint1'), ('rover4', 'waypoint9', 'waypoint3'), ('rover5', 'waypoint12', 'waypoint9'), ('rover5', 'waypoint12', 'waypoint10'), ('rover4', 'waypoint6', 'waypoint0'), ('rover4', 'waypoint17', 'waypoint2'), ('rover2', 'waypoint10', 'waypoint9'), ('rover4', 'waypoint0', 'waypoint5'), ('rover4', 'waypoint0', 'waypoint18'), ('rover1', 'waypoint16', 'waypoint1'), ('rover4', 'waypoint2', 'waypoint7'), ('rover4', 'waypoint18', 'waypoint10'), ('rover1', 'waypoint17', 'waypoint5'), ('rover0', 'waypoint6', 'waypoint16'), ('rover4', 'waypoint3', 'waypoint9'), ('rover2', 'waypoint19', 'waypoint13'), ('rover0', 'waypoint2', 'waypoint9'), ('rover1', 'waypoint10', 'waypoint2'), ('rover3', 'waypoint7', 'waypoint12'), ('rover4', 'waypoint5', 'waypoint11'), ('rover4', 'waypoint2', 'waypoint17'), ('rover1', 'waypoint16', 'waypoint6'), ('rover3', 'waypoint9', 'waypoint0'), ('rover2', 'waypoint7', 'waypoint4'), ('rover3', 'waypoint11', 'waypoint14'), ('rover4', 'waypoint6', 'waypoint1'), ('rover5', 'waypoint4', 'waypoint17'), ('rover5', 'waypoint5', 'waypoint19'), ('rover3', 'waypoint18', 'waypoint7'), ('rover0', 'waypoint13', 'waypoint0'), ('rover1', 'waypoint9', 'waypoint2'), ('rover3', 'waypoint3', 'waypoint7'), ('rover2', 'waypoint13', 'waypoint7'), ('rover4', 'waypoint5', 'waypoint15'), ('rover2', 'waypoint8', 'waypoint6'), ('rover3', 'waypoint11', 'waypoint7'), ('rover2', 'waypoint5', 'waypoint0'), ('rover3', 'waypoint8', 'waypoint14'), ('rover0', 'waypoint9', 'waypoint10'), ('rover2', 'waypoint6', 'waypoint8'), ('rover4', 'waypoint13', 'waypoint6'), ('rover5', 'waypoint12', 'waypoint4'), ('rover1', 'waypoint5', 'waypoint17'), ('rover3', 'waypoint11', 'waypoint17'), ('rover5', 'waypoint9', 'waypoint12'), ('rover2', 'waypoint4', 'waypoint7'), ('rover3', 'waypoint13', 'waypoint7'), ('rover0', 'waypoint18', 'waypoint8'), ('rover3', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint16', 'waypoint5'), ('rover0', 'waypoint2', 'waypoint4'), ('rover1', 'waypoint0', 'waypoint6'), ('rover3', 'waypoint9', 'waypoint11'), ('rover3', 'waypoint7', 'waypoint3'), ('rover5', 'waypoint12', 'waypoint14'), ('rover1', 'waypoint19', 'waypoint6'), ('rover3', 'waypoint12', 'waypoint7'), ('rover1', 'waypoint15', 'waypoint6'), ('rover5', 'waypoint5', 'waypoint0'), ('rover3', 'waypoint16', 'waypoint11'), ('rover5', 'waypoint12', 'waypoint7'), ('rover4', 'waypoint5', 'waypoint12'), ('rover2', 'waypoint18', 'waypoint17'), ('rover4', 'waypoint15', 'waypoint5'), ('rover1', 'waypoint2', 'waypoint0'), ('rover0', 'waypoint6', 'waypoint0'), ('rover1', 'waypoint1', 'waypoint16'), ('rover0', 'waypoint4', 'waypoint1'), ('rover0', 'waypoint4', 'waypoint12'), ('rover2', 'waypoint7', 'waypoint2'), ('rover2', 'waypoint0', 'waypoint13'), ('rover5', 'waypoint7', 'waypoint12'), ('rover0', 'waypoint2', 'waypoint7'), ('rover1', 'waypoint18', 'waypoint0'), ('rover4', 'waypoint8', 'waypoint14'), ('rover4', 'waypoint0', 'waypoint6'), ('rover3', 'waypoint2', 'waypoint19'), ('rover0', 'waypoint0', 'waypoint19'), ('rover0', 'waypoint5', 'waypoint11'), ('rover4', 'waypoint7', 'waypoint2'), ('rover0', 'waypoint15', 'waypoint5'), ('rover4', 'waypoint12', 'waypoint5'), ('rover0', 'waypoint10', 'waypoint9'), ('rover1', 'waypoint6', 'waypoint16'), ('rover2', 'waypoint5', 'waypoint3'), ('rover5', 'waypoint0', 'waypoint5'), ('rover1', 'waypoint2', 'waypoint9'), ('rover1', 'waypoint2', 'waypoint10'), ('rover5', 'waypoint5', 'waypoint13'), ('rover3', 'waypoint10', 'waypoint14'), ('rover5', 'waypoint19', 'waypoint5'), ('rover1', 'waypoint12', 'waypoint15'), ('rover2', 'waypoint16', 'waypoint13'), ('rover0', 'waypoint5', 'waypoint15'), ('rover2', 'waypoint11', 'waypoint16'), ('rover2', 'waypoint17', 'waypoint18'), ('rover0', 'waypoint4', 'waypoint2'), ('rover5', 'waypoint10', 'waypoint12'), ('rover4', 'waypoint3', 'waypoint2'), ('rover0', 'waypoint7', 'waypoint2'), ('rover5', 'waypoint7', 'waypoint8'), ('rover5', 'waypoint14', 'waypoint12'), ('rover0', 'waypoint17', 'waypoint4'), ('rover5', 'waypoint6', 'waypoint1'), ('rover1', 'waypoint7', 'waypoint13'), ('rover3', 'waypoint7', 'waypoint2'), ('rover1', 'waypoint6', 'waypoint19'), ('rover0', 'waypoint4', 'waypoint3'), ('rover0', 'waypoint1', 'waypoint4'), ('rover4', 'waypoint3', 'waypoint4'), ('rover0', 'waypoint18', 'waypoint2'), ('rover1', 'waypoint6', 'waypoint13'), ('rover4', 'waypoint8', 'waypoint2'), ('rover1', 'waypoint15', 'waypoint12'), ('rover5', 'waypoint8', 'waypoint7'), ('rover5', 'waypoint16', 'waypoint12'), ('rover2', 'waypoint19', 'waypoint14'), ('rover3', 'waypoint16', 'waypoint6'), ('rover0', 'waypoint9', 'waypoint2'), ('rover4', 'waypoint11', 'waypoint5'), ('rover1', 'waypoint8', 'waypoint6'), ('rover0', 'waypoint14', 'waypoint3'), ('rover1', 'waypoint5', 'waypoint0'), ('rover0', 'waypoint19', 'waypoint0'), ('rover0', 'waypoint3', 'waypoint4'), ('rover1', 'waypoint2', 'waypoint3'), ('rover2', 'waypoint0', 'waypoint9'), ('rover1', 'waypoint13', 'waypoint6'), ('rover1', 'waypoint2', 'waypoint4'), ('rover3', 'waypoint17', 'waypoint11'), ('rover4', 'waypoint2', 'waypoint19'), ('rover1', 'waypoint6', 'waypoint15'), ('rover3', 'waypoint11', 'waypoint16'), ('rover1', 'waypoint8', 'waypoint11'), ('rover1', 'waypoint11', 'waypoint8'), ('rover1', 'waypoint14', 'waypoint11'), ('rover4', 'waypoint10', 'waypoint18'), ('rover1', 'waypoint0', 'waypoint2'), ('rover0', 'waypoint11', 'waypoint5'), ('rover5', 'waypoint3', 'waypoint4'), ('rover2', 'waypoint15', 'waypoint6'), ('rover0', 'waypoint3', 'waypoint14'), ('rover0', 'waypoint4', 'waypoint17'), ('rover5', 'waypoint5', 'waypoint12'), ('rover1', 'waypoint6', 'waypoint0'), ('rover2', 'waypoint16', 'waypoint1'), ('rover2', 'waypoint13', 'waypoint19'), ('rover0', 'waypoint0', 'waypoint6'), ('rover3', 'waypoint0', 'waypoint9'), ('rover5', 'waypoint18', 'waypoint7'), ('rover0', 'waypoint0', 'waypoint13'), ('rover3', 'waypoint14', 'waypoint10'), ('rover2', 'waypoint1', 'waypoint16'), ('rover0', 'waypoint12', 'waypoint4'), ('rover1', 'waypoint11', 'waypoint14'), ('rover2', 'waypoint16', 'waypoint11'), ('rover5', 'waypoint12', 'waypoint16'), ('rover4', 'waypoint0', 'waypoint2'), ('rover5', 'waypoint7', 'waypoint2'), ('rover3', 'waypoint14', 'waypoint11'), ('rover4', 'waypoint2', 'waypoint0'), ('rover4', 'waypoint19', 'waypoint2'), ('rover2', 'waypoint7', 'waypoint13'), ] )
rigid.equipped_for_soil_analysis = set( [('rover4',), ('rover5',), ('rover3',), ('rover2',), ] )
rigid.equipped_for_rock_analysis = set( [('rover4',), ('rover3',), ('rover5',), ] )
rigid.on_board = set( [('camera1', 'rover1'), ('camera5', 'rover3'), ('camera3', 'rover0'), ('camera2', 'rover1'), ('camera6', 'rover5'), ('camera0', 'rover2'), ('camera4', 'rover4'), ] )
rigid.calibration_target = set( [('camera3', 'objective5'), ('camera0', 'objective0'), ('camera2', 'objective0'), ('camera6', 'objective6'), ('camera1', 'objective1'), ('camera5', 'objective0'), ('camera4', 'objective2'), ] )
rigid.supports = set( [('camera6', 'colour'), ('camera0', 'colour'), ('camera6', 'high_res'), ('camera2', 'low_res'), ('camera6', 'low_res'), ('camera0', 'high_res'), ('camera4', 'low_res'), ('camera2', 'high_res'), ('camera3', 'high_res'), ('camera5', 'low_res'), ('camera4', 'colour'), ('camera5', 'colour'), ('camera1', 'high_res'), ('camera0', 'low_res'), ] )
rigid.visible_from = set( [('objective0', 'waypoint11'), ('objective3', 'waypoint8'), ('objective3', 'waypoint2'), ('objective5', 'waypoint2'), ('objective4', 'waypoint3'), ('objective6', 'waypoint1'), ('objective4', 'waypoint4'), ('objective6', 'waypoint9'), ('objective0', 'waypoint15'), ('objective3', 'waypoint3'), ('objective6', 'waypoint6'), ('objective3', 'waypoint4'), ('objective5', 'waypoint3'), ('objective5', 'waypoint4'), ('objective7', 'waypoint5'), ('objective4', 'waypoint14'), ('objective0', 'waypoint0'), ('objective6', 'waypoint8'), ('objective4', 'waypoint7'), ('objective4', 'waypoint17'), ('objective6', 'waypoint3'), ('objective0', 'waypoint1'), ('objective0', 'waypoint12'), ('objective6', 'waypoint4'), ('objective0', 'waypoint9'), ('objective0', 'waypoint10'), ('objective0', 'waypoint6'), ('objective4', 'waypoint2'), ('objective0', 'waypoint8'), ('objective6', 'waypoint7'), ('objective2', 'waypoint5'), ('objective0', 'waypoint3'), ('objective0', 'waypoint4'), ('objective3', 'waypoint5'), ('objective7', 'waypoint10'), ('objective5', 'waypoint5'), ('objective6', 'waypoint2'), ('objective7', 'waypoint13'), ('objective0', 'waypoint14'), ('objective7', 'waypoint11'), ('objective0', 'waypoint7'), ('objective2', 'waypoint0'), ('objective7', 'waypoint0'), ('objective4', 'waypoint16'), ('objective3', 'waypoint0'), ('objective0', 'waypoint2'), ('objective5', 'waypoint0'), ('objective2', 'waypoint1'), ('objective7', 'waypoint14'), ('objective2', 'waypoint9'), ('objective2', 'waypoint10'), ('objective4', 'waypoint5'), ('objective4', 'waypoint18'), ('objective2', 'waypoint6'), ('objective7', 'waypoint1'), ('objective7', 'waypoint12'), ('objective7', 'waypoint7'), ('objective7', 'waypoint9'), ('objective5', 'waypoint9'), ('objective5', 'waypoint10'), ('objective4', 'waypoint13'), ('objective7', 'waypoint6'), ('objective5', 'waypoint6'), ('objective2', 'waypoint8'), ('objective5', 'waypoint13'), ('objective5', 'waypoint11'), ('objective4', 'waypoint15'), ('objective7', 'waypoint8'), ('objective7', 'waypoint2'), ('objective2', 'waypoint3'), ('objective2', 'waypoint4'), ('objective5', 'waypoint8'), ('objective6', 'waypoint5'), ('objective7', 'waypoint3'), ('objective7', 'waypoint4'), ('objective4', 'waypoint0'), ('objective2', 'waypoint7'), ('objective4', 'waypoint1'), ('objective4', 'waypoint12'), ('objective4', 'waypoint9'), ('objective4', 'waypoint10'), ('objective3', 'waypoint1'), ('objective4', 'waypoint6'), ('objective3', 'waypoint7'), ('objective5', 'waypoint1'), ('objective5', 'waypoint12'), ('objective5', 'waypoint7'), ('objective0', 'waypoint5'), ('objective1', 'waypoint0'), ('objective3', 'waypoint6'), ('objective4', 'waypoint11'), ('objective6', 'waypoint0'), ('objective2', 'waypoint2'), ('objective0', 'waypoint13'), ('objective4', 'waypoint8'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint8',), ('waypoint5',), ('waypoint18',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint19',), ('waypoint3',), ('waypoint6',), ('waypoint4',), ('waypoint17',), ('waypoint9',), ] )
rigid.goal_communicated_image_data = set( [('objective7', 'low_res'), ('objective4', 'high_res'), ('objective0', 'high_res'), ('objective0', 'colour'), ('objective7', 'colour'), ('objective2', 'low_res'), ('objective6', 'low_res'), ('objective5', 'colour'), ] )
state.calibrated = set( [] )
state.have_image = set( [] )
state.communicated_rock_data = set( [] )
state.have_soil_analysis = set( [] )
state.communicated_image_data = set( [] )
state.have_rock_analysis = set( [] )
state.full = set( [] )
state.communicated_soil_data = set( [] )

task_list = [('achieve__goals',)]