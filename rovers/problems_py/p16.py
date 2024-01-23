from ipyhop import State

from ordered_set import OrderedSet

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.location = OrderedSet(['objective0', 'objective1', 'objective2', 'objective3', 'objective4', 'waypoint0', 'waypoint1', 'waypoint2', 'waypoint3', 'waypoint4', 'waypoint5', 'waypoint6', 'waypoint7', 'waypoint8', 'waypoint9', 'waypoint10', 'waypoint11'])
rigid.objective = OrderedSet(['objective0', 'objective1', 'objective2', 'objective3', 'objective4'])
rigid.waypoint = OrderedSet(['waypoint0', 'waypoint1', 'waypoint2', 'waypoint3', 'waypoint4', 'waypoint5', 'waypoint6', 'waypoint7', 'waypoint8', 'waypoint9', 'waypoint10', 'waypoint11'])
rigid.object = OrderedSet(['general', 'waypoint0', 'waypoint1', 'waypoint2', 'waypoint3', 'waypoint4', 'waypoint5', 'waypoint6', 'waypoint7', 'waypoint8', 'waypoint9', 'waypoint10', 'waypoint11', 'rover0', 'rover1', 'rover2', 'rover3', 'rover0store', 'rover1store', 'rover2store', 'rover3store', 'objective0', 'objective1', 'objective2', 'objective3', 'objective4', 'colour', 'high_res', 'low_res', 'camera0', 'camera1', 'camera2', 'camera3'])
rigid.camera = OrderedSet(['camera0', 'camera1', 'camera2', 'camera3'])
rigid.lander = OrderedSet(['general'])
rigid.mode = OrderedSet(['colour', 'high_res', 'low_res'])
rigid.rover = OrderedSet(['rover0', 'rover1', 'rover2', 'rover3'])
rigid.store = OrderedSet(['rover0store', 'rover1store', 'rover2store', 'rover3store'])
rigid.visible = OrderedSet( [('waypoint0', 'waypoint10'), ('waypoint10', 'waypoint0'), ('waypoint0', 'waypoint11'), ('waypoint11', 'waypoint0'), ('waypoint1', 'waypoint0'), ('waypoint0', 'waypoint1'), ('waypoint1', 'waypoint3'), ('waypoint3', 'waypoint1'), ('waypoint1', 'waypoint10'), ('waypoint10', 'waypoint1'), ('waypoint2', 'waypoint4'), ('waypoint4', 'waypoint2'), ('waypoint2', 'waypoint5'), ('waypoint5', 'waypoint2'), ('waypoint2', 'waypoint9'), ('waypoint9', 'waypoint2'), ('waypoint2', 'waypoint10'), ('waypoint10', 'waypoint2'), ('waypoint3', 'waypoint2'), ('waypoint2', 'waypoint3'), ('waypoint3', 'waypoint4'), ('waypoint4', 'waypoint3'), ('waypoint3', 'waypoint5'), ('waypoint5', 'waypoint3'), ('waypoint3', 'waypoint8'), ('waypoint8', 'waypoint3'), ('waypoint3', 'waypoint9'), ('waypoint9', 'waypoint3'), ('waypoint3', 'waypoint10'), ('waypoint10', 'waypoint3'), ('waypoint4', 'waypoint5'), ('waypoint5', 'waypoint4'), ('waypoint4', 'waypoint7'), ('waypoint7', 'waypoint4'), ('waypoint4', 'waypoint11'), ('waypoint11', 'waypoint4'), ('waypoint6', 'waypoint1'), ('waypoint1', 'waypoint6'), ('waypoint6', 'waypoint2'), ('waypoint2', 'waypoint6'), ('waypoint6', 'waypoint8'), ('waypoint8', 'waypoint6'), ('waypoint7', 'waypoint0'), ('waypoint0', 'waypoint7'), ('waypoint7', 'waypoint5'), ('waypoint5', 'waypoint7'), ('waypoint7', 'waypoint6'), ('waypoint6', 'waypoint7'), ('waypoint7', 'waypoint10'), ('waypoint10', 'waypoint7'), ('waypoint8', 'waypoint0'), ('waypoint0', 'waypoint8'), ('waypoint8', 'waypoint5'), ('waypoint5', 'waypoint8'), ('waypoint8', 'waypoint7'), ('waypoint7', 'waypoint8'), ('waypoint8', 'waypoint10'), ('waypoint10', 'waypoint8'), ('waypoint9', 'waypoint0'), ('waypoint0', 'waypoint9'), ('waypoint9', 'waypoint1'), ('waypoint1', 'waypoint9'), ('waypoint9', 'waypoint4'), ('waypoint4', 'waypoint9'), ('waypoint10', 'waypoint5'), ('waypoint5', 'waypoint10'), ('waypoint10', 'waypoint9'), ('waypoint9', 'waypoint10'), ('waypoint11', 'waypoint7'), ('waypoint7', 'waypoint11'), ('waypoint11', 'waypoint8'), ('waypoint8', 'waypoint11'), ('waypoint11', 'waypoint9'), ('waypoint9', 'waypoint11'), ('waypoint11', 'waypoint10'), ('waypoint10', 'waypoint11'), ] )
state.at_soil_sample = OrderedSet( [('waypoint0',), ('waypoint1',), ('waypoint4',), ('waypoint5',), ('waypoint7',), ('waypoint8',), ('waypoint9',), ('waypoint11',), ] )
state.at_rock_sample = OrderedSet( [('waypoint1',), ('waypoint2',), ('waypoint3',), ('waypoint5',), ('waypoint8',), ('waypoint9',), ('waypoint10',), ('waypoint11',), ] )
rigid.at_lander = OrderedSet( [('general', 'waypoint6'), ] )
rigid.channel_free = OrderedSet( [('general',), ] )
state.at = OrderedSet( [('rover0', 'waypoint6'), ('rover1', 'waypoint2'), ('rover2', 'waypoint9'), ('rover3', 'waypoint0'), ] )
rigid.available = OrderedSet( [('rover0',), ('rover1',), ('rover2',), ('rover3',), ] )
rigid.store_of = OrderedSet( [('rover0store', 'rover0'), ('rover1store', 'rover1'), ('rover2store', 'rover2'), ('rover3store', 'rover3'), ] )
state.empty = OrderedSet( [('rover0store',), ('rover1store',), ('rover2store',), ('rover3store',), ] )
rigid.equipped_for_soil_analysis = OrderedSet( [('rover0',), ('rover1',), ] )
rigid.equipped_for_rock_analysis = OrderedSet( [('rover0',), ('rover1',), ('rover2',), ('rover3',), ] )
rigid.equipped_for_imaging = OrderedSet( [('rover0',), ('rover2',), ] )
rigid.can_traverse = OrderedSet( [('rover0', 'waypoint6', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint6'), ('rover0', 'waypoint6', 'waypoint2'), ('rover0', 'waypoint2', 'waypoint6'), ('rover0', 'waypoint6', 'waypoint7'), ('rover0', 'waypoint7', 'waypoint6'), ('rover0', 'waypoint1', 'waypoint0'), ('rover0', 'waypoint0', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint3'), ('rover0', 'waypoint3', 'waypoint1'), ('rover0', 'waypoint1', 'waypoint9'), ('rover0', 'waypoint9', 'waypoint1'), ('rover0', 'waypoint2', 'waypoint5'), ('rover0', 'waypoint5', 'waypoint2'), ('rover0', 'waypoint7', 'waypoint4'), ('rover0', 'waypoint4', 'waypoint7'), ('rover0', 'waypoint7', 'waypoint8'), ('rover0', 'waypoint8', 'waypoint7'), ('rover0', 'waypoint7', 'waypoint10'), ('rover0', 'waypoint10', 'waypoint7'), ('rover0', 'waypoint7', 'waypoint11'), ('rover0', 'waypoint11', 'waypoint7'), ('rover1', 'waypoint2', 'waypoint3'), ('rover1', 'waypoint3', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint4'), ('rover1', 'waypoint4', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint5'), ('rover1', 'waypoint5', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint6'), ('rover1', 'waypoint6', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint9'), ('rover1', 'waypoint9', 'waypoint2'), ('rover1', 'waypoint2', 'waypoint10'), ('rover1', 'waypoint10', 'waypoint2'), ('rover1', 'waypoint3', 'waypoint1'), ('rover1', 'waypoint1', 'waypoint3'), ('rover1', 'waypoint3', 'waypoint8'), ('rover1', 'waypoint8', 'waypoint3'), ('rover1', 'waypoint4', 'waypoint7'), ('rover1', 'waypoint7', 'waypoint4'), ('rover1', 'waypoint9', 'waypoint11'), ('rover1', 'waypoint11', 'waypoint9'), ('rover1', 'waypoint1', 'waypoint0'), ('rover1', 'waypoint0', 'waypoint1'), ('rover2', 'waypoint9', 'waypoint0'), ('rover2', 'waypoint0', 'waypoint9'), ('rover2', 'waypoint9', 'waypoint1'), ('rover2', 'waypoint1', 'waypoint9'), ('rover2', 'waypoint9', 'waypoint2'), ('rover2', 'waypoint2', 'waypoint9'), ('rover2', 'waypoint9', 'waypoint3'), ('rover2', 'waypoint3', 'waypoint9'), ('rover2', 'waypoint9', 'waypoint4'), ('rover2', 'waypoint4', 'waypoint9'), ('rover2', 'waypoint0', 'waypoint7'), ('rover2', 'waypoint7', 'waypoint0'), ('rover2', 'waypoint0', 'waypoint8'), ('rover2', 'waypoint8', 'waypoint0'), ('rover2', 'waypoint0', 'waypoint10'), ('rover2', 'waypoint10', 'waypoint0'), ('rover2', 'waypoint0', 'waypoint11'), ('rover2', 'waypoint11', 'waypoint0'), ('rover2', 'waypoint2', 'waypoint5'), ('rover2', 'waypoint5', 'waypoint2'), ('rover2', 'waypoint2', 'waypoint6'), ('rover2', 'waypoint6', 'waypoint2'), ('rover3', 'waypoint0', 'waypoint1'), ('rover3', 'waypoint1', 'waypoint0'), ('rover3', 'waypoint0', 'waypoint8'), ('rover3', 'waypoint8', 'waypoint0'), ('rover3', 'waypoint0', 'waypoint9'), ('rover3', 'waypoint9', 'waypoint0'), ('rover3', 'waypoint0', 'waypoint10'), ('rover3', 'waypoint10', 'waypoint0'), ('rover3', 'waypoint0', 'waypoint11'), ('rover3', 'waypoint11', 'waypoint0'), ('rover3', 'waypoint1', 'waypoint3'), ('rover3', 'waypoint3', 'waypoint1'), ('rover3', 'waypoint1', 'waypoint6'), ('rover3', 'waypoint6', 'waypoint1'), ('rover3', 'waypoint9', 'waypoint4'), ('rover3', 'waypoint4', 'waypoint9'), ('rover3', 'waypoint10', 'waypoint2'), ('rover3', 'waypoint2', 'waypoint10'), ('rover3', 'waypoint10', 'waypoint5'), ('rover3', 'waypoint5', 'waypoint10'), ('rover3', 'waypoint10', 'waypoint7'), ('rover3', 'waypoint7', 'waypoint10'), ] )
rigid.on_board = OrderedSet( [('camera0', 'rover2'), ('camera1', 'rover2'), ('camera2', 'rover0'), ('camera3', 'rover2'), ] )
rigid.calibration_target = OrderedSet( [('camera0', 'objective3'), ('camera1', 'objective4'), ('camera2', 'objective2'), ('camera3', 'objective3'), ] )
rigid.supports = OrderedSet( [('camera0', 'low_res'), ('camera1', 'colour'), ('camera2', 'high_res'), ('camera3', 'colour'), ('camera3', 'high_res'), ('camera3', 'low_res'), ] )
rigid.visible_from = OrderedSet( [('objective0', 'waypoint0'), ('objective0', 'waypoint1'), ('objective0', 'waypoint2'), ('objective0', 'waypoint3'), ('objective0', 'waypoint4'), ('objective0', 'waypoint5'), ('objective0', 'waypoint6'), ('objective0', 'waypoint7'), ('objective0', 'waypoint8'), ('objective1', 'waypoint0'), ('objective1', 'waypoint1'), ('objective1', 'waypoint2'), ('objective1', 'waypoint3'), ('objective1', 'waypoint4'), ('objective1', 'waypoint5'), ('objective1', 'waypoint6'), ('objective2', 'waypoint0'), ('objective2', 'waypoint1'), ('objective2', 'waypoint2'), ('objective2', 'waypoint3'), ('objective2', 'waypoint4'), ('objective2', 'waypoint5'), ('objective2', 'waypoint6'), ('objective2', 'waypoint7'), ('objective2', 'waypoint8'), ('objective2', 'waypoint9'), ('objective3', 'waypoint0'), ('objective3', 'waypoint1'), ('objective4', 'waypoint0'), ('objective4', 'waypoint1'), ('objective4', 'waypoint2'), ('objective4', 'waypoint3'), ('objective4', 'waypoint4'), ('objective4', 'waypoint5'), ('objective4', 'waypoint6'), ('objective4', 'waypoint7'), ('objective4', 'waypoint8'), ('objective4', 'waypoint9'), ('objective4', 'waypoint10'), ] )
rigid.goal_communicated_soil_data = OrderedSet( [('waypoint4',), ('waypoint9',), ('waypoint1',), ('waypoint7',), ] )
rigid.goal_communicated_rock_data = OrderedSet( [('waypoint3',), ('waypoint10',), ('waypoint5',), ('waypoint1',), ] )
rigid.goal_communicated_image_data = OrderedSet( [('objective0', 'high_res'), ('objective4', 'high_res'), ('objective2', 'high_res'), ] )
state.full = OrderedSet( [] )
state.have_rock_analysis = OrderedSet( [] )
state.have_soil_analysis = OrderedSet( [] )
state.calibrated = OrderedSet( [] )
state.have_image = OrderedSet( [] )
state.communicated_soil_data = OrderedSet( [] )
state.communicated_rock_data = OrderedSet( [] )
state.communicated_image_data = OrderedSet( [] )

task_list = [('achieve__goals',)]
