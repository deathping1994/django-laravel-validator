# -*- coding:utf-8 -*-
# PROJECT_NAME : laravel_validator
# FILE_NAME    : 
# AUTHOR       : younger shen


def format_args_split(format_str):
    if ':' in format_str:
        args = format_str.split(':')[1].split(',')
        return args
    else:
        return None


def check_errors(error_list, error_list_ext):

    for key in error_list:
        value = error_list.get(key)
        if not value:
            return False

    if not error_list_ext:
        return False

    return True


def error_message_generate(field, rule, message, error):
    if not message:
        return error[0]
    else:
        message_key = field + '.' + rule
        message_str = message.get(message_key, None)
        if message_str:
            return message_str
        else:
            return error[0]