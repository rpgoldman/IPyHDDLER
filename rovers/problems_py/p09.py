from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'waypoint0', 'objective1', 'camera1', 'high_res', 'rover3', 'waypoint3', 'waypoint5', 'objective2', 'camera4', 'rover0store', 'rover2', 'camera0', 'low_res', 'waypoint1', 'rover0', 'camera2', 'rover1', 'rover1store', 'camera3', 'rover2store', 'objective0', 'waypoint2', 'waypoint6', 'rover3store', 'colour', 'general', 'waypoint4'}
rigid.rover = {'rover2', 'rover0', 'rover3', 'rover1'}
rigid.location = {'waypoint0', 'waypoint1', 'objective1', 'waypoint5', 'waypoint3', 'objective2', 'objective0', 'waypoint2', 'waypoint6', 'waypoint4'}
rigid.mode = {'high_res', 'colour', 'low_res'}
rigid.waypoint = {'waypoint0', 'waypoint1', 'waypoint5', 'waypoint2', 'waypoint6', 'waypoint4', 'waypoint3'}
rigid.camera = {'camera4', 'camera2', 'camera1', 'camera3', 'camera0'}
rigid.objective = {'objective1', 'objective2', 'objective0'}
rigid.store = {'rover0store', 'rover3store', 'rover2store', 'rover1store'}
rigid.lander = {'general'}
rigid.visible = set( [('waypoint6', 'waypoint3'), ('waypoint5', 'waypoint2'), ('waypoint3', 'waypoint4'), ('waypoint2', 'waypoint5'), ('waypoint2', 'waypoint0'), ('waypoint1', 'waypoint4'), ('waypoint3', 'waypoint0'), ('waypoint5', 'waypoint6'), ('waypoint6', 'waypoint4'), ('waypoint1', 'waypoint5'), ('waypoint1', 'waypoint0'), ('waypoint0', 'waypoint5'), ('waypoint5', 'waypoint1'), ('waypoint6', 'waypoint5'), ('waypoint6', 'waypoint0'), ('waypoint2', 'waypoint1'), ('waypoint5', 'waypoint0'), ('waypoint3', 'waypoint1'), ('waypoint4', 'waypoint1'), ('waypoint1', 'waypoint2'), ('waypoint2', 'waypoint6'), ('waypoint6', 'waypoint1'), ('waypoint0', 'waypoint2'), ('waypoint0', 'waypoint1'), ('waypoint6', 'waypoint2'), ('waypoint3', 'waypoint6'), ('waypoint4', 'waypoint3'), ('waypoint4', 'waypoint6'), ('waypoint1', 'waypoint3'), ('waypoint1', 'waypoint6'), ('waypoint0', 'waypoint3'), ('waypoint0', 'waypoint6'), ] )
state.at_soil_sample = set( [('waypoint4',), ('waypoint6',), ('waypoint1',), ('waypoint5',), ('waypoint0',), ] )
state.at_rock_sample = set( [('waypoint3',), ('waypoint6',), ('waypoint1',), ('waypoint5',), ('waypoint0',), ] )
rigid.at_lander = set( [('general', 'waypoint4'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover3', 'waypoint2'), ('rover0', 'waypoint5'), ('rover2', 'waypoint0'), ('rover1', 'waypoint2'), ] )
rigid.available = set( [('rover2',), ('rover0',), ('rover3',), ('rover1',), ] )
rigid.store_of = set( [('rover0store', 'rover0'), ('rover2store', 'rover2'), ('rover3store', 'rover3'), ('rover1store', 'rover1'), ] )
state.empty = set( [('rover0store',), ('rover1store',), ('rover2store',), ('rover3store',), ] )
rigid.equipped_for_imaging = set( [('rover2',), ('rover0',), ('rover3',), ('rover1',), ] )
rigid.can_traverse = set( [('rover2', 'waypoint6', 'waypoint0'), ('rover0', 'waypoint5', 'waypoint1'), ('rover2', 'waypoint1', 'waypoint5'), ('rover0', 'waypoint5', 'waypoint2'), ('rover2', 'waypoint1', 'waypoint0'), ('rover2', 'waypoint2', 'waypoint1'), ('rover3', 'waypoint2', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint3'), ('rover1', 'waypoint2', 'waypoint1'), ('rover3', 'waypoint6', 'waypoint2'), ('rover0', 'waypoint5', 'waypoint6'), ('rover0', 'waypoint2', 'waypoint5'), ('rover3', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint3', 'waypoint1'), ('rover3', 'waypoint2', 'waypoint6'), ('rover0', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint1', 'waypoint2'), ('rover1', 'waypoint4', 'waypoint1'), ('rover1', 'waypoint0', 'waypoint2'), ('rover0', 'waypoint6', 'waypoint5'), ('rover2', 'waypoint0', 'waypoint1'), ('rover3', 'waypoint0', 'waypoint2'), ('rover1', 'waypoint5', 'waypoint2'), ('rover1', 'waypoint6', 'waypoint2'), ('rover0', 'waypoint1', 'waypoint5'), ('rover1', 'waypoint1', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint6'), ('rover0', 'waypoint0', 'waypoint5'), ('rover2', 'waypoint1', 'waypoint2'), ('rover0', 'waypoint5', 'waypoint0'), ('rover2', 'waypoint5', 'waypoint1'), ('rover2', 'waypoint0', 'waypoint3'), ('rover3', 'waypoint0', 'waypoint3'), ('rover2', 'waypoint0', 'waypoint6'), ('rover2', 'waypoint3', 'waypoint4'), ('rover1', 'waypoint1', 'waypoint3'), ('rover2', 'waypoint4', 'waypoint3'), ('rover3', 'waypoint2', 'waypoint0'), ('rover3', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint3', 'waypoint0'), ('rover2', 'waypoint3', 'waypoint0'), ('rover0', 'waypoint3', 'waypoint1'), ('rover1', 'waypoint2', 'waypoint5'), ('rover1', 'waypoint2', 'waypoint0'), ('rover0', 'waypoint4', 'waypoint1'), ('rover3', 'waypoint0', 'waypoint5'), ('rover1', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint5', 'waypoint0'), ] )
rigid.equipped_for_rock_analysis = set( [('rover1',), ] )
rigid.equipped_for_soil_analysis = set( [('rover2',), ('rover3',), ] )
rigid.on_board = set( [('camera4', 'rover1'), ('camera2', 'rover0'), ('camera3', 'rover2'), ('camera0', 'rover3'), ('camera1', 'rover0'), ] )
rigid.calibration_target = set( [('camera3', 'objective0'), ('camera0', 'objective2'), ('camera1', 'objective2'), ('camera2', 'objective0'), ('camera4', 'objective1'), ] )
rigid.supports = set( [('camera1', 'colour'), ('camera3', 'high_res'), ('camera0', 'colour'), ('camera4', 'colour'), ('camera2', 'low_res'), ('camera3', 'low_res'), ('camera4', 'low_res'), ('camera3', 'colour'), ('camera0', 'low_res'), ] )
rigid.visible_from = set( [('objective2', 'waypoint2'), ('objective2', 'waypoint0'), ('objective2', 'waypoint1'), ('objective0', 'waypoint1'), ('objective1', 'waypoint4'), ('objective1', 'waypoint3'), ('objective0', 'waypoint2'), ('objective2', 'waypoint6'), ('objective1', 'waypoint1'), ('objective0', 'waypoint0'), ('objective1', 'waypoint2'), ('objective2', 'waypoint4'), ('objective1', 'waypoint5'), ('objective2', 'waypoint3'), ('objective1', 'waypoint0'), ('objective2', 'waypoint5'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint4',), ('waypoint0',), ('waypoint6',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint3',), ('waypoint0',), ('waypoint6',), ] )
rigid.goal_communicated_image_data = set( [('objective2', 'low_res'), ('objective2', 'colour'), ] )
state.have_rock_analysis = set( [] )
state.calibrated = set( [] )
state.communicated_soil_data = set( [] )
state.communicated_rock_data = set( [] )
state.communicated_image_data = set( [] )
state.have_soil_analysis = set( [] )
state.full = set( [] )
state.have_image = set( [] )

task_list = [('achieve_goals',)]
