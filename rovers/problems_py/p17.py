from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.location = {'waypoint11', 'waypoint2', 'waypoint5', 'waypoint7', 'waypoint14', 'waypoint12', 'waypoint6', 'objective1', 'waypoint9', 'objective4', 'waypoint0', 'objective5', 'waypoint3', 'objective3', 'waypoint13', 'objective2', 'waypoint1', 'waypoint10', 'waypoint8', 'waypoint4', 'objective0'}
rigid.objective = {'objective5', 'objective1', 'objective0', 'objective3', 'objective4', 'objective2'}
rigid.object = {'rover5', 'camera2', 'waypoint11', 'waypoint5', 'camera1', 'waypoint14', 'high_res', 'waypoint12', 'colour', 'objective1', 'rover5store', 'camera4', 'waypoint0', 'waypoint3', 'rover2', 'rover0', 'waypoint13', 'objective2', 'camera0', 'camera6', 'waypoint1', 'waypoint10', 'rover2store', 'rover0store', 'rover1store', 'camera5', 'rover3', 'waypoint2', 'waypoint7', 'camera3', 'waypoint6', 'waypoint9', 'objective4', 'low_res', 'rover3store', 'general', 'objective5', 'rover1', 'rover4', 'objective3', 'rover4store', 'waypoint8', 'waypoint4', 'objective0'}
rigid.store = {'rover1store', 'rover4store', 'rover5store', 'rover2store', 'rover0store', 'rover3store'}
rigid.lander = {'general'}
rigid.waypoint = {'waypoint3', 'waypoint11', 'waypoint2', 'waypoint5', 'waypoint7', 'waypoint14', 'waypoint12', 'waypoint13', 'waypoint6', 'waypoint1', 'waypoint10', 'waypoint8', 'waypoint4', 'waypoint0', 'waypoint9'}
rigid.rover = {'rover5', 'rover1', 'rover3', 'rover4', 'rover2', 'rover0'}
rigid.camera = {'camera3', 'camera0', 'camera6', 'camera2', 'camera5', 'camera4', 'camera1'}
rigid.mode = {'colour', 'low_res', 'high_res'}
rigid.visible = set( [('waypoint12', 'waypoint5'), ('waypoint0', 'waypoint3'), ('waypoint7', 'waypoint6'), ('waypoint7', 'waypoint12'), ('waypoint9', 'waypoint8'), ('waypoint13', 'waypoint14'), ('waypoint1', 'waypoint12'), ('waypoint2', 'waypoint4'), ('waypoint3', 'waypoint14'), ('waypoint11', 'waypoint4'), ('waypoint3', 'waypoint13'), ('waypoint1', 'waypoint14'), ('waypoint12', 'waypoint1'), ('waypoint2', 'waypoint14'), ('waypoint5', 'waypoint1'), ('waypoint12', 'waypoint6'), ('waypoint6', 'waypoint12'), ('waypoint5', 'waypoint12'), ('waypoint5', 'waypoint6'), ('waypoint8', 'waypoint2'), ('waypoint6', 'waypoint2'), ('waypoint14', 'waypoint3'), ('waypoint10', 'waypoint0'), ('waypoint11', 'waypoint10'), ('waypoint5', 'waypoint14'), ('waypoint4', 'waypoint11'), ('waypoint9', 'waypoint14'), ('waypoint6', 'waypoint0'), ('waypoint3', 'waypoint6'), ('waypoint7', 'waypoint3'), ('waypoint14', 'waypoint9'), ('waypoint3', 'waypoint2'), ('waypoint11', 'waypoint1'), ('waypoint4', 'waypoint10'), ('waypoint2', 'waypoint6'), ('waypoint10', 'waypoint3'), ('waypoint11', 'waypoint2'), ('waypoint13', 'waypoint0'), ('waypoint7', 'waypoint9'), ('waypoint8', 'waypoint3'), ('waypoint3', 'waypoint0'), ('waypoint14', 'waypoint4'), ('waypoint6', 'waypoint3'), ('waypoint5', 'waypoint3'), ('waypoint4', 'waypoint1'), ('waypoint1', 'waypoint0'), ('waypoint5', 'waypoint2'), ('waypoint4', 'waypoint6'), ('waypoint9', 'waypoint2'), ('waypoint14', 'waypoint13'), ('waypoint8', 'waypoint9'), ('waypoint13', 'waypoint3'), ('waypoint4', 'waypoint14'), ('waypoint12', 'waypoint0'), ('waypoint14', 'waypoint10'), ('waypoint10', 'waypoint4'), ('waypoint14', 'waypoint5'), ('waypoint10', 'waypoint11'), ('waypoint0', 'waypoint13'), ('waypoint2', 'waypoint3'), ('waypoint11', 'waypoint3'), ('waypoint8', 'waypoint11'), ('waypoint0', 'waypoint10'), ('waypoint7', 'waypoint8'), ('waypoint8', 'waypoint7'), ('waypoint14', 'waypoint1'), ('waypoint6', 'waypoint7'), ('waypoint10', 'waypoint8'), ('waypoint11', 'waypoint9'), ('waypoint8', 'waypoint10'), ('waypoint8', 'waypoint5'), ('waypoint6', 'waypoint10'), ('waypoint0', 'waypoint1'), ('waypoint4', 'waypoint2'), ('waypoint6', 'waypoint5'), ('waypoint5', 'waypoint8'), ('waypoint3', 'waypoint11'), ('waypoint0', 'waypoint6'), ('waypoint0', 'waypoint12'), ('waypoint3', 'waypoint7'), ('waypoint1', 'waypoint4'), ('waypoint1', 'waypoint11'), ('waypoint10', 'waypoint6'), ('waypoint2', 'waypoint11'), ('waypoint8', 'waypoint1'), ('waypoint13', 'waypoint5'), ('waypoint10', 'waypoint14'), ('waypoint3', 'waypoint10'), ('waypoint6', 'waypoint4'), ('waypoint3', 'waypoint8'), ('waypoint3', 'waypoint5'), ('waypoint12', 'waypoint7'), ('waypoint1', 'waypoint8'), ('waypoint1', 'waypoint5'), ('waypoint9', 'waypoint11'), ('waypoint2', 'waypoint8'), ('waypoint2', 'waypoint5'), ('waypoint9', 'waypoint7'), ('waypoint2', 'waypoint9'), ('waypoint6', 'waypoint13'), ('waypoint11', 'waypoint8'), ('waypoint5', 'waypoint13'), ('waypoint14', 'waypoint2'), ('waypoint13', 'waypoint6'), ] )
state.at_soil_sample = set( [('waypoint0',), ('waypoint3',), ('waypoint4',), ('waypoint2',), ('waypoint14',), ('waypoint13',), ('waypoint9',), ('waypoint5',), ] )
state.at_rock_sample = set( [('waypoint11',), ('waypoint3',), ('waypoint7',), ('waypoint6',), ('waypoint4',), ('waypoint2',), ('waypoint14',), ('waypoint10',), ('waypoint1',), ('waypoint13',), ('waypoint12',), ('waypoint9',), ('waypoint5',), ] )
rigid.at_lander = set( [('general', 'waypoint13'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover2', 'waypoint5'), ('rover3', 'waypoint13'), ('rover1', 'waypoint12'), ('rover5', 'waypoint8'), ('rover0', 'waypoint12'), ('rover4', 'waypoint1'), ] )
rigid.available = set( [('rover4',), ('rover2',), ('rover1',), ('rover5',), ('rover3',), ('rover0',), ] )
rigid.store_of = set( [('rover2store', 'rover2'), ('rover5store', 'rover5'), ('rover0store', 'rover0'), ('rover3store', 'rover3'), ('rover4store', 'rover4'), ('rover1store', 'rover1'), ] )
state.empty = set( [('rover4store',), ('rover1store',), ('rover5store',), ('rover0store',), ('rover2store',), ('rover3store',), ] )
rigid.equipped_for_rock_analysis = set( [('rover4',), ('rover0',), ('rover5',), ] )
rigid.can_traverse = set( [('rover3', 'waypoint6', 'waypoint13'), ('rover2', 'waypoint11', 'waypoint2'), ('rover4', 'waypoint14', 'waypoint1'), ('rover2', 'waypoint1', 'waypoint5'), ('rover5', 'waypoint11', 'waypoint8'), ('rover2', 'waypoint2', 'waypoint5'), ('rover4', 'waypoint1', 'waypoint8'), ('rover2', 'waypoint2', 'waypoint9'), ('rover3', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint0', 'waypoint3'), ('rover1', 'waypoint7', 'waypoint6'), ('rover1', 'waypoint5', 'waypoint8'), ('rover4', 'waypoint3', 'waypoint0'), ('rover1', 'waypoint12', 'waypoint0'), ('rover5', 'waypoint8', 'waypoint10'), ('rover2', 'waypoint6', 'waypoint5'), ('rover0', 'waypoint7', 'waypoint9'), ('rover5', 'waypoint5', 'waypoint8'), ('rover5', 'waypoint1', 'waypoint12'), ('rover2', 'waypoint9', 'waypoint2'), ('rover1', 'waypoint10', 'waypoint6'), ('rover2', 'waypoint5', 'waypoint8'), ('rover5', 'waypoint9', 'waypoint8'), ('rover1', 'waypoint6', 'waypoint4'), ('rover2', 'waypoint1', 'waypoint4'), ('rover1', 'waypoint1', 'waypoint14'), ('rover4', 'waypoint1', 'waypoint4'), ('rover5', 'waypoint13', 'waypoint5'), ('rover0', 'waypoint12', 'waypoint0'), ('rover2', 'waypoint2', 'waypoint11'), ('rover1', 'waypoint5', 'waypoint12'), ('rover3', 'waypoint0', 'waypoint13'), ('rover5', 'waypoint8', 'waypoint1'), ('rover0', 'waypoint0', 'waypoint12'), ('rover3', 'waypoint11', 'waypoint3'), ('rover3', 'waypoint13', 'waypoint5'), ('rover3', 'waypoint3', 'waypoint8'), ('rover4', 'waypoint0', 'waypoint13'), ('rover2', 'waypoint5', 'waypoint6'), ('rover0', 'waypoint1', 'waypoint11'), ('rover5', 'waypoint2', 'waypoint5'), ('rover4', 'waypoint0', 'waypoint10'), ('rover4', 'waypoint7', 'waypoint8'), ('rover5', 'waypoint5', 'waypoint13'), ('rover2', 'waypoint4', 'waypoint1'), ('rover2', 'waypoint5', 'waypoint14'), ('rover4', 'waypoint8', 'waypoint7'), ('rover4', 'waypoint1', 'waypoint5'), ('rover2', 'waypoint5', 'waypoint13'), ('rover5', 'waypoint3', 'waypoint6'), ('rover1', 'waypoint1', 'waypoint12'), ('rover0', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint11', 'waypoint1'), ('rover3', 'waypoint0', 'waypoint1'), ('rover5', 'waypoint0', 'waypoint3'), ('rover4', 'waypoint4', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint8'), ('rover0', 'waypoint1', 'waypoint5'), ('rover3', 'waypoint12', 'waypoint5'), ('rover3', 'waypoint3', 'waypoint11'), ('rover0', 'waypoint9', 'waypoint7'), ('rover3', 'waypoint3', 'waypoint7'), ('rover3', 'waypoint1', 'waypoint4'), ('rover1', 'waypoint6', 'waypoint12'), ('rover2', 'waypoint7', 'waypoint6'), ('rover4', 'waypoint0', 'waypoint1'), ('rover5', 'waypoint6', 'waypoint3'), ('rover4', 'waypoint4', 'waypoint2'), ('rover3', 'waypoint3', 'waypoint13'), ('rover4', 'waypoint1', 'waypoint12'), ('rover1', 'waypoint3', 'waypoint0'), ('rover4', 'waypoint0', 'waypoint6'), ('rover0', 'waypoint7', 'waypoint12'), ('rover0', 'waypoint0', 'waypoint3'), ('rover2', 'waypoint6', 'waypoint12'), ('rover5', 'waypoint8', 'waypoint3'), ('rover2', 'waypoint13', 'waypoint5'), ('rover5', 'waypoint3', 'waypoint0'), ('rover1', 'waypoint5', 'waypoint2'), ('rover0', 'waypoint1', 'waypoint4'), ('rover4', 'waypoint1', 'waypoint14'), ('rover2', 'waypoint5', 'waypoint1'), ('rover4', 'waypoint5', 'waypoint1'), ('rover1', 'waypoint9', 'waypoint11'), ('rover5', 'waypoint5', 'waypoint2'), ('rover2', 'waypoint1', 'waypoint0'), ('rover2', 'waypoint5', 'waypoint2'), ('rover0', 'waypoint8', 'waypoint1'), ('rover3', 'waypoint2', 'waypoint5'), ('rover1', 'waypoint12', 'waypoint5'), ('rover3', 'waypoint5', 'waypoint14'), ('rover0', 'waypoint12', 'waypoint7'), ('rover3', 'waypoint5', 'waypoint13'), ('rover5', 'waypoint8', 'waypoint9'), ('rover3', 'waypoint13', 'waypoint6'), ('rover0', 'waypoint6', 'waypoint13'), ('rover3', 'waypoint14', 'waypoint5'), ('rover1', 'waypoint0', 'waypoint13'), ('rover1', 'waypoint13', 'waypoint0'), ('rover2', 'waypoint14', 'waypoint5'), ('rover0', 'waypoint13', 'waypoint6'), ('rover4', 'waypoint6', 'waypoint0'), ('rover4', 'waypoint14', 'waypoint9'), ('rover5', 'waypoint12', 'waypoint1'), ('rover2', 'waypoint2', 'waypoint3'), ('rover1', 'waypoint12', 'waypoint6'), ('rover4', 'waypoint0', 'waypoint3'), ('rover5', 'waypoint14', 'waypoint1'), ('rover5', 'waypoint8', 'waypoint11'), ('rover5', 'waypoint7', 'waypoint8'), ('rover5', 'waypoint8', 'waypoint7'), ('rover4', 'waypoint2', 'waypoint4'), ('rover5', 'waypoint1', 'waypoint8'), ('rover3', 'waypoint13', 'waypoint0'), ('rover3', 'waypoint8', 'waypoint3'), ('rover4', 'waypoint11', 'waypoint4'), ('rover0', 'waypoint1', 'waypoint12'), ('rover0', 'waypoint11', 'waypoint1'), ('rover1', 'waypoint4', 'waypoint6'), ('rover3', 'waypoint5', 'waypoint12'), ('rover5', 'waypoint10', 'waypoint8'), ('rover4', 'waypoint8', 'waypoint1'), ('rover0', 'waypoint12', 'waypoint1'), ('rover1', 'waypoint8', 'waypoint5'), ('rover4', 'waypoint12', 'waypoint1'), ('rover2', 'waypoint10', 'waypoint8'), ('rover5', 'waypoint4', 'waypoint1'), ('rover3', 'waypoint1', 'waypoint0'), ('rover3', 'waypoint5', 'waypoint2'), ('rover0', 'waypoint12', 'waypoint6'), ('rover0', 'waypoint6', 'waypoint12'), ('rover1', 'waypoint0', 'waypoint12'), ('rover3', 'waypoint10', 'waypoint0'), ('rover4', 'waypoint1', 'waypoint0'), ('rover5', 'waypoint8', 'waypoint5'), ('rover2', 'waypoint8', 'waypoint10'), ('rover0', 'waypoint5', 'waypoint1'), ('rover0', 'waypoint3', 'waypoint0'), ('rover2', 'waypoint8', 'waypoint5'), ('rover2', 'waypoint0', 'waypoint1'), ('rover5', 'waypoint1', 'waypoint4'), ('rover1', 'waypoint1', 'waypoint11'), ('rover3', 'waypoint13', 'waypoint3'), ('rover4', 'waypoint10', 'waypoint0'), ('rover4', 'waypoint4', 'waypoint11'), ('rover3', 'waypoint7', 'waypoint3'), ('rover4', 'waypoint9', 'waypoint14'), ('rover5', 'waypoint1', 'waypoint14'), ('rover1', 'waypoint6', 'waypoint7'), ('rover1', 'waypoint12', 'waypoint1'), ('rover1', 'waypoint14', 'waypoint1'), ('rover2', 'waypoint3', 'waypoint2'), ('rover5', 'waypoint3', 'waypoint8'), ('rover2', 'waypoint6', 'waypoint7'), ('rover1', 'waypoint2', 'waypoint5'), ('rover3', 'waypoint0', 'waypoint10'), ('rover4', 'waypoint13', 'waypoint0'), ('rover1', 'waypoint6', 'waypoint10'), ('rover1', 'waypoint11', 'waypoint9'), ('rover2', 'waypoint12', 'waypoint6'), ] )
rigid.equipped_for_imaging = set( [('rover4',), ('rover2',), ('rover1',), ('rover5',), ('rover3',), ] )
rigid.equipped_for_soil_analysis = set( [('rover3',), ] )
rigid.on_board = set( [('camera5', 'rover1'), ('camera2', 'rover5'), ('camera0', 'rover4'), ('camera1', 'rover3'), ('camera3', 'rover3'), ('camera6', 'rover2'), ('camera4', 'rover5'), ] )
rigid.calibration_target = set( [('camera3', 'objective5'), ('camera0', 'objective2'), ('camera2', 'objective1'), ('camera5', 'objective0'), ('camera1', 'objective2'), ('camera4', 'objective3'), ('camera6', 'objective5'), ] )
rigid.supports = set( [('camera4', 'low_res'), ('camera0', 'low_res'), ('camera6', 'high_res'), ('camera2', 'high_res'), ('camera4', 'colour'), ('camera6', 'colour'), ('camera1', 'colour'), ('camera5', 'low_res'), ('camera4', 'high_res'), ('camera0', 'high_res'), ('camera3', 'colour'), ('camera2', 'colour'), ] )
rigid.visible_from = set( [('objective2', 'waypoint7'), ('objective2', 'waypoint11'), ('objective5', 'waypoint1'), ('objective3', 'waypoint3'), ('objective2', 'waypoint2'), ('objective3', 'waypoint2'), ('objective2', 'waypoint13'), ('objective2', 'waypoint14'), ('objective0', 'waypoint0'), ('objective4', 'waypoint8'), ('objective4', 'waypoint5'), ('objective4', 'waypoint10'), ('objective4', 'waypoint0'), ('objective3', 'waypoint1'), ('objective4', 'waypoint9'), ('objective2', 'waypoint8'), ('objective2', 'waypoint5'), ('objective2', 'waypoint10'), ('objective3', 'waypoint4'), ('objective2', 'waypoint9'), ('objective2', 'waypoint0'), ('objective3', 'waypoint5'), ('objective1', 'waypoint0'), ('objective3', 'waypoint0'), ('objective5', 'waypoint0'), ('objective0', 'waypoint1'), ('objective4', 'waypoint1'), ('objective4', 'waypoint4'), ('objective0', 'waypoint3'), ('objective4', 'waypoint12'), ('objective4', 'waypoint6'), ('objective4', 'waypoint3'), ('objective0', 'waypoint2'), ('objective4', 'waypoint7'), ('objective4', 'waypoint11'), ('objective2', 'waypoint1'), ('objective2', 'waypoint4'), ('objective1', 'waypoint1'), ('objective2', 'waypoint12'), ('objective2', 'waypoint6'), ('objective2', 'waypoint3'), ('objective4', 'waypoint2'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint14',), ('waypoint2',), ('waypoint5',), ('waypoint3',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint9',), ('waypoint12',), ('waypoint3',), ('waypoint5',), ] )
rigid.goal_communicated_image_data = set( [('objective5', 'colour'), ('objective2', 'low_res'), ('objective3', 'colour'), ('objective2', 'colour'), ('objective4', 'colour'), ] )
state.have_rock_analysis = set( [] )
state.communicated_soil_data = set( [] )
state.full = set( [] )
state.have_soil_analysis = set( [] )
state.communicated_rock_data = set( [] )
state.calibrated = set( [] )
state.communicated_image_data = set( [] )
state.have_image = set( [] )

task_list = [('achieve_goals',)]
