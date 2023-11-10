from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'objective2', 'rover1store', 'waypoint5', 'waypoint3', 'rover0store', 'camera2', 'waypoint4', 'camera0', 'rover2store', 'general', 'rover3', 'rover0', 'waypoint2', 'camera1', 'high_res', 'objective3', 'objective1', 'colour', 'camera3', 'waypoint6', 'low_res', 'waypoint7', 'objective0', 'rover1', 'rover2', 'waypoint1', 'rover3store', 'waypoint0'}
rigid.mode = {'high_res', 'low_res', 'colour'}
rigid.rover = {'rover3', 'rover0', 'rover1', 'rover2'}
rigid.camera = {'camera3', 'camera0', 'camera1', 'camera2'}
rigid.location = {'objective2', 'waypoint2', 'waypoint5', 'waypoint3', 'objective3', 'objective1', 'waypoint6', 'waypoint7', 'waypoint4', 'objective0', 'waypoint1', 'waypoint0'}
rigid.lander = {'general'}
rigid.store = {'rover2store', 'rover1store', 'rover0store', 'rover3store'}
rigid.waypoint = {'waypoint2', 'waypoint5', 'waypoint3', 'waypoint6', 'waypoint7', 'waypoint4', 'waypoint1', 'waypoint0'}
rigid.objective = {'objective1', 'objective3', 'objective0', 'objective2'}
rigid.visible = set( [('waypoint5', 'waypoint2'), ('waypoint5', 'waypoint6'), ('waypoint0', 'waypoint3'), ('waypoint7', 'waypoint0'), ('waypoint3', 'waypoint2'), ('waypoint7', 'waypoint1'), ('waypoint2', 'waypoint7'), ('waypoint2', 'waypoint0'), ('waypoint6', 'waypoint5'), ('waypoint0', 'waypoint2'), ('waypoint7', 'waypoint4'), ('waypoint4', 'waypoint2'), ('waypoint2', 'waypoint4'), ('waypoint7', 'waypoint3'), ('waypoint0', 'waypoint6'), ('waypoint2', 'waypoint3'), ('waypoint4', 'waypoint6'), ('waypoint1', 'waypoint5'), ('waypoint3', 'waypoint5'), ('waypoint7', 'waypoint2'), ('waypoint6', 'waypoint7'), ('waypoint6', 'waypoint0'), ('waypoint0', 'waypoint5'), ('waypoint4', 'waypoint5'), ('waypoint5', 'waypoint1'), ('waypoint5', 'waypoint7'), ('waypoint5', 'waypoint0'), ('waypoint7', 'waypoint6'), ('waypoint6', 'waypoint4'), ('waypoint1', 'waypoint7'), ('waypoint3', 'waypoint7'), ('waypoint1', 'waypoint0'), ('waypoint5', 'waypoint4'), ('waypoint3', 'waypoint0'), ('waypoint5', 'waypoint3'), ('waypoint7', 'waypoint5'), ('waypoint0', 'waypoint7'), ('waypoint2', 'waypoint5'), ('waypoint0', 'waypoint1'), ('waypoint4', 'waypoint7'), ] )
state.at_soil_sample = set( [('waypoint0',), ] )
state.at_rock_sample = set( [('waypoint3',), ('waypoint5',), ('waypoint7',), ('waypoint0',), ('waypoint6',), ('waypoint2',), ] )
rigid.at_lander = set( [('general', 'waypoint2'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover3', 'waypoint7'), ('rover2', 'waypoint7'), ('rover0', 'waypoint4'), ('rover1', 'waypoint4'), ] )
rigid.available = set( [('rover1',), ('rover3',), ('rover0',), ('rover2',), ] )
rigid.store_of = set( [('rover3store', 'rover3'), ('rover2store', 'rover2'), ('rover1store', 'rover1'), ('rover0store', 'rover0'), ] )
state.empty = set( [('rover0store',), ('rover1store',), ('rover3store',), ('rover2store',), ] )
rigid.equipped_for_imaging = set( [('rover3',), ('rover0',), ('rover2',), ] )
rigid.can_traverse = set( [('rover2', 'waypoint7', 'waypoint6'), ('rover2', 'waypoint1', 'waypoint7'), ('rover0', 'waypoint4', 'waypoint2'), ('rover2', 'waypoint3', 'waypoint7'), ('rover3', 'waypoint5', 'waypoint7'), ('rover0', 'waypoint2', 'waypoint4'), ('rover0', 'waypoint6', 'waypoint5'), ('rover2', 'waypoint7', 'waypoint5'), ('rover3', 'waypoint3', 'waypoint7'), ('rover1', 'waypoint3', 'waypoint2'), ('rover0', 'waypoint7', 'waypoint2'), ('rover2', 'waypoint6', 'waypoint7'), ('rover3', 'waypoint7', 'waypoint5'), ('rover3', 'waypoint6', 'waypoint0'), ('rover0', 'waypoint2', 'waypoint3'), ('rover0', 'waypoint1', 'waypoint5'), ('rover1', 'waypoint0', 'waypoint2'), ('rover2', 'waypoint0', 'waypoint7'), ('rover3', 'waypoint1', 'waypoint7'), ('rover0', 'waypoint5', 'waypoint6'), ('rover1', 'waypoint2', 'waypoint7'), ('rover1', 'waypoint4', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint0'), ('rover0', 'waypoint0', 'waypoint5'), ('rover0', 'waypoint5', 'waypoint0'), ('rover0', 'waypoint4', 'waypoint5'), ('rover0', 'waypoint5', 'waypoint1'), ('rover3', 'waypoint0', 'waypoint7'), ('rover1', 'waypoint4', 'waypoint6'), ('rover3', 'waypoint4', 'waypoint7'), ('rover1', 'waypoint1', 'waypoint5'), ('rover1', 'waypoint2', 'waypoint4'), ('rover2', 'waypoint7', 'waypoint0'), ('rover3', 'waypoint7', 'waypoint0'), ('rover3', 'waypoint7', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint3'), ('rover0', 'waypoint5', 'waypoint4'), ('rover1', 'waypoint7', 'waypoint2'), ('rover2', 'waypoint7', 'waypoint1'), ('rover3', 'waypoint7', 'waypoint1'), ('rover1', 'waypoint4', 'waypoint5'), ('rover3', 'waypoint7', 'waypoint4'), ('rover2', 'waypoint2', 'waypoint7'), ('rover2', 'waypoint7', 'waypoint3'), ('rover3', 'waypoint2', 'waypoint7'), ('rover3', 'waypoint7', 'waypoint3'), ('rover1', 'waypoint5', 'waypoint1'), ('rover0', 'waypoint3', 'waypoint2'), ('rover1', 'waypoint6', 'waypoint4'), ('rover2', 'waypoint7', 'waypoint2'), ('rover1', 'waypoint5', 'waypoint4'), ('rover3', 'waypoint0', 'waypoint6'), ('rover2', 'waypoint5', 'waypoint7'), ('rover0', 'waypoint2', 'waypoint7'), ] )
rigid.equipped_for_soil_analysis = set( [('rover1',), ('rover3',), ('rover2',), ] )
rigid.equipped_for_rock_analysis = set( [('rover1',), ('rover3',), ] )
rigid.on_board = set( [('camera2', 'rover0'), ('camera1', 'rover2'), ('camera3', 'rover3'), ('camera0', 'rover3'), ] )
rigid.calibration_target = set( [('camera1', 'objective1'), ('camera0', 'objective2'), ('camera2', 'objective0'), ('camera3', 'objective3'), ] )
rigid.supports = set( [('camera1', 'high_res'), ('camera3', 'high_res'), ('camera0', 'high_res'), ('camera3', 'colour'), ('camera3', 'low_res'), ('camera2', 'low_res'), ] )
rigid.visible_from = set( [('objective3', 'waypoint1'), ('objective2', 'waypoint3'), ('objective2', 'waypoint0'), ('objective3', 'waypoint2'), ('objective2', 'waypoint1'), ('objective0', 'waypoint0'), ('objective0', 'waypoint1'), ('objective3', 'waypoint5'), ('objective1', 'waypoint3'), ('objective1', 'waypoint0'), ('objective2', 'waypoint2'), ('objective3', 'waypoint4'), ('objective3', 'waypoint3'), ('objective1', 'waypoint1'), ('objective2', 'waypoint4'), ('objective1', 'waypoint2'), ('objective3', 'waypoint0'), ('objective0', 'waypoint2'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint0',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint3',), ('waypoint6',), ] )
rigid.goal_communicated_image_data = set( [('objective2', 'low_res'), ('objective3', 'low_res'), ('objective1', 'high_res'), ] )
state.communicated_soil_data = set( [] )
state.full = set( [] )
state.have_image = set( [] )
state.have_rock_analysis = set( [] )
state.calibrated = set( [] )
state.communicated_rock_data = set( [] )
state.have_soil_analysis = set( [] )
state.communicated_image_data = set( [] )

task_list = [('achieve__goals',)]
