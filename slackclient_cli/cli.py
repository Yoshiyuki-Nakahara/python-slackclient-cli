
import os
import argparse
import json
from slackclient import SlackClient

import slack_api_specific
import extra_args

env_var_key_prefix = "SLACK_API_"
arg_required_string = "Required"


def _get_version():
    version_txt_path = os.path.abspath(os.path.dirname(__file__)) + '/__version__.txt'
    return open(version_txt_path).read().splitlines()[0]


def parse_program_args():
    description = u"{0} [Args] [Options]\nDetailed options -h or --help".format(__file__)
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--version', action='version', version=_get_version())
    sub_parsers = parser.add_subparsers(dest="method")

    # check method args
    for k, v in slack_api_specific.get().iteritems():
        method_parser = sub_parsers.add_parser(k)
        method_parser.add_argument('--quiet', action='store_true', dest="is_quiet", default=False, help="don't print api response")
        for p in v:
            # convert dictionary keyname for argparser use
            p["required"] = True if p.pop("Required") == arg_required_string else False
            p["help"] = p.pop("Description")

            # supplement by environment variable
            arg_name = p.pop("Argument")
            env_var_key = env_var_key_prefix + arg_name.upper()
            if env_var_key in os.environ:
                p["default"] = os.environ[env_var_key]
                p["required"] = False

            # pop extra parameter
            if "extra_function" in p:
                p.pop("extra_function")

            method_parser.add_argument("--" + arg_name, action="store", dest=arg_name, **p)

    method_args = vars(parser.parse_args())
    method_args = extra_args.parse(method_args)

    method = method_args.pop("method")
    is_quiet = method_args.pop("is_quiet")
    return is_quiet, method, method_args


def main():
    is_quiet, method, method_args = parse_program_args()
    slack_api_options = dict((k, v) for k, v in method_args.iteritems() if v)
    slack_client = SlackClient(slack_api_options["token"])
    timeout = 1
    res = slack_client.api_call(method, timeout, **slack_api_options)
    if not is_quiet:
        print(json.dumps(res))


if __name__ == '__main__':
    main()
