from ipyhop import State

state = State( 'init_state' )
rigid = State( 'rigid' )
rigid.object = {'objective2', 'rover7', 'camera4', 'waypoint8', 'objective5', 'waypoint16', 'waypoint24', 'waypoint21', 'camera5', 'rover4store', 'waypoint19', 'rover6store', 'rover2store', 'objective4', 'rover6', 'waypoint18', 'waypoint14', 'rover0', 'waypoint2', 'waypoint23', 'camera1', 'high_res', 'waypoint17', 'objective3', 'colour', 'camera3', 'rover1', 'waypoint20', 'waypoint7', 'waypoint1', 'general', 'camera6', 'rover3store', 'objective6', 'waypoint0', 'rover5', 'rover1store', 'waypoint3', 'waypoint22', 'rover0store', 'waypoint13', 'camera2', 'waypoint4', 'objective7', 'waypoint9', 'rover7store', 'camera0', 'rover3', 'waypoint10', 'waypoint15', 'objective1', 'waypoint6', 'low_res', 'waypoint12', 'rover5store', 'objective0', 'waypoint11', 'rover2', 'waypoint5', 'rover4'}
rigid.mode = {'high_res', 'low_res', 'colour'}
rigid.rover = {'rover5', 'rover0', 'rover7', 'rover1', 'rover2', 'rover4', 'rover3', 'rover6'}
rigid.camera = {'camera4', 'camera1', 'camera2', 'camera5', 'camera6', 'camera0', 'camera3'}
rigid.location = {'objective2', 'waypoint5', 'waypoint8', 'waypoint3', 'waypoint22', 'objective5', 'waypoint16', 'waypoint13', 'waypoint24', 'waypoint21', 'waypoint4', 'objective6', 'objective7', 'waypoint9', 'waypoint19', 'objective4', 'waypoint18', 'waypoint14', 'waypoint2', 'waypoint23', 'waypoint1', 'waypoint10', 'waypoint17', 'waypoint15', 'objective3', 'objective1', 'waypoint6', 'waypoint12', 'objective0', 'waypoint11', 'waypoint20', 'waypoint7', 'waypoint0'}
rigid.lander = {'general'}
rigid.store = {'rover1store', 'rover0store', 'rover5store', 'rover4store', 'rover7store', 'rover6store', 'rover2store', 'rover3store'}
rigid.waypoint = {'waypoint5', 'waypoint8', 'waypoint3', 'waypoint22', 'waypoint16', 'waypoint13', 'waypoint24', 'waypoint21', 'waypoint4', 'waypoint9', 'waypoint19', 'waypoint18', 'waypoint14', 'waypoint2', 'waypoint23', 'waypoint1', 'waypoint10', 'waypoint17', 'waypoint15', 'waypoint6', 'waypoint12', 'waypoint11', 'waypoint20', 'waypoint7', 'waypoint0'}
rigid.objective = {'objective2', 'objective3', 'objective1', 'objective5', 'objective0', 'objective6', 'objective7', 'objective4'}
rigid.visible = set( [('waypoint16', 'waypoint7'), ('waypoint8', 'waypoint11'), ('waypoint17', 'waypoint9'), ('waypoint17', 'waypoint7'), ('waypoint11', 'waypoint8'), ('waypoint23', 'waypoint2'), ('waypoint16', 'waypoint4'), ('waypoint6', 'waypoint21'), ('waypoint24', 'waypoint20'), ('waypoint18', 'waypoint8'), ('waypoint20', 'waypoint4'), ('waypoint5', 'waypoint21'), ('waypoint6', 'waypoint14'), ('waypoint4', 'waypoint20'), ('waypoint15', 'waypoint12'), ('waypoint13', 'waypoint3'), ('waypoint7', 'waypoint16'), ('waypoint5', 'waypoint14'), ('waypoint17', 'waypoint11'), ('waypoint22', 'waypoint16'), ('waypoint6', 'waypoint15'), ('waypoint14', 'waypoint9'), ('waypoint13', 'waypoint20'), ('waypoint12', 'waypoint14'), ('waypoint15', 'waypoint13'), ('waypoint1', 'waypoint14'), ('waypoint6', 'waypoint9'), ('waypoint10', 'waypoint18'), ('waypoint24', 'waypoint5'), ('waypoint9', 'waypoint14'), ('waypoint18', 'waypoint3'), ('waypoint13', 'waypoint12'), ('waypoint1', 'waypoint15'), ('waypoint12', 'waypoint15'), ('waypoint11', 'waypoint22'), ('waypoint6', 'waypoint4'), ('waypoint23', 'waypoint18'), ('waypoint3', 'waypoint18'), ('waypoint6', 'waypoint19'), ('waypoint14', 'waypoint2'), ('waypoint15', 'waypoint1'), ('waypoint11', 'waypoint12'), ('waypoint24', 'waypoint18'), ('waypoint11', 'waypoint21'), ('waypoint6', 'waypoint11'), ('waypoint9', 'waypoint7'), ('waypoint21', 'waypoint6'), ('waypoint14', 'waypoint6'), ('waypoint2', 'waypoint14'), ('waypoint8', 'waypoint4'), ('waypoint15', 'waypoint16'), ('waypoint20', 'waypoint24'), ('waypoint12', 'waypoint19'), ('waypoint9', 'waypoint17'), ('waypoint12', 'waypoint11'), ('waypoint21', 'waypoint5'), ('waypoint14', 'waypoint5'), ('waypoint23', 'waypoint20'), ('waypoint19', 'waypoint4'), ('waypoint4', 'waypoint16'), ('waypoint3', 'waypoint20'), ('waypoint7', 'waypoint9'), ('waypoint16', 'waypoint10'), ('waypoint21', 'waypoint8'), ('waypoint14', 'waypoint8'), ('waypoint8', 'waypoint6'), ('waypoint2', 'waypoint1'), ('waypoint20', 'waypoint3'), ('waypoint19', 'waypoint11'), ('waypoint23', 'waypoint12'), ('waypoint16', 'waypoint20'), ('waypoint7', 'waypoint4'), ('waypoint3', 'waypoint12'), ('waypoint21', 'waypoint18'), ('waypoint7', 'waypoint17'), ('waypoint10', 'waypoint15'), ('waypoint17', 'waypoint20'), ('waypoint16', 'waypoint2'), ('waypoint2', 'waypoint16'), ('waypoint24', 'waypoint12'), ('waypoint12', 'waypoint23'), ('waypoint1', 'waypoint23'), ('waypoint8', 'waypoint5'), ('waypoint14', 'waypoint0'), ('waypoint11', 'waypoint17'), ('waypoint18', 'waypoint1'), ('waypoint19', 'waypoint6'), ('waypoint22', 'waypoint11'), ('waypoint4', 'waypoint21'), ('waypoint0', 'waypoint5'), ('waypoint5', 'waypoint9'), ('waypoint8', 'waypoint18'), ('waypoint16', 'waypoint5'), ('waypoint13', 'waypoint21'), ('waypoint21', 'waypoint22'), ('waypoint14', 'waypoint20'), ('waypoint10', 'waypoint16'), ('waypoint23', 'waypoint1'), ('waypoint4', 'waypoint13'), ('waypoint2', 'waypoint23'), ('waypoint16', 'waypoint8'), ('waypoint5', 'waypoint4'), ('waypoint15', 'waypoint10'), ('waypoint13', 'waypoint14'), ('waypoint0', 'waypoint18'), ('waypoint17', 'waypoint8'), ('waypoint13', 'waypoint15'), ('waypoint14', 'waypoint12'), ('waypoint6', 'waypoint2'), ('waypoint15', 'waypoint17'), ('waypoint4', 'waypoint7'), ('waypoint1', 'waypoint4'), ('waypoint18', 'waypoint21'), ('waypoint5', 'waypoint2'), ('waypoint4', 'waypoint1'), ('waypoint17', 'waypoint18'), ('waypoint5', 'waypoint6'), ('waypoint21', 'waypoint13'), ('waypoint4', 'waypoint19'), ('waypoint7', 'waypoint0'), ('waypoint1', 'waypoint2'), ('waypoint10', 'waypoint23'), ('waypoint20', 'waypoint16'), ('waypoint2', 'waypoint9'), ('waypoint19', 'waypoint20'), ('waypoint6', 'waypoint5'), ('waypoint9', 'waypoint2'), ('waypoint12', 'waypoint6'), ('waypoint16', 'waypoint22'), ('waypoint18', 'waypoint9'), ('waypoint6', 'waypoint8'), ('waypoint11', 'waypoint10'), ('waypoint19', 'waypoint12'), ('waypoint5', 'waypoint8'), ('waypoint24', 'waypoint23'), ('waypoint1', 'waypoint5'), ('waypoint11', 'waypoint19'), ('waypoint6', 'waypoint18'), ('waypoint18', 'waypoint17'), ('waypoint5', 'waypoint24'), ('waypoint0', 'waypoint14'), ('waypoint3', 'waypoint13'), ('waypoint17', 'waypoint21'), ('waypoint3', 'waypoint15'), ('waypoint5', 'waypoint0'), ('waypoint0', 'waypoint15'), ('waypoint12', 'waypoint24'), ('waypoint1', 'waypoint18'), ('waypoint15', 'waypoint0'), ('waypoint20', 'waypoint14'), ('waypoint17', 'waypoint14'), ('waypoint20', 'waypoint13'), ('waypoint10', 'waypoint11'), ('waypoint17', 'waypoint15'), ('waypoint3', 'waypoint1'), ('waypoint0', 'waypoint7'), ('waypoint24', 'waypoint7'), ('waypoint8', 'waypoint16'), ('waypoint7', 'waypoint8'), ('waypoint12', 'waypoint3'), ('waypoint1', 'waypoint3'), ('waypoint18', 'waypoint23'), ('waypoint6', 'waypoint12'), ('waypoint7', 'waypoint24'), ('waypoint12', 'waypoint22'), ('waypoint20', 'waypoint17'), ('waypoint14', 'waypoint13'), ('waypoint20', 'waypoint19'), ('waypoint15', 'waypoint6'), ('waypoint18', 'waypoint24'), ('waypoint13', 'waypoint4'), ('waypoint8', 'waypoint21'), ('waypoint18', 'waypoint0'), ('waypoint9', 'waypoint6'), ('waypoint4', 'waypoint6'), ('waypoint14', 'waypoint1'), ('waypoint8', 'waypoint14'), ('waypoint19', 'waypoint21'), ('waypoint0', 'waypoint23'), ('waypoint18', 'waypoint10'), ('waypoint12', 'waypoint13'), ('waypoint21', 'waypoint4'), ('waypoint21', 'waypoint17'), ('waypoint14', 'waypoint17'), ('waypoint21', 'waypoint19'), ('waypoint9', 'waypoint5'), ('waypoint23', 'waypoint24'), ('waypoint4', 'waypoint5'), ('waypoint5', 'waypoint1'), ('waypoint20', 'waypoint23'), ('waypoint21', 'waypoint11'), ('waypoint2', 'waypoint6'), ('waypoint23', 'waypoint0'), ('waypoint8', 'waypoint7'), ('waypoint22', 'waypoint12'), ('waypoint4', 'waypoint8'), ('waypoint22', 'waypoint21'), ('waypoint11', 'waypoint6'), ('waypoint5', 'waypoint16'), ('waypoint16', 'waypoint15'), ('waypoint9', 'waypoint18'), ('waypoint23', 'waypoint10'), ('waypoint18', 'waypoint6'), ('waypoint8', 'waypoint17'), ('waypoint2', 'waypoint5'), ('waypoint15', 'waypoint3'), ] )
state.at_soil_sample = set( [('waypoint18',), ('waypoint7',), ('waypoint9',), ('waypoint0',), ('waypoint13',), ('waypoint1',), ('waypoint23',), ('waypoint15',), ('waypoint11',), ('waypoint20',), ('waypoint8',), ('waypoint22',), ('waypoint17',), ('waypoint24',), ] )
state.at_rock_sample = set( [('waypoint18',), ('waypoint14',), ('waypoint7',), ('waypoint9',), ('waypoint12',), ('waypoint21',), ('waypoint10',), ('waypoint22',), ('waypoint16',), ] )
rigid.at_lander = set( [('general', 'waypoint1'), ] )
rigid.channel_free = set( [('general',), ] )
state.at = set( [('rover2', 'waypoint3'), ('rover4', 'waypoint16'), ('rover6', 'waypoint4'), ('rover5', 'waypoint10'), ('rover3', 'waypoint3'), ('rover7', 'waypoint16'), ('rover1', 'waypoint4'), ('rover0', 'waypoint22'), ] )
rigid.available = set( [('rover4',), ('rover7',), ('rover6',), ('rover1',), ('rover3',), ('rover0',), ('rover2',), ('rover5',), ] )
rigid.store_of = set( [('rover5store', 'rover5'), ('rover2store', 'rover2'), ('rover4store', 'rover4'), ('rover6store', 'rover6'), ('rover7store', 'rover7'), ('rover3store', 'rover3'), ('rover1store', 'rover1'), ('rover0store', 'rover0'), ] )
state.empty = set( [('rover7store',), ('rover6store',), ('rover3store',), ('rover0store',), ('rover4store',), ('rover5store',), ('rover1store',), ('rover2store',), ] )
rigid.equipped_for_soil_analysis = set( [('rover6',), ('rover3',), ('rover0',), ] )
rigid.equipped_for_imaging = set( [('rover4',), ('rover6',), ('rover1',), ('rover0',), ('rover2',), ('rover5',), ] )
rigid.can_traverse = set( [('rover7', 'waypoint10', 'waypoint16'), ('rover4', 'waypoint14', 'waypoint2'), ('rover0', 'waypoint11', 'waypoint17'), ('rover0', 'waypoint6', 'waypoint14'), ('rover1', 'waypoint13', 'waypoint4'), ('rover4', 'waypoint1', 'waypoint4'), ('rover6', 'waypoint16', 'waypoint10'), ('rover6', 'waypoint20', 'waypoint24'), ('rover6', 'waypoint4', 'waypoint1'), ('rover6', 'waypoint16', 'waypoint4'), ('rover0', 'waypoint0', 'waypoint5'), ('rover0', 'waypoint5', 'waypoint0'), ('rover0', 'waypoint12', 'waypoint24'), ('rover3', 'waypoint4', 'waypoint7'), ('rover6', 'waypoint12', 'waypoint6'), ('rover3', 'waypoint4', 'waypoint1'), ('rover0', 'waypoint14', 'waypoint6'), ('rover6', 'waypoint9', 'waypoint6'), ('rover7', 'waypoint16', 'waypoint20'), ('rover3', 'waypoint12', 'waypoint22'), ('rover5', 'waypoint1', 'waypoint15'), ('rover7', 'waypoint12', 'waypoint6'), ('rover2', 'waypoint5', 'waypoint8'), ('rover2', 'waypoint1', 'waypoint5'), ('rover3', 'waypoint16', 'waypoint20'), ('rover2', 'waypoint21', 'waypoint11'), ('rover3', 'waypoint22', 'waypoint12'), ('rover3', 'waypoint1', 'waypoint15'), ('rover7', 'waypoint16', 'waypoint8'), ('rover0', 'waypoint9', 'waypoint6'), ('rover2', 'waypoint6', 'waypoint18'), ('rover0', 'waypoint17', 'waypoint11'), ('rover0', 'waypoint3', 'waypoint13'), ('rover6', 'waypoint1', 'waypoint3'), ('rover0', 'waypoint11', 'waypoint19'), ('rover5', 'waypoint12', 'waypoint11'), ('rover7', 'waypoint8', 'waypoint16'), ('rover7', 'waypoint6', 'waypoint12'), ('rover4', 'waypoint9', 'waypoint2'), ('rover2', 'waypoint13', 'waypoint3'), ('rover1', 'waypoint5', 'waypoint9'), ('rover3', 'waypoint6', 'waypoint12'), ('rover2', 'waypoint12', 'waypoint14'), ('rover4', 'waypoint16', 'waypoint2'), ('rover0', 'waypoint12', 'waypoint22'), ('rover6', 'waypoint23', 'waypoint0'), ('rover0', 'waypoint20', 'waypoint17'), ('rover7', 'waypoint2', 'waypoint6'), ('rover1', 'waypoint19', 'waypoint4'), ('rover3', 'waypoint15', 'waypoint1'), ('rover7', 'waypoint2', 'waypoint5'), ('rover0', 'waypoint12', 'waypoint13'), ('rover5', 'waypoint5', 'waypoint6'), ('rover6', 'waypoint6', 'waypoint12'), ('rover3', 'waypoint1', 'waypoint4'), ('rover1', 'waypoint4', 'waypoint21'), ('rover0', 'waypoint22', 'waypoint21'), ('rover6', 'waypoint7', 'waypoint16'), ('rover6', 'waypoint16', 'waypoint22'), ('rover2', 'waypoint10', 'waypoint15'), ('rover3', 'waypoint1', 'waypoint2'), ('rover1', 'waypoint5', 'waypoint0'), ('rover1', 'waypoint4', 'waypoint1'), ('rover2', 'waypoint13', 'waypoint21'), ('rover0', 'waypoint5', 'waypoint21'), ('rover2', 'waypoint4', 'waypoint13'), ('rover6', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint3', 'waypoint1'), ('rover6', 'waypoint8', 'waypoint17'), ('rover5', 'waypoint10', 'waypoint23'), ('rover1', 'waypoint16', 'waypoint4'), ('rover7', 'waypoint21', 'waypoint5'), ('rover4', 'waypoint15', 'waypoint3'), ('rover1', 'waypoint12', 'waypoint6'), ('rover4', 'waypoint17', 'waypoint7'), ('rover6', 'waypoint6', 'waypoint21'), ('rover7', 'waypoint18', 'waypoint8'), ('rover1', 'waypoint3', 'waypoint13'), ('rover5', 'waypoint6', 'waypoint5'), ('rover5', 'waypoint16', 'waypoint2'), ('rover4', 'waypoint4', 'waypoint20'), ('rover1', 'waypoint24', 'waypoint5'), ('rover0', 'waypoint15', 'waypoint16'), ('rover3', 'waypoint20', 'waypoint3'), ('rover0', 'waypoint19', 'waypoint11'), ('rover3', 'waypoint18', 'waypoint17'), ('rover5', 'waypoint23', 'waypoint10'), ('rover4', 'waypoint6', 'waypoint15'), ('rover3', 'waypoint1', 'waypoint5'), ('rover6', 'waypoint6', 'waypoint4'), ('rover2', 'waypoint21', 'waypoint22'), ('rover4', 'waypoint20', 'waypoint23'), ('rover2', 'waypoint3', 'waypoint1'), ('rover1', 'waypoint6', 'waypoint12'), ('rover0', 'waypoint4', 'waypoint21'), ('rover2', 'waypoint18', 'waypoint23'), ('rover1', 'waypoint18', 'waypoint10'), ('rover4', 'waypoint23', 'waypoint20'), ('rover2', 'waypoint17', 'waypoint18'), ('rover2', 'waypoint21', 'waypoint13'), ('rover1', 'waypoint9', 'waypoint5'), ('rover6', 'waypoint1', 'waypoint5'), ('rover5', 'waypoint24', 'waypoint23'), ('rover5', 'waypoint23', 'waypoint24'), ('rover2', 'waypoint14', 'waypoint1'), ('rover4', 'waypoint2', 'waypoint16'), ('rover5', 'waypoint11', 'waypoint12'), ('rover6', 'waypoint1', 'waypoint18'), ('rover7', 'waypoint8', 'waypoint7'), ('rover4', 'waypoint4', 'waypoint13'), ('rover5', 'waypoint23', 'waypoint20'), ('rover1', 'waypoint20', 'waypoint17'), ('rover4', 'waypoint11', 'waypoint8'), ('rover1', 'waypoint16', 'waypoint22'), ('rover0', 'waypoint6', 'waypoint9'), ('rover4', 'waypoint21', 'waypoint5'), ('rover7', 'waypoint9', 'waypoint2'), ('rover1', 'waypoint1', 'waypoint15'), ('rover5', 'waypoint22', 'waypoint11'), ('rover3', 'waypoint13', 'waypoint3'), ('rover4', 'waypoint19', 'waypoint21'), ('rover2', 'waypoint1', 'waypoint14'), ('rover1', 'waypoint6', 'waypoint4'), ('rover7', 'waypoint0', 'waypoint14'), ('rover1', 'waypoint5', 'waypoint4'), ('rover2', 'waypoint18', 'waypoint3'), ('rover5', 'waypoint15', 'waypoint1'), ('rover5', 'waypoint11', 'waypoint21'), ('rover4', 'waypoint5', 'waypoint24'), ('rover5', 'waypoint6', 'waypoint19'), ('rover5', 'waypoint6', 'waypoint11'), ('rover7', 'waypoint23', 'waypoint2'), ('rover0', 'waypoint22', 'waypoint12'), ('rover5', 'waypoint2', 'waypoint16'), ('rover4', 'waypoint22', 'waypoint16'), ('rover1', 'waypoint5', 'waypoint24'), ('rover3', 'waypoint7', 'waypoint4'), ('rover3', 'waypoint3', 'waypoint12'), ('rover6', 'waypoint4', 'waypoint6'), ('rover6', 'waypoint0', 'waypoint23'), ('rover2', 'waypoint0', 'waypoint5'), ('rover1', 'waypoint1', 'waypoint4'), ('rover3', 'waypoint13', 'waypoint21'), ('rover6', 'waypoint4', 'waypoint8'), ('rover0', 'waypoint21', 'waypoint4'), ('rover0', 'waypoint23', 'waypoint24'), ('rover2', 'waypoint24', 'waypoint18'), ('rover3', 'waypoint4', 'waypoint8'), ('rover7', 'waypoint4', 'waypoint16'), ('rover4', 'waypoint5', 'waypoint16'), ('rover0', 'waypoint1', 'waypoint15'), ('rover4', 'waypoint16', 'waypoint7'), ('rover3', 'waypoint12', 'waypoint3'), ('rover2', 'waypoint20', 'waypoint16'), ('rover3', 'waypoint6', 'waypoint11'), ('rover0', 'waypoint15', 'waypoint1'), ('rover1', 'waypoint5', 'waypoint8'), ('rover7', 'waypoint10', 'waypoint15'), ('rover4', 'waypoint20', 'waypoint4'), ('rover7', 'waypoint2', 'waypoint16'), ('rover2', 'waypoint7', 'waypoint4'), ('rover3', 'waypoint18', 'waypoint9'), ('rover6', 'waypoint6', 'waypoint15'), ('rover3', 'waypoint19', 'waypoint12'), ('rover5', 'waypoint11', 'waypoint6'), ('rover5', 'waypoint15', 'waypoint0'), ('rover3', 'waypoint24', 'waypoint12'), ('rover6', 'waypoint2', 'waypoint6'), ('rover5', 'waypoint17', 'waypoint15'), ('rover7', 'waypoint4', 'waypoint13'), ('rover4', 'waypoint21', 'waypoint19'), ('rover7', 'waypoint7', 'waypoint8'), ('rover7', 'waypoint17', 'waypoint8'), ('rover5', 'waypoint11', 'waypoint8'), ('rover6', 'waypoint6', 'waypoint11'), ('rover2', 'waypoint15', 'waypoint10'), ('rover6', 'waypoint21', 'waypoint6'), ('rover3', 'waypoint11', 'waypoint6'), ('rover2', 'waypoint14', 'waypoint12'), ('rover2', 'waypoint1', 'waypoint3'), ('rover7', 'waypoint6', 'waypoint2'), ('rover7', 'waypoint5', 'waypoint2'), ('rover0', 'waypoint2', 'waypoint6'), ('rover3', 'waypoint17', 'waypoint18'), ('rover7', 'waypoint20', 'waypoint3'), ('rover7', 'waypoint14', 'waypoint1'), ('rover2', 'waypoint13', 'waypoint4'), ('rover5', 'waypoint10', 'waypoint18'), ('rover6', 'waypoint14', 'waypoint1'), ('rover5', 'waypoint18', 'waypoint3'), ('rover5', 'waypoint11', 'waypoint22'), ('rover0', 'waypoint21', 'waypoint5'), ('rover2', 'waypoint18', 'waypoint9'), ('rover3', 'waypoint18', 'waypoint0'), ('rover1', 'waypoint1', 'waypoint18'), ('rover4', 'waypoint15', 'waypoint12'), ('rover0', 'waypoint6', 'waypoint11'), ('rover5', 'waypoint21', 'waypoint11'), ('rover3', 'waypoint14', 'waypoint1'), ('rover2', 'waypoint8', 'waypoint5'), ('rover6', 'waypoint11', 'waypoint6'), ('rover0', 'waypoint21', 'waypoint18'), ('rover3', 'waypoint1', 'waypoint14'), ('rover2', 'waypoint18', 'waypoint6'), ('rover1', 'waypoint4', 'waypoint20'), ('rover5', 'waypoint16', 'waypoint7'), ('rover4', 'waypoint8', 'waypoint18'), ('rover6', 'waypoint6', 'waypoint2'), ('rover4', 'waypoint2', 'waypoint14'), ('rover0', 'waypoint21', 'waypoint22'), ('rover7', 'waypoint4', 'waypoint19'), ('rover1', 'waypoint4', 'waypoint6'), ('rover6', 'waypoint4', 'waypoint19'), ('rover6', 'waypoint22', 'waypoint16'), ('rover1', 'waypoint21', 'waypoint4'), ('rover4', 'waypoint13', 'waypoint4'), ('rover2', 'waypoint20', 'waypoint19'), ('rover4', 'waypoint4', 'waypoint16'), ('rover1', 'waypoint4', 'waypoint5'), ('rover3', 'waypoint21', 'waypoint13'), ('rover0', 'waypoint6', 'waypoint2'), ('rover7', 'waypoint1', 'waypoint14'), ('rover3', 'waypoint1', 'waypoint23'), ('rover3', 'waypoint18', 'waypoint3'), ('rover1', 'waypoint6', 'waypoint11'), ('rover5', 'waypoint13', 'waypoint15'), ('rover2', 'waypoint5', 'waypoint1'), ('rover6', 'waypoint3', 'waypoint1'), ('rover4', 'waypoint3', 'waypoint15'), ('rover3', 'waypoint10', 'waypoint16'), ('rover3', 'waypoint3', 'waypoint18'), ('rover5', 'waypoint4', 'waypoint16'), ('rover2', 'waypoint3', 'waypoint20'), ('rover5', 'waypoint10', 'waypoint15'), ('rover7', 'waypoint14', 'waypoint0'), ('rover3', 'waypoint8', 'waypoint4'), ('rover4', 'waypoint7', 'waypoint16'), ('rover1', 'waypoint23', 'waypoint18'), ('rover1', 'waypoint4', 'waypoint13'), ('rover3', 'waypoint12', 'waypoint6'), ('rover1', 'waypoint15', 'waypoint1'), ('rover3', 'waypoint3', 'waypoint13'), ('rover5', 'waypoint10', 'waypoint11'), ('rover5', 'waypoint15', 'waypoint10'), ('rover1', 'waypoint2', 'waypoint5'), ('rover0', 'waypoint15', 'waypoint12'), ('rover0', 'waypoint13', 'waypoint3'), ('rover2', 'waypoint3', 'waypoint18'), ('rover3', 'waypoint23', 'waypoint1'), ('rover4', 'waypoint12', 'waypoint15'), ('rover1', 'waypoint5', 'waypoint2'), ('rover6', 'waypoint16', 'waypoint7'), ('rover7', 'waypoint20', 'waypoint24'), ('rover6', 'waypoint8', 'waypoint4'), ('rover4', 'waypoint16', 'waypoint15'), ('rover2', 'waypoint4', 'waypoint7'), ('rover0', 'waypoint13', 'waypoint12'), ('rover0', 'waypoint24', 'waypoint23'), ('rover3', 'waypoint1', 'waypoint3'), ('rover5', 'waypoint11', 'waypoint10'), ('rover2', 'waypoint19', 'waypoint20'), ('rover4', 'waypoint7', 'waypoint17'), ('rover4', 'waypoint8', 'waypoint11'), ('rover6', 'waypoint4', 'waypoint20'), ('rover0', 'waypoint8', 'waypoint7'), ('rover4', 'waypoint15', 'waypoint6'), ('rover3', 'waypoint2', 'waypoint1'), ('rover5', 'waypoint0', 'waypoint15'), ('rover1', 'waypoint11', 'waypoint6'), ('rover2', 'waypoint3', 'waypoint13'), ('rover1', 'waypoint18', 'waypoint23'), ('rover2', 'waypoint5', 'waypoint0'), ('rover7', 'waypoint8', 'waypoint18'), ('rover1', 'waypoint4', 'waypoint19'), ('rover1', 'waypoint7', 'waypoint0'), ('rover3', 'waypoint9', 'waypoint18'), ('rover7', 'waypoint2', 'waypoint14'), ('rover0', 'waypoint22', 'waypoint11'), ('rover4', 'waypoint15', 'waypoint16'), ('rover3', 'waypoint0', 'waypoint18'), ('rover1', 'waypoint14', 'waypoint1'), ('rover6', 'waypoint13', 'waypoint4'), ('rover5', 'waypoint7', 'waypoint16'), ('rover7', 'waypoint20', 'waypoint16'), ('rover7', 'waypoint2', 'waypoint9'), ('rover6', 'waypoint4', 'waypoint16'), ('rover6', 'waypoint18', 'waypoint1'), ('rover4', 'waypoint16', 'waypoint10'), ('rover0', 'waypoint18', 'waypoint21'), ('rover4', 'waypoint16', 'waypoint4'), ('rover3', 'waypoint20', 'waypoint16'), ('rover2', 'waypoint2', 'waypoint1'), ('rover7', 'waypoint11', 'waypoint10'), ('rover2', 'waypoint16', 'waypoint20'), ('rover1', 'waypoint0', 'waypoint7'), ('rover4', 'waypoint24', 'waypoint5'), ('rover6', 'waypoint4', 'waypoint13'), ('rover7', 'waypoint10', 'waypoint11'), ('rover7', 'waypoint2', 'waypoint23'), ('rover7', 'waypoint15', 'waypoint10'), ('rover4', 'waypoint10', 'waypoint16'), ('rover0', 'waypoint11', 'waypoint10'), ('rover1', 'waypoint20', 'waypoint4'), ('rover2', 'waypoint9', 'waypoint18'), ('rover3', 'waypoint5', 'waypoint1'), ('rover4', 'waypoint5', 'waypoint0'), ('rover6', 'waypoint17', 'waypoint8'), ('rover7', 'waypoint8', 'waypoint17'), ('rover0', 'waypoint24', 'waypoint12'), ('rover1', 'waypoint22', 'waypoint16'), ('rover4', 'waypoint4', 'waypoint1'), ('rover0', 'waypoint10', 'waypoint11'), ('rover1', 'waypoint1', 'waypoint14'), ('rover1', 'waypoint10', 'waypoint18'), ('rover3', 'waypoint12', 'waypoint19'), ('rover7', 'waypoint13', 'waypoint4'), ('rover7', 'waypoint5', 'waypoint21'), ('rover2', 'waypoint18', 'waypoint24'), ('rover5', 'waypoint15', 'waypoint13'), ('rover5', 'waypoint6', 'waypoint14'), ('rover5', 'waypoint10', 'waypoint16'), ('rover6', 'waypoint5', 'waypoint1'), ('rover7', 'waypoint14', 'waypoint2'), ('rover5', 'waypoint3', 'waypoint18'), ('rover2', 'waypoint1', 'waypoint15'), ('rover5', 'waypoint6', 'waypoint9'), ('rover2', 'waypoint23', 'waypoint18'), ('rover5', 'waypoint15', 'waypoint17'), ('rover5', 'waypoint14', 'waypoint6'), ('rover4', 'waypoint0', 'waypoint5'), ('rover2', 'waypoint15', 'waypoint1'), ('rover2', 'waypoint22', 'waypoint21'), ('rover0', 'waypoint17', 'waypoint20'), ('rover2', 'waypoint11', 'waypoint21'), ('rover4', 'waypoint16', 'waypoint5'), ('rover4', 'waypoint16', 'waypoint8'), ('rover5', 'waypoint8', 'waypoint11'), ('rover1', 'waypoint13', 'waypoint3'), ('rover0', 'waypoint12', 'waypoint15'), ('rover5', 'waypoint16', 'waypoint10'), ('rover5', 'waypoint16', 'waypoint4'), ('rover3', 'waypoint3', 'waypoint20'), ('rover4', 'waypoint8', 'waypoint16'), ('rover5', 'waypoint19', 'waypoint6'), ('rover2', 'waypoint20', 'waypoint3'), ('rover1', 'waypoint0', 'waypoint5'), ('rover0', 'waypoint11', 'waypoint6'), ('rover6', 'waypoint15', 'waypoint6'), ('rover0', 'waypoint7', 'waypoint8'), ('rover4', 'waypoint2', 'waypoint9'), ('rover6', 'waypoint1', 'waypoint14'), ('rover4', 'waypoint16', 'waypoint22'), ('rover0', 'waypoint11', 'waypoint8'), ('rover6', 'waypoint10', 'waypoint16'), ('rover6', 'waypoint19', 'waypoint4'), ('rover1', 'waypoint4', 'waypoint16'), ('rover3', 'waypoint12', 'waypoint24'), ('rover7', 'waypoint19', 'waypoint4'), ('rover1', 'waypoint17', 'waypoint20'), ('rover7', 'waypoint16', 'waypoint10'), ('rover7', 'waypoint3', 'waypoint20'), ('rover0', 'waypoint11', 'waypoint22'), ('rover1', 'waypoint18', 'waypoint1'), ('rover7', 'waypoint16', 'waypoint4'), ('rover7', 'waypoint24', 'waypoint20'), ('rover2', 'waypoint1', 'waypoint2'), ('rover6', 'waypoint24', 'waypoint20'), ('rover4', 'waypoint18', 'waypoint8'), ('rover5', 'waypoint9', 'waypoint6'), ('rover6', 'waypoint20', 'waypoint4'), ('rover0', 'waypoint16', 'waypoint15'), ('rover5', 'waypoint18', 'waypoint10'), ('rover6', 'waypoint1', 'waypoint23'), ('rover3', 'waypoint16', 'waypoint10'), ('rover7', 'waypoint16', 'waypoint2'), ('rover1', 'waypoint8', 'waypoint5'), ('rover5', 'waypoint20', 'waypoint23'), ('rover4', 'waypoint5', 'waypoint21'), ('rover6', 'waypoint6', 'waypoint9'), ('rover2', 'waypoint18', 'waypoint17'), ('rover0', 'waypoint8', 'waypoint11'), ('rover6', 'waypoint23', 'waypoint1'), ] )
rigid.equipped_for_rock_analysis = set( [('rover4',), ('rover3',), ('rover7',), ('rover2',), ] )
rigid.on_board = set( [('camera1', 'rover1'), ('camera2', 'rover4'), ('camera3', 'rover2'), ('camera4', 'rover1'), ('camera0', 'rover0'), ('camera5', 'rover5'), ('camera6', 'rover6'), ] )
rigid.calibration_target = set( [('camera5', 'objective4'), ('camera0', 'objective6'), ('camera6', 'objective5'), ('camera1', 'objective1'), ('camera4', 'objective4'), ('camera3', 'objective2'), ('camera2', 'objective0'), ] )
rigid.supports = set( [('camera1', 'high_res'), ('camera6', 'colour'), ('camera6', 'low_res'), ('camera3', 'high_res'), ('camera0', 'high_res'), ('camera4', 'high_res'), ('camera2', 'high_res'), ('camera1', 'colour'), ('camera5', 'high_res'), ('camera4', 'colour'), ('camera0', 'colour'), ('camera3', 'low_res'), ('camera2', 'colour'), ('camera6', 'high_res'), ('camera2', 'low_res'), ] )
rigid.visible_from = set( [('objective4', 'waypoint14'), ('objective3', 'waypoint16'), ('objective1', 'waypoint3'), ('objective4', 'waypoint13'), ('objective4', 'waypoint15'), ('objective6', 'waypoint0'), ('objective2', 'waypoint12'), ('objective6', 'waypoint10'), ('objective4', 'waypoint7'), ('objective4', 'waypoint1'), ('objective7', 'waypoint14'), ('objective4', 'waypoint17'), ('objective0', 'waypoint9'), ('objective6', 'waypoint2'), ('objective7', 'waypoint15'), ('objective3', 'waypoint14'), ('objective0', 'waypoint10'), ('objective6', 'waypoint6'), ('objective0', 'waypoint4'), ('objective3', 'waypoint13'), ('objective7', 'waypoint9'), ('objective3', 'waypoint15'), ('objective5', 'waypoint9'), ('objective7', 'waypoint7'), ('objective5', 'waypoint10'), ('objective0', 'waypoint11'), ('objective6', 'waypoint5'), ('objective7', 'waypoint4'), ('objective1', 'waypoint1'), ('objective2', 'waypoint16'), ('objective3', 'waypoint7'), ('objective5', 'waypoint4'), ('objective7', 'waypoint17'), ('objective7', 'waypoint19'), ('objective4', 'waypoint23'), ('objective3', 'waypoint1'), ('objective6', 'waypoint8'), ('objective7', 'waypoint11'), ('objective5', 'waypoint11'), ('objective3', 'waypoint17'), ('objective3', 'waypoint19'), ('objective5', 'waypoint2'), ('objective3', 'waypoint11'), ('objective4', 'waypoint9'), ('objective6', 'waypoint3'), ('objective4', 'waypoint10'), ('objective2', 'waypoint14'), ('objective4', 'waypoint4'), ('objective2', 'waypoint13'), ('objective0', 'waypoint0'), ('objective2', 'waypoint15'), ('objective4', 'waypoint19'), ('objective4', 'waypoint11'), ('objective4', 'waypoint2'), ('objective7', 'waypoint0'), ('objective2', 'waypoint7'), ('objective5', 'waypoint0'), ('objective7', 'waypoint16'), ('objective2', 'waypoint1'), ('objective7', 'waypoint10'), ('objective2', 'waypoint17'), ('objective3', 'waypoint9'), ('objective5', 'waypoint3'), ('objective0', 'waypoint2'), ('objective2', 'waypoint11'), ('objective7', 'waypoint20'), ('objective3', 'waypoint10'), ('objective0', 'waypoint6'), ('objective3', 'waypoint4'), ('objective7', 'waypoint2'), ('objective6', 'waypoint1'), ('objective1', 'waypoint2'), ('objective7', 'waypoint6'), ('objective0', 'waypoint5'), ('objective5', 'waypoint6'), ('objective3', 'waypoint2'), ('objective4', 'waypoint0'), ('objective0', 'waypoint8'), ('objective3', 'waypoint6'), ('objective7', 'waypoint5'), ('objective5', 'waypoint5'), ('objective4', 'waypoint3'), ('objective7', 'waypoint8'), ('objective5', 'waypoint8'), ('objective3', 'waypoint5'), ('objective4', 'waypoint20'), ('objective7', 'waypoint18'), ('objective3', 'waypoint8'), ('objective2', 'waypoint9'), ('objective0', 'waypoint3'), ('objective2', 'waypoint10'), ('objective1', 'waypoint0'), ('objective3', 'waypoint18'), ('objective4', 'waypoint6'), ('objective2', 'waypoint4'), ('objective3', 'waypoint0'), ('objective7', 'waypoint3'), ('objective4', 'waypoint5'), ('objective0', 'waypoint12'), ('objective2', 'waypoint2'), ('objective3', 'waypoint3'), ('objective6', 'waypoint9'), ('objective4', 'waypoint8'), ('objective6', 'waypoint7'), ('objective2', 'waypoint6'), ('objective0', 'waypoint14'), ('objective7', 'waypoint12'), ('objective5', 'waypoint12'), ('objective6', 'waypoint4'), ('objective0', 'waypoint13'), ('objective4', 'waypoint18'), ('objective0', 'waypoint15'), ('objective2', 'waypoint5'), ('objective3', 'waypoint12'), ('objective5', 'waypoint14'), ('objective4', 'waypoint16'), ('objective7', 'waypoint13'), ('objective0', 'waypoint7'), ('objective2', 'waypoint8'), ('objective5', 'waypoint13'), ('objective0', 'waypoint1'), ('objective4', 'waypoint22'), ('objective5', 'waypoint7'), ('objective0', 'waypoint16'), ('objective7', 'waypoint1'), ('objective2', 'waypoint0'), ('objective5', 'waypoint1'), ('objective4', 'waypoint12'), ('objective4', 'waypoint21'), ('objective2', 'waypoint3'), ] )
rigid.goal_communicated_soil_data = set( [('waypoint7',), ('waypoint13',), ('waypoint20',), ('waypoint11',), ('waypoint8',), ('waypoint23',), ] )
rigid.goal_communicated_rock_data = set( [('waypoint18',), ('waypoint14',), ('waypoint7',), ('waypoint9',), ('waypoint12',), ('waypoint21',), ('waypoint10',), ('waypoint22',), ('waypoint16',), ] )
rigid.goal_communicated_image_data = set( [('objective5', 'high_res'), ('objective2', 'high_res'), ('objective3', 'colour'), ('objective0', 'high_res'), ('objective7', 'colour'), ] )
state.communicated_soil_data = set( [] )
state.full = set( [] )
state.have_image = set( [] )
state.have_rock_analysis = set( [] )
state.calibrated = set( [] )
state.communicated_rock_data = set( [] )
state.have_soil_analysis = set( [] )
state.communicated_image_data = set( [] )

task_list = [('achieve__goals',)]