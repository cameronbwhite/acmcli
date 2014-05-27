DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
DATE_FORMAT = '%Y-%m-%d'
DEFAULT_BASE_URL = 'https://acm.pdx.edu/api/v1'

from .parser import parser
from .routines import *
from acmlib import AcmLib

def acmcli():
    args = parser.parse_args()

    acmlib = AcmLib(
            username = args.username,
            password = args.password,
            base_url = args.base_url,
            )

    if args.subparser1 == 'events':
        if args.subparser2 == 'add':
            events_add(acmlib, args)
        elif args.subparser2 == 'update':
            events_update(acmlib, args)
        elif args.subparser2 == 'list': 
            events_list(acmlib, args)
    elif args.subparser1 == 'posts':
        if args.subparser2 == 'add':
            posts_add(acmlib, args)
        elif args.subparser2 == 'update':
            posts_update(acmlib, args)
        elif args.subparser2 == 'list': 
            posts_list(acmlib, args)
    elif args.subparser1 == 'people':
        if args.subparser2 == 'add':
            people_add(acmlib, args)
        elif args.subparser2 == 'update':
            people_update(acmlib, args)
        elif args.subparser2 == 'list': 
            people_list(acmlib, args)
        elif args.subparser2 == 'delete':
            people_delete(acmlib, args)
    elif args.subparser1 == 'memberships':
        if args.subparser2 == 'add':
            memberships_add(acmlib, args)
        elif args.subparser2 == 'update':
            memberships_update(acmlib, args)
        elif args.subparser2 == 'list': 
            memberships_list(acmlib, args)
        elif args.subparser2 == 'delete':
            memberships_delete(acmlib, args)
    elif args.subparser1 == 'officerships':
        if args.subparser2 == 'add':
            officerships_add(acmlib, args)
        elif args.subparser2 == 'update':
            officerships_update(acmlib, args)
        elif args.subparser2 == 'list': 
            officerships_list(acmlib, args)
        elif args.subparser2 == 'delete':
            officerships_delete(acmlib, args)
    elif args.subparser1 == 'database':
        database_get(acmlib, args)
