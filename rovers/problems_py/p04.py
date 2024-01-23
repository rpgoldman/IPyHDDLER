from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.location = OrderedSet(['objective0', 'objective1', 'objective2', 'waypoint0', 'waypoint1', 'waypoint2', 'waypoint3'])
rigid.objective = OrderedSet(['objective0', 'objective1', 'objective2'])
rigid.waypoint = OrderedSet(['waypoint0', 'waypoint1', 'waypoint2', 'waypoint3'])
rigid.object = OrderedSet(['general', 'waypoint0', 'waypoint1', 'waypoint2', 'waypoint3', 'rover0', 'rover1', 'rover0store', 'rover1store', 'objective0', 'objective1', 'objective2', 'colour', 'high_res', 'low_res', 'camera0', 'camera1', 'camera2'])
rigid.camera = OrderedSet(['camera0', 'camera1', 'camera2'])
rigid.lander = OrderedSet(['general'])
rigid.mode = OrderedSet(['colour', 'high_res', 'low_res'])
rigid.rover = OrderedSet(['rover0', 'rover1'])
rigid.store = OrderedSet(['rover0store', 'rover1store'])
rigid.visible = OrderedSet( [('waypoint1', 'waypoint0'), ('waypoint0', 'waypoint1'), ('waypoint2', 'waypoint1'), ('waypoint1', 'waypoint2'), ('waypoint2', 'waypoint3'), ('waypoint3', 'waypoint2'), ('waypoint3', 'waypoint1'), ('waypoint1', 'waypoint3'), ] )
state.at_rock_sample = OrderedSet( [('waypoint1',), ('waypoint3',), ] )
state.at_soil_sample = OrderedSet( [('waypoint2',), ('waypoint3',), ] )
rigid.at_lander = OrderedSet( [('general', 'waypoint2'), ] )
rigid.channel_free = OrderedSet( [('general',), ] )
state.at = OrderedSet( [('rover0', 'waypoint3'), ('rover1', 'waypoint2'), ] )
rigid.available = OrderedSet( [('rover0',), ('rover1',), ] )
rigid.store_of = OrderedSet( [('rover0store', 'rover0'), ('rover1store', 'rover1'), ] )
state.empty = OrderedSet( [('rover0store',), ('rover1store',), ] )
rigid.equipped_for_soil_analysis = OrderedSet( [('rover0',), ('rover1',), ] )
rigid.equipped_for_imaging = OrderedSet( [('rover0',), ('rover1',), ] )
rigid.can_traverse = OrderedSet( [('rover0', 'waypoint3', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint3'), ('rover1', 'waypoint2', 'waypoint1'), ('rover1', 'waypoint1', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint3'), ('rover1', 'waypoint3', 'waypoint2'), ('rover1', 'waypoint1', 'waypoint0'), ('rover1', 'waypoint0', 'waypoint1'), ] )
rigid.equipped_for_rock_analysis = OrderedSet( [('rover1',), ] )
rigid.on_board = OrderedSet( [('camera0', 'rover1'), ('camera1', 'rover0'), ('camera2', 'rover0'), ] )
rigid.calibration_target = OrderedSet( [('camera0', 'objective0'), ('camera1', 'objective0'), ('camera2', 'objective1'), ] )
rigid.supports = OrderedSet( [('camera0', 'colour'), ('camera0', 'high_res'), ('camera1', 'colour'), ('camera1', 'low_res'), ('camera2', 'low_res'), ] )
rigid.visible_from = OrderedSet( [('objective0', 'waypoint0'), ('objective0', 'waypoint1'), ('objective0', 'waypoint2'), ('objective0', 'waypoint3'), ('objective1', 'waypoint0'), ('objective1', 'waypoint1'), ('objective2', 'waypoint0'), ('objective2', 'waypoint1'), ('objective2', 'waypoint2'), ] )
rigid.goal_communicated_soil_data = OrderedSet( [('waypoint3',), ] )
rigid.goal_communicated_rock_data = OrderedSet( [('waypoint1',), ] )
rigid.goal_communicated_image_data = OrderedSet( [('objective0', 'high_res'), ] )
state.full = OrderedSet( [] )
state.have_rock_analysis = OrderedSet( [] )
state.have_soil_analysis = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
state.communicated_soil_data = OrderedSet( [] )
state.communicated_rock_data = OrderedSet( [] )
state.communicated_image_data = OrderedSet( [] )

task_list = [('achieve__goals',)]
