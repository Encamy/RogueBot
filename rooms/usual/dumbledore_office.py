name = 'Кабинет директора'

def get_actions(user):
	return ['Уйти']

#Цитата из книги, описание кабинета директора Хогвартса. Пока как просто маленькая пасхалочка, потенциально может вылиться в мини-квест по тематики ГП.
def enter(user, reply):
    reply('Это была круглая, просторная комната, полная еле слышных странных звуков. '
          'Множество таинственных серебряных приборов стояло на вращающихся столах — они жужжали, '
          'выпуская небольшие клубы дыма. Стены увешаны портретами прежних директоров и директрис, '
          'которые мирно дремали в красивых рамах. '
          'В центре громадный письменный стол на когтистых лапах, '
          'а за ним на полке — потертая, латаная-перелатаная Волшебная шляпа.\n')

def action(user, reply, text):
      user.leave(reply)