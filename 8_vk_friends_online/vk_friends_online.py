import getpass
import vk


def get_vk_api(login, password, protocol_version='5.87'):
    session = vk.AuthSession(
        app_id='6755461',
        user_login=login,
        user_password=password,
        scope='friends'
    )
    return vk.API(session, v=protocol_version)


def get_online_friends_names(vk_api):
    online_friends_ids = vk_api.friends.getOnline()
    return vk_api.users.get(user_ids=online_friends_ids)


def print_online_friends_names_to_console(online_friends_names):
    if online_friends_names:
        for online_friend_name in online_friends_names:
            friend_first_name = online_friend_name['first_name']
            friend_last_name = online_friend_name['last_name']
            print('{} {}'.format(friend_first_name, friend_last_name))
    else:
        print('All friends are offline')


if __name__ == '__main__':
    login = input('Please enter your login: ')
    password = getpass.getpass('Please enter your password: ')
    try:
        vk_api = get_vk_api(login, password)
    except vk.exceptions.VkAuthError:
        exit('Incorrect login or password')
    online_friends_names = get_online_friends_names(vk_api)
    print_online_friends_names_to_console(online_friends_names)
