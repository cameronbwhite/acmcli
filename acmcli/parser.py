import argparse
import datetime

from . import DATETIME_FORMAT, DATE_FORMAT, DEFAULT_BASE_URL

def date_type(x):
    """ A function which acts as a type for reqparse.
    
    Given a string this function will return a date object if the string
    is in the currect format.

    >>> date_type('2014-04-11')
    datetime.date(2014, 4, 11)
    """
    try:
        return datetime.datetime.strptime(x, DATE_FORMAT).date()
    except ValueError:
        raise argparse.ArgumentTypeError(
            'Must be a valid date in the {} format'.format(DATE_FORMAT))

def datetime_type(x):
    """ A function which acts as a type for reqparse.

    Given a string this function will return a datetime object if the 
    string is in the currect format. 

    >>> datetime_type('2014-04-11 16:20:00.00000')
    datetime.datetime(2014, 4, 11, 16, 20)
    """
    try:
        return datetime.datetime.strptime(x, DATETIME_FORMAT)
    except ValueError:
        raise argparse.ArgumentTypeError(
            'Must be a valid datetime in the {} format'.format(DATETIME_FORMAT))

parser = argparse.ArgumentParser(
        description="")

parser.add_argument('--base_url', type=str, default=DEFAULT_BASE_URL)
parser.add_argument('--username', type=str)
parser.add_argument('--password', type=str)

subparsers = parser.add_subparsers(
        description="",
        dest='subparser1')

#
# Events Parser
#

events_parser = subparsers.add_parser('events')

events_subparsers = events_parser.add_subparsers(dest='subparser2')

events_add_parser = events_subparsers.add_parser('add')

events_add_parser.add_argument('--title', type=str)
events_add_parser.add_argument('--description', type=str)
events_add_parser.add_argument('--location', type=str)
events_add_parser.add_argument('--speaker', type=str)
events_add_parser.add_argument('--canceled', type=bool)
events_add_parser.add_argument('--hidden', type=bool)
events_add_parser.add_argument('--start', type=datetime_type)
events_add_parser.add_argument('--end', type=datetime_type)

events_update_parser = events_subparsers.add_parser('update')

events_update_parser.add_argument('--title', type=str)
events_update_parser.add_argument('--description', type=str)
events_update_parser.add_argument('--location', type=str)
events_update_parser.add_argument('--speaker', type=str)
events_update_parser.add_argument('--canceled', type=bool)
events_update_parser.add_argument('--hidden', type=bool)
events_update_parser.add_argument('--start', type=datetime_type)
events_update_parser.add_argument('--end', type=datetime_type)

events_list_parser = events_subparsers.add_parser('list')

events_list_parser.add_argument('--event_id')

#
# Posts Parser
#

posts_parser = subparsers.add_parser('posts')

posts_subparsers = posts_parser.add_subparsers(dest='subparser2')

posts_add_parser = posts_subparsers.add_parser('add')

posts_add_parser.add_argument('--title', type=str)
posts_add_parser.add_argument('--description', type=str)
posts_add_parser.add_argument('--content', type=str)

posts_update_parser = posts_subparsers.add_parser('update')

posts_update_parser.add_argument('--title', type=str)
posts_update_parser.add_argument('--description', type=str)
posts_update_parser.add_argument('--content', type=str)

posts_list_parser = posts_subparsers.add_parser('list')

posts_list_parser.add_argument('--post_id')

#
# People Parser
#

people_parser = subparsers.add_parser('people')

people_subparsers = people_parser.add_subparsers(dest='subparser2')

people_add_parser = people_subparsers.add_parser('add')

people_add_parser.add_argument('username', type=str)
people_add_parser.add_argument('password', type=str)
people_add_parser.add_argument('--name', type=str)
people_add_parser.add_argument('--email', type=str)
people_add_parser.add_argument('--website', type=str)

people_update_parser = people_subparsers.add_parser('update')


people_update_parser.add_argument('id_or_username')
people_update_parser.add_argument('--password')
people_update_parser.add_argument('--name')
people_update_parser.add_argument('--email')
people_update_parser.add_argument('--website')

people_list_parser = people_subparsers.add_parser('list')

people_list_parser.add_argument('--id_or_username')

people_delete_parser = people_subparsers.add_parser('delete')

people_delete_parser.add_argument('id_or_username')

#
# Memberships Parser
#

memberships_parser = subparsers.add_parser('memberships')

memberships_subparsers = memberships_parser.add_subparsers(dest='subparser2')

memberships_add_parser = memberships_subparsers.add_parser('add')

memberships_add_parser.add_argument('person_id', type=int)
memberships_add_parser.add_argument('start')
memberships_add_parser.add_argument('--end')

memberships_update_parser = memberships_subparsers.add_parser('update')

memberships_update_parser.add_argument('--person_id', type=int)
memberships_update_parser.add_argument('--start', type=date_type)
memberships_update_parser.add_argument('--end', type=date_type)

memberships_list_parser = memberships_subparsers.add_parser('list')

memberships_list_parser.add_argument('--membership_id', type=int)

memberships_delete_parser = memberships_subparsers.add_parser('delete')

memberships_delete_parser.add_argument('membership_id', type=int)

#
# Officerships Parser
#

officerships_parser = subparsers.add_parser('officerships')

officerships_subparsers = officerships_parser.add_subparsers(dest='subparser2')

officerships_add_parser = officerships_subparsers.add_parser('add')

officerships_add_parser.add_argument('person_id', type=int)
officerships_add_parser.add_argument('title', type=str)
officerships_add_parser.add_argument('start', type=date_type)
officerships_add_parser.add_argument('--end', type=date_type)

officerships_update_parser = officerships_subparsers.add_parser('update')

officerships_update_parser.add_argument('--person_id', type=int)
officerships_update_parser.add_argument('--title', type=str)
officerships_update_parser.add_argument('--start', type=date_type)
officerships_update_parser.add_argument('--end', type=date_type)

officerships_list_parser = officerships_subparsers.add_parser('list')

officerships_list_parser.add_argument('--officership_id', type=int)

officerships_delete_parser = officerships_subparsers.add_parser('delete')

officerships_delete_parser.add_argument('officership_id', type=int)

parser.parse_args()
