import sys

def exit_with_message_on_errors(f):
    
    def new_f(acmlib, args):

        try:
            return f(acmlib, args)
        except Exception as e:
            sys.exit("Error: {}".format(e.message))

    new_f.__name__ = f.__name__
    return new_f

@exit_with_message_on_errors
def events_add(acmlib, args):
    
    return acmlib.update_event(
        start = args.start,
        end = args.end,
        title = args.title,
        description = args.description,
        location = args.location,
        speaker = args.speaker)


@exit_with_message_on_errors
def events_update(acmlib, args):

    return acmlib.update_event(
        event_id = args.event_id,
        start = args.start,
        end = args.end,
        title = args.title,
        description = args.description,
        location = args.location,
        speaker = args.speaker)

@exit_with_message_on_errors
def events_list(acmlib, args):

    format_str = \
        'Result #{}\n'\
        '\tevent_id: {}\n'\
        '\ttitle: {}\n'\
        '\tdescrption: {}\n'\
        '\tspeaker: {}\n'\
        '\teditor_id: {}\n'\
        '\tedited_at: {}\n'\
        '\tstart: {}\n'\
        '\tend: {}\n'\
        '\tcanceled: {}\n'\
        '\trevision: {}\n'

    if args.event_id:
        events = acmlib.get_event(args.event_id)
    else:
        events = acmlib.get_events() 

    for i, event in enumerate(events):

        print(format_str.format(i+1, event.event_id, event.title,
            event.description, event.speaker, event.editor_id,
            event.edited_at, event.start, event.end, event.canceled,
            event.revision))

@exit_with_message_on_errors
def posts_add(acmlib, args):

    return acmlib.add_post(
        title = args.title,
        description = args.description,
        content = args.content)

@exit_with_message_on_errors
def posts_update(acmlib, args):

    return acmlib.add_post(
        post_id = args.post_id,
        title = args.title,
        description = args.description,
        content = args.content)

@exit_with_message_on_errors
def posts_list(acmlib, args):
    format_str = \
        'Result #{}\n'\
        '\tpost_id: {}\n'\
        '\ttitle: {}\n'\
        '\tdescrption: {}\n'\
        '\tcontent: {}\n'\
        '\teditor_id: {}\n'\
        '\tedited_at: {}\n'\

    if args.post_id:
        posts = acmlib.get_post(args.post_id)
    else:
        posts = acmlib.get_posts() 

    for i, post in enumerate(posts):

        print(format_str.format(i+1, post.post_id, post.title,
            post.description, post.content, post.editor_id,
            post.edited_at))

@exit_with_message_on_errors
def people_add(acmlib, args):

    return acmlib.add_person(
        username = args.username,
        password = args.password,
        name = args.name,
        email = args.email,
        website = args.website)

@exit_with_message_on_errors
def people_update(acmlib, args):

    return acmlib.add_person(
        id_or_username = args.id_or_username, 
        password = args.password,
        name = args.name,
        email = args.email,
        website = args.website)

@exit_with_message_on_errors
def people_list(acmlib, args):
    format_str = \
        'Result #{}\n'\
        '\tid: {}\n'\
        '\tname: {}\n'\
        '\tusername: {}\n'\
        '\temail: {}\n'\
        '\twebsite: {}\n'

    if args.id_or_username:
        person = acmlib.get_person(args.id_or_username)
        print(format_str.format(1, person.id, person.name,
            person.username, person.email, person.website))
    else:
        people = acmlib.get_people() 

        for i, person in enumerate(people):

            print(format_str.format(i+1, person.id, person.name,
                person.username, person.email, person.website))

@exit_with_message_on_errors
def people_delete(acmlib, args):

    acmlib.delete_person(args.id_or_username)

@exit_with_message_on_errors
def memberships_add(acmlib, args):

    return acmlib.add_membership(
            person_id = args.person_id,
            start = args.start,
            end = args.end)

@exit_with_message_on_errors
def memberships_update(acmlib, args):

    return acmlib.add_membership(
            membership_id = args.membership_id,
            person_id = args.person_id,
            start = args.start,
            end = args.end)

@exit_with_message_on_errors
def memberships_list(acmlib, args):
    format_str = \
        'Result #{}\n'\
        '\tid: {}\n'\
        '\tperson_id: {}\n'\
        '\tstart: {}\n'\
        '\tend: {}\n'\

    if args.membership_id:
        memberships  = acmlib.get_membership(args.membership_id)
    else:
        memberships = acmlib.get_memberships() 

    for i, membership in enumerate(memberships):

        print(format_str.format(i+1, membership.id, membership.person_id,
            membership.start, membership.end))

@exit_with_message_on_errors
def memberships_delete(acmlib, args):
    acmlib.delete_membership(args.membership_id)

@exit_with_message_on_errors
def officerships_add(acmlib, args):

    return acmlib.add_officership(
            person_id = args.person_id,
            title = args.title,
            start = args.start,
            end = args.end)

@exit_with_message_on_errors
def officerships_update(acmlib, args):

    return acmlib.add_officership(
            officership_id = args.officership_id,
            person_id = args.person_id,
            title = args.title,
            start = args.start,
            end = args.end)

@exit_with_message_on_errors
def officerships_list(acmlib, args):
    format_str = \
        'Result #{}\n'\
        '\tid: {}\n'\
        '\ttitle: {}\n'\
        '\tperson_id: {}\n'\
        '\tstart_date: {}\n'\
        '\tend_date: {}\n'\

    if args.officership_id:
        officerships  = acmlib.get_officership(args.officership_id)
    else:
        officerships = acmlib.get_officerships() 

    for i, officership in enumerate(officerships):

        print(format_str.format(i+1, officership.id, officership.title,
            officership.person_id, officership.start_date, officership.end_date))

@exit_with_message_on_errors
def officerships_delete(acmlib, args):

    acmlib.delete_officership(args.officership_id)

