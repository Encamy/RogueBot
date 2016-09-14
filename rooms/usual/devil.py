from utils.buffs import DevilPower
from utils.buffs import DevilInt
from utils.buffs import DevilMoney
from utils.buffs import DevilEntity

COUGH = 'Кашлянуть'
QUIT = 'Уйти'
MLEAVE = 'Я пойду, пожалуй'

name = 'Уютная комната'

def enter(user, reply):
	reply('Ты видишь просторную комнату.\nВ углу тихо потрескивает камин, на стенах развешаны охотничьи трофеи.\nЗдесь довольно уютно.\nЧуть погодя, твои глаза привыкли к полумраку царящему в комнате и ты замечаешь человека за столом. Он поглощен работой, постоянно что-то сверяет на разных листах бумаги. Как он это делает в такой темноте?')
	user.set_room_temp('question', 'first')

def action(user, text, reply):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == COUGH:
			reply('Это не возымело никакого эффекта')
		elif text == 'Подойти к столу':
			reply('Ты подходишь вплотную к столу. Человек отрывается от бумаг, поправляет очки и выжидательно смотрит на тебя')
			user.set_room_temp('question', 'second')
		else:
			user.leave(reply)
	elif question == 'second':
		if text == MLEAVE:
			reply('Человек ухмыляется и возвращается к работе')
			user.leave(reply)
		elif text == 'Кто вы?':
			reply('У меня много имен, &имя&. В разных культурах меня называли по разному. я помогал людям добиться превосходных результатов, начинал войны, насылал болезни.')
			user.set_room_temp('question', 'third')
	elif question == 'third':
		if text == MLEAVE:
			reply(' Человек изменился в лице, кажется ему не понравилось это. -Тогда вот тебе маленький подарок, чтобы ты знал, что не нужно отрывать меня от работы по пустякам')
			user.max_hp = 125
			user.leave(reply)
		elif text == 'Вы дьявол?':
			reply('Человек рассмеялся. -Ну зачем сразу так грубо? Возможно это и одно из моих имен, но точно не самое любимое. Все что тебе нужно знать, это то, что я твой друг. Ну, чего ты хочешь?')
			user.set_room_temp('question', 'forth')
		else:
			reply('Внезапно он исчез из виду и вы услышали шепот у себя в голове\n-Может ты хочешь бесконечную силу, чтобы все трепетали пред тобой?\nИли ты хочешь быть гением, способным на всё?\nХотя нет, наверное, ты хочешь несметного богатства?\nИли же всё сразу?\nВыбирай, смертный!')	
			user.set_room_temp('question', 'propose')
	elif question == 'forth':
		if text == MLEAVE:
			reply(' Дьявол изменился в лице, кажется ему не понравилось это. -Тогда вот тебе маленький подарок, чтобы ты знал, что не нужно отрывать меня от работы по пустякам')
			user.max_hp = 125
			user.leave(reply)
		elif text == 'А что ты можешь предложить мне?':
			reply('Внезапно он исчез из виду и вы услышали шепот у себя в голове\n-Может ты хочешь бесконечную силу, чтобы все трепетали пред тобой?\nИли ты хочешь быть гением, способным на всё?\nХотя нет, наверное, ты хочешь несметного богатства?\nИли же всё сразу?\nВыбирай, смертный!')	
			user.set_room_temp('question', 'propose')
	elif question == 'propose':
		if text == 'Силу!':
			reply('Отличный выбор, а теперь подпиши здесь и вот здесь.\nПеред вами возник исписанный на непонятном языке пергамент с двумя галочками.\n-Ну же, условия стандартные, когда умрешь я заберу твою душу.')
			user.new_buff(DevilPower())
			user.set_room_temp('question', 'deathq')
		elif text == 'Знания!':
			reply('Отличный выбор, а теперь подпиши здесь и вот здесь.\nПеред вами возник исписанный на непонятном языке пергамент с двумя галочками.\n-Ну же, условия стандартные, когда умрешь я заберу твою душу.')
			user.new_buff(DevilInt())
			user.set_room_temp('question', 'deathq')
		elif text == 'Деньги!':
			reply('Отличный выбор, а теперь подпиши здесь и вот здесь.\nПеред вами возник исписанный на непонятном языке пергамент с двумя галочками.\n-Ну же, условия стандартные, когда умрешь я заберу твою душу.')
			user.new_buff(DevilMoney())
			user.gold += 500000
			user.add_item('special', 'lepergold')
			user.set_room_temp('question', 'deathq')
		else:
			reply('-Вот это жадность. Ты напоминаешь мне меня в молодости, я тогда тоже был ненасытен...\nДьявол улыбнулся своим воспоминаниям.\n-Вернемся к делу! Подпиши здесь и здесь.\nПеред вами возник исписанный на непонятном языке пергамент с двумя галочками.\n-Ну же, условия стандартные, когда умрешь я заберу твою душу.')
			user.new_buff(DevilEntity())
			user.gold += 500000
			user.add_item('special', 'lepergold')
			user.set_room_temp('question', 'deathq')
	elif question == 'deathq':
		if text == 'А когда я умру?':
			reply('У дьявола сверкнули глаза.\n-Увы этого никто не знает, даже я.')
			user.set_room_temp('question', 'signature')
	elif question == 'signature':
		if text == 'Подписать':
			reply('-Замечательно! А теперь мне пора вернуться к работе, а ты можешь идти и покорять мир!\nУ тебя в руках остался контракт, вглядевшись, ты видишь цифру 7...\n-Дай сюда! Он тебе не нужен.')
			user.leave(reply)	

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == ' first':
		ans = [ COUGH, 'Подойти к столу', QUIT ]
	elif question == 'second':
		ans = [ MLEAVE, 'Кто вы?' ]
	elif question == 'third':
		ans = [ MLEAVE, 'Вы дьявол?', 'А что ты предложишь мне?' ]
	elif question == 'forth':
		ans = [ MLEAVE, 'А что ты предложишь мне?' ]
	elif question == 'propose':
		ans = [ 'Силу!', 'Знания!', 'Деньги!', 'Я хочу всё!' ]	
	elif question == 'deathq':
		ans = [ 'А когда я умру?' ]	
	elif question == 'signature':
		ans = [ 'Подписать' ]

	return ans		
