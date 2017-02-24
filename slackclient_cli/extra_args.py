
import slack_api_specific
from slackclient import SlackClient


def file_upload_by_filename(method_args):
    ex_key = "ex-content"
    if ex_key in method_args:
        filename = method_args.pop(ex_key)
        if filename is not None:
            method_args["content"] = open(filename, 'rb').read()
    return method_args


def _get_channel_dict(method_args):
    slack_client = SlackClient(method_args["token"])
    timeout = 1
    res = slack_client.api_call("channels.list", timeout)
    channel_dict = dict()
    for v in res["channels"]:
        channel_dict[v["name"]] = v
    return channel_dict


def channel_names_to_ids(method_args):
    channels = list()
    ex_key = "ex-channels"
    if ex_key in method_args:
        channel_names = method_args.pop(ex_key)
        if channel_names is not None:
            channel_dict = _get_channel_dict(method_args)
            for v in channel_names.split(","):
                channels.append(channel_dict[v]["id"])
    method_args["channels"] = ",".join(channels)
    return method_args


def channel_name_to_id(method_args):
    ex_key = "ex-channel"
    if ex_key in method_args:
        channel_name = method_args.pop(ex_key)
        if channel_name is not None:
            channel_dict = _get_channel_dict(method_args)
            method_args["channel"] = channel_dict[channel_name]["id"]
    return method_args


def _get_user_dict(method_args):
    slack_client = SlackClient(method_args["token"])
    timeout = 1
    res = slack_client.api_call("users.list", timeout)
    user_dict = dict()
    for v in res["members"]:
        user_dict[v["name"]] = v
    return user_dict


def user_names_to_ids(method_args):
    users = list()
    ex_key = "ex-users"
    if ex_key in method_args:
        user_names = method_args.pop(ex_key)
        if user_names is not None:
            user_dict = _get_user_dict(method_args)
            for v in user_names.split(","):
                users.append(user_dict[v]["id"])
    method_args["users"] = ",".join(users)
    return method_args


def user_name_to_id(method_args):
    ex_key = "ex-user"
    if ex_key in method_args:
        user_name = method_args.pop(ex_key)
        if user_name is not None:
            user_dict = _get_user_dict(method_args)
            method_args["user"] = user_dict[user_name]["id"]
    return method_args


def parse(method_args):
    api_specific = slack_api_specific.get()
    for v in api_specific[method_args["method"]]:
        if ("extra_function" in v) and (v["Argument"] in method_args):
            extra_function = v["extra_function"]
            method_args = eval(extra_function + "(method_args)")
    return method_args
