from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'low_res', 'waypoint2', 'colour', 'rover0store', 'rover0', 'high_res', 'camera1', 'waypoint1', 'camera0', 'objective1', 'camera2', 'rover1store', 'rover1', 'waypoint3', 'objective0', 'objective2', 'general', 'waypoint0'}
rigid.camera = {'camera2', 'camera1', 'camera0'}
rigid.mode = {'low_res', 'high_res', 'colour'}
rigid.location = {'waypoint2', 'waypoint3', 'waypoint1', 'objective2', 'objective0', 'objective1', 'waypoint0'}
rigid.waypoint = {'waypoint1', 'waypoint2', 'waypoint3', 'waypoint0'}
rigid.lander = {'general'}
rigid.rover = {'rover0', 'rover1'}
rigid.store = {'rover1store', 'rover0store'}
rigid.objective = {'objective2', 'objective0', 'objective1'}
rigid.visible = set( [('waypoint2', 'waypoint0'), ('waypoint2', 'waypoint3'), ('waypoint3', 'waypoint2'), ('waypoint3', 'waypoint1'), ('waypoint1', 'waypoint0'), ('waypoint1', 'waypoint3'), ('waypoint1', 'waypoint2'), ('waypoint2', 'waypoint1'), ('waypoint0', 'waypoint3'), ('waypoint0', 'waypoint2'), ('waypoint3', 'waypoint0'), ('waypoint0', 'waypoint1'), ] )
state.at_rock_sample = set( [('waypoint1',), ('waypoint0',), ] )
state.at_soil_sample = set( [('waypoint1',), ('waypoint3',), ('waypoint2',), ] )
rigid.at_lander = set( [('general', 'waypoint3'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover1', 'waypoint0'), ('rover0', 'waypoint0'), ] )
rigid.available = set( [('rover1',), ('rover0',), ] )
rigid.store_of = set( [('rover0store', 'rover0'), ('rover1store', 'rover1'), ] )
state.empty = set( [('rover0store',), ('rover1store',), ] )
rigid.equipped_for_rock_analysis = set( [('rover0',), ] )
rigid.equipped_for_imaging = set( [('rover1',), ('rover0',), ] )
rigid.can_traverse = set( [('rover1', 'waypoint2', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint0'), ('rover0', 'waypoint0', 'waypoint3'), ('rover1', 'waypoint0', 'waypoint1'), ('rover1', 'waypoint1', 'waypoint0'), ('rover1', 'waypoint1', 'waypoint3'), ('rover1', 'waypoint3', 'waypoint1'), ('rover0', 'waypoint3', 'waypoint0'), ('rover0', 'waypoint0', 'waypoint1'), ('rover1', 'waypoint1', 'waypoint2'), ] )
rigid.equipped_for_soil_analysis = set( [('rover1',), ] )
rigid.on_board = set( [('camera2', 'rover0'), ('camera1', 'rover1'), ('camera0', 'rover1'), ] )
rigid.calibration_target = set( [('camera1', 'objective1'), ('camera2', 'objective1'), ('camera0', 'objective1'), ] )
rigid.supports = set( [('camera2', 'low_res'), ('camera1', 'colour'), ('camera2', 'colour'), ('camera0', 'high_res'), ('camera0', 'low_res'), ('camera1', 'high_res'), ('camera2', 'high_res'), ] )
rigid.visible_from = set( [('objective1', 'waypoint0'), ('objective1', 'waypoint2'), ('objective0', 'waypoint0'), ('objective0', 'waypoint3'), ('objective2', 'waypoint0'), ('objective1', 'waypoint1'), ('objective0', 'waypoint2'), ('objective2', 'waypoint2'), ('objective0', 'waypoint1'), ('objective2', 'waypoint1'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint1',), ('waypoint2',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint1',), ('waypoint0',), ] )
rigid.goal_communicated_image_data = set( [('objective0', 'high_res'), ('objective2', 'high_res'), ('objective0', 'colour'), ] )
state.have_rock_analysis = set( [] )
state.communicated_rock_data = set( [] )
state.have_image = set( [] )
state.have_soil_analysis = set( [] )
state.full = set( [] )
state.communicated_soil_data = set( [] )
state.calibrated = set( [] )
state.communicated_image_data = set( [] )

task_list = [('achieve__goals',)]
