from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'camera3', 'objective0', 'low_res', 'rover2store', 'objective2', 'waypoint9', 'objective3', 'waypoint2', 'camera1', 'rover0', 'rover3', 'general', 'waypoint3', 'waypoint5', 'waypoint0', 'rover0store', 'rover3store', 'high_res', 'camera0', 'waypoint6', 'waypoint7', 'waypoint1', 'waypoint8', 'colour', 'camera4', 'rover1store', 'rover2', 'rover1', 'objective1', 'camera2', 'waypoint4'}
rigid.rover = {'rover2', 'rover1', 'rover3', 'rover0'}
rigid.location = {'objective0', 'waypoint6', 'waypoint7', 'waypoint9', 'waypoint1', 'waypoint8', 'objective2', 'objective3', 'waypoint2', 'waypoint3', 'waypoint5', 'waypoint0', 'objective1', 'waypoint4'}
rigid.objective = {'objective3', 'objective0', 'objective1', 'objective2'}
rigid.mode = {'colour', 'low_res', 'high_res'}
rigid.lander = {'general'}
rigid.waypoint = {'waypoint6', 'waypoint7', 'waypoint9', 'waypoint1', 'waypoint8', 'waypoint2', 'waypoint3', 'waypoint5', 'waypoint0', 'waypoint4'}
rigid.camera = {'camera3', 'camera4', 'camera2', 'camera1', 'camera0'}
rigid.store = {'rover2store', 'rover0store', 'rover3store', 'rover1store'}
rigid.visible = set( [('waypoint4', 'waypoint9'), ('waypoint6', 'waypoint0'), ('waypoint5', 'waypoint3'), ('waypoint6', 'waypoint5'), ('waypoint5', 'waypoint6'), ('waypoint2', 'waypoint6'), ('waypoint2', 'waypoint3'), ('waypoint1', 'waypoint6'), ('waypoint0', 'waypoint4'), ('waypoint4', 'waypoint2'), ('waypoint9', 'waypoint2'), ('waypoint7', 'waypoint5'), ('waypoint7', 'waypoint1'), ('waypoint8', 'waypoint6'), ('waypoint3', 'waypoint6'), ('waypoint4', 'waypoint8'), ('waypoint2', 'waypoint9'), ('waypoint6', 'waypoint3'), ('waypoint4', 'waypoint1'), ('waypoint8', 'waypoint9'), ('waypoint9', 'waypoint8'), ('waypoint5', 'waypoint2'), ('waypoint3', 'waypoint9'), ('waypoint1', 'waypoint2'), ('waypoint7', 'waypoint3'), ('waypoint0', 'waypoint6'), ('waypoint0', 'waypoint3'), ('waypoint4', 'waypoint0'), ('waypoint3', 'waypoint2'), ('waypoint9', 'waypoint4'), ('waypoint4', 'waypoint5'), ('waypoint5', 'waypoint1'), ('waypoint6', 'waypoint9'), ('waypoint9', 'waypoint0'), ('waypoint1', 'waypoint8'), ('waypoint2', 'waypoint1'), ('waypoint6', 'waypoint2'), ('waypoint0', 'waypoint9'), ('waypoint8', 'waypoint1'), ('waypoint5', 'waypoint4'), ('waypoint2', 'waypoint4'), ('waypoint4', 'waypoint6'), ('waypoint1', 'waypoint4'), ('waypoint6', 'waypoint8'), ('waypoint1', 'waypoint5'), ('waypoint2', 'waypoint5'), ('waypoint8', 'waypoint4'), ('waypoint6', 'waypoint1'), ('waypoint5', 'waypoint7'), ('waypoint9', 'waypoint6'), ('waypoint9', 'waypoint3'), ('waypoint1', 'waypoint7'), ('waypoint3', 'waypoint5'), ('waypoint3', 'waypoint0'), ('waypoint7', 'waypoint8'), ('waypoint8', 'waypoint7'), ('waypoint3', 'waypoint7'), ('waypoint6', 'waypoint4'), ] )
state.at_rock_sample = set( [('waypoint4',), ('waypoint5',), ('waypoint8',), ('waypoint3',), ('waypoint1',), ] )
state.at_soil_sample = set( [('waypoint4',), ('waypoint6',), ('waypoint3',), ('waypoint9',), ] )
rigid.at_lander = set( [('general', 'waypoint7'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover0', 'waypoint1'), ('rover2', 'waypoint0'), ('rover3', 'waypoint2'), ('rover1', 'waypoint4'), ] )
rigid.available = set( [('rover3',), ('rover0',), ('rover2',), ('rover1',), ] )
rigid.store_of = set( [('rover3store', 'rover3'), ('rover0store', 'rover0'), ('rover1store', 'rover1'), ('rover2store', 'rover2'), ] )
state.empty = set( [('rover0store',), ('rover1store',), ('rover2store',), ('rover3store',), ] )
rigid.equipped_for_soil_analysis = set( [('rover0',), ('rover1',), ] )
rigid.equipped_for_imaging = set( [('rover3',), ('rover0',), ('rover2',), ('rover1',), ] )
rigid.can_traverse = set( [('rover1', 'waypoint5', 'waypoint7'), ('rover3', 'waypoint2', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint6'), ('rover1', 'waypoint4', 'waypoint6'), ('rover1', 'waypoint6', 'waypoint8'), ('rover0', 'waypoint2', 'waypoint3'), ('rover2', 'waypoint0', 'waypoint3'), ('rover2', 'waypoint4', 'waypoint0'), ('rover2', 'waypoint0', 'waypoint6'), ('rover2', 'waypoint3', 'waypoint2'), ('rover2', 'waypoint4', 'waypoint5'), ('rover2', 'waypoint5', 'waypoint4'), ('rover0', 'waypoint0', 'waypoint4'), ('rover2', 'waypoint9', 'waypoint0'), ('rover3', 'waypoint6', 'waypoint8'), ('rover3', 'waypoint1', 'waypoint4'), ('rover1', 'waypoint6', 'waypoint4'), ('rover3', 'waypoint1', 'waypoint5'), ('rover1', 'waypoint4', 'waypoint9'), ('rover2', 'waypoint0', 'waypoint9'), ('rover3', 'waypoint1', 'waypoint7'), ('rover0', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint3', 'waypoint0'), ('rover3', 'waypoint6', 'waypoint0'), ('rover0', 'waypoint1', 'waypoint2'), ('rover1', 'waypoint4', 'waypoint2'), ('rover2', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint7', 'waypoint1'), ('rover1', 'waypoint0', 'waypoint4'), ('rover3', 'waypoint9', 'waypoint2'), ('rover1', 'waypoint7', 'waypoint5'), ('rover0', 'waypoint9', 'waypoint4'), ('rover3', 'waypoint3', 'waypoint6'), ('rover0', 'waypoint4', 'waypoint5'), ('rover0', 'waypoint4', 'waypoint0'), ('rover2', 'waypoint3', 'waypoint0'), ('rover0', 'waypoint3', 'waypoint2'), ('rover3', 'waypoint2', 'waypoint6'), ('rover0', 'waypoint5', 'waypoint4'), ('rover0', 'waypoint1', 'waypoint8'), ('rover3', 'waypoint8', 'waypoint6'), ('rover2', 'waypoint8', 'waypoint4'), ('rover1', 'waypoint8', 'waypoint6'), ('rover0', 'waypoint2', 'waypoint1'), ('rover2', 'waypoint6', 'waypoint0'), ('rover3', 'waypoint6', 'waypoint3'), ('rover0', 'waypoint8', 'waypoint1'), ('rover2', 'waypoint2', 'waypoint3'), ('rover3', 'waypoint0', 'waypoint6'), ('rover0', 'waypoint1', 'waypoint4'), ('rover2', 'waypoint0', 'waypoint4'), ('rover3', 'waypoint2', 'waypoint9'), ('rover1', 'waypoint4', 'waypoint0'), ('rover1', 'waypoint0', 'waypoint3'), ('rover3', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint4', 'waypoint5'), ('rover0', 'waypoint6', 'waypoint1'), ('rover3', 'waypoint1', 'waypoint2'), ('rover1', 'waypoint1', 'waypoint2'), ('rover2', 'waypoint4', 'waypoint8'), ('rover0', 'waypoint8', 'waypoint7'), ('rover3', 'waypoint5', 'waypoint1'), ('rover1', 'waypoint2', 'waypoint1'), ('rover0', 'waypoint7', 'waypoint8'), ('rover2', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint9', 'waypoint4'), ('rover3', 'waypoint6', 'waypoint2'), ('rover1', 'waypoint5', 'waypoint4'), ('rover0', 'waypoint4', 'waypoint9'), ('rover1', 'waypoint2', 'waypoint4'), ] )
rigid.equipped_for_rock_analysis = set( [('rover1',), ] )
rigid.on_board = set( [('camera4', 'rover0'), ('camera1', 'rover2'), ('camera2', 'rover1'), ('camera3', 'rover1'), ('camera0', 'rover3'), ] )
rigid.calibration_target = set( [('camera3', 'objective0'), ('camera4', 'objective3'), ('camera0', 'objective2'), ('camera2', 'objective3'), ('camera1', 'objective3'), ] )
rigid.supports = set( [('camera0', 'colour'), ('camera2', 'low_res'), ('camera1', 'colour'), ('camera0', 'low_res'), ('camera4', 'colour'), ('camera3', 'low_res'), ('camera4', 'low_res'), ('camera3', 'colour'), ] )
rigid.visible_from = set( [('objective2', 'waypoint5'), ('objective2', 'waypoint0'), ('objective1', 'waypoint2'), ('objective3', 'waypoint4'), ('objective2', 'waypoint7'), ('objective3', 'waypoint5'), ('objective3', 'waypoint0'), ('objective0', 'waypoint6'), ('objective0', 'waypoint3'), ('objective1', 'waypoint1'), ('objective2', 'waypoint6'), ('objective2', 'waypoint3'), ('objective1', 'waypoint4'), ('objective3', 'waypoint6'), ('objective1', 'waypoint5'), ('objective3', 'waypoint3'), ('objective1', 'waypoint0'), ('objective0', 'waypoint2'), ('objective2', 'waypoint2'), ('objective0', 'waypoint1'), ('objective3', 'waypoint2'), ('objective1', 'waypoint6'), ('objective1', 'waypoint3'), ('objective2', 'waypoint1'), ('objective2', 'waypoint8'), ('objective0', 'waypoint4'), ('objective0', 'waypoint5'), ('objective0', 'waypoint0'), ('objective3', 'waypoint1'), ('objective2', 'waypoint4'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint6',), ('waypoint3',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint4',), ('waypoint8',), ('waypoint5',), ] )
rigid.goal_communicated_image_data = set( [('objective0', 'low_res'), ('objective2', 'low_res'), ('objective0', 'colour'), ] )
state.have_image = set( [] )
state.full = set( [] )
state.communicated_image_data = set( [] )
state.have_rock_analysis = set( [] )
state.have_soil_analysis = set( [] )
state.communicated_soil_data = set( [] )
state.communicated_rock_data = set( [] )
state.calibrated = set( [] )

task_list = [('achieve_goals',)]
