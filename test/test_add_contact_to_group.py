# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
from model.group import Group


def test_add_contact_to_some_group(app, db, check_ui):
    # перешли на нужную страницу
    app.select_home()
    # проверил контакт и группу, если нет  то создал
    if len(db.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.add(
            Contact(firstname="Yura", middlename="middlename", lastname="Goroshkin", nickname="nickname", title="Title",
                    company="Company", address="Address", telephone_home="88005553225", telephone_mobile="88005553225",
                    telephone_work="88005553225",
                    telephone_fax="88005553225", email="test@email.ru", email2="email2", email3="test@gemail.com",
                    homepage="Homepage", byear="1988", ayear="1998", address2="Addres2", phone2="Phone2",
                    notes="Notes"))
        app.open_home_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='the_only'))
        app.open_home_page()
    old_contacts = db.get_contact_list()
    # обозначил какой контакт будет выбран для теста
    index = randrange(len(old_contacts))
    id = old_contacts[index].id
    # значение группы куда мы собираемся добавить контакт
    value = app.contact.select_grop_from_list_checked()
    check_in_bd = db.address_in_groups()
    # добавил контакт в случайную группу <----- УБРАТЬ СЛУЧАЙНУЮ (перебором) - ту в которой нет данного контакта
    app.contact.put_contact_by_id_to_group(id)
    number_group = value[1]
    app.select_home()
    # связка полученная в ходе шагов теста id(contact) + group_id
    tuple_contact_and_group = (int(id), int(value[0]))
    # все связкм полученная из БД id(contact) + group_id
    all_list_address_in_groups = db.address_in_groups()
    # поиск полученной связки, со связкой из БД - проверка что она создалась
    assert tuple_contact_and_group in all_list_address_in_groups
    if check_ui:
        # переход в ту группу, куда был добавлен контакт и проверка наличия по id того контакта в группе
        id_list_contact = app.contact.check_in_group_contact(number_group)
        assert id in id_list_contact

